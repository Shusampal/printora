import os

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


def env_flag(name, default=False):
    value = os.getenv(name)
    if value is None:
        return default
    return value.strip().lower() in {"1", "true", "yes", "on"}


class Command(BaseCommand):
    help = "Create or update a superuser from environment variables."

    def handle(self, *args, **options):
        phone_number = os.getenv("DJANGO_SUPERUSER_PHONE_NUMBER")
        full_name = os.getenv("DJANGO_SUPERUSER_FULL_NAME")
        password = os.getenv("DJANGO_SUPERUSER_PASSWORD")

        if not phone_number or not full_name or not password:
            self.stdout.write(
                self.style.WARNING(
                    "Skipping superuser setup. Set DJANGO_SUPERUSER_PHONE_NUMBER, "
                    "DJANGO_SUPERUSER_FULL_NAME, and DJANGO_SUPERUSER_PASSWORD "
                    "to enable automatic admin creation."
                )
            )
            return

        user_model = get_user_model()
        user, created = user_model.objects.get_or_create(
            phone_number=phone_number,
            defaults={
                "full_name": full_name,
            },
        )

        user.full_name = full_name
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True

        if hasattr(user, "is_phone_verified"):
            user.is_phone_verified = env_flag("DJANGO_SUPERUSER_PHONE_VERIFIED", True)

        user.set_password(password)
        user.save()

        if created:
            self.stdout.write(self.style.SUCCESS("Superuser created successfully."))
        else:
            self.stdout.write(self.style.SUCCESS("Superuser updated successfully."))
