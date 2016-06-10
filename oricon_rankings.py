import urllib.request

from bs4 import BeautifulSoup
import datetime
import psycopg2


HOST = "seconddb.czxvyjraryb5.us-west-2.rds.amazonaws.com"
PORT = 5432
DATABASE = "postgres"
USER = "yasuneko"
PASSWORD = "Bazumaru"

conn = psycopg2.connect(host=HOST, port=PORT, database=DATABASE, user=USER, password=PASSWORD)

cur = conn.cursor()

url = "http://www.oricon.co.jp/rank/js/d/"

with urllib.request.urlopen(url) as response:
    html = BeautifulSoup(response.read(), 'html.parser')
    for x in html.find_all("section", {"class": "box-rank-entry"}):
        print(x.find("p", {"class": "num"}).get_text())
        print(x.find("h2", {"class": "title"}).get_text())
        print(x.find("p", {"class": "name"}).get_text())
        print(datetime.date.today())
        print('=================================================================')

        cur.execute("""
                        INSERT INTO oricon_rankings (song, artist, rank, rank_day) VALUES ('{0}', '{1}', {2}, '{3}')
                    """.format( x.find("h2", {"class": "title"}).get_text()
                                , x.find("p", {"class": "name"}).get_text(), int(x.find("p", {"class": "num"}).get_text()), datetime.date.today()))

conn.commit()

cur.execute("SELECT * FROM oricon_rankings")

for x in cur.fetchall():
    print(x)

cur.close()
conn.close()
