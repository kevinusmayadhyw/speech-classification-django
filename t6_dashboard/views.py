from django.shortcuts import render
from .models import topUsers

def index(request):
    topUsers.objects.all().delete()
    user = topUsers(fullname = "Dhani Iskandar", department = "Marketing", division = "Area Marketing division", point=128)
    user.save()
    user = topUsers(fullname = "Arief Key", department = "Marketing", division = "Area Marketing division", point=125)
    user.save()

    user = topUsers(fullname = "Sabiru muda", department = "Marketing", division = "Area Marketing division", point=120)
    user.save()

    user = topUsers(fullname = "Paday hu", department = "Akuntasi", division = "Area Akuntasi division", point=100)
    user.save()

    user = topUsers(fullname = "Q Muhid", department = "Akuntasi", division = "Area Akuntasi division", point=50)
    user.save()

    user_list = topUsers.objects.all()

    context = {'user_list': user_list}

    return render(request, 't6_dashboard/index.html', context)