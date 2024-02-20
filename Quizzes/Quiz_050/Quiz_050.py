from Lessons.Lesson_Library_Login import DatabaseWorker

my_db = DatabaseWorker("../Quiz_049/bitcoin_exchange.db")
create_users = """CREATE TABLE IF NOT EXISTS Users(
                    id Integer primary key,
                    username TEXT NOT NULL unique,
                    email TEXT)"""

my_db.run_query(create_users)


# insert_query = """INSERT INTO Users (id, username, email) VALUES (560, 'bob', 'bob1@x.yz'), (371, 'bob2', 'bob2@x.yz'), (488, 'bob3', 'bob3@x.yz'),
# (561, 'bob4', 'bob4@x.yz'), (254, 'bob5', 'bob5@x.yz'), (920, 'bob6', 'bob6@x.yz'), (438, 'bob7', 'bob7@x.yz'), (744, 'bob8', 'bob8@x.yz'),
# (261, 'bob9', 'bob9@x.yz')"""
#
# my_db.run_query(insert_query)

connection_query = """Select * from ledger join Users on ledger.sender_id = users.id where ledger.sender_id = 920"""
connection_query2 = """Select * from ledger join Users on ledger.receiver_id = users.id where ledger.receiver_id = 920"""

res = my_db.search(connection_query, multiple=True) + my_db.search(connection_query2, multiple=True)
print(res)
