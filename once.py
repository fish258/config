#!/usr/bin/python
x = 0
f = open("AutoCreateAlarm","r+")
a = f.readlines()
if a[2].strip()=="count=0":
    x = 1
    print(1)
f.close()
f = open("AutoCreateAlarm","r+")
f.writelines("#!/usr/bin/python\nimport os\ncount=1")
f.close()
