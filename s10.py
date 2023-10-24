import pymysql
#                     localhost
db = pymysql.connect(host='127.0.0.1', user='root', password='root')
cursor = db.cursor()
# cursor.execute("SELECT * FROM shop.fruits WHERE name like '%gilan%' AND price<50000 ORDER BY price;")
# info = cursor.fetchall() # fetch  برو همه رو بیار
# info = cursor.fetchmany(5) # برو چند تا رو بیار
# for item in info:
#     print(item)
# info = cursor.fetchone() # برو یه دونه رو بیار
# print(info)
cursor.execute("DELETE FROM `shop`.`fruits` WHERE (`id` = '58');")
db.commit()