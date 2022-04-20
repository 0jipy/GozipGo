from re import template
# from django.shortcuts import render
from django.views.generic import ListView, DetailView
from requests import post
from .models import Post

# views.py의 import 목록
import csv

from django.shortcuts import render
from django.http import HttpResponse
# db 모델들.. 여기서는 Nutrition만 쓸 예정
from .models import Nutrition
####

class PostList(ListView):
    model = Post
    ordering = '-pk'

class PostDetail(DetailView):
    model = Post

# def index(request):
#     posts = Post.objects.all().order_by('-pk')

#     return render(
#         request,
#         'blog/index.html',
#         {
#             'posts' : posts,
#         }
#     )

# 
# def single_post_page(request, pk):
#     post = Post.objects.get(pk=pk)

#     return render(
#         request, 
#         'blog/single_post_page.html',
#         {
#             'post': post,
#         }
#     )

# C:\github\GozipGo\nutritions.csv

data = None
file_dir = r'C:\github\GozipGo' + "/"

def read_data(table_name):
    with open(file_dir +f'{table_name}.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        global data
        data = list(reader)
    return

def footer(table_name, class_name, bulk_list):
    class_name.objects.bulk_create(bulk_list)
    
    with open(file_dir + f'{table_name}.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
    return

def add_nutritions(request):
    read_data('nutritions')
    if not data:
        return HttpResponse('Nothing to update')

    arr = []
    for row in data:
        arr.append(Nutrition(
            one_serving_kcal=row[0],
            sodium_mg=row[1],
            fat_g=row[2],
            sugars_g=row[3],
            protein_g=row[4],
            caffeine_mg=row[5]
        ))

    footer('nutritions', Nutrition, arr)
    return HttpResponse('Nutritions table updated')