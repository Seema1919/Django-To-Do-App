from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

# List all tasks
def task_list(request):
    tasks = Task.objects.all()
    return render(request, "tasks/task_list.html", {"tasks": tasks})

# Create a new task
def add_task(request):
    if request.method == "POST":
        title = request.POST["title"]
        description = request.POST.get("description", "")
        Task.objects.create(title=title, description=description)
        return redirect("task_list")
    return render(request, "tasks/add_task.html")

# Edit/update a task
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == "POST":
        task.title = request.POST["title"]
        task.description = request.POST.get("description", "")
        task.completed = "completed" in request.POST
        task.save()
        return redirect("task_list")
    return render(request, "tasks/edit_task.html", {"task": task})

# Delete a task
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect("task_list")

# Mark a task as completed
def complete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = True
    task.save()
    return redirect("task_list")
