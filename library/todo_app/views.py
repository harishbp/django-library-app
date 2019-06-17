from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import TodoItem
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

def todoVeiw(request):
	all_todos = TodoItem.objects.all()

	return render(request,'todo.html',{'all_todos':all_todos})

def addTodo(request):
	newTodo = TodoItem(Book_title = request.POST['book_title'],Author_name = request.POST['author_name'],Published_year = request.POST['pub_year'])
	newTodo.save()
	return HttpResponseRedirect('/todo/')


def deleteTodo(request, todo_id):
	print(todo_id)
	delTodo = TodoItem.objects.get(id = todo_id)
	delTodo.delete()
	return HttpResponseRedirect('/todo/')

def editTodo(request, todo_id):
	edTodo = TodoItem.objects.get(id = todo_id)
	# print(edTodo.id)

	return render(request,'todoedit.html',{'t_id':edTodo})

def updateTodo(request, todo_id):
	# print("update")
	edTodo = TodoItem.objects.get(id = todo_id)
	# print(edTodo.Book_title)
	edTodo.Book_title = request.POST['book_title']
	edTodo.Author_name = request.POST['author_name']
	edTodo.Published_year = request.POST['pub_year']

	# print(request.POST['book_title'])
	edTodo.save()
	return HttpResponseRedirect('/todo/')
