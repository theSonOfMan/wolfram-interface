from django.shortcuts import render

def index_view(request, *args, **kwargs):
    return render(request, "index.html", {})

def result_view(request, *args, **kwargs):
    return render(request, "result.html", {})
# Create your views here.
