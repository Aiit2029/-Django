from django.shortcuts import render,HttpResponse


def index(request):

    import datetime

    now = datetime.datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    # return HttpResponse('Django')
    return render(request,'index.html',{'current_time':current_time})