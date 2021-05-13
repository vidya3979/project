"""crmluminar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import render
from django.urls import path, include

from crmapp.views import adminpage, SearchFollowUp, CreatePayment, CreateEnquiry, ViewPayment, CreateBatch, \
    DelBatch, UpdateBatch, ViewBatch, ViewCourse, UpdateCourse,Enquiry_Delete, DelCourse, CreateCounsellor, ListCounsellor, \
    UpdateCounsellor, log_out,Update_Enquiry,DeleteCounsellor, CreateCourse, load_course

urlpatterns = [
    path("", lambda request: render(request, "crmapp/base.html")),
    path("user",lambda request:render(request,"crmapp/base0.html")),
    path("adminlogin", adminpage, name="adminlogin"),
    path("adminlogout",log_out,name="adminLogout"),

    path("counsellorCreate", CreateCounsellor.as_view(), name="counsellorCreate"),
    path("ViewCounsellor", ListCounsellor.as_view(), name="View_Counsellor"),
    path("update_counsellor/<int:pk>", UpdateCounsellor.as_view(), name="update_counsellor"),
    path("delete_counsellor/<int:pk>", DeleteCounsellor.as_view(), name="delete_counsellor"),
    path("create_course",CreateCourse.as_view(),name="create_course"),
    path("view_course",ViewCourse.as_view(),name="View_course"),
    path("create_batch",CreateBatch.as_view(),name="create_batch"),
    path("View_Batch",ViewBatch.as_view(),name="View_Batch"),
    path("create_payment",CreatePayment.as_view(),name="create_payment"),
    path("View_Payment",ViewPayment.as_view(),name="View_Payment"),
    path("update_course/<int:pk>",UpdateCourse.as_view(),name="update_course"),
    path("Del_course/<int:pk>",DelCourse.as_view(),name="Del_course"),
    path("update_batch/<int:pk>",UpdateBatch.as_view(),name="update_batch"),
    path("Del_batch/<int:pk>",DelBatch.as_view(),name="Del_batch"),

    path("Create_Enquiry",CreateEnquiry.as_view(),name="Create_Enquiry"),
    path("Followup",SearchFollowUp.as_view(),name="Followup"),
    path("Delete_Enquiry/<int:id>",Enquiry_Delete.as_view(),name="Delete_Enquiry"),
    path("Update_Enquiry/<int:id>",Update_Enquiry.as_view(),name="UpEnquiry"),

    path('ajax/load-course/',load_course,name='ajax_load_course'),

]
