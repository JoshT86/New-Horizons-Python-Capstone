import mysql.connector
from mysql.connector import Error


def create_server_connection(host_name, user_name, user_password, db_name):
    connector = None
    try:
        connector = mysql.connector.connect(
            host=host_name,
            user=user_name,
            password=user_password,
            database=db_name
        )
        print("MySql Database connection successful")
    except Error as err:
        print(f"Error: {err}")
    return connector


def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully!")
    except Error as err:
        print(f"Error: {err}")


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query Successful")
    except Error as err:
        print(f"Error: {err}")


def read_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: {err}")


create_employees_table = """
CREATE TABLE employees(
    Employee_ID VARCHAR(5) NOT NULL,
    First_name VARCHAR(50) NOT NULL,
    Last_name VARCHAR(50) NOT NULL,
    Birth_date VARCHAR(12) NOT NULL,
    Gender VARCHAR(12) NOT NULL,
    Education VARCHAR(15) NOT NULL,
    Years_Experience VARCHAR(10) NOT NULL,
    Hire_Date VARCHAR(12) NOT NULL);"""

create_salaries_table = """
CREATE TABLE salaries(
    Employee_ID VARCHAR(5) NOT NULL,
    First_name VARCHAR(50) NOT NULL,
    Last_name VARCHAR(50) NOT NULL,
    Hire_date VARCHAR(12) NOT NULL,
    Salary VARCHAR(10) NOT NULL);"""

create_department_table = """ 
CREATE TABLE department(
    Surgery VARCHAR(50) NOT NULL,
    Burn_unit VARCHAR(50) NOT NULL,
    Urgent_care VARCHAR(50) NOT NULL);"""

table_employees = """
INSERT INTO employees VALUES
("001", "james", "smith", "07/02/1958", "Male", "B.A.Sc. Bus.", "15y", "07/01/2007"),
("002", "crystal", "magnis", "01/01/2000", "Female", "R.N.", "3y", "02/15/2020"),
("003", "chantelle", "mikelson", "08/09/1996", "non-binary", "RN", "1y", "6/22/2021"),
("004", "nathan", "ford", "12/5/1970", "male", "M.D.", "15y", "01/01/2005"),
("005", "ismael", "trujillo", "10/31/1980", "male", "C.M.A.", "10y", "06/05/2011"),
("006", "johnny", "cash", "02/14/2000", "male", "R.N.", "3y", "06/24/2017"),
("007", "jessica", "damelo", "11/7/1989", "female", "B.S.N.", "4y", "08/09/2018"),
("008", "kristen", "steward", "12/20/1995", "female", "R.N.", "5y", "01/01/2019"),
("009", "sam", "tucker", "06/04/1992", "female", "C.M.A.", "2y", "07/05/2020"),
("010", "frederick", "stone", "03/15/2000", "male", "R.N.", "<12m", "06/22/2022");"""

table_salaries = """
INSERT INTO salaries VALUES
("001", "james", "smith", "07/01/2007", "$85000"),
("002", "crystal", "magnis", "02/15/2020", "$65000"),
("003", "chantelle", "mikelson", "6/22/2021", "$65000"),
("004", "nathan", "ford", "01/01/2005", "$90000"),
("005", "ismael", "trujillo", "06/05/2011", "$35000"),
("006", "johnny", "cash", "06/24/2017", "$65000"),
("007", "jessica", "damelo", "08/09/2018", "$70000"),
("008", "kristen", "steward", "01/01/2019", "$65000"),
("009", "sam", "tucker", "07/05/2020", "$35000"),
("010", "frederick", "stone", "06/22/2022", "$65000");"""

table_department = """
INSERT INTO department VALUES
("N/A", "N/A", "01BA"),
("N/A", "02RN", "02RN"),
("03RN", "03RN", "N/A"),
("04MD", "04MD", "N/A"),
("N/A", "05CMA", "05CMA"),
("06RN", "N/A", "06RN"),
("N/A", "07BSN", "07BSN"),
("08RN", "N/A", "08RN"),
("09CMA", "09CMA", "09CMA"),
("N/A", "10RN", "10RN");"""

connection = create_server_connection("localhost", "root", "student", "Hospital")
execute_query(connection, create_department_table)
execute_query(connection, create_employees_table)
execute_query(connection, create_salaries_table)

display_info = """
SELECT * FROM employees;"""

display_info = """
SELECT * FROM salaries;"""

display_info = """
SELECT * FROM department"""

execute_query(connection, table_employees)
execute_query(connection, table_salaries)
execute_query(connection, table_department)

results = read_query(connection, display_info)
for result in results:
    print(result)