from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import SiteSetting


class HomePageView(TemplateView):
    template_name = 'core/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Get featured projects
        from portfolio.models import Project
        context['featured_projects'] = Project.objects.filter(
            is_featured=True, 
            is_active=True
        )[:6]
        
        # Get latest blog articles
        from blog.models import Article
        context['latest_articles'] = Article.objects.filter(
            published=True
        )[:3]
        
        # Get skills for homepage and group them
        from pages.models import Skill, AboutSection, Service
        context['skills'] = Skill.objects.all().order_by('group', 'order', 'name')
        context['about_section'] = AboutSection.get_singleton()
        context['services'] = Service.objects.all().prefetch_related('features')
        
        skills_by_group = {}
        for skill in context['skills']:
            group = skill.get_group_display()
            if group not in skills_by_group:
                skills_by_group[group] = []
            skills_by_group[group].append(skill)
        context['skills_by_group'] = skills_by_group
        
        return context


@method_decorator(csrf_exempt, name='dispatch')
class ContactFormView(TemplateView):
    template_name = 'core/contact.html'
    
    def post(self, request, *args, **kwargs):
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')
        
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            # AJAX request
            if name and email and message:
                try:
                    # Send email
                    site_settings = SiteSetting.get_singleton()
                    send_mail(
                        subject=f"Contact Form: {subject}",
                        message=f"From: {name} ({email})\n\n{message}",
                        from_email=settings.DEFAULT_FROM_EMAIL,
                        recipient_list=[site_settings.contact_email or settings.EMAIL_HOST_USER],
                        fail_silently=False,
                    )
                    return JsonResponse({'success': True, 'message': 'Message sent successfully!'})
                except Exception as e:
                    return JsonResponse({'success': False, 'message': f'Error sending message: {str(e)}'})
            else:
                return JsonResponse({'success': False, 'message': 'Please fill in all required fields.'})
        else:
            # Regular form submission
            if name and email and message:
                try:
                    site_settings = SiteSetting.get_singleton()
                    send_mail(
                        subject=f"Contact Form: {subject}",
                        message=f"From: {name} ({email})\n\n{message}",
                        from_email=settings.DEFAULT_FROM_EMAIL,
                        recipient_list=[site_settings.contact_email or settings.EMAIL_HOST_USER],
                        fail_silently=False,
                    )
                    messages.success(request, 'Message sent successfully!')
                except Exception as e:
                    messages.error(request, f'Error sending message: {str(e)}')
            else:
                messages.error(request, 'Please fill in all required fields.')
            
            return self.get(request, *args, **kwargs)
