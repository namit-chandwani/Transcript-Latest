from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView


from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

    # Django Login
    url(r'^login/', views.loginform, name="login"),
    url(r'^logout/', views.logoutform, name="logout"),

    #login_success
   # url(r'^accounts/profile/', views.login_success, name='login-success'),


   # url(r'^project/', views.project, name="faculty"),
    url(r'^arc/$', views.hod, name="arc"),
    url(r'^arc-gradesheet/$', views.arcGradesheet, name="arc-gradesheet"),
    
    url(r'^upload/$', views.upload, name="upload"),
    url(r'^transcript_upload/$', views.transcript_upload, name="transcript_upload"),
    # url(r'^warden/$', views.hod, name="hod"),
    # url(r'^leave/', views.leave, name="leave"),
    url(r'^gradesheet/', views.gradesheet, name="gradesheet"),
    url(r'^gradesheet2/(?P<bits_id>\w+)/$', views.gradesheet2, name="gradesheet2"),
    url(r'^gradesheet3/(?P<bits_id>\w+)/$', views.gradesheet3, name="gradesheet3"),
    
    url(r'^transcript/', views.transcript, name="transcript"),
    url(r'^transcript-continuing-price/', views.transcriptContinuingPrice, name="transcript3"),
    url(r'^transcript-graduated-price/', views.transcriptGraduatedPrice, name="transcript4"),
    url(r'^transcript2/(?P<bits_id>\w+)/$', views.transcript2, name="transcript2"),
    url(r'^arc/([0-9]+)/$', views.hodprojectapprove, name="arcprojectapprove"),
    url(r'^arc-gradesheet/([0-9]+)/$', views.arcgradesheetapprove, name="arcgradesheetapprove"),
    # url(r'^hostelsuperintendent/([0-9]+)/$', views.hostelsuperintendentdaypassapprove, name="hostelsuperintendentdaypassapprove"),
    # url(r'^student/(?P<id>\d+)/$',views.studentDetails, name="studentDetails"),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
