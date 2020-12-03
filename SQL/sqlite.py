import sqlite3

conn = sqlite3.connect('test.db')
cusor = conn.cursor()

'''cusor.execute('create table user (id varchar(20) primary key,name varchar(20))')
cusor.execute('insert into user (id,name) values (\'1\',\'Michael\')')

# 通过rowcount获得插入的行数:
# 使用Cursor对象执行insert，update，delete语句时，执行结果由rowcount返回影响的行数，就可以拿到执行结果
print(cusor.rowcount)
'''

# 如果SQL语句带有参数，那么需要把参数按照位置传递给execute()方法，有几个?占位符就必须对应几个参数，例：
# cursor.execute('select * from user where name=? and pwd=?', ('abc', 'password'))
cusor.execute('select * from user where id=?', ('1',))

# 使用Cursor对象执行select语句时，通过fetchall()可以拿到结果集。结果集是一个list，每个元素都是一个tuple，对应一行记录
# 比如[('1', 'Michael')]
values = cusor.fetchall()
print(values)

# Connection和Cursor对象，打开后一定记得关闭，就可以放心地使用
# 确保出错的情况下也关闭掉Connection对象和Cursor对象呢？请回忆try:...except:...finally:...的用法
cusor.close()
conn.commit()
conn.close()
