from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request,'main.html')


def PersonalInfo(request):
    return render(request,'PersonalInfo.html')

def Education(request):
    return render(request,'Education.html')

def exit1(request):
    return render(request,'exit.html')
def skills(request):
    return render(request,'skills.html')

def languages(request):
    return render(request,'languages.html')

def certificates(request):
    return render(request,'certificates.html')

def projects(request):
    return render(request,'Projects.html')

def interns(request):
    return render(request,'internships.html')

def achievements(request):
    return render(request,'achievements.html')
