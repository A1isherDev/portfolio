from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class SiteSetting(models.Model):
    site_name = models.CharField(max_length=200, default="A1isherDev")
    hero_title = models.CharField(max_length=500, default="I'm Alisher")
    hero_subtitle = models.CharField(max_length=500, default="Web Developer")
    hero_greeting = models.CharField(max_length=100, default="👋 Hello there!")
    hero_description = models.TextField(default="I'm a passionate Software Developer who enjoys understanding how systems work.")
    contact_email = models.EmailField(default="alisher@example.com")
    logo = models.FileField(upload_to='core/', blank=True, null=True)
    favicon = models.FileField(upload_to='core/', blank=True, null=True)
    cv = models.FileField(upload_to='cv/', blank=True, null=True)
    
    class Meta:
        verbose_name = "Site Setting"
        verbose_name_plural = "Site Settings"
    
    def __str__(self):
        return self.site_name
    
    @classmethod
    def get_singleton(cls):
        obj, created = cls.objects.get_or_create(
            pk=1,
            defaults={
                'site_name': 'A1isherDev',
                'hero_title': "I'm Alisher",
                'hero_subtitle': 'Web Developer',
                'hero_greeting': '👋 Hello there!',
                'hero_description': "I'm a passionate Software Developer who enjoys understanding how systems work.",
                'contact_email': 'alisher@example.com'
            }
        )
        return obj


class SocialLink(models.Model):
    PLATFORM_CHOICES = [
        ('discord', 'Discord'),
        ('linkedin', 'LinkedIn'),
        ('github', 'GitHub'),
        ('instagram', 'Instagram'),
        ('telegram', 'Telegram'),
        ('twitter', 'Twitter'),
        ('facebook', 'Facebook'),
        ('youtube', 'YouTube'),
    ]
    
    platform_name = models.CharField(max_length=50, choices=PLATFORM_CHOICES)
    url = models.URLField()
    icon_class = models.CharField(max_length=100, help_text="Font Awesome icon class")
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['order']
        verbose_name = "Social Link"
        verbose_name_plural = "Social Links"
    
    def __str__(self):
        return f"{self.get_platform_name_display()} - {self.url}"


class SEO(models.Model):
    page_key = models.CharField(max_length=100, unique=True, help_text="Unique identifier for the page")
    meta_title = models.CharField(max_length=200)
    meta_description = models.TextField(max_length=500)
    meta_keywords = models.CharField(max_length=500, blank=True)
    og_image = models.FileField(upload_to='seo/', blank=True, null=True)
    
    class Meta:
        verbose_name = "SEO Metadata"
        verbose_name_plural = "SEO Metadata"
    
    def __str__(self):
        return f"{self.page_key} - {self.meta_title}"
