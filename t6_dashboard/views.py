from django.shortcuts import render
from django.db.models import Sum
from .models import topUsers
from .models import points
from .models import division

def index(request):
    deleteAll(topUsers)
    deleteAllPoint(points)
    deleteAllDivision(division)

    user_list = dataDummy(topUsers)
    point_list = dataDummyPoint(points).order_by('created_at')[:2]
    point_sum = topUsers.objects.aggregate(Sum('point')).get('point__sum')
    target = 200
    percent = point_sum/target * 100
    division_list = dataDummyDivision(division)
    count_department = division_list.all().values('department').distinct().count()

    context = {'user_list': user_list, 'point_list' : point_list, 'point_sum' : point_sum, 'percent' : percent, 'target' : target, 'division_list' : division_list,'count_department' : count_department}

    return render(request, 't6_dashboard/index.html', context)

def deleteAll(topUsers):
    topUsers.objects.all().delete()

def deleteAllPoint(points):
    points.objects.all().delete()

def deleteAllDivision(division):
    division.objects.all().delete()

def dataDummyDivision(division):
    div = division(name = "Area Marketing division 1", department = "Marketing")
    div.save()

    div = division(name = "Area Marketing division 2", department = "Marketing")
    div.save()

    div = division(name = "Area Akuntasi division 1", department = "Akuntasi")
    div.save()

    div = division(name = "Area Akuntasi division 2", department = "Akuntasi")
    div.save()

    div = division(name = "Data dummy", department = "Data dummy")
    div.save()

    div = division(name = "Data dummy 1", department = "Data dummy 1")
    div.save()

    div = division(name = "Data dummy 2", department = "Data dummy 2")
    div.save()

    div = division(name = "Data dummy 3", department = "Data dummy 3")
    div.save()

    div = division(name = "Data dummy 4", department = "Data dummy 4")
    div.save()

    return division.objects.all()


def dataDummyPoint(points):
    point = points(point=1000)
    point.save()

    point = points(point=1500)
    point.save()

    return points.objects.all()

def dataDummy(topUsers):
    user = topUsers(fullname = "Dhani Iskandar", department = "Marketing", division = "Area Marketing division", point=30)
    user.save()
    
    user = topUsers(fullname = "Arief Key", department = "Marketing", division = "Area Marketing division", point=5)
    user.save()

    user = topUsers(fullname = "Sabiru muda", department = "Marketing", division = "Area Marketing division", point=10)
    user.save()

    user = topUsers(fullname = "Paday hu", department = "Akuntasi", division = "Area Akuntasi division", point=15)
    user.save()

    user = topUsers(fullname = "Q Muhid", department = "Akuntasi", division = "Area Akuntasi division", point=20)
    user.save()

    user = topUsers(fullname = "Data dummy", department = "Data dummy", division = "Data dummy", point=20)
    user.save()

    user = topUsers(fullname = "Data dummy", department = "Data dummy", division = "Data dummy", point=0)
    user.save()

    user = topUsers(fullname = "Data dummy", department = "Data dummy", division = "Data dummy", point=0)
    user.save()

    user = topUsers(fullname = "Data dummy", department = "Data dummy", division = "Data dummy", point=0)
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