from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm
from django.contrib.auth.decorators import login_required


# 🏠 Home Page (List + Add Task)
@login_required(login_url='login')
def index(request):
    tasks = Task.objects.filter(user=request.user)

    # 🔍 SEARCH
    search = request.GET.get('search')
    if search:
        tasks = tasks.filter(title__icontains=search)

    # 🎯 FILTER
    status = request.GET.get('status')
    if status == 'completed':
        tasks = tasks.filter(completed=True)
    elif status == 'pending':
        tasks = tasks.filter(completed=False)

    # sort
    tasks = tasks.order_by('-created')

    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('index')

    return render(request, 'todo/index.html', {
        'tasks': tasks,
        'form': form
    })


# ✅ Mark task as completed
@login_required(login_url='login')
def complete_task(request, pk):
    task = get_object_or_404(Task, id=pk, user=request.user)
    task.completed = not task.completed  # Toggle completion
    task.save()
    return redirect('index')


# ✏️ Edit Task
@login_required(login_url='login')
def edit_task(request, pk):
    task = get_object_or_404(Task, id=pk, user=request.user)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TaskForm(instance=task)

    return render(request, 'todo/edit.html', {'form': form})


# ❌ Delete Task
@login_required(login_url='login')
def delete_task(request, pk):
    task = get_object_or_404(Task, id=pk, user=request.user)
    task.delete()
    return redirect('index')

def editTask(request, pk):
    task = get_object_or_404(Task, id=pk)

    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('index')  # ✅ IMPORTANT

    return render(request, 'todo/edit.html', {'form': form})

def completeTask(request, pk):
    task = Task.objects.get(id=pk)

    # 🔁 TOGGLE
    task.completed = not task.completed
    task.save()

    return redirect('index')  # ✅ add here (last line)