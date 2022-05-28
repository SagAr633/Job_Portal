from django.shortcuts import render,redirect
from jp_app.models import User
from jp_app.forms import UserRegistrationForm,SignInForm
from django.views.generic import CreateView,FormView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login,logout


class SignUpView(CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')


class SigninView(FormView):
    model = User
    form_class = SignInForm
    template_name = 'login.html'

    def post(self,request,*args,**kwargs):
        form=SignInForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(request,username=username,password=password)
            if not user:
                return render(request,'login.html',{'form':form})
            login(request,user)
            if request.user.is_candidate:
                return redirect('c-home')
            else:
                return redirect('emp_home')




