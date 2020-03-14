from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework.authentication import BasicAuthentication,TokenAuthentication,SessionAuthentication,BaseAuthentication
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework import exceptions
import requests
from .models import User, UserToken
import time
import hashlib
import random

from rest_framework.parsers import FormParser, JSONParser, FileUploadParser, MultiPartParser

from .permissions import MyPermission

from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from django.http import HttpResponse
# Create your views here.

potato_list=[]
idp=random.choice(potato_list)

def sendTextMessage(text,potato_id):
         data = {'chat_type': 2, 'chat_id': 11612720, 'text': text}
         url = 'https://api.rct2008.com:8443/{}/sendTextMessage'.format(potato_id)
         req = requests.post(url, json=data)
         print(req.text)
         # return json.loads(req.content.decode('utf-8'))
         return req.text

def get_md5(user):
    ctime = str(time.time())
    m = hashlib.md5(bytes(user, encoding='utf-8'))
    m.update(bytes(ctime, encoding='utf-8'))
    return m.hexdigest()

class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        ret = {'code': 1, 'msg': None, 'data': {}}
        # user = request._request.POST.get('username')
        # user = request._request.POST.get('username')
        user = request.POST.get('username')
        pwd = request.POST.get('password')
        obj = User.objects.filter(username=user, password=pwd).first()
        if not obj:
            ret['code'] = -1
            ret['msg'] = "用户名或密码错误"
        token = get_md5(user)
        UserToken.objects.update_or_create(user=obj, defaults={'token': token})
        ret['token'] = token
        return JsonResponse(ret)

class MyAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = request.META.get('HTTP_TOKEN')
        obj = UserToken.objects.filter(token=token).first()
        if not obj:
            raise exceptions.AuthenticationFailed('验证失败')
        else:
            return (obj.user, obj)

class CartView(APIView):
    #
    # authentication_classes = [BasicAuthentication,TokenAuthentication,SessionAuthentication]
    # permission_classes = [IsAuthenticated]
    # 自己写的认证类
    #authentication_classes = [MyAuthentication]
    #permission_classes = [MyPermission]
    # 基于jwt验证
    authentication_classes = [JSONWebTokenAuthentication]
    permission_classes = [IsAuthenticated,IsAuthenticatedOrReadOnly]
    parser_classes = [JSONParser, FormParser, MultiPartParser,FileUploadParser]
    def get(self,request,*args,**kwargs):
        #sendTextMessage('hi harry 奥林匹克好玩不？', idp)
        ctx = {
            "code": 1,
            "msg": "ok",
            "data": {
                "goods": [
                    {
                        "name": "苹果",
                        "price": 12
                    },
                    {
                        "name": "苹果1",
                        "price": 13
                    },
                ]
            }
        }
        return JsonResponse(ctx)
    def post(self, request, *args, **kwargs):
        #linux下
        # curl http://192.168.11.44:8888/api5/carts/ -X POST -H "Content-Type:application/json" -H "Authorization:JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjozLCJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNTg0Njc2NDYyLCJlbWFpbCI6ImthcnJ5d3UxMjNAZ21haWwuY29tIn0.ZXiiConuYrkvnR4b3DSYOufPoGHe0DtBOHmADcC_SP4" -d '{"text":"fool吊毛"}'
        #Windows 下
        #curl -X POST -H "Content-Type: application/json" -H "Authorization:JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjozLCJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNTg0Njc2NDYyLCJlbWFpbCI6ImthcnJ5d3UxMjNAZ21haWwuY29tIn0.ZXiiConuYrkvnR4b3DSYOufPoGHe0DtBOHmADcC_SP4" -d "{\"text\":\"foll\"}" http://192.168.11.44:8888/api5/carts/
        # print("body:", request.body.decode())
        print("content_type:", request.content_type)
        # 获取请求的值，并使用对应的JSONParser进行处理
        print("data:", request.data)
        # application/x-www-form-urlencoded 或 multipart/form-data时，request.POST中才有值
        print("POST:", request.POST)
        print("FILES:", request.FILES)
        text=request.data.get('text')

        sendTextMessage(text, idp)
        return HttpResponse('响应')
from django.contrib.auth import login