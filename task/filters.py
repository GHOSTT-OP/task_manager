from .models import Task
from django.db.models import Q

# Filter tasks by user
def filter_by_user(user_id):
    tasks = Task.objects.filter(Q(to_user=user_id) | Q(from_user=user_id))
    return tasks

# Filter tasks by category
def filter_by_category(category_id):
    tasks = Task.objects.filter(category=category_id)
    return tasks

# Filter tasks by name (case-insensitive)
def filter_by_name(name):
    tasks = Task.objects.filter(name__icontains=name)  # Case-insensitive search
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

# Filter tasks by creation date range
def filter_by_creation_date(start_date, end_date):
    tasks = Task.objects.filter(created_at__range=[start_date, end_date])
    return tasks

# Filter tasks by start date range
def filter_by_start_date(start_date, end_date):
    tasks = Task.objects.filter(start_date__range=[start_date, end_date])
    return tasks

# Filter tasks by deadline range
def filter_by_deadline(start_date, end_date):
    tasks = Task.objects.filter(deadline__range=[start_date, end_date])
    return tasks

# Filter tasks by private status
def filter_by_private(private):
    tasks = Task.objects.filter(private=private)
    return tasks

# Filter tasks by completion status
def filter_by_completed(completed):
    tasks = Task.objects.filter(completed=completed)
    return tasks

# Filter tasks by percentage range
def filter_by_percentage(min_percentage, max_percentage):
    tasks = Task.objects.filter(percentage__range=[min_percentage, max_percentage])
    return tasks
