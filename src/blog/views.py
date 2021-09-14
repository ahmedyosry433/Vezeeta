
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from .models import Blog, Comment, Like
from.forms import AddPost, CommentForm
from django.core.paginator import Paginator
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.

# Create Blog List
def blog_list (request):
    query_set = Blog.objects.all().order_by('-created_in')
    new_filter = Blog.objects.all().order_by('-created_in')[:3]
    # Paginator
    paginator = Paginator(query_set, 2)  # Show 3 contacts per page.
    page_number = request.GET.get('page')
    query_set = paginator.get_page(page_number)
    # Search
    if request.GET.get('searched'):
        query_set = Blog.objects.filter(title__icontains=request.GET.get('searched'))
    context = {
        'all':query_set,   
        'old':new_filter, # Filter New Blog 
        
    }
    return render (request,'blog/blog_list.html' , context)


# Create Blog Details
def blog_detail(request , slug):
    post = Blog.objects.get(slug=slug)
    old = Blog.objects.all().order_by('-created_in')[:3]
    
    # Comment
    comments = Comment.objects.all()
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(request.POST ,request.FILES)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    
   
    context = {
        'detail' :post,
        'old':old,
        
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form
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

    #if the button is clicked
    delete_blog = get_object_or_404(Blog, id=id)
    if request.POST:
            delete_blog.delete()
            return redirect('blog:blog_list')
            
    return render(request,'blog/delete_post.html')


# Create Like Button
@login_required()
def like_post(request,slug):
    user=request.user
    if request.method == 'POST':
        post_id=request.POST.get('post_id')
        post_obj= Blog.objects.get(slug=post_id)
        
        if user in post_obj.liked.all():
            post_obj.liked.remove(user)
        else:
            post_obj.liked.add(user)
            
        # print('ahmedddddd'*100)
        # like , created =Like.objects.get_or_create(user=user, post_id=post_id) 
        # if not created :
        #     if like.value == 'Like':
        #         like.value == 'Unlike'
                
        #     else:
        #         like.value == 'Like'
        # like.save()
    return HttpResponseRedirect(reverse('blog:blog_detail', args=[str(slug)]))
 
