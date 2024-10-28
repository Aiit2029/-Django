import datetime

from django.views import View

from application_new import models

from django.urls import reverse

from django.http import JsonResponse, HttpResponse

from django.shortcuts import render,redirect


# Create your views here.




def index(request):
    # import datetime
    print(reverse('application_new:index'))

    now = datetime.datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    return render(request, 'index.html',{'current_time':current_time})

def login(request):
    print(request.method)



    return render(request, 'login.html')

def main(request):
    print(request.POST)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # flag = models.select_one(username,password)
        # if flag:
        #     main()
        # else:
        #     HttpResponse('登陆失败')
        if username == 'root' and password == 'root':
            return render(request, 'main.html')
        else:
            return HttpResponse('登陆失败')
    elif request.method == 'GET':
        return render(request, 'auth.html')

class myView(View):
    def get(self,request):
        return render(request, 'login.html')


def books(request,year):





    return render(request,'books.html',{'year':year})





# def get_current_time(request):
#     current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     return JsonResponse({"current_time": current_time})

# def at_init(request):
#     return render(request, 'init.html')
