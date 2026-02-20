from django.db import models


class Skill(models.Model):
    SKILL_GROUPS = [
        ('frontend', 'Frontend Development'),
        ('backend', 'Backend Development'),
        ('database', 'Database Management'),
        ('devops', 'DevOps & Tools'),
        ('other', 'Other'),
    ]
    
    name = models.CharField(max_length=100)
    level = models.PositiveIntegerField(default=50, help_text="Skill level from 1 to 100")
    group = models.CharField(max_length=20, choices=SKILL_GROUPS, default='other')
    icon_class = models.CharField(max_length=100, blank=True, help_text="Font Awesome icon class")
    order = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ['group', 'order', 'name']
        verbose_name = "Skill"
        verbose_name_plural = "Skills"
    
    def __str__(self):
        return f"{self.name} ({self.get_group_display()})"


class Experience(models.Model):
    company = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    is_current = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ['-start_date', 'order']
        verbose_name = "Experience"
        verbose_name_plural = "Experiences"
    
    def __str__(self):
        return f"{self.role} at {self.company}"
    
    @property
    def duration_display(self):
        if self.is_current:
            return f"{self.start_date.strftime('%B %Y')} - Present"
        elif self.end_date:
            return f"{self.start_date.strftime('%B %Y')} - {self.end_date.strftime('%B %Y')}"
        return f"{self.start_date.strftime('%B %Y')}"


class AboutSection(models.Model):
    title = models.CharField(max_length=200, default="About Me")
    content = models.TextField()
    education = models.CharField(max_length=200, default="Computer Science")
    location = models.CharField(max_length=200, default="Uzbekistan Fergana")
    years_experience = models.CharField(max_length=50, default="2+")
    projects_completed = models.CharField(max_length=50, default="30+")
    happy_clients = models.CharField(max_length=50, default="0+")
    
    class Meta:
        verbose_name = "About Section"
        verbose_name_plural = "About Sections"
    
    def __str__(self):
        return self.title
    
    @classmethod
    def get_singleton(cls):
        obj, created = cls.objects.get_or_create(
            pk=1,
            defaults={
                'title': 'About Me',
                'education': 'Computer Science',
                'location': 'Uzbekistan Fergana',
                'years_experience': '2+',
                'projects_completed': '30+',
                'happy_clients': '0+'
            }
        )
        return obj


class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon_class = models.CharField(max_length=100, help_text="Font Awesome icon class")
    order = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ['order', 'title']
        verbose_name = "Service"
        verbose_name_plural = "Services"
    
    def __str__(self):
        return self.title


class ServiceFeature(models.Model):
    service = models.ForeignKey(Service, related_name='features', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
