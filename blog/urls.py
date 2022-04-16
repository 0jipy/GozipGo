from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('', views.PostList.as_view()),
    # path('', views.index),    
    path('<int:pk>/', views.single_post_page),
]