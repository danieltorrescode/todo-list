from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from .forms import *
# Create your views here.
# this app allow to sign up, log in 
# and log out the users
# it uses class and function based views
# with the User model provided by django
class sign_up(CreateView):
    model = User
    template_name = 'users/sign_up.html'
    form_class = UserForm
    success_url = reverse_lazy('tasks:list')

    def get_context_data(self, **kwargs):
        context = super(sign_up, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect(self.get_success_url())

        return self.render_to_response(self.get_context_data(form=form))

def log_in(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('tasks:list') 
            else:
                return render(request, 'users/log_in.html',
                                {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'users/log_in.html',
                                {'error_message': 'Invalid login'})
    return render(request, 'users/log_in.html')

@login_required(login_url='/log_in/')
def log_out(request):
    logout(request)
    return redirect('users:log_in')
