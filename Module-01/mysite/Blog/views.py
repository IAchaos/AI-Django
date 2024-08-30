from django.shortcuts import render , get_object_or_404
from .models import Post
from django.http import Http404

def postList(request):
    posts = Post.objects.all()
    return render(request, 'Blog/post/postList.html', {'posts': posts})


def postDetail(request, post_id):
    # method 1
    '''
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        raise Http404('Post not found')
    
    return render(request, 'Blog/post/postDetails.html', {'post': post})
    '''
    
    # method 2
    post = get_object_or_404(Post, status = Post.Status.DRAFT, id=post_id)
    return render(request, 'Blog/post/postDetails.html', {'post': post})
    
 






