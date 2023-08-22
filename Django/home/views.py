from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from home.models import Task
# Create your views here.
def home(request):
    context = {'success' : False}
    if request.method == "POST":
        ## HAndle the form
        title = request.POST['title']
        desc = request.POST['desc']
        print(title, desc)
        ins = Task(taskTitle = title, taskDesc = desc)
        ins.save()
        context = {'success' : True}
    return render(request, 'index.html', context)
   

def tasks(request):
    allTasks = Task.objects.all()
    context = {'tasks': allTasks}
    return render(request, 'tasks.html', context)

def delete_task(request, task_id):
    try:
        # Fetch the task with the given task_id from the database
        task_to_delete = Task.objects.get(id=task_id)
        # Delete the task
        task_to_delete.delete()
        # Redirect to the tasks view after deletion
        return redirect('tasks')
    except Task.DoesNotExist:
        # If the task does not exist, handle the error as per your requirement
        # For example, you can show an error page or redirect to the tasks page with a message.
        return render(request, 'error.html', {'message': 'Task not found'})
    

def update_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == "POST":
        # Handle the form data for updating the task
        title = request.POST['title']
        desc = request.POST['desc']
        task.taskTitle = title
        task.taskDesc = desc
        task.save()
        return redirect('tasks')

    context = {'task': task}
    return render(request, 'update_task.html', context)
