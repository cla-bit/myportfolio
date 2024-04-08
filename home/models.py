from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


# Create your models here.


class Portfolio(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    resume = models.FileField(upload_to='resume')
    linkedin_link = models.URLField(blank=True, null=False)
    github_link = models.URLField(blank=True, null=False)
    google_link = models.URLField(blank=True, null=False)

    class Meta:
        indexes = [
            models.Index(fields=('linkedin_link', 'github_link', 'google_link')),
        ]
        verbose_name_plural = 'Portfolio'

    def __str__(self):
        return self.user.username


class Project(models.Model):
    project_name = models.CharField(max_length=50, blank=True, null=True, verbose_name="Project Name")
    project_slug = models.SlugField(max_length=50, blank=True, null=True, verbose_name="Project Slug")
    project_img = models.ImageField(upload_to='projects_img', default="", blank=True, null=True, verbose_name="Project Image")
    project_desc = models.TextField(blank=True, null=True, verbose_name="Project Description")
    docu_url_on = models.BooleanField(default=False)
    docu_url = models.URLField(blank=True, null=False, verbose_name="Document URL")
    git_url_on = models.BooleanField(default=False)
    git_url = models.URLField(blank=True, null=False, verbose_name="Git URL")
    video_url_on = models.BooleanField(default=False)
    video_url = models.URLField(blank=True, null=False, verbose_name="Video URL")
    done = models.BooleanField(default=False)
    date_done = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['project_name']
        indexes = [
            models.Index(fields=('project_name',)),
            models.Index(fields=('project_img',)),
            models.Index(fields=('project_desc',)),
            models.Index(fields=('docu_url', 'git_url', 'video_url'))
        ]
        verbose_name_plural = 'Projects'

    def __str__(self):
        return self.project_name

    def get_absolute_url(self):
        return reverse('home:project_detail', args=[self.project_slug])


class Contact(models.Model):
    name = models.CharField(max_length=100, null=True, verbose_name='Your Name')
    email = models.EmailField(null=True, verbose_name='Your Email')
    subject = models.CharField(max_length=100, null=True)
    message = models.TextField(null=True)

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=('name',))
        ]
        verbose_name_plural = 'Contacts'

    def __str__(self):
        return self.name
