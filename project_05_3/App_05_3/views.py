from django.shortcuts import render

def homepage(request):
    return render(request, 'App_05_3/homepage.html')
