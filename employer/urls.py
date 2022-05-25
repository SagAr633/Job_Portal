from django.urls import path
from employer import views

urlpatterns=[
    path('ehome',views.EmployerHomeView.as_view(),name='emp_home'),
    path('epro',views.EmployerProfileView.as_view(),name='emp-profile'),
    path('e-detail',views.EmployerDetailView.as_view(),name='emp-detail'),
    path('add-job',views.JobCreateView.as_view(),name='emp-jobs'),
    path('all-jobs',views.ListAllJobs.as_view(),name='emp-all-jobs'),
    path('detail/<int:id>',views.JobDetailView.as_view(),name='job-detail'),
    path('edit-job/<int:id>',views.UpdateView.as_view(),name='edit-job'),
    path('view_applic/<int:id>',views.ViewApplication.as_view(),name='view_applic'),
    path('applic-det/<int:id>',views.ApplicantDetailView.as_view(),name='applicant-det'),
    path('status/<int:id>',views.update_application,name='status'),
    path('a_status/<int:id>',views.accept_application,name='a_status')
]