from django.shortcuts import render
from django.http import HttpResponse

post = [
    {'author':'Gopal Yadav',
    'title':'My life My Rules',
    'content':'Amazing',
    'date_posted' : '21 Aug 2018'
    },
    {
        'author':'Dark Knight',
        'title':'Batman',
        'content':'Bat',
        'date_posted' : '31 Dec 2018'
    }
]

def home(request):
    context = {
        'posts':post
    }
    return render(request , 'blog/home.html' , context)

def about(request):
    return render(request , 'blog/about.html', {'title':'About'})
