from blog.models import Blog, Comment
from django.contrib import admin

# Register your models here.


admin.site.register(Blog)
class PostAdmin(admin.ModelAdmin):
    
    list_filter = ['created_on', 'active']
    list_display = ['name', 'post', 'created_on',  'active']
    search_fields = ['name', 'post']


admin.site.register(Comment, PostAdmin)




