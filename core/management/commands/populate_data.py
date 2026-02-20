from django.core.management.base import BaseCommand
from django.utils.text import slugify
from core.models import SiteSetting, SocialLink, SEO
from pages.models import Skill, Experience, AboutSection
from portfolio.models import Technology, Project
from blog.models import Category, Tag, Article
from django.utils import timezone
from datetime import date


class Command(BaseCommand):
    help = 'Populate the database with initial data'

    def handle(self, *args, **options):
        self.stdout.write('Populating initial data...')
        
        # Create site settings
        site_settings, created = SiteSetting.objects.get_or_create(
            pk=1,
            defaults={
                'site_name': 'A1isherDev',
                'hero_title': "I'm Alisher",
                'hero_subtitle': 'Web Developer',
                'contact_email': 'alisher@example.com',
            }
        )
        if created:
            self.stdout.write('Created site settings')
        
        # Create social links
        social_links_data = [
            {
                'platform_name': 'discord',
                'url': 'https://discord.com/users/1354328698454675500',
                'icon_class': 'fab fa-discord',
                'order': 1,
            },
            {
                'platform_name': 'linkedin',
                'url': 'https://www.linkedin.com/in/alisher-muhammadaliyev-616795344/',
                'icon_class': 'fab fa-linkedin-in',
                'order': 2,
            },
            {
                'platform_name': 'github',
                'url': 'https://github.com/A1isherDev',
                'icon_class': 'fab fa-github',
                'order': 3,
            },
            {
                'platform_name': 'instagram',
                'url': 'https://instagram.com/a1isherdev/',
                'icon_class': 'fab fa-instagram',
                'order': 4,
            },
        ]
        
        for social_data in social_links_data:
            social_link, created = SocialLink.objects.get_or_create(
                platform_name=social_data['platform_name'],
                defaults=social_data
            )
            if created:
                self.stdout.write(f"Created social link: {social_data['platform_name']}")
        
        # Create skills
        skills_data = [
            {'name': 'HTML5', 'level': 95, 'group': 'frontend', 'icon_class': 'fab fa-html5'},
            {'name': 'CSS3', 'level': 60, 'group': 'frontend', 'icon_class': 'fab fa-css3-alt'},
            {'name': 'JavaScript', 'level': 20, 'group': 'frontend', 'icon_class': 'fab fa-js-square'},
            {'name': 'Node.js', 'level': 40, 'group': 'backend', 'icon_class': 'fab fa-node-js'},
            {'name': 'Python', 'level': 80, 'group': 'backend', 'icon_class': 'fab fa-python'},
            {'name': 'Server', 'level': 50, 'group': 'backend', 'icon_class': 'fas fa-server'},
            {'name': 'SQLite', 'level': 35, 'group': 'database', 'icon_class': 'fas fa-database'},
            {'name': 'MySQL', 'level': 20, 'group': 'database', 'icon_class': 'fas fa-database'},
            {'name': 'PostgreSQL', 'level': 70, 'group': 'database', 'icon_class': 'fas fa-database'},
            {'name': 'Git', 'level': 90, 'group': 'devops', 'icon_class': 'fab fa-git-alt'},
            {'name': 'Docker', 'level': 60, 'group': 'devops', 'icon_class': 'fab fa-docker'},
            {'name': 'VS Code', 'level': 95, 'group': 'devops', 'icon_class': 'fas fa-code'},
        ]
        
        for skill_data in skills_data:
            skill, created = Skill.objects.get_or_create(
                name=skill_data['name'],
                defaults=skill_data
            )
            if created:
                self.stdout.write(f"Created skill: {skill_data['name']}")
        
        # Create technologies
        technologies_data = [
            {'name': 'Django', 'icon_class': 'fas fa-code'},
            {'name': 'Python', 'icon_class': 'fab fa-python'},
            {'name': 'JavaScript', 'icon_class': 'fab fa-js'},
            {'name': 'HTML5', 'icon_class': 'fab fa-html5'},
            {'name': 'CSS3', 'icon_class': 'fab fa-css3-alt'},
            {'name': 'PostgreSQL', 'icon_class': 'fas fa-database'},
            {'name': 'Docker', 'icon_class': 'fab fa-docker'},
            {'name': 'Git', 'icon_class': 'fab fa-git-alt'},
        ]
        
        for tech_data in technologies_data:
            tech, created = Technology.objects.get_or_create(
                name=tech_data['name'],
                defaults=tech_data
            )
            if created:
                self.stdout.write(f"Created technology: {tech_data['name']}")
        
        # Create blog categories
        categories_data = [
            {'name': 'Web Development', 'description': 'Articles about web development'},
            {'name': 'Python', 'description': 'Python programming tutorials and tips'},
            {'name': 'Django', 'description': 'Django framework tutorials'},
            {'name': 'Tutorial', 'description': 'Step-by-step tutorials'},
        ]
        
        for cat_data in categories_data:
            category, created = Category.objects.get_or_create(
                name=cat_data['name'],
                defaults=cat_data
            )
            if created:
                self.stdout.write(f"Created category: {cat_data['name']}")
        
        # Create tags
        tags_data = [
            'python', 'django', 'web-development', 'tutorial', 'javascript', 
            'css', 'html', 'database', 'docker', 'git'
        ]
        
        for tag_name in tags_data:
            tag, created = Tag.objects.get_or_create(
                name=tag_name,
                defaults={'slug': slugify(tag_name)}
            )
            if created:
                self.stdout.write(f"Created tag: {tag_name}")
        
        # Create about section
        about_section, created = AboutSection.objects.get_or_create(
            pk=1,
            defaults={
                'title': 'About Me',
                'greeting': '👋 Hello there!',
                'hero_description': "I'm Alisher Muhammadaliyev, a passionate Software Developer who enjoys understanding how systems work — from low-level logic circuits to high-level applications. With solid experience in Python and modern web technologies, I aim to create efficient, reliable, and scalable software that combines logic and creativity.",
                'content': "<p>I'm a dedicated backend developer from Uzbekistan with a strong and growing skill set in modern web technologies. My journey in programming began a few years ago, and since then I've been continuously improving my expertise in building reliable, scalable, and efficient backend systems.</p><p>I primarily work with Python, Django, Django REST Framework, and PostgreSQL — crafting clean APIs and solid server-side logic. I also enjoy working with frontend fundamentals and modern tools when needed, allowing me to understand the full picture of a web application.</p><p>My focus is always on writing maintainable code, solving real problems, and delivering systems that perform smoothly in production. I love learning new technologies, experimenting with fresh ideas, and improving my craft step by step.</p>",
                'education': 'Computer Science',
                'location': 'Uzbekistan Fergana',
                'years_experience': '2+',
                'projects_completed': '30+',
                'happy_clients': '0+',
            }
        )
        if created:
            self.stdout.write('Created about section')
        
        # Create sample projects
        django_tech = Technology.objects.get(name='Django')
        python_tech = Technology.objects.get(name='Python')
        postgres_tech = Technology.objects.get(name='PostgreSQL')
        
        projects_data = [
            {
                'title': 'Portfolio Website',
                'slug': 'portfolio-website',
                'short_description': 'A modern portfolio website built with Django showcasing my projects and skills.',
                'description': 'This is my personal portfolio website built from scratch using Django 5. It features a clean, responsive design with dynamic content management, blog functionality, and project showcase. The site includes features like contact forms, RSS feeds, sitemaps, and SEO optimization.',
                'github_url': 'https://github.com/A1isherDev/portfolio',
                'live_url': 'https://alisherdev.com',
                'is_featured': True,
            },
            {
                'title': 'Task Management API',
                'slug': 'task-management-api',
                'short_description': 'RESTful API for task management with Django REST Framework.',
                'description': 'A comprehensive RESTful API built with Django REST Framework for managing tasks and projects. Features include user authentication, role-based permissions, real-time updates with WebSockets, and comprehensive API documentation.',
                'github_url': 'https://github.com/A1isherDev/task-api',
                'is_featured': True,
            },
            {
                'title': 'E-commerce Platform',
                'slug': 'ecommerce-platform',
                'short_description': 'Full-featured e-commerce platform with payment integration.',
                'description': 'A complete e-commerce solution built with Django and PostgreSQL. Includes product catalog, shopping cart, order management, payment processing with Stripe, inventory management, and admin dashboard.',
                'github_url': 'https://github.com/A1isherDev/ecommerce',
                'is_featured': False,
            },
        ]
        
        for project_data in projects_data:
            project, created = Project.objects.get_or_create(
                slug=project_data['slug'],
                defaults=project_data
            )
            if created:
                # Add technologies to project
                project.technologies.add(django_tech, python_tech, postgres_tech)
                self.stdout.write(f"Created project: {project_data['title']}")
        
        # Create sample blog articles
        web_dev_cat = Category.objects.get(name='Web Development')
        python_cat = Category.objects.get(name='Python')
        
        articles_data = [
            {
                'title': 'Getting Started with Django 5',
                'slug': 'getting-started-django-5',
                'excerpt': 'Learn how to set up your first Django 5 project and explore the new features.',
                'content': '''# Getting Started with Django 5

Django 5 brings exciting new features and improvements that make web development even more enjoyable. In this tutorial, we'll walk through setting up your first Django 5 project.

## Installation

First, let's install Django 5:

```bash
pip install django==5.0
```

## Creating Your First Project

Once installed, you can create a new project:

```bash
django-admin startproject myproject
cd myproject
python manage.py runserver
```

## What's New in Django 5

Django 5 introduces several new features:
- Improved async support
- Better database constraints
- Enhanced security features
- Updated admin interface

## Conclusion

Django 5 is a significant update that brings many improvements. Start exploring these new features today!''',
                'category': web_dev_cat,
                'published': True,
                'published_at': timezone.now(),
            },
            {
                'title': 'Python Best Practices for Clean Code',
                'slug': 'python-best-practices-clean-code',
                'excerpt': 'Discover essential Python best practices for writing clean, maintainable code.',
                'content': '''# Python Best Practices for Clean Code

Writing clean code is essential for maintainable and scalable applications. Here are some Python best practices.

## Naming Conventions

Use descriptive names for variables, functions, and classes:

```python
# Good
user_name = "John"
def calculate_total_price(items):
    pass

# Bad
un = "John"
def calc(x):
    pass
```

## Function Design

Keep functions small and focused on a single responsibility:

```python
# Good
def validate_email(email):
    return "@" in email and "." in email

def send_welcome_email(email):
    if validate_email(email):
        # Send email logic
        pass

# Bad
def process_user(email, name):
    if "@" in email and "." in email:
        # Send email logic
        pass
```

## Conclusion

Following these practices will make your Python code more readable and maintainable.''',
                'category': python_cat,
                'published': True,
                'published_at': timezone.now(),
            },
        ]
        
        for article_data in articles_data:
            article, created = Article.objects.get_or_create(
                slug=article_data['slug'],
                defaults=article_data
            )
            if created:
                # Add some tags
                python_tag = Tag.objects.get(name='python')
                django_tag = Tag.objects.get(name='django')
                article.tags.add(python_tag, django_tag)
                self.stdout.write(f"Created article: {article_data['title']}")
        
        # Create SEO data
        seo_data = [
            {
                'page_key': 'home',
                'meta_title': 'A1isherDev - Web Developer Portfolio',
                'meta_description': 'Alisher Muhammadaliyev - Passionate Software Developer specializing in Python, Django, and modern web technologies.',
                'meta_keywords': 'portfolio, developer, django, python, web development, software engineer',
            },
            {
                'page_key': 'about',
                'meta_title': 'About - A1isherDev',
                'meta_description': 'Learn more about Alisher Muhammadaliyev, his background, skills, and experience in web development.',
                'meta_keywords': 'about, alisher muhammadaliyev, background, experience, skills',
            },
        ]
        
        for seo_item in seo_data:
            seo, created = SEO.objects.get_or_create(
                page_key=seo_item['page_key'],
                defaults=seo_item
            )
            if created:
                self.stdout.write(f"Created SEO data for: {seo_item['page_key']}")
        
        self.stdout.write(self.style.SUCCESS('Initial data populated successfully!'))
