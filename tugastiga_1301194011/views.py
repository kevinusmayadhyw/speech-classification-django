from django.shortcuts import render, redirect, get_object_or_404
from .models import Message

# Create your views here.
def index(request):
    message_list = Message.objects.all()

    context = {'message_list': message_list}

    return render(request, 'tugastiga_1301194011/index.html', context)

def add(request):
    return render(request, 'tugastiga_1301194011/add.html')

def save(request):
    message = Message(name = request.POST['name'], messages = request.POST['messages'])
    message.save()

    return redirect('/tugastiga_1301194011')

def detail(request, id):
    message = get_object_or_404(Message, id=id)
    context = {'message': message}

    return render(request, 'tugastiga_1301194011/detail.html', context)

def delete(request, id):
    message = get_object_or_404(Message, id=id)
    message.delete()

    return redirect('/tugastiga_1301194011')

def edit(request, id):
    message = get_object_or_404(Message, id=id)
    context = {'message': message}

    return render(request, 'tugastiga_1301194011/edit.html', context)

def update(request, id):
    message = get_object_or_404(Message, id=id)

    message.name = request.POST['name']
    message.messages = request.POST['messages']
    message.save()

    return redirect('/tugastiga_1301194011')