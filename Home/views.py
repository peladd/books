from django.shortcuts import render

# Create your views here.

def home(request):
    name = ['samhheart', 'Tunde', 'messi']
    context = {
        'Key' : name
    }
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')