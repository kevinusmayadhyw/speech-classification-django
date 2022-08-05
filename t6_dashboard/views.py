from django.shortcuts import render
from .models import topUsers

def index(request):
    deleteAll(topUsers)

    user_list = dataDummy(topUsers)[:5]
    

    context = {'user_list': user_list}

    return render(request, 't6_dashboard/index.html', context)

def deleteAll(topUsers):
    topUsers.objects.all().delete()

def dataDummy(topUsers):
    user = topUsers(fullname = "Dhani Iskandar", department = "Marketing", division = "Area Marketing division", point=128)
    user.save()
    user = topUsers(fullname = "Arief Key", department = "Marketing", division = "Area Marketing division", point=120)
    user.save()

    user = topUsers(fullname = "Sabiru muda", department = "Marketing", division = "Area Marketing division", point=125)
    user.save()

    user = topUsers(fullname = "Paday hu", department = "Akuntasi", division = "Area Akuntasi division", point=75)
    user.save()

    user = topUsers(fullname = "Q Muhid", department = "Akuntasi", division = "Area Akuntasi division", point=50)
    user.save()

    user = topUsers(fullname = "Data dummy", department = "Data dummy", division = "Data dummy", point=0)
    user.save()

    return topUsers.objects.all().order_by('-point')


def save(request):
    user = topUsers(fullname = request.POST['fullname'], department = request.POST['department'], division = request.POST['division'], point = request.POST['point'])
    user.save()

    return redirect('/t6_dashboard')

def detail(request, id):
    user = get_object_or_404(topUsers, id=id)
    context = {'user': user}

    return render(request, 't6_dashboard/', context)

def delete(request, id):
    user = get_object_or_404(topUsers, id=id)
    user.delete()

    return redirect('/t6_dashboard')

def edit(request, id):
    user = get_object_or_404(topUsers, id=id)
    context = {'user': user}

    return render(request, 't6_dashboard/', context)

def update(request, id):
    user = get_object_or_404(topUsers, id=id)
    user.fullname = request.POST['fullname']
    user.department = request.POST['department']
    user.division = request.POST['division']
    user.point = request.POST['point']
    user.save()

    return redirect('/t6_dashboard')