import datetime
import psycopg2

host = "seconddb.czxvyjraryb5.us-west-2.rds.amazonaws.com"
port = 5432
database = "postgres"
user = "yasuneko"
password = "Bazumaru"

conn = psycopg2.connect(host=host, port=port, database=database, user=user, password=password)

cur = conn.cursor()

sql = """ drop table oricon_rankings
      """

cur.execute(sql)

sql = """
    CREATE TABLE oricon_rankings( id serial PRIMARY KEY, song varchar(255), artist varchar(255), rank integer, rank_day date )
"""

cur.execute(sql)

conn.commit()

# cur.execute("""
#
#    insert into oricon_rankings (song, artist, rank_day) VALUES ('test_song', 'test_artist', '{0}')
#    """.format(datetime.date.today()))

# conn.commit()

#cur.execute("SELECT * FROM oricon_rankings")

# for x in cur.fetchall():
#    print(x)

cur.close()
conn.close()
