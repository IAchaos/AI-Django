from django.shortcuts import render , get_object_or_404 
from django.contrib import messages
from .models import Post
from django.http import Http404
from django.core.paginator import Paginator

def postList(request):
    
    posts_list = Post.objects.all()
    
    paginator = Paginator(posts_list, 1)
    page_number = request.GET.get('page', 1)
    try:
        posts = paginator.get_page(page_number)
    except Exception as e:
        messages.error(request, f'Error: {e}')
        posts = paginator.get_page(1)
   
    
    return render(request, 'Blog/post/postList.html', {'posts': posts})





def postDetail(request, year, month, day, post):
    # method 1
    #'''
    #try:
    #    post = Post.objects.get(id=post_id)
    #except Post.DoesNotExist:
    #    raise Http404('Post not found')
    #
    #return render(request, 'Blog/post/postDetail.html', {'post': post})
    #'''
    
    # method 2
    
    post = get_object_or_404(Post, status = Post.Status.PUBLISHED,
                             publish__year = year,
                             publish__month = month,
                             publish__day = day,
                             slug = post
                             )
        
    return render(request, 'Blog/post/postDetail.html', {'post': post})
    
    
 






