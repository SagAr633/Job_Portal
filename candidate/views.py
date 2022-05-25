from django.shortcuts import render,redirect
from django.views.generic import TemplateView,CreateView,ListView
from candidate.models import CandidateProfile
from employer.models import Jobs,Applications
from candidate.forms import CandidateProfileForm
from django.urls import reverse_lazy

class CandidateHome(TemplateView):
    template_name = 'cand-home.html'

class CandidateProfileCreateView(CreateView):
    model = CandidateProfile
    form_class = CandidateProfileForm
    template_name = 'cand-pro-regi.html'
    success_url = reverse_lazy('c-home')

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)

class CandidateDetailView(TemplateView):
    template_name = 'cand-detail.html'

class AllJobsView(ListView):
    model = Jobs
    template_name = 'all_jobs.html'
    context_object_name = 'jobs'

def apply_now(request,*args,**kwargs):
    job_id=kwargs.get('id')
    job=Jobs.objects.get(id=job_id)
    applicant=request.user
    Applications.objects.create(applicant=applicant,job=job)
    return redirect('c-home')

class MyApplicationView(ListView):
    model = Applications
    template_name = 'applied_jobs.html'
    context_object_name = 'applied'

    def get_queryset(self):
        return Applications.objects.filter(applicant=self.request.user)

class AcceptedApplications(ListView):
    model = Applications
    template_name = 'accepted_jobs.html'
    context_object_name = 'application'

    def get_queryset(self):
        return Applications.objects.filter(applicant=self.request.user,status='accepted')