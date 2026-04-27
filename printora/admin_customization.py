"""
Custom Admin Interface Customization
Customizes Django admin site title, header, and styling
"""

from django.contrib import admin


def customize_admin_site():
    """Customize the Django admin site"""
    try:
        admin.site.site_header = "Printora Admin Panel"
        admin.site.site_title = "Printora Management"
        admin.site.index_title = "Welcome to Printora Admin Dashboard"
    except Exception:
        pass
