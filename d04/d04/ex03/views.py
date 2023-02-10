from django.shortcuts import render

def index(request):
    return render(request, 'ex03/index.html', {'list' : range(0, 250, 5)})
