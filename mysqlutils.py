import pymysql

# # 打开数据库连接
# # db = pymysql.connect("localhost", "root", "123456", "mydb1")
# db = pymysql.connect(
#     host='localhost',
#     user='root',
#     password='123456',
#     db='mydb1',
#     charset='utf8',
#        # autocommit=True,    # 如果插入数据，， 是否自动提交? 和conn.commit()功能一致。
# )
#
# # 使用 cursor() 方法创建一个游标对象 cursor
# cursor = db.cursor()
#
# # 使用 execute()  方法执行 SQL 查询
# cursor.execute("SELECT * FROM table1")
#
# # 使用 fetchone() 方法获取单条数据.
# data = cursor.fetchall()
# for d in data:
#     print(d)
#
# # 关闭数据库连接
# db.close()
#
#


def get_movies_info_from_db():
    db = pymysql.connect(
        host='localhost',
        user='root',
        password='123456',
        db='mydb1',
        charset='utf8',
        # autocommit=True,    # 如果插入数据，， 是否自动提交? 和conn.commit()功能一致。
    )
    try:
        cursor = db.cursor()
        sql = """ select * from movie order by morder """
        print("sql:" + sql)
        cursor.execute(sql)
        movies = cursor.fetchall()
        movie_info_str_for_show = ""
        for m in movies:
            movie_info_str_for_show += str(m)+"\n"
    except Exception as e:
        raise e
    finally:
        print(movie_info_str_for_show)
        db.close()


get_movies_info_from_db()