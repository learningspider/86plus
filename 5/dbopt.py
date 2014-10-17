# -*- coding: utf8 -*-
#!/usr/bin/env python

import MySQLdb,time,os

def dbopt():
    mkdir_dir="/bak/mysqlbak/"+time.strftime('%Y%m')+"/"
    if not os.path.exists(mkdir_dir): 
        os.mkdir(mkdir_dir) 
        print 'Successfully created directory', mkdir_dir 
    today_sql=mkdir_dir+'app_86plus'+'_'+time.strftime('%Y%m%d%H%M%S')+'.sql'
    sql_comm="/usr/bin/mysqldump -u %s -p'%s' %s > %s"%('root','zhouchao1850','app_86plus',today_sql) 
    if os.system(sql_comm) == 0: 
        print 'app_86plus is backup successfully'
    else: 
        print 'app_86plus is backup Failed'
    time.sleep(5) 

    try:
        conn=MySQLdb.connect(host='127.0.0.1',user='root',passwd='zhouchao1850',db='app_86plus',port=3306)
        cur=conn.cursor()
        cur.execute('drop table plus86_riqiqiandaopre')
        time.sleep(5)
        cur.execute('create table plus86_riqiqiandaopre as select * from plus86_riqiqiandao')
        time.sleep(5)
        cur.execute('drop table plus86_riqiqiandao')
        time.sleep(5)
        cur.execute('create table plus86_riqiqiandao as select * from plus86_riqiqiandaopre where 1=2')
        cur.close()
        conn.close()
    except MySQLdb.Error,e:
         print "Mysql Error %d: %s" % (e.args[0], e.args[1])

if __name__ == "__main__":
    dbopt()