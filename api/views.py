from django.db.models.fields import EmailField
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import response

from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from api import serializers
from .models import *
from rest_framework.exceptions import AuthenticationFailed
import jwt, datetime
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        "List":"/task-list/",
        "Detail View":"/task-detail/<str:pk>/",
        "Create":"/task-create/",
        "Update":"/task-update/<str:pk>/",
        "Delete":"/task-delete/<str:pk>/",
    }
    return Response(api_urls)

@api_view(['GET'])####ข้อมูลส่วนตัว
def profile_con(request):
    token = request.COOKIES.get('jwt')
    if not token:
        raise AuthenticationFailed('Unauthenticated!')

    try:
        payload = jwt.decode(token, 'secret' , algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed('Unauthenticated!')

    profile = Profile.objects.filter(id=payload['id']).first()
    serializer = ProfileSerializer(profile)

    return Response(serializer.data)
    # data = Profile.objects.all()
    # serializerprofile = ProfileSerializer(data, many=True)
    # return Response(serializerprofile.data)
@api_view(['GET'])####ข้อมูลส่วนตัว
def User_Degree_con(request):
    token = request.COOKIES.get('jwt')
    if not token:
        raise User_DegreeSerializer('Unauthenticated!')

    try:
        payload = jwt.decode(token, 'secret' , algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        raise User_DegreeSerializer('Unauthenticated!')

    user_Degree = User_Degree.objects.filter(id=payload['id']).first()
    serializer = User_DegreeSerializer(user_Degree)

    return Response(serializer.data)




@api_view(['GET'])#####เอกสาร
def Document_con(request):
    Document_data = Document.objects.all()
    serializerDocument = DocumentSerializer(Document_data, many=True)
    return Response(serializerDocument.data)

@api_view(['GET'])
def Event_con(request):
    Event_data = Event.objects.all()
    serializerEvent = EventSerializer(Event_data, many=True)
    return Response(serializerEvent.data)

@api_view(['GET'])
def Budget_con(request):
    Budget_data = Budget.objects.all()
    serializerBudget = BudgetSerializer(Budget_data, many=True)
    return Response(serializerBudget.data)

@api_view(['GET'])
def Study_leave_con(request):
    Study_leave_data = Study_leave.objects.all()
    serializerStudy_leave = Study_leaveSerializer(Study_leave_data, many=True)
    return Response(serializerStudy_leave.data)

@api_view(['GET'])
def Pending_con(request):
    Pending_data = Pending.objects.all()
    serializerPending = PendingSerializer(Pending_data, many=True)
    return Response(serializerPending.data)

@api_view(['GET'])
def Approval_con(request):
    Approval_data = Approval.objects.all()
    serializerApproval = ApprovalSerializer(Approval_data, many=True)
    return Response(serializerApproval.data)


class LoginView(APIView):
    def post(self, request):
        username = request.data['username']
        password = request.data['password']

        user =User.objects.filter(username=username).first()

        if user is None:
            raise AuthenticationFailed('User not found!')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret' ,algorithm='HS256')
        
        response = Response()

        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data ={
            'jwt' : token 
        }
            
        return response

# class UserView(APIView):

#     def get(self, request):
#         token = request.COOKIES.get('jwt')

#         if not token:
#             raise AuthenticationFailed('Unauthenticated!')

#         try:
#             payload = jwt.decode(token, 'secret', algorithm=['HS256'])
#         except jwt.ExpiredSignatureError:
#             raise AuthenticationFailed('Unauthenticated!')

#         user = User.objects.filter(id=payload['id']).first()
#         serializer = UserSerializer(user)
#         return Response(serializer.data)


class UserView(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            payload = jwt.decode(token, 'secret' , algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)

        return Response(serializer.data)

class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message' : 'success'
        }
        return response