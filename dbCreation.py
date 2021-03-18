import sqlite3 as sql
#
con = sql.connect('flask.db')
cursor = con.cursor()
#
#
# #table creations
# cursor.execute('create table books(id integer primary key AUTOINCREMENT, name text, author text)')
#
# cursor.execute('create table tvShows(name text unique, platform text)')
#
# cursor.execute('create table games(name text,publisher text,year number)')
#
# print('table created')
#
#
# #data for books table
# cursor.execute("""insert into books(name,author)
#                  values
#                  ('To Kill a Mockingbird', 'Harper Lee'),
#                  ('1984', 'George Orwell'),
#                  ("Harry Potter and the Philosopher's Stone", 'J.K. Rowling'),
#                  ('The Lord of the Rings','J.R.R'),
#                  ('The Great Gatsby', 'F. Scott Fitzgerald'),
#                  ('Pride and Prejudice', 'Jane Austen'),
#                  ('The Diary Of A Young Girl', 'Anne Frank'),
#                  ('The Book Thief', 'Markus Zusak')
#                  """)
# print('tables inserted')
#
# con.commit()
# #data for tvshows table
#
# cursor.execute("""insert into tvShows
#                  values
#                  ('The best streaming service around by far', 'Netflix'),
#                 ('A strong selection of both popular films and TV', 'Amazon Prime Video'),
#                  ('The go-to for big name TV shows', 'Netflix'),
#                  ('The new home of Disney shows and movies','Disney Plus'),
#                  ('Live TV streaming without the hassle','YouTube TV'),
#                  ('Max', 'max')
#                  """)
# print('data inserted')
# con.commit()
#
# #data for games table
# cursor.execute("""insert into games
#                  values
#                  ("Madden NFL 2003" ,"EA Sports",2020),
#                  ("Portal 2" ,"Valve Software",2002),
#                  ("Metal Gear Solid V: The Phantom Pain", "Konami",2005),
#                  ("World of Goo", "2D Boy",2005),
#                  ("BioShock Infinite", "2K Games",2006),
#                  ("Monster Hunter World","Sony",2005),
#                  ("Titanfall 2","Sony",2006),
#                  ("Fallout 4","Sony",2007),
#                  ("Rise of the Tomb Raider","Sony",2005),
#                  ("Dishonored 2","Sony",2007),
#                  ('The Sims Series','EA Sport',2020),
#                  ('The Need For Speed Series','EA Sport',2020),
#                  ('The Madden NFL Series','2k Games', 2007),
#                  ('The Battlefield Series','EA Sport',2005)
#                  """)
# con.commit()
# # print('table created')
# result = cursor.execute("SELECT name FROM sqlite_master WHERE type = 'table'")
#
# print(result.fetchall())
# con.close()


cursor.execute('insert into games values("prince of persia sands of time","ubi soft",2014,)')
