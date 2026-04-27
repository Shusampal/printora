from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Blogpost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'time_upload', 'publish', 'created_at']
    list_filter = ['time_upload', 'publish', 'author']
    search_fields = ['title', 'overview', 'author']
    ordering = ('-time_upload',)
    readonly_fields = ('created_at', 'updated_at', 'slug')
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = (
        ('Blog Post Information', {'fields': ('title', 'slug', 'author')}),
        ('Content', {'fields': ('overview',)}),
        ('Media', {'fields': ('thumbnail',)}),
        ('Publishing', {'fields': ('time_upload', 'publish')}),
        ('Metadata', {'fields': ('created_at',
         'updated_at'), 'classes': ('collapse',)}),
    )
