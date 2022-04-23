from django.contrib import admin
from sympy import N
from .models import Netflix, Disney, Watcha, Wavve
# Register your models here.

admin.site.register(Netflix)
admin.site.register(Disney)
admin.site.register(Watcha)
admin.site.register(Wavve)

