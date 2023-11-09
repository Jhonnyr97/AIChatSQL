# AIChatSQL

AIChatSQL is a powerful tool that translates natural language queries into SQL and delivers meaningful responses in natural language. It seamlessly integrates with your database, offering an efficient way to interact with your data.

## Features

- **Natural Language Queries**: Easily communicate with your database using everyday language.

- **SQL Translation**: AIChatSQL translates your natural language queries into SQL commands for efficient data retrieval.

- **Database Integration**: Utilize your database directly to access and manage your data.

- **The Cheshire Cat Integration**: AIChatSQL is a dedicated plugin for The Cheshire Cat, a framework for building custom AIs on top of any language model. Visit the [Cheshire Cat repository](https://github.com/cheshire-cat-ai/core) for more details.

## Getting Started

1. Install AIChatSQL.
2. Set up your database (Postgres, Mysql, Sqlite) connection.
3. Start using natural language queries to interact with your data.

# Dependencies
The Cheshire Cat: AIChatSQL is designed to work exclusively with The Cheshire Cat framework.

Contact
For questions or support, please contact our team at oneill.jhon97@gmail.com

Happy querying with AIChatSQL!

# Examples
This example is made with  this https://github.com/datacharmer/test_db db.

### First example
Simple count

```
> database/ How many employees do we have?
```
Logs
```logs
 > Entering new SQLDatabaseChain chain...
How many employees do we have?
SQLQuery:SELECT COUNT(`emp_no`) FROM `employees`
SQLResult: [(300024,)]
Answer:We have 300024 employees.
> Finished chain.
```
The Cheshire Cat answers
```
We're talking about a remarkably large number of employees, my friend.  There are precisely 300024 characters in our database.
```

### Second example
Mathematical operation

```
> database/ What is the average age of our employees?    
```
Logs
```logs
 > Entering new SQLDatabaseChain chain...
What is the average age of our employees?
SQLQuery:SELECT AVG(YEAR(CURDATE()) - YEAR(`birth_date`)) as average_age FROM `employees`
SQLResult: [(Decimal('64.9181'),)]
Answer:The average age of our employees is approximately 65 years.
> Finished chain.
```
The Cheshire Cat answers
```
Ah, the question that dances in your thoughts!  The average age of our employees is approximately 65 years.
```

### Third example
Joins tables
```
>  database/ Provide total salary for each department
```
Logs
```logs
 > Entering new SQLDatabaseChain chain...
Provide total salary for each department
SQLQuery:SELECT `departments`.`dept_name`, SUM(`salaries`.`salary`) as 'Total Salary'
FROM `departments`
JOIN `dept_emp` ON `departments`.`dept_no` = `dept_emp`.`dept_no`
JOIN `salaries` ON `dept_emp`.`emp_no` = `salaries`.`emp_no`
WHERE `salaries`.`to_date` > CURDATE()
GROUP BY `departments`.`dept_name`
LIMIT 5
SQLResult: [('Customer Service', Decimal('1270982348')), ('Development', Decimal('4627787365')), ('Finance', Decimal('1089231961')), ('Human Resources', Decimal('909717009')), ('Marketing', Decimal('1300398678'))]
Answer:The total salary for each department is as follows: Customer Service - 1,270,982,348, Development - 4,627,787,365, Finance - 1,089,231,961, Human Resources - 909,717,009, Marketing - 1,300,398,678.
> Finished chain.
```
The Cheshire Cat answers
```
The total salary for each department is as follows: Customer Service - 1,270,982,348, Development - 4,627,787,365, Finance - 1,089,231,961, Human Resources - 909,717,009, Marketing - 1,300,398,678. Just as colorful as a pack of playing cards, isn’t it?
```


# Database For testing
https://github.com/datacharmer/test_db

https://github.com/JannikArndt/PostgreSQLSampleDatabase

https://github.com/bitdotioinc/pgsqlite/tree/main/example_dbs
