from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Task
from .forms import TaskForm


class TaskList(ListView):
    model = Task
    context_object_name = "tasks"
    template_name = "main/task_list.html"


class TaskDetail(DetailView):
    model = Task
    context_object_name = "task"
    template_name = "main/task.html"


class TaskCreate(CreateView):
    model = Task
    fields = "__all__"
    template_name = "main/task_create.html"
    success_url = reverse_lazy("main:tasks")

    def post(self, request, *args, **kwargs):
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:tasks')
        return render(request, template_name="main/task_create.html", context={'form': form})


class TaskUpdate(UpdateView):
    model = Task
    fields = "__all__"
    template_name = "main/task_create.html"
    success_url = reverse_lazy("main:tasks")

    def form_valid(self, form):
        title = form.cleaned_data.get('title')

        if len(title) > 50:
            form.add_error('title', "The title cannot exceed 50 characters.")
            return self.form_invalid(form)

        description = form.cleaned_data.get('description')

        if len(description) > 500:
            form.add_error('description', "The description cannot exceed 500 characters.")
            return self.form_invalid(form)

        return super().form_valid(form)


class TaskDelete(DeleteView):
    model = Task
    context_object_name = "task"
    template_name = "main/task_delete.html"
    success_url = reverse_lazy("main:tasks")
