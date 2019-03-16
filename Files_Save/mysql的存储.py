import pymysql
db = pymysql.connect(host='localhost', user='root', password='52linfeibaby', port=3306, charset='utf8')
cursor = db.cursor()
'''
插入数据
data = {
    'id ': '20120001',
    'name' : 'Bob',
    'age': 20
}
table = 'students'
keys = '，'.join(data.keys())
values = '，'.join(['%s']*len(data))

创建数据库
cursor.execute('select version()')
data = cursor.fetchone()
print('Database version:', data)

更新数据
data = {
    'id ': '20120001',
    'name': 'Bob',
    'age': 21
}
table = 'students'
keys = '，'.join(data.keys())
values = '，'.join(['%s']*len(data))
'''
# 建表 sql = 'create table if not exists students (id varchar(255) not null, name varchar(255) not null, age int not null, primary key (id))'
# 插入数据 sql = 'insert into {table}({keys}) values ({values})'.format(table=table, keys=keys, values=values)
'''
更新数据
sql = 'update students set age = %s where name = %s'

sql = 'insert into {table}({keys}) values ({values}) on duplicate key update'.format(table=table, keys=keys, values=values)
update = '，'.join([" {key} = %s".format(key=key) for key in data])
sql += update

删除数据
table = 'students'
condition = 'age > 19'
sql = 'delete from {table} where {condition}'.format(table=table, condition=condition)
'''
sql = 'select * from students where age >= 19'

try:
    cursor.execute(sql)
    print('Count:', cursor.rowcount)
    row = cursor.fetchone()
    while row:
        print('Row:', row)
        row = cursor.fetchone()
except:
    print('Error')

db.close()