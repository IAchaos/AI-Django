from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'
    
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated  = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)
    
    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=[
                '-publish'
            ])
        ]
    
    def __str__(self):
        return self.title
    
    
    def get_absolute_url(self):
        
        # reverse() is a helper function that generates URLs using the URL patterns defined in the project's urls.py file.
        return reverse("Blog:post_detail", args=[
            self.publish.year,
            self.publish.month,
            self.publish.day,
            self.slug
        ])
        
class Comment(models.Model):
    
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_created = True)
    active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['created']
        indexes = [
            models.Index(fields=['created'])
        ]
            
    def __str__(self):
        return self.name + ' commented on ' + self.post.title
    
    
    