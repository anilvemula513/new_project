from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def static_page(request):
    return render(request, 'myapp/static_page.html')


