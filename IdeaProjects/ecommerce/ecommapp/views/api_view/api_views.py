from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from ecommapp.serializer import AdminSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from ecommapp.models import Customer, Admin
from rest_framework import status


@csrf_exempt
@api_view(['GET', 'POST'])
def admin_list(request):
    if request.method == 'GET':
        admin = Admin.objects.all()
        serializer = AdminSerializer(admin, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = AdminSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def admin_detail(request, pk):
    try:
        admin = Admin.objects.get(pk=pk)
    except Admin.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AdminSerializer(admin, many=False)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = AdminSerializer(admin, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        admin.delete()
        return HttpResponse(status=204)
