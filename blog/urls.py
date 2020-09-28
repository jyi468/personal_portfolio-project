from django.urls import path, include
from . import views  # import blog's views

urlpatterns = [
    path('', views.all_blogs, name='all_blogs')  # if forwarded, it has the other url added to it
]