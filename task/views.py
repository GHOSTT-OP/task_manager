from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Task
from .serializers import TaskSerializer
from .filters import filter_by_user, filter_by_category, filter_by_name, filter_by_creation_date, filter_by_start_date, filter_by_deadline, filter_by_private, filter_by_completed, filter_by_percentage
from .pagination import CustomPagination

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def task_view(request, pk=None):
    paginator = CustomPagination()

    if request.method == 'GET':
        tasks = Task.objects.all()

        # Filtering tasks based on query parameters
        name = request.query_params.get('name')
        if name:
            tasks = tasks.filter(name__icontains=name)

        user_id = request.query_params.get('user_id')
        if user_id:
            tasks = tasks.filter(to_user_id=user_id, from_user_id=user_id)

        category_id = request.query_params.get('category_id')
        if category_id:
            tasks = tasks.filter(category_id=category_id)

        # Paginate queryset
        result_page = paginator.paginate_queryset(tasks, request)
        serializer = TaskSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    elif request.method == 'POST':
        serializer = TaskSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save(from_user=request.user)
            return Response({"msg": "Task successfully created"}, status=status.HTTP_201_CREATED)
        return Response({"msg": "Invalid data provided", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        if pk:
            try:
                task = Task.objects.get(pk=pk)
                serializer = TaskSerializer(task, data=request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response({"msg": "Task successfully updated"})
                return Response({"msg": "Invalid data provided"}, status=status.HTTP_400_BAD_REQUEST)
            except Task.DoesNotExist:
                return Response({"msg": "Task not found"}, status=status.HTTP_404_NOT_FOUND)
        return Response({"msg": "Task ID not provided"}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        if pk:
            try:
                task = Task.objects.get(pk=pk)
                task.delete()
                return Response({"msg": "Task successfully deleted"})
            except Task.DoesNotExist:
                return Response({"msg": "Task not found"}, status=status.HTTP_404_NOT_FOUND)
        return Response({"msg": "Task ID not provided"}, status=status.HTTP_400_BAD_REQUEST)

    return Response({"msg": "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
