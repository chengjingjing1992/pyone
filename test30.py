#coding=utf-8
import pymysql
conn = pymysql.connect(host='localhost',
                    port=3306,
                    user='root',
                    passwd='123456',   # password也可以
                    db='mmall',
                    charset='utf8')   # 如果查询有中文需要指定数据库编码

# 2. 从连接建立游标（有了游标才能操作数据库）
cur = conn.cursor()

# 3. 查询数据库（读）
cur.execute("select * from mmall_user where id=13")

# 4. 获取查询结果
result = cur.fetchall()
print(result)

# 3. 更改数据库（写）
cur.execute("update mmall_user set username='gelly1' where id=13")

# 4. 提交更改
conn.commit()  # 注意是用的conn不是cur

# 5. 关闭游标及连接
cur.close()
conn.close()