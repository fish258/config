# configSite

1. This is a automatic script group for setting up all a moodle sites for students needs. 

2. After running these scripts, students have their own moodle sites by typing own %IP_address/moodle on browser.(All basic configurations already have been set up. All the students need to do is configure their personal main administrator account which will have complete control over the site.)

3. After cloning this directory from this site, Run "python3 configSite/installLAMP.py" （Generally, the whole process will be finished within 3 min.）

4. The script files are automatic calling each other once users call the first script - installLAMP.py

(PS: Internal Running Order: installLAMP.py → installMYsql.sh → mdlScript.py → phpmyadmin.sh → ftp-script.py)


5. To access phpmyadmin to manage their database of moodle site:
Username: moodledude
Password: PWD123pwd@
When they access phpmyadmin, they can change their password to be private.

6. To access ftp system to manage their moodle site files:
① They should go to the website https://www.net2ftp.com first
② Use ip_address as FTP server
③ Use ftpuser as Username
④ Use 1234 as the Password 






#Introduction of these files:

#1. installLAMP.py will install all software the moodle site needs. And it will call installMysql.sh, which could install mysql in silence.

#2. In addition, at the end of installLAMP.py, it calls mdlScript.py, which downloads moodle from github and set up some configuration.

#3. At the end of mdlScript.py(After creating mysql user of moodle), it calls phpmyadmin.sh to install phpmyadmin in silence. And at the same time, it uses moodle mysql user's name as username and pwd as pwd. 
 