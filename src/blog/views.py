
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from .models import Blog
from.forms import AddPost
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import RedirectView
# Create your views here.

class LikePost(RedirectView):
    def get_redirect_url(self,*args,**kwargs):
        slug=self.kwargs.get("slug")
        print(slug)
        obj=get_object_or_404(Blog ,slug=slug)
        url_ =obj.get_absolute_url()
        user = self.request.user
        if user.is_authenticated():
            if user in obj.likes.all():
                obj.likes.remove(user)
            else:
                obj.likes.add(user)
                
        return url_
        
    
# Create Blog List
def blog_list (request):
    query_set = Blog.objects.all().order_by('-created_in')
    old_filter = Blog.objects.all().order_by('-created_in')[:3]
    # Paginator
    paginator = Paginator(query_set, 2)  # Show 3 contacts per page.
    page_number = request.GET.get('page')
    query_set = paginator.get_page(page_number)
    # Search
    if request.GET.get('searched'):
        query_set = Blog.objects.filter(title__icontains=request.GET.get('searched'))
    context = {
        'all':query_set,   
        'old':old_filter,
        
    }
    return render (request,'blog/blog_list.html' , context)


# Create Blog Details
def blog_detail(request , slug):
    detail = Blog.objects.get(slug=slug)
    old = Blog.objects.all().order_by('-created_in')[:3]
    
   
    context = {
        'detail' :detail,
        'old':old,
        
    }
    return render (request, 'blog/blog_details.html' , context)


# Create Add Blog 
@login_required()
def add_post (request):
    if request.method == 'POST':
        form = AddPost(request.POST ,request.FILES)
        if form.is_valid():
            new_form =form.save(commit =False)
            new_form.user =request.user
            new_form.save()
            return redirect('blog:blog_list')   
    else:
        form = AddPost()
    context={
        'formadd':form
    }
    return render (request, 'blog/add_post.html',context)


# Create Edit Blog 
@login_required()
def edit_post (request, id):
    post = get_object_or_404(Blog, id=id)
    if request.method == 'POST':
        form = AddPost(request.POST , request.FILES , instance=post)
        if form.is_valid():
            new_form=form.save(commit=False)
            new_form.user=request.user
            new_form.save()
            return redirect('blog:blog_list')
    else:
        form =AddPost(instance=post)
    context = {
        'editpost':form
    }
    return render (request , 'blog/edit_post.html',context)


# Create Delete Blog 
@login_required()
def delete_post (request,id):

    if(request.GET.get('delete')): 

        post = get_object_or_404(Blog, id=id)
        if request.method == 'POST':
            form = AddPost(request.POST , request.FILES , instance=post)
            if form.is_valid():
                new_form=form.save(commit=False)
                new_form.user=request.user
                new_form.delete()
                return redirect('blog:blog_list')
    return render(request,'blog/delete_post.html')
