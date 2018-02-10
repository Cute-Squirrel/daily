# -*- coding:utf-8 -*-
from django.shortcuts import render, redirect
from hashlib import sha1
from models import *
from datetime import datetime
from django.http import JsonResponse,HttpResponseRedirect


# Create your views here.
def register(request):
    context = {
        'title': '用户注册',
    }
    return render(request, 'userinfo/register.html', context)


def register_handle(request):
    # 接收数据
    if request.method == 'POST':
        post = request.POST
        user_name = post.get('user_name')
        user_pwd = post.get('pwd')
        user_cpwd = post.get('cpwd')
        user_email = post.get('email')
        # 密码加密
        if user_pwd != user_cpwd:
            return redirect('/user/register/')

        user_spwd = sha1(user_pwd).hexdigest()

        # 构造对象，保存
        user = UserInfo()
        user.uname = user_name
        user.upwd = user_spwd
        user.uemail = user_email
        user.udate = datetime.now()
        user.save()

        return redirect('/user/login/')


def register_exist(request):
    user_name = request.GET.get('uname')
    count = UserInfo.objects.filter(uname=user_name).count()
    return JsonResponse({'count': count})


def login(request):
    user_name=request.COOKIES.get('user_name','')
    context = {
        'title': '用户登录','error_name':0,'error_pwd':0,'user_name':user_name
    }
    return render(request, 'userinfo/login.html', context)
def login_handle(request):
    post=request.POST
    user_name=post.get('user_name')
    user_pwd=post.get('pwd')
    rember=post.get('rember',0)

    user=UserInfo.objects.filter(uname=user_name)

    if len(user)==1:
        user_spwd = sha1(user_pwd).hexdigest()
        if user_spwd==user[0].upwd:
            remb=HttpResponseRedirect('/user/info/')
            if rember!=0:
                remb.set_cookie('uname',user_name)
            else:
                remb.set_cookie('uname','',max_age=-1)
            request.session['user_id']=user[0].id
            request.session['user_name']=user_name
            return remb
        else:
            context={'title':'用户登陆','error_name':0,'error_pwd':1,'user_name':user_name,'pwd':user_pwd}
            return render(request,'userinfo/login.html',context)
    else:
        context = {'title': '用户登陆', 'error_name': 1, 'error_pwd': 0, 'user_name': user_name, 'pwd': user_pwd}
        return render(request, 'userinfo/login.html', context)




