"""
URL configuration for DjangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, re_path,include


from application_new import views


app_name = 'application_new'
urlpatterns = [

    path('index/',views.index,name = 'index'),
    path('login/',views.login),
    path('main/',views.main),
    # path('main/',views.main),
    re_path('books/([0-9]{4})/',views.books),
    path('login/',views.myView.as_view()),


    # path('index/',views.get_current_time,name='get_current_time'),
    # path('/',views.at_init)

]
