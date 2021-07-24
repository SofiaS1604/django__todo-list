from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy


def index(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('home')
        else:
            error = 'Форма была неверной'

    form = TaskForm()
    tasks = Task.objects.all()

    context = {
        'form': form,
        'error': error,
        'title': 'To do list',
        'tasks': tasks
    }

    return render(request, 'main/index.html', context)


class AuthorDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy('home')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)