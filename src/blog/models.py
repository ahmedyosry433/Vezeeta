from django.contrib.auth.models import User
from django.db import models
from django.db.models.deletion import CASCADE
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
    liked =models.ManyToManyField(User ,default=None,blank=True ,related_name='liked')
    
    
    
    
    def __str__(self):

        return self.title
    def save (self,*args,**kwargs):
        self.slug=slugify(self.title)
        super(Blog,self).save(*args,**kwargs)
        
    
    
# Create Comment

class Comment (models.Model):
    
    post = models.ForeignKey(Blog , on_delete=models.CASCADE , related_name='comments')
    name= models.CharField(max_length=80)
    email =models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now=False, auto_now_add=True)
    active=models.BooleanField(default=False)


    class Meta :
        ordering= ['created_on']
        
        
    def __str__(self):
        return '#Comment" {} " #by" {} " #in post" {} "'.format(self.body, self.name,self.post)
    
    
    
    
# Create Like 
   
LIKE_CHOICES =(
    ('Like','Like'),
    ('Unlike','Unlike'),
)
class Like(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post =models.ForeignKey(Blog, on_delete=CASCADE)
    value =models.CharField(choices=LIKE_CHOICES ,default='Like',max_length=10)
    
    def __str__(self):
        return str(self.post)