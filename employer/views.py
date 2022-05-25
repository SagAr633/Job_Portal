from django.shortcuts import render,redirect
from django.views.generic import TemplateView,CreateView,ListView,DetailView,UpdateView
from employer.models import EmployerProfile,Jobs,Applications
from employer.forms import EmployerProfileForm,JobForm
from django.urls import reverse_lazy
from django.core.mail import send_mail

class EmployerHomeView(TemplateView):
    template_name = 'emp-home.html'

class EmployerProfileView(CreateView):
    model = EmployerProfile
    form_class = EmployerProfileForm
    template_name = 'emp-profile.html'
    success_url = reverse_lazy('emp-detail')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class EmployerDetailView(TemplateView):
    template_name = 'emp-detail.html'

class JobCreateView(CreateView):
    model = Jobs
    form_class = JobForm
    template_name = 'emp-add-job.html'
    success_url = reverse_lazy('emp_home')

    def form_valid(self, form):
        form.instance.posted_by=self.request.user
        return super().form_valid(form)

class ListAllJobs(ListView):
    model = Jobs
    context_object_name = 'jobs'
    template_name = 'emp-job-list.html'

    def get_queryset(self):
        return Jobs.objects.filter(posted_by=self.request.user)

class JobDetailView(DetailView):
    model = Jobs
    template_name = 'job-detail.html'
    context_object_name = 'job'
    pk_url_kwarg = 'id'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        qs=Applications.objects.filter(applicant=self.request.user,job=self.object)
        print(qs)
        context['status']=qs
        return context

class UpdateJobView(UpdateView):
    model = Jobs
    form_class = JobForm
    template_name = 'edit_job.html'
    success_url = reverse_lazy('job-detail')
    pk_url_kwarg = 'id'

    def get_queryset(self):
        return Jobs.objects.get(posted_by=self.request.user)

class ViewApplication(ListView):
    model = Applications
    template_name = 'all_applications.html'
    context_object_name = 'all_app'

    def get_queryset(self):
        return Applications.objects.filter(job=self.kwargs.get('id'))

class ApplicantDetailView(DetailView):
    model = Applications
    template_name = 'applicant_detail.html'
    context_object_name = 'applic'
    pk_url_kwarg = 'id'

def update_application(request,*args,**kwargs):
    app_id=kwargs.get('id')
    qs=Applications.objects.get(id=app_id)
    qs.status='rejected'
    qs.save()
    return redirect('emp_home')

def accept_application(request,*args,**kwargs):
    app_id=kwargs.get('id')
    qs=Applications.objects.get(id=app_id)
    qs.status='accepted'
    qs.save()
    send_mail(
        'Job Notification',
        'You are accepted for....',
        'sagarms2009@gmail.com',
        ['microsearch143@gmail.com'],
        fail_silently=False,
    )
    return redirect('emp_home')


