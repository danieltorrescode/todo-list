from django.shortcuts import render,redirect
from django.http import Http404,HttpResponse,HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView,ListView,UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from .forms import *
from .models import *
# Create your views here.
# this is the task CRUD 
# all function related to task managment
# can be found here
# views class based are used 
def index(request):
    # return render(request, 'index.html')
    return redirect(reverse_lazy('tasks:list'))

class tasks(LoginRequiredMixin,ListView):
    login_url = '/users/log_in/'
    model = Task
    template_name = 'tasks/list.html'

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user).order_by('-id')

class create(LoginRequiredMixin,CreateView):
    login_url = '/users/log_in/'
    model = Task
    form_class = TaskForm
    template_name = 'tasks/create.html'
    success_url = reverse_lazy('tasks:list')
    # the post method of class is overwrited
    # to get the current user id
    # and assign it to the task
    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        if form.is_valid():
            task = form.save()
            task.user = self.request.user
            task.save()
            return HttpResponseRedirect(self.get_success_url())
        return self.render_to_response(self.get_context_data(form=form))

class update(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
	login_url = '/users/log_in/'
	model = Task
	form_class = TaskForm
	template_name = 'tasks/update.html'
	success_url = reverse_lazy('tasks:list')

    # test_func is function inherited from UserPassesTestMixin
    # this allow the action if the user if related to the task 
	def test_func(self):
		task=Task.objects.get(id=self.get_object().pk)
		if task.user == self.request.user:
			return True
		else:
			return False

class delete(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Task
    template_name = 'tasks/delete.html'
    success_url = reverse_lazy('tasks:list')

    def test_func(self):
        task=Task.objects.get(id=self.get_object().pk)
        if task.user == self.request.user:
            return True
        else:
            return False
    