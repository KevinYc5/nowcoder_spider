import pymysql
from scrapyspider import settings
# 用于数据库存储
class DBPipeline(object):
    def __init__(self):
        # 连接数据库
        self.connect = pymysql.connect(
            host=settings.MYSQL_HOST,
            port=3306,
            db=settings.MYSQL_DBNAME,
            user=settings.MYSQL_USER,
            passwd=settings.MYSQL_PASSWD,
            charset='utf8',
            use_unicode=True)

        # 通过cursor执行增删查改
        self.cursor = self.connect.cursor();

    def process_item(self, item, spider):
        try:
            # 插入数据
            self.cursor.execute(
                """insert into doubanmovie(name, ranking, score, num)
                value (%s, %s, %s, %s)""",
                (item['movie_name'],
                 item['ranking'],
                 item['score'],
                 item['score_num']))

            # 提交sql语句
            self.connect.commit()

        except Exception as error:
            print("0")
            # 出现错误时打印错误日志
            # log(error)
        return item