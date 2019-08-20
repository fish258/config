# configSite
When clone this directory from this site, Run "python3 configSite/installLAMP.py" （Generally, the whole process will be finished within 3 min.）

The 4 script files are automatic calling each other once users call the first script - installLAMP.py

1. installLAMP.py will install all software the moodle site needs. And it will call installMysql.sh, which could install mysql in silence.

2. In addition, at the end of installLAMP.py, it calls mdlScript.py, which downloads moodle from github and set up some configuration.

3. At the end of mdlScript.py(After creating mysql user of moodle), it calls phpmyadmin.sh to install phpmyadmin in silence. And at the same time, it uses moodle mysql user's name as username and pwd as pwd. 
