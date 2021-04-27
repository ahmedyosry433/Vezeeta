from django.contrib.auth.models import User
from django.db import models
from django.urls.base import reverse
from django.utils.text import slugify

# Create your models here.
class Blog (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    description = models.TextField(max_length= 900)
    created_in = models.DateTimeField(auto_now=False, auto_now_add=True)
    img = models.ImageField(upload_to='blog', blank=True, null=True)
    slug=models.SlugField(blank=True , null = True)
    likes =models.ManyToManyField(User , related_name='blog_post')
    
    
    
    
    def __str__(self):

        return self.title
    def save (self,*args,**kwargs):
        self.slug=slugify(self.title)
        super(Blog,self).save(*args,**kwargs)
        
    def get_absolute_url(self):
        return reverse("blog:blog_detail",kwargs={"slug" : self.slug})
        
    def get_like_url(self):
        return reverse("blog:like_post",kwargs={"slug" : self.slug})
    