from django.shortcuts import render
from secondapp.models import Todo

# Create your views here.
def index(request):
    todos = Todo.objects.all()
    return render(request, 'secondapp/index.html',{'todos':todos})
def new(request):
    return render(request, 'secondapp/new.html')