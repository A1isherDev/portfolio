"""
URL configuration for portfolio_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
# Trigger reload
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap

from core.views import HomePageView
from pages.views import StaticSitemap, PortfolioSitemap, BlogSitemap

sitemaps = {
    'static': StaticSitemap,
    'portfolio': PortfolioSitemap,
    'blog': BlogSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('', HomePageView.as_view(), name='home'),
    path('pages/', include('pages.urls')),
    path('projects/', include('portfolio.urls')),
    path('blog/', include('blog.urls')),
    path('', include('core.urls')),

    # Sitemap
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]

# Serve media files in development. Static files are served automatically by
# Django's staticfiles app (from STATICFILES_DIRS) when DEBUG is True, and by
# WhiteNoise in production — so we only need to wire up media here.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
