import psycopg2
from config import host, user, password, db_name, query
from psycopg2.extras import NamedTupleCursor
import pandas as pd
import pretty_html_table

try:
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        dbname=db_name
    )

    with connection.cursor(cursor_factory=NamedTupleCursor) as cursor:
        cursor.execute(query)
        table=cursor.fetchall()

finally:
    if connection:
        connection.close()

df = pd.DataFrame(table)
html_table=pretty_html_table.build_table(df, 'blue_light')

with open ("/var/www/html/static.html") as file:
    static = file.read()
with open ("/var/www/html/index.html", "w") as o:
    o.write(static)
    o.write(html_table)