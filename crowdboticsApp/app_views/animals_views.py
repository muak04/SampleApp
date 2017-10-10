from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from crowdboticsApp.app_forms.animals_forms import DogForm, CatForm
from crowdboticsApp.models import Dog, Cat


class DogCreate(CreateView):
    form_class = DogForm
    template_name = 'create.html'
    success_url = '/index/'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(DogCreate, self).form_valid(form)


class DogUpdate(UpdateView):
    template_name = 'create.html'
    model = Dog
    fields = ['name', 'birthday']
    success_url = '/index/'


class CatCreate(CreateView):
    form_class = CatForm
    template_name = 'create.html'
    success_url = '/index/'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(CatCreate, self).form_valid(form)


class CatUpdate(UpdateView):
    template_name = 'create.html'
    model = Cat
    fields = ['name', 'birthday']
    success_url = '/index/'


@login_required(login_url='/login/')
def animals_list(request):
    user = request.user
    cats = Cat.objects.filter(owner=user)
    dogs = Dog.objects.filter(owner=user)

    return render_to_response('index.html', {'dogs': dogs, 'cats': cats})