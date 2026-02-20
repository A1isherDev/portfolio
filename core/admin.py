from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import SiteSetting, SocialLink, SEO


@admin.register(SiteSetting)
class SiteSettingAdmin(ModelAdmin):
    list_display = ['site_name', 'contact_email']
    fieldsets = (
        ('Basic Information', {
            'fields': ('site_name', 'hero_title', 'hero_subtitle', 'hero_greeting', 'hero_description', 'contact_email')
        }),
        ('Media', {
            'fields': ('logo', 'favicon')
        }),
    )
    
    def has_add_permission(self, request):
        # Only allow one instance
        return not SiteSetting.objects.exists()


@admin.register(SocialLink)
class SocialLinkAdmin(ModelAdmin):
    list_display = ['platform_name', 'url', 'order', 'is_active']
    list_filter = ['platform_name', 'is_active']
    search_fields = ['platform_name', 'url']
    list_editable = ['order', 'is_active']
    ordering = ['order']


@admin.register(SEO)
class SEOAdmin(ModelAdmin):
    list_display = ['page_key', 'meta_title']
    search_fields = ['page_key', 'meta_title', 'meta_description']
    list_filter = ['page_key']
    fieldsets = (
        ('Basic SEO', {
            'fields': ('page_key', 'meta_title', 'meta_description')
        }),
        ('Advanced SEO', {
            'fields': ('meta_keywords', 'og_image'),
            'classes': ('collapse',)
        }),
    )
