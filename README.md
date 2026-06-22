# Django Portfolio Website

A production-grade, reusable Django portfolio template with a dynamic, CMS-like structure and full admin capabilities. It ships with neutral placeholder content (the "Alex Morgan" persona) seeded via `populate_data` — replace it with your own from the Django admin (`/admin/`) without touching any code.

## 🚀 Features

### Core Features
- **Dynamic Content Management**: All content editable from Django admin
- **SEO Optimized**: Meta tags, Open Graph, sitemap.xml, RSS feeds
- **Responsive Design**: Mobile-friendly layouts
- **Contact Form**: Messages are saved to the database (viewable in the admin) with AJAX submission and toast feedback; email delivery is optional
- **Media Management**: Image uploads for projects, articles, and site settings

### Apps Structure
- **core**: Site settings, social links, SEO metadata
- **pages**: Homepage sections (about, skills, experience)
- **portfolio**: Projects and technologies with filtering
- **blog**: Articles, categories, tags with Markdown support

### Advanced Features
- **Pagination**: For blog articles and projects
- **RSS Feed**: Blog syndication at `/blog/feed/`
- **Sitemap**: Dynamic sitemap at `/sitemap.xml`
- **Markdown Rendering**: For blog articles with syntax highlighting
- **Search & Filters**: In admin and frontend
- **Slug-based URLs**: Clean, SEO-friendly URLs

## 🛠 Tech Stack

- **Backend**: Django 5.2+, Python 3.12+
- **Database**: SQLite (development), PostgreSQL ready for production
- **Frontend**: HTML5, CSS3, JavaScript, Font Awesome
- **Admin**: Django Summernote for rich text editing
- **Deployment**: Ready for Gunicorn + Nginx

## 📦 Installation

### Prerequisites
- Python 3.12+
- pip package manager

### Setup Instructions

1. **Clone and Navigate**
   ```bash
   cd portfolio
   ```

2. **Create Virtual Environment**
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # Linux/Mac
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create Superuser**
   ```bash
   python manage.py createsuperuser
   ```

6. **Populate Initial Data**
   ```bash
   python manage.py populate_data
   ```

7. **Collect Static Files**
   ```bash
   python manage.py collectstatic
   ```

8. **Run Development Server**
   ```bash
   python manage.py runserver
   ```

9. **Access the Application**
   - Website: http://127.0.0.1:8000/
   - Admin: http://127.0.0.1:8000/admin/

## 🎯 Quick Start Guide

### 1. Configure Site Settings
1. Go to Admin → Core → Site Settings
2. Update your site name, hero title, and contact email
3. Upload your logo and favicon

### 2. Add Social Links
1. Go to Admin → Core → Social Links
2. Add your social media profiles with proper URLs

### 3. Create Skills
1. Go to Admin → Pages → Skills
2. Add your technical skills with proficiency levels
3. Group them by category (Frontend, Backend, Database, DevOps)

### 4. Add Projects
1. Go to Admin → Portfolio → Technologies
2. Add technologies you work with
3. Go to Admin → Portfolio → Projects
4. Create projects with descriptions, images, and links
5. Mark featured projects to appear on homepage

### 5. Write Blog Articles
1. Go to Admin → Blog → Categories
2. Create article categories
3. Go to Admin → Blog → Tags
4. Add relevant tags
5. Go to Admin → Blog → Articles
6. Write articles using Markdown or the rich text editor

### 6. Configure SEO
1. Go to Admin → Core → SEO
2. Set meta titles and descriptions for key pages

## 📁 Project Structure

```
portfolio/
├── portfolio_project/          # Main Django project
│   ├── settings.py             # Project settings
│   ├── urls.py                 # Main URL configuration
│   └── wsgi.py                 # WSGI configuration
├── core/                       # Core app (settings, social links)
│   ├── models.py               # SiteSetting, SocialLink, SEO
│   ├── views.py                # HomePageView, ContactFormView
│   ├── admin.py                # Admin configuration
│   └── management/             # Custom management commands
├── pages/                      # Pages app (about, skills, experience)
│   ├── models.py               # Skill, Experience, AboutSection
│   ├── views.py                # AboutView, SkillsView, ExperienceView
│   └── admin.py                # Admin configuration
├── portfolio/                  # Portfolio app (projects)
│   ├── models.py               # Project, Technology
│   ├── views.py                # ProjectListView, ProjectDetailView
│   └── admin.py                # Admin configuration
├── blog/                       # Blog app (articles)
│   ├── models.py               # Article, Category, Tag
│   ├── views.py                # ArticleListView, ArticleDetailView
│   ├── admin.py                # Admin configuration
│   └── templatetags/           # Custom template tags
├── templates/                  # Django templates
│   ├── base.html               # Base template
│   ├── partials/               # Template partials
│   ├── core/                   # Core app templates
│   ├── pages/                  # Pages app templates
│   ├── portfolio/              # Portfolio app templates
│   └── blog/                   # Blog app templates
├── static/                     # Static files
│   ├── css/                    # CSS files
│   ├── js/                     # JavaScript files
│   └── images/                 # Image files
├── media/                      # User uploaded files
└── staticfiles/                # Collected static files
```

## 🔧 Configuration

### Email Settings (Contact Form)
Update `portfolio_project/settings.py` with your email configuration:

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'your-app-password'
DEFAULT_FROM_EMAIL = 'noreply@yourdomain.com'
```

### Production Settings
For production deployment, update these settings:

```python
DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']

# Database (PostgreSQL recommended)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'portfolio_db',
        'USER': 'portfolio_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Security
SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
```

## 🚀 Deployment

### Using Gunicorn + Nginx

1. **Install Gunicorn**
   ```bash
   pip install gunicorn
   ```

2. **Create Gunicorn Service**
   ```bash
   gunicorn portfolio_project.wsgi:application --bind 0.0.0.0:8000
   ```

3. **Configure Nginx**
   ```nginx
   server {
       listen 80;
       server_name yourdomain.com;
       
       location /static/ {
           alias /path/to/portfolio/staticfiles/;
       }
       
       location /media/ {
           alias /path/to/portfolio/media/;
       }
       
       location / {
           proxy_pass http://127.0.0.1:8000;
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
       }
   }
   ```

### Using Docker
Create `Dockerfile`:
```dockerfile
FROM python:3.12-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
RUN python manage.py collectstatic --noinput

EXPOSE 8000
CMD ["gunicorn", "portfolio_project.wsgi:application", "--bind", "0.0.0.0:8000"]
```

## 📝 Customization Guide

### Adding New Sections
1. Create new models in appropriate app
2. Update admin configuration
3. Create views and templates
4. Add URL patterns

### Modifying Design
- Edit `static/css/style.css` for main styles
- Edit `static/css/django-styles.css` for Django-specific styles
- Update templates in `templates/` directory

### Adding New Apps
1. `python manage.py startapp new_app`
2. Add to `INSTALLED_APPS` in settings
3. Configure URLs, models, views, templates

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🆘 Support

If you encounter any issues:

1. Check the Django documentation
2. Review the error logs
3. Ensure all dependencies are installed
4. Verify static files are collected: `python manage.py collectstatic`
5. Clear browser cache and restart development server

## 🔄 Updates

To update the project:

1. Backup your database
2. Pull latest changes
3. Run migrations: `python manage.py migrate`
4. Collect static files: `python manage.py collectstatic`
5. Restart the server

## 📊 Performance Tips

- Use PostgreSQL in production
- Enable Django caching
- Optimize images before uploading
- Use CDN for static files in production
- Enable database connection pooling
- Monitor and optimize database queries

---

**Happy Coding! 🎉**
