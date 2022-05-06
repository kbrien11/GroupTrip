from django.shortcuts import render

# Create your views here.


from django.contrib.auth.models import User
import threading
from django.contrib.auth.hashers import check_password,make_password
from rest_framework.views import Response
from .models import Plan,Message
from rest_framework.decorators import action,api_view
from rest_framework.authtoken.models import Token
from rest_framework import status
from .serializers import UserSerializer,PlanSerializer,MessageSerializer




@api_view(['POST'])
def createUser(request):
        password = request.data.get("password")
        serializer = UserSerializer(data=request.data)
        print(password)
        if serializer.is_valid():
            serializer.validated_data['is_active'] = False
            serializer.save()
            user = User.objects.filter(username=serializer.data['username']).first()
            token = Token.objects.get(user=user)
            print(token)
            # data = {
            #     'Messages': [
            #         {
            #             "From": {
            #                 "Email": "kbrien11@gmail.com",
            #                 "Name": "Keith"
            #             },
            #             "To": [
            #                 {
            #                     "Email": email,
            #                     "Name": first_name
            #                 }
            #             ],
            #             "Subject": "Thank you for registering",
            #             "TextPart": "My first Mailjet email",
            #             "HTMLPart": "<h3> Hi {}, thank you for signing up. Feel free to create a league or join an existing one. Goodluck on your boxes".format(str(first_name))
            #
            #         }
            #     ]
            # }
            # result = mailjet.send.create(data=data)
            # print(result.json)
            return Response({"data":serializer.data, "token":token.key})
        else:
            return Response({"error":"errro"})




@api_view(['POST'])
def login(request):
    email = request.data.get("email")
    password = request.data.get("password")
    user_obj = User.objects.filter(email__iexact=email).first()
    ser = UserSerializer(instance=user_obj,data=request.data, many=False, partial=True)
    if ser.is_valid():
        if user_obj:
            # validate_password = check_password(password, str(ser.validated_data['password']))
            # print(str(ser.validated_data['password']) == str(password))
            if str(ser.validated_data['password']) == str(password):
                token = Token.objects.get(user=user_obj)
                ser.validated_data['is_active'] = True
                if ser.validated_data['is_active'] == True:
                    ser.save()
                    print(token.key)
                    return Response({'token': token.key,"active":ser.data['is_active'],'user':ser.data['username']})
            else:
                print("error logging in")
                return Response({"passwordError": "invalid password"})
        else:
            print("email is wrong")
            return Response({"EmailError": "invalid email"})


@api_view(['POST'])
def sendMessage(request,token,groupName):
    user = Token.objects.get(key = token).user
    print(user)
    user_obj = User.objects.filter(username=user).first()
    print(user_obj)

    mess = request.data.get("message")
    date = request.data.get("date")
    new_message = Message(date = date,message = mess,username = user,group_name = groupName)
    if new_message:
        new_message.save()
        return Response({"data":new_message.message})
    else:
        print("error")

@api_view(['GET'])
def viewMessages(request,token,groupName):
    messages = Message.objects.filter(group_name=groupName).all()
    messages_ser = MessageSerializer(messages,many=True)
    if messages_ser.data:
        return Response({"data":messages_ser.data})
    else:
        return Response({"error":"getting messages"})


@api_view(['GET'])
def getUsersPerGroup(request,groupName,token):
    user = Token.objects.get(key=token).user
    print(user)
    output = []
    data = Message.objects.filter(group_name=groupName).all()
    data_ser = MessageSerializer(data,many=True)
    for i in data_ser.data:
        print(str(i['username']) == str(user))
        if i['username'] in output or str(i['username']) == str(user):
            continue
        else:
            print(i)
            output.append(i)

    return Response({"data":output})


@api_view(['GET'])
def checkActiveUser(request,username):
    user = User.objects.filter(username=username).first()
    user_ser = UserSerializer(user,many=False)
    if user_ser:
        return Response({"active":user_ser.data['is_active']})
    else:
        print("error")

@api_view(['GET'])
def logout(request,username):
    user = User.objects.filter(username=username).first()
    user_ser = UserSerializer(instance=user,data=request.data, many=False, partial=True)
    if user_ser.is_valid():
        user_ser.validated_data['is_active'] = False
        user_ser.save()
        return Response({"active": user_ser.data['is_active']})
    else:
        print("error")