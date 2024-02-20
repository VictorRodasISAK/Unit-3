# Quiz 044
## Download the database cmoon.db from the learning Log, and write the SQL statements to solve the questions below:
### Answers of the questions below:

1) How many tables are there in the database?
R\\ 3 Tables, Inhabitant, Item, and Village.
2) How many Male inhabitants are Friendly?
R\\ 4
3) What is the average gold by village?
R\\ Slowville: 112.5, Steepmount: 137.5, Stoneville: 129.17, Wetriver: 118.75
4) How many items are there that start with the letter “A”
R\\ 3
5) How many different jobs are there? 
R\\ 15 different jobs
6) What are the items owned by the herbalists?
R\\ Daggers

### SQL statements to solve the questions below:
```sql
-- 1) How many tables are there in the database?
SELECT COUNT(*) FROM sqlite_master WHERE type='table';

-- 2) How many Male inhabitants are Friendly?
select * from INHABITANT where gender = 'Male' and state = 'Friendly';

-- 3) What is the average gold by village?
select avg(gold), V.name from INHABITANT join VILLAGE V
on V.villageid = INHABITANT.villageid group by V.name;

-- 4) How many items are there that start with the letter “A”
select count(*) from ITEM where item like 'a%';

-- 5) How many different jobs are there?
select count(distinct job) from INHABITANT;

-- 6) What are the items owned by the herbalists?
select * from INHABITANT where job like '%herba%';
select * from ITEM where owner = 4 or owner = 18;
```
### Screenshots of the results:

1) How many tables are there in the database?


![Screen Shot 2024-02-17 at 14.48.19.png](Quiz_044_Images%2FScreen%20Shot%202024-02-17%20at%2014.48.19.png)


*Fig.1* Tables in the database
2) How many Male inhabitants are Friendly?


![Screen Shot 2024-02-17 at 14.49.38.png](Quiz_044_Images%2FScreen%20Shot%202024-02-17%20at%2014.49.38.png)


*Fig.2* Male inhabitants that are friendly
3) What is the average gold by village?


![Screen Shot 2024-02-17 at 14.51.07.png](Quiz_044_Images%2FScreen%20Shot%202024-02-17%20at%2014.51.07.png)


*Fig.3* Average gold by village
4) How many items are there that start with the letter “A”?


![Screen Shot 2024-02-17 at 14.53.09.png](Quiz_044_Images%2FScreen%20Shot%202024-02-17%20at%2014.53.09.png)


*Fig.4* Items that start with the letter "A"
5) How many different jobs are there?


![Screen Shot 2024-02-17 at 14.54.04.png](Quiz_044_Images%2FScreen%20Shot%202024-02-17%20at%2014.54.04.png)


*Fig.5* Different jobs
6) What are the items owned by the herbalists?


![Screen Shot 2024-02-17 at 14.54.42.png](Quiz_044_Images%2FScreen%20Shot%202024-02-17%20at%2014.54.42.png)


*Fig.6* Items owned by the herbalists

### ER Diagram of the database:
![ER_Diagram.png](Quiz_044_Images%2FER_Diagram.png)

*Fig.7* ER Diagram of the database