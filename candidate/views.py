from django.shortcuts import render,redirect
from django.views.generic import TemplateView,CreateView,ListView,UpdateView
from candidate.models import CandidateProfile
from employer.models import Jobs,Applications
from candidate.forms import CandidateProfileForm
from django.urls import reverse_lazy
from django.contrib.auth import logout
from candidate.filters import JobFilter
from jp_app.decorators import signin_required
from django.utils.decorators import method_decorator

@method_decorator(signin_required,name='dispatch')
class CandidateHome(TemplateView):
    template_name = 'cand-home.html'
    def get(self,request,*args,**kwargs):
        filter=JobFilter(request.GET,queryset=Jobs.objects.all())
        return render(request,'cand-home.html',{'filter':filter})

@method_decorator(signin_required,name='dispatch')
class CandidateProfileCreateView(CreateView):
    model = CandidateProfile
    form_class = CandidateProfileForm
    template_name = 'cand-pro-regi.html'
    success_url = reverse_lazy('c-home')

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)

@method_decorator(signin_required,name='dispatch')
class CandidateDetailView(TemplateView):
    template_name = 'cand-detail.html'

@method_decorator(signin_required,name='dispatch')
class AllJobsView(ListView):
    model = Jobs
    template_name = 'all_jobs.html'
    context_object_name = 'jobs'
    ordering = ['-id']
    paginate_by = 2

@signin_required
def apply_now(request,*args,**kwargs):
    job_id=kwargs.get('id')
    job=Jobs.objects.get(id=job_id)
    applicant=request.user
    Applications.objects.create(applicant=applicant,job=job)
    return redirect('c-home')

@method_decorator(signin_required,name='dispatch')
class MyApplicationView(ListView):
    model = Applications
    template_name = 'applied_jobs.html'
    context_object_name = 'applied'

    def get_queryset(self):
        return Applications.objects.filter(applicant=self.request.user)

@method_decorator(signin_required,name='dispatch')
class AcceptedApplications(ListView):
    model = Applications
    template_name = 'accepted_jobs.html'
    context_object_name = 'application'

    def get_queryset(self):
        return Applications.objects.filter(applicant=self.request.user,status='accepted')

@signin_required
def signout(request):
    logout(request)
    return redirect('login')

@method_decorator(signin_required,name='dispatch')
class CandProfileEditView(UpdateView):
    model = CandidateProfile
    form_class = CandidateProfileForm
    template_name = 'cand-pro-update.html'
    success_url = reverse_lazy('c-detail')
    pk_url_kwarg = 'id'


