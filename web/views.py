from django.shortcuts import render
from django.views import generic
from soupsieve import select
from .models import Disney

# Create your views here.

def index(request):
    return render(
        request,
        'web/index.html',
    )


class movieweb(generic.TemplateView):
    def get(self, request, *args, **kwargs):
        # template_name = 'movie_detail/detail_page2.html'
        template_name = 'web/index.html'
        disney = Disney.objects.all()
        return render(request, template_name, {"disney":disney})


        