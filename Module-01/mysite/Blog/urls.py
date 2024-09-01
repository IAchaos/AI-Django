from django.urls import path
from . import views

app_name = 'Blog'

urlpatterns = [
    path('', views.postList, name = 'post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.postDetail, name='post_detail'),
]
