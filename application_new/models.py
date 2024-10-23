from django.db import models
# Create your models here.
import pymysql

connection = pymysql.connect(host='127.0.0.1',port=3306,user='root',passwd='root',db='django_db1')
cursor = connection.cursor(pymysql.cursors.DictCursor)
def select_one(username,password):
    select_sql = "select username,password from django_userinfo1 where username = '%s' and password = '%s'"
    cursor.execute(select_sql,(username,password))
    ret = cursor.fetchone()

    if ret:
        return True
    else:
        return False
# select_sql()

