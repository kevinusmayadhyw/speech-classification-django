from django.shortcuts import render


def index(request):
    return render(request, 't6_dashboard/index.html')