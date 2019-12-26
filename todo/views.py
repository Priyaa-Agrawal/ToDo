from django.shortcuts import render,redirect
from .models import Todo
from django.contrib.auth.models import User,auth

# Create your views here.
def index(request, username):
    todo_items = list()
    todo_items = Todo.objects.filter(username=username)    
    todo_list = todo_items.order_by('id')
    context = {'todo_list' : todo_list}
    return render(request, 'todo/index.html', context)

def task(request, username):
    if request.method == 'POST':
        text = request.POST['text']
        todo = Todo.objects.create(username=username,text=text)
        todo.save()
        return redirect('/todo/index/' + username)


def complete(request, todo_id,todo_username):
    todo = Todo.objects.get(pk=todo_id)
    todo.complete = True
    todo.save()
    return redirect('/todo/index/' + todo_username)

def deletecomplete(request, username):
    Todo.objects.filter(complete=True).delete()
    return redirect('/todo/index/' + username)

def deleteall(request, username):
    Todo.objects.all().delete()
    return redirect('/todo/index/' + username)