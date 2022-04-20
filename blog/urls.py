from django.urls import URLPattern, path
from . import views

##
from django.urls import path
from .views import add_nutritions
##

urlpatterns = [
    path('<int:pk>/', views.PostDetail.as_view()),
    path('', views.PostList.as_view()),       
    path('nutritions/', add_nutritions)
    # path('<int:pk>/', views.single_post_page),
    # path('', views.index), 
]