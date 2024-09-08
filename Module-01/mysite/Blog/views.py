from django.shortcuts import render , get_object_or_404 
from django.contrib import messages
from .models import Post
from django.http import Http404
from django.core.paginator import Paginator
from django.views.generic import ListView
from .forms import EmailPostForm
from django.core.mail import send_mail

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
    
    
    

#------------------------------------- POST DETAILS --------------------------------

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


#------------------------------------ SHARE POST VIE EMAIL ----------------------

def postShare(request, post_id):
    # retrieve post by id
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    sent = False
    
    # Cheking form if submitted
    if request.method == 'POST':
        # Form was submitted
        form = EmailPostForm(request.POST)
        if form.is_valid():
            # Form fields passed validation
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url()) 
            subject = f"{cd['name']} recommends you to read {post.title}"
            message = f"Read {post.title} at {post_url} \n {cd['name']}\'s comments : {cd['comments']}"
            
            # this function is used to send emails from one direction which is the email used in the 
            # cfg , and sent to any email reciver 
            send_mail(subject, message, cd['email'],[cd['to']])
            sent = True
    else:
        form = EmailPostForm()
    
    return render(request, 'Blog/post/sharePost.html',{'form': form, 'post': post,  'sent': sent })
        
    
 






