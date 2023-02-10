from django.shortcuts import render, redirect
from django.conf import settings
from django.http import HttpResponse
from .forms import MyForm
from datetime import datetime


def index(request):
    log_print = ""
    log=[]
    if(request.method=='POST'):
        form = MyForm(request.POST)
        if form.is_valid():
            with open(settings.LOG_FILE, "a") as f:
                f.write(str(datetime.now()))
                f.write("    ")
                f.write(form.cleaned_data['input'])
                f.write("\n")
            return redirect('/ex02')
    else:
        try:
            with open(settings.LOG_FILE, "r") as f:
                for line in f:
                    log.append(line)
        except:
            log = []
        form = MyForm()
    return render(request, 'ex02/index.html', {'form' : form, 'log' : log})
