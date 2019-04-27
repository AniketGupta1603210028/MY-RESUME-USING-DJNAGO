from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.homepage,name="main"),
    path('PersonalInfo/',views.PersonalInfo,name="PersonalInfo"),
    path('Education/',views.Education,name="Education"),
    path('skills/',views.skills,name="skills"),
    path('languages/',views.languages,name="languages"),
    path('certificates/',views.certificates,name="certificates"),
    path('projects/',views.projects,name="projects"),
    path('achievements/',views.achievements,name="achievements"),
    path('interns/',views.interns,name="internships"),
    path('exit/',views.exit1,name="exit"),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
