from django.shortcuts import render , get_object_or_404 
from django.contrib import messages
from .models import Post
from django.http import Http404
from django.core.paginator import Paginator
from django.views.generic import ListView

'''
# METHOD 1 : Using Django Function Based View
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
'''

# METHOD 2 : Using Django Generic View (Class Based View)

class PostListView(ListView):
    model = Post
    
    # By default, the ListView class uses the <app_name>/<model_name>_list.html template.
    # In this case, it would use the Blog/post/post_list.html template.
    template_name = 'Blog/post/postList.html'
    paginate_by = 1
    context_object_name = 'posts'
    
    
    

#------------------------------------------------------------------------------------------------

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
    
    
 






