# BankMate: Bank Account Management System

This simple banking system application is implemented in Python using MySQL for data storage. The system provides various functionalities to manage bank account records, including inserting new records, updating existing records, deleting records, and performing transactions such as debit and credit. The application allows users to interact with a MySQL database to maintain and retrieve account details.

## Features -
- **Insert Records**: Add new bank account details into the database.
- **Display Records**: Retrieve and display all records sorted by account number.
- **Search Records**: Search for a specific bank account by its account number.
- **Update Records**: Modify existing bank account details.
- **Delete Records**: Remove a bank account record from the database.
- **Debit Transactions**: Withdraw funds from an account while ensuring a minimum balance.
- **Credit Transactions**: Deposit funds into an account.

## Technologies Used -
- **Python**:The main programming language used for the project.
- **MySQL Server**: The database system used to store and manage records.
- **MySQL Connector**: A Python library used to connect Python applications to MySQL databases.

## Installation -
1. **Clone the repository:**
    ```bash
    git clone https://github.com/dhritishetty/BankMate
    ```
2. **Install MySQL:**
    - Install MySQL on your system if not already installed.
3. **Install MySQL Connector:**
    ```bash
    pip install mysql-connector-python
    ```
4. **Set Up the Database**
   - Create a MySQL database named BankPro.
   - Create a table in the database with the following structure
      ```sql
      CREATE TABLE bank (
      accno INT PRIMARY KEY,
      name VARCHAR(255),
      mobile INT,
      email VARCHAR(255),
      address VARCHAR(255),
      city VARCHAR(255),
      balance FLOAT
      );
      ```

## Usage -
- Run the banking_system.py script to start the application.
- Follow the on-screen menu to manage bank account records.
