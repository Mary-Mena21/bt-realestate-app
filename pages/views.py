from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # """View function for the home page of the site."""
    return render(request, 'pages/index.html')  
    # return HttpResponse('<h1>Welcome to the Home Page</h1><p>This is a simple Django application.</p>')

# Create your views here.
def about(request):
    # """View function for the about page of the site."""
    # return render(request, 'pages/about.html', {})
    return render(request, 'pages/about.html', {
        'title': 'About Us',
        'content': 'This is the about page of our Django application. Here you can find information about our project and team.',
    })
