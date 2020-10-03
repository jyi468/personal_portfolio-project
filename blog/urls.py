from django.urls import path, include
from . import views  # import blog's views

app_name = 'blog'  # specify app name's detail. like blog:detail

urlpatterns = [
    path('', views.all_blogs, name='all_blogs'),  # if forwarded, it has the other url added to it
    path('<int:blog_id>/', views.detail, name='detail')  # match int blog_id from address and pass detail in views
]
