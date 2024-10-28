from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views import View
from django.utils.decorators import method_decorator

# Create your views here.

def warrper(func):
    x = 1
    def inner(*args, **kwargs):
        print('加了装饰器哦')
        ret = func(*args, **kwargs)
        print('方法结束了喔')
        return ret
    return inner

# @method_decorator(warrper,name='get')  #  给 名称为 get 的方法  加装饰器
class MyViews(View):
    # @method_decorator(warrper)  第一种  给所有方法加装饰器
    def dispatch(self, request, *args, **kwargs):

        ret = super(MyViews, self).dispatch(request, *args, **kwargs)

        return ret
    # @method_decorator(warrper)  第二种 方法 单个 给get加装饰器
    def get(self, request):

        return render(request,'index.html')

    def post(self, request):

        return HttpResponse('登陆成功')