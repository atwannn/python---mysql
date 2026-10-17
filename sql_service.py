import os
import pymysql
import dotenv
dotenv.load_dotenv() 



conn = pymysql.Connection(
    host=os.getenv('SQL_HOST'),
    password=os.getenv('SQL_PASSWORD'),
    user=os.getenv('SQL_USER'),
    database=os.getenv('SQL_DATABASE')

)
print('mysql is up!')

