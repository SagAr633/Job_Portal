from django.urls import path
from candidate import views


urlpatterns=[
    path('chome',views.CandidateHome.as_view(),name='c-home'),
    path('cpro',views.CandidateProfileCreateView.as_view(),name='c-profile'),
    path('cdetail',views.CandidateDetailView.as_view(),name='c-detail'),
    path('jobs',views.AllJobsView.as_view(),name='c-jobs'),
    path('application/add/<int:id>',views.apply_now,name='apply_now'),
    path('myapp',views.MyApplicationView.as_view(),name='my_app'),
    path('accepted',views.AcceptedApplications.as_view(),name='accp_jobs')
]