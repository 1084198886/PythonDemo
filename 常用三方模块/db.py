"""
访问数据库
"""

import sqlite3

try:
    conn = sqlite3.connect('ecard_nc_dtl_db.db')
    cursor = conn.cursor()
    # cursor.execute('select * from tb_transdtl where  recno in (?,?)', (110, -1))
    # cursor.execute('select * from tb_transdtl where  recno=? and 1=1', (110,))
    # cursor.execute('select * from tb_transdtl')
    values = cursor.fetchall()  # 结果集是一个list
    # cursor.execute(r"-- insert into tb_credit_limitcnt values ('adjfksdflk',1,'20220825',1)")
    cursor.execute('create table t_user (id varchar(20) primary  key,'
                   'name varchar(20))')
    # print(values)
    print('rowcount=', cursor.rowcount)
    conn.commit()
except Exception as e:
    print(e)
finally:
    cursor.close()
    conn.close()

# import mysql.connector
#
# conn = mysql.connector.connect(user='root', password='password', database='test')
# cursor = conn.cursor()
#
# from sqlalchemy import Column, String, create_engine
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.ext.declarative import declarative_base
#

from  mymodule import  *