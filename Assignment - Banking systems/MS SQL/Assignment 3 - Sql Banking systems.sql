--ASSIGNMENT – 3 ( SQL & OOPS Banking System )


--Task1 : Database design

--1. Create the database named "HMBank" 

CREATE DATABASE HMbank;
use HMbank;

--2. Define the schema for the Customers, Accounts, and Transactions tables based on the provided schema 

CREATE TABLE customers(
    customer_id INT primary key,
    first_name VARCHAR(40),
    last_name VARCHAR(40),
    DOB DATE NOT NULL,
    email VARCHAR(40),
    phone_number VARCHAR(40),
    address VARCHAR(40)
	);


create table Accounts(
account_id int PRIMARY KEY,
customer_id int,
account_type varchar(50),
balance int,
FOREIGN KEY (customer_id) REFERENCES Customers (customer_id)
);

create table Transactions(
transaction_id int PRIMARY KEY,
account_id int,
transaction_type varchar(50),
amount int,
transaction_date date
FOREIGN KEY (account_id) REFERENCES Accounts (account_id)
);

-- Task2 : Select, Where, Between, AND, LIKE

-- 1.Insert at least 10 sample records into each of the following tables. 
-- Customers , Accounts , Transactions


insert into Customers values
(1, 'Rahul', 'K', '14-Sep-95', 'rahul@gmail.com', 1555123456, 'Mumbai'),
(2, 'Neha', 'S', '22-Jun-00', 'neha@gmail.com', 1666777888, 'Chennai'),
(3, 'Riya', 'P', '12-Oct-94', 'riya@gmail.com', 1999222333, 'Bangalore'),
(4, 'Arjun', 'R', '02-May-97', 'arjun@gmail.com', 1771888222, 'Delhi'),
(5, 'Tanvi', 'M', '30-Nov-02', 'tanvi@gmail.com', 1888555666, 'Pune'),
(6, 'Vikas', 'L', '08-Apr-91', 'vikas@gmail.com', 1888777666, 'Mumbai'),
(7, 'Nisha', 'K', '01-Feb-95', 'nisha@gmail.com', 1888777444, 'Kolkata'),
(8, 'Rahul', 'B', '19-Jul-98', 'rahulb@gmail.com', 1888666111, 'Agra'),
(9, 'Varun', 'T', '26-Dec-03', 'varun@gmail.com', 1888555222, 'Chennai'),
(10, 'Sanya', 'G', '18-Oct-96', 'sanya@gmail.com', 1888444333, 'Bangalore');

insert into Accounts values
(111, 1, 'current', 25000),
(112, 2, 'savings', 30000),
(113, 3, 'current', 5000),
(114, 4, 'savings', 40000),
(115, 5, 'savings', 2000),
(116, 6, 'current', 18000),
(117, 7, 'savings', 4000),
(118, 8, 'current', 3000),
(119, 9, 'savings', 2000),
(120, 10, 'savings', 8000);

insert into Transactions values
(221, 111, 'deposit', 2000, '03-Jul-23'),
(222, 112, 'withdrawal', 1000, '17-Jun-23'),
(223, 113, 'deposit', 2500, '25-Mar-23'),
(224, 114, 'withdrawal', 500, '12-Nov-22'),
(225, 115, 'transfer', 1500, '10-Oct-22'),
(226, 116, 'deposit', 3000, '07-Sep-23'),
(227, 117, 'withdrawal', 2000, '29-Aug-23'),
(228, 118, 'deposit', 400, '18-Jul-23'),
(229, 119, 'withdrawal', 800, '14-May-23'),
(230, 120, 'transfer', 1800, '22-Apr-23');

select * from customers;
select * from Accounts;
select * from Transactions;

-- 2.Write SQL queries for the following tasks:

-- 1.Write a SQL query to retrieve the name, account type and email of all customers.
select first_name, last_name, account_type, email from customers 
join accounts on customers.customer_id = accounts.customer_id;

-- 2. Write a SQL query to list all transaction corresponding customer.
select c.first_name, c.last_name, t.transaction_id, t.transaction_type, t.amount, t.transaction_date from customers c 
join accounts a on c.customer_id = a.customer_id 
join transactions t on a.account_id = t.account_id;



-- 3.Write a SQL query to increase the balance of a specific account by a certain amount
UPDATE Accounts SET balance = balance + (100) WHERE account_id = (101);

-- 4.Write a SQL query to Combine first and last names of customers as a full_name
       SELECT CONCAT(first_name, ' ', last_name) AS full_name FROM Customers;

-- 5.Write a SQL query to remove accounts with a balance of zero where the account type is savings.

DELETE FROM Accounts WHERE balance = 0 AND account_type = 'savings'

-- 6. Write a SQL query to Find customers living in a specific city
SELECT * FROM Customers WHERE address LIKE 'mumbai';


-- 7.Write a SQL query to Get the account balance for a specific account
 
SELECT balance FROM Accounts WHERE account_id = (114);

-- 8.Write a SQL query to List all current accounts with a balance greater than $1,000
SELECT * FROM Accounts WHERE account_type = 'current' AND balance > 1000;

 
-- 9.Write a SQL query to Retrieve all transactions for a specific account
SELECT * FROM Transactions WHERE account_id = (118);

-- 10. Write a SQL query to Calculate the interest accrued on savings accounts based on a given interest rate
SELECT account_id, balance * 0.05 AS interest_accrued FROM Accounts WHERE account_type = 'savings';
 
 
-- 11.Write a SQL query to Identify accounts where the balance is less than a specified
SELECT * FROM Accounts WHERE balance < 500;
 
-- 12.Write a SQL query to Find customers not living in a specific city
SELECT * FROM Customers WHERE address NOT LIKE 'delhi';



--TASK – 3 :
--Aggregate functions, Having, Order By, GroupBy and Joins

-- 1.Write a SQL query to Find the average account balance for all customers.
SELECT AVG(balance) AS average_balance FROM accounts;
 
-- 2. Write a SQL query to Retrieve the top 10 highest account balances.
SELECT TOP 10 * FROM accounts ORDER BY balance DESC;
 
-- 3.Write a SQL query to Calculate Total Deposits for All Customers in specific date.
SELECT SUM(amount) AS total_deposits FROM transactions
WHERE CONVERT(DATE, transaction_date) = '12-Nov-22' AND amount > 0;
 
-- 4.Write a SQL query to Find the Oldest and Newest Customers
SELECT first_name, last_name,
           	MIN(DOB) AS oldest_dob,
           	MAX(DOB) AS newest_dob
FROM Customers
GROUP BY first_name, last_name;
 
-- 5.Write a SQL query to Retrieve transaction details along with the account type
SELECT t.*, a.account_type
FROM Transactions t
INNER JOIN Accounts a ON t.account_id = a.account_id;

-- 6.Write a SQL query to Get a list of customers along with their account details
SELECT c.*, a.*
FROM Customers c
INNER JOIN Accounts a ON c.customer_id = a.customer_id;

-- 7. Write a SQL query to Retrieve transaction details along with customer information for a specific account
SELECT t.*, c.*
FROM Transactions t
INNER JOIN Accounts a ON t.account_id = a.account_id
INNER JOIN Customers c ON a.customer_id = c.customer_id
WHERE a.account_id = '115';
 
-- 8. Write a SQL query to Identify customers who have more than one account
SELECT customer_id
FROM Accounts
GROUP BY customer_id
HAVING COUNT(*) > 1;
 
-- 9. Write a SQL query to Calculate the difference in transaction amounts between deposits and withdrawal
SELECT account_id, SUM(CASE WHEN transaction_type = 'deposit' THEN amount ELSE -amount END) AS transaction_difference
FROM Transactions
GROUP BY account_id;
 
-- 10.Write a SQL query to Calculate the average daily balance for each account over a specified period.
SELECT account_id, AVG(500) AS average_daily_balance
FROM Transactions
GROUP BY account_id;

-- 11.Calculate the total balance for each account type
SELECT account_type, SUM(1000) AS total_balance
FROM Accounts
GROUP BY account_type;
 
-- 12. Identify accounts with the highest number of transactions order by descending order.
SELECT account_id, COUNT(*) AS transaction_count
FROM Transactions
GROUP BY account_id
ORDER BY transaction_count DESC;

-- 13. List customers with high aggregate account balances, along with their account types.
SELECT c.customer_id, c.first_name, c.last_name, a.account_type, SUM(a.balance) AS total_balance
FROM Customers c
INNER JOIN Accounts a ON c.customer_id = a.customer_id
GROUP BY c.customer_id, c.first_name, c.last_name, a.account_type
ORDER BY total_balance DESC;
 
-- 14.Identify and list duplicate transactions based on transaction amount, date.
SELECT t.transaction_id, t.amount, t.transaction_date, t.account_id, dup.duplicate_count
FROM Transactions t
INNER JOIN (
           	SELECT amount, transaction_date, account_id, COUNT(*) AS duplicate_count
           	FROM Transactions
           	GROUP BY amount, transaction_date, account_id
           	HAVING COUNT(*) > 1
) dup ON t.amount = dup.amount
           	AND t.transaction_date = dup.transaction_date
           	AND t.account_id = dup.account_id
          	ORDER BY t.amount, t.transaction_date, t.account_id;
 
--Task 4

-- 1.Retrieve the customer(s) with the highest account balance.
SELECT c.first_name, c.last_name, c.customer_id as max_balance
FROM Customers c
JOIN Accounts a ON c.customer_id = a.customer_id
WHERE a.balance = (SELECT MAX(balance) FROM Accounts);
                                    	
-- 2.Calculate the average account balance for customers who have more than one account.
SELECT AVG(balance) AS average_balance FROM ( SELECT customer_id
FROM Accounts
GROUP BY customer_id
HAVING COUNT(*) > 1
) AS multiple_accounts
JOIN Accounts ON multiple_accounts.customer_id = Accounts.customer_id;
 
-- 3.Retrieve accounts with transactions whose amounts exceed the average transaction amount.
select distinct a.account_id from accounts a join transactions t on a.account_id = t.account_id where t.amount > (select avg(amount) from transactions);

-- 4.Identify customers who have no recorded transactions
select c.customer_id, c.first_name from customers c left join accounts a on c.customer_id = a.customer_id left join transactions t on a.account_id = t.account_id where t.transaction_id is null;
 
-- 5.Calculate the total balance of accounts with no recorded transactions
SELECT SUM(balance) AS total_balance_no_transactions
FROM Accounts
WHERE account_id NOT IN (
	       	SELECT DISTINCT account_id
	       	FROM Transactions
);
 
-- 6.Retrieve transactions for accounts with the lowest balance.
SELECT *
FROM Transactions
WHERE account_id IN (
	       	SELECT account_id
	       	FROM Accounts
	       	WHERE balance = (SELECT MIN(balance) FROM Accounts)
);
 
-- 7.Identify customers who have accounts of multiple types
select customer_id
from accounts
group by customer_id
having count(distinct account_type) > 1;

-- 8.Calculate the percentage of each account type out of the total number of accounts.
	SELECT account_type,
	COUNT(*) * 100.0 / (SELECT COUNT(*) FROM Accounts) AS percentage
	FROM Accounts
    GROUP BY account_type;


-- 9.Retrieve all transactions for a customer with a given customer_id.
SELECT *
FROM Transactions
WHERE account_id IN (
SELECT account_id
FROM Accounts
WHERE customer_id = (customer_id)
);
 
-- 10. Calculate the total balance for each account type, including a subquery within the SELECT clause.
SELECT
account_type,
(SELECT SUM(balance) FROM Accounts WHERE account_type = A.account_type) AS total_balance
FROM Accounts A
GROUP BY account_type;
 
                                            
 
 
 
 

