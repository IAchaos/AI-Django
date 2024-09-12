from django.urls import path
from . import views

app_name = 'Blog'

urlpatterns = [
    
    #path('', views.postList, name = 'post_list'), # METHOD 1
    path('', views.PostListView.as_view(), name = 'post_list'), # METHOD 2  
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.postDetail, name='post_detail'),
    
    path('share/<int:post_id>', views.postShare, name='post_share'),
    path('comment/<int:post_id>', views.postComment, name='post_comment')
]
