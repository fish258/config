#!/usr/bin/python3
import sys
sys.path.append("H:\\apps\\Python27\\lib\\site-package")
import cgi
import psycopg2
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import ssl
import pymysql


l=[]
conf = open('change.txt',"r")
for i in conf:
    print(i)
    test = i.split('\n')  # 这里变成了 list ['I','love','python']
    test = ''.join(test)
    print(len(test))
    l.append(test)
conf.close()
print(l)
name = l[0]
email = l[1]
moodle_pwd =l[2]
ftp_pwd=l[3]
print("Content-type: text/html\n")
print("<title>change_password</title>")
print("<body><center>")

if len(moodle_pwd)>=1 :
    conn = pymysql.connect(host="127.0.0.1",port=3306, user='root',passwd='')
    cursor=conn.cursor()

    str1 = "alter user %s@'%%' identified by '%s';" % (name, str(ftp_pwd))
    print(str1)
    SQLcmd1 = cursor.execute(str1)
    SQLcmd6 = cursor.execute("flush privileges;")
    conn.commit()
    cursor.close()
    conn.close()
else:

print("""
<form action="../PWD.html" method="GET">
    <input type="submit" value="GO BACK TO THE PAGE">
</form>
""")
print('</center></body>')
