# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import calendar
from django.forms.models import model_to_dict
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .forms import UesrForm, LoginForm
from django.http import HttpResponse
from django.template import loader
from .models import admin_td, Car_td, Vister_td, carareanum, CardataApril, CardataAugust, CardataDecember, \
    CardataFebruary, CardataJanuary
from django.contrib.auth import authenticate, login as auth_login, logout
import json


def index(request):
    if request.user.is_authenticated:
        username = request.user.username
        return render(request, 'cars/index.html', {'username': username})
    else:
        username = ''
        print request.user.username
        return render(request, 'cars/index.html', {'username': username})


def register(request):
    if request.method == 'POST':
        form = UesrForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            carNum = form.cleaned_data['carNum']
            user = Vister_td(username=username, password=password, carNum=carNum, is_staff=False)
            user.save()
            auth_login(request, user)
            return HttpResponseRedirect('/cars/')

    else:
        form = UesrForm()
    return render(request, 'cars/register.html', {'form': form})


def login(request):
    error = 0
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = Vister_td.objects.filter(username=username, password=password)[0]
            if user is not None:
                auth_login(request, user)
                print request.user.username
                return HttpResponseRedirect('/cars/')
            else:
                print request.POST['username']

        except Exception:
            print "error"
            error = -1
    return render(request, 'cars/login.html', {'form': LoginForm, 'error': error})


@login_required
def log_out(request):
    logout(request)
    return HttpResponseRedirect("/cars")


@login_required
def dataView(request):
    isStaff = 0
    if request.user.is_staff:
        isStaff = 1
        # isStaff区分用户和管理员

    return render(request, 'cars/dataView.html', {'isStaff': isStaff})


@login_required
@csrf_exempt
def ajaxHcharts(request):
    if request.method == 'POST':
        json_receive = json.loads(request.body)
        isInputQuery = json_receive['isInputQuery']
        year = json_receive['year']
        month = json_receive['month']
        Num = json_receive['carID']
        s = year + '+' + month + '+' + Num
        print s
        xA = {
            'year': year,
            'month': month
        }

        # 区分用户和管理员

        if request.user.is_staff:
            isStaff = True
            carNum = None
            print 'admin'
            # 若为管理员登陆，不管carNum
        else:
            isStaff = False
            print request.user.username
            t_user = Vister_td.objects.filter(username=request.user.username)[0]
            print t_user.carNum
            carNum = t_user.carNum
            # 若为用户登陆，获取其车牌号

        if not isInputQuery and isStaff:
            # 此处为管理员查询 所有车辆
            # 此处你需要写
            if (xA['month'] == '0'):
                a = Car_td.objects.filter(entertime_year=year)
                yearList = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                for c in a:
                    index = c.entertime_month - 1
                    print index
                    print 'queryAll'
                    yearList[index] += 1
                data = yearList

            else:
                monthRange = calendar.monthrange(int(year), int(month))
                montList = [0 for x in range(0, monthRange[1])]
                a = Car_td.objects.filter(entertime_year=year, entertime_month=month)
                for c in a:
                    index = c.entertime_day - 1
                    montList[index] += 1
                data = montList

        else:
            # 此处查询为单量车（分为管理员通过车牌号查询  和  用户自行查询自己）

            # 管理员通过输入车牌号查询
            if isStaff:
                a = Car_td.objects.filter(carnum=Num).order_by('entertime_month')

                # 判断车牌号是否存在数据库
                if len(a) == 0:
                    ret = {'exist': 0, }
                    return HttpResponse(json.dumps(ret))

            # 用户自行查询自己
            else:
                a = Car_td.objects.filter(entertime_year=year, carnum=carNum).order_by('entertime_month')

            # 从数据库提取某量车某月月出入量（包括用户查询和管理员输入车牌号查询）
            if (xA['month'] == '0'):
                yearList = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                for c in a:
                    index = c.entertime_month - 1
                    yearList[index] += 1
                data = yearList
                print 'inputQuery'
                print data
                # 从数据库提取用户车辆某年年出入量
            else:
                print 'month'
                monthRange = calendar.monthrange(int(year), int(month))
                montList = [0 for x in range(0, monthRange[1])]
                if isStaff:
                    carID = Num
                    print carID
                else:
                    carID = carNum
                    print carID
                a = Car_td.objects.filter(carnum=carID, entertime_year=year, entertime_month=month)
                for c in a:
                    index = c.entertime_day - 1
                    montList[index] += 1
                data = montList
                print data

        # 汇总 接口
        returnDic = {
            'data': data,
            'xA': xA,
            'Num': Num,
            'userCarNum': carNum
        }

        return HttpResponse(json.dumps(returnDic))
    return render(request, 'cars/dataView.html')
