from django.shortcuts import render
from user_app.serializers import *
from user_app.models import *
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
# Create your views here.

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def view_company(request):
    if request.method == 'GET':
        posts = Company_register.objects.all().order_by('id')
        serialzer = Company_registerSerializer(posts, many=True)
        return Response(serialzer.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_company_application(request, id):
    try:
        post = Company_register.objects.get(pk=id) 
    except post.DoesNotExist:
        return Response(status=404)

    if request.method == 'PUT':
        serializer = Company_registerSerializer(post, data=request.data,partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

@api_view(['GET'])
def view_slot(request):
    if request.method == 'GET':
        posts = Slot.objects.all().order_by('id')
        serialzer = SlotSerializer(posts, many=True)
        return Response(serialzer.data)

@api_view(['PUT','GET'])
@permission_classes([IsAuthenticated])
def use_slot(request,sid,cid):
    slot = Slot.objects.get(id=sid)
    slot.book='True'
    slot.save()
    company=Company_register.objects.get(id=cid)
    company.slot=sid
    company.save()
    posts = Slot.objects.all().order_by('id')
    serialzer = SlotSerializer(posts, many=True)
    return Response(serialzer.data)
    
@api_view(['GET'])
def view_company_slot(request):
    if request.method == 'GET':
        print("Hello")
        posts = Company_register.objects.filter(approved=True,slot=0).order_by('id')
        serialzer = Company_registerSerializer(posts, many=True)
        return Response(serialzer.data)