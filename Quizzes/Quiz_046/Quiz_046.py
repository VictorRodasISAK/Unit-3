from Lessons.Lesson_Library_Login import DatabaseWorker

haiku = """Code flows like a stream
algorithms guide its way
in silence, it solves"""

db = DatabaseWorker("Quiz046.db")
db.create()

# for word in haiku.split():
#     query = f"""INSERT INTO Words (text, length) VALUES ('{word}', {len(word)})"""
#     db.insert(query)
out = db.search("""SELECT avg(length) FROM Words""")
print("Average world length is: ", out)

db.close()