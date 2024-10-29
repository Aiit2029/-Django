from django.shortcuts import render
from django.urls import reverse

# Create your views here.




def index(request):
    print(reverse('app03:index'))

    import datetime
    s = "hello"
    l = [111, 222, 333]  # 列表
    dic = {"name": "yuan", "age": 18}  # 字典
    date = datetime.date(1993, 5, 2)  # 日期对象




    class Person(object):
        def __init__(self, name):
            self.name = name
        def dream(self):
            return 'dreamer'
    person_yuan = Person("chao")  # 自定义类对象
    person_egon = Person("yantao")
    person_alex = Person("jinxin")

    person_list = [person_yuan, person_egon, person_alex]

    return render(request, "app03_index.html", {"l": l, "dic": dic, "date": date, "person_list": person_list})
    # return render(request,'index.html',locals())
    #locals()获取函数内容所有的变量，然后通过render方法给了index.html文件进行模板渲染，如果你图省事，你可以用它，但是很多多余的变量也被传进去了，效率低