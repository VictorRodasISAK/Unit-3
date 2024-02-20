# Quiz 049
## Use the database bitcoin_exchange.db: and create a program that calculates the total amount of bitcoins transferred for only those transactions that are valid:
### Python code
```python
from Lessons.Lesson_Library_Login import DatabaseWorker, check_hash

query = """Select * from ledger"""

my_db = DatabaseWorker("bitcoin_exchange.db")
info = my_db.search(query, multiple=True)
for row in info:
    id = row[0]
    sender_id = row[1]
    receiver_id = row[2]
    amount = row[3]
    signature = row[4]

    hash = f'id {id},sender_id {sender_id},receiver_id {receiver_id},amount {amount}'
    if check_hash(hash, signature):
        print(f"The amount of bitcoins transferred is {amount}")

my_db.close()
```

### Proof
![Quiz_049_Proof.png](Quiz_049_Proof.png)

*Fig.1* Quiz 049 Proof

### ER Diagram
![ER_Diagram49.png](ER_Diagram49.png)

*Fig.2* ER Diagram