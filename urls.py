from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('test/',views.test),
    path('login/',views.login),
    path('register/',views.register),
    path('studenthome/',views.studenthome),
    path('adminhome/',views.adminhome),
    path('addcourse/',views.addcourse),
    path('courselist1/',views.courselist1),
    path('studentlist/',views.studentlist),
    path('searchcourse/',views.searchcourse),
    path('addbatch/',views.addbatch),
    path('newbatchlist1/',views.newbatchlist1),
    path('courselist3/',views.courselist3),
    path('admission/',views.admission),
    path('bookbatch/',views.bookbatch),
    path('logout/',views.logout),
    path('searchprofile/',views.searchprofile),
    path('updateprofile/',views.updateprofile),
    path('newbatchlist2/',views.newbatchlist2),
    path('upcomingbatches/',views.upcomingbatches),
    path('contact/',views.contact),
    path('gallery/',views.gallery),
    path('success/',views.success),    
    path('profilesuccess/',views.profilesuccess),    
    path('addfaculty/',views.addfaculty),
    path('facultylist/',views.facultylist),
]
