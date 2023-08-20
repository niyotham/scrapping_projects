import sqlite3
from employee import Employee

conn = sqlite3.connect('employees.db')
cur = conn.cursor()
cur.execute(""" CREATE TABLE if not exists employees(
             first text,
             last text,
             pay integer
            )""")

def insert_emp(emp):
    with conn:
        cur.execute("INSERT INTO employees VALUES(:first,:last,:pay)",
                {'first':emp.first, 'last': emp.last, 'pay':emp.pay})


def get_emps_by_name(lastname):
    cur.execute("SELECT * FROM employees WHERE last=:last",{'last':lastname })
    return cur.fetchall()


def update_pay(emp, pay):
    with conn:
        cur.execute(""" UPDATE employees SET pay=:pay 
                    WHERE first = :first AND last = :last""",
                    {'first': emp.first,'last': emp.last,'pay': pay }
        )


def remove_emp(emp):
    with conn:
        cur.execute(""" DELETE FROM employees WHERE first= :first AND last = :last""",
                    {'first': emp.first,'last': emp.last})

emp_1 = Employee('John', 'Doe', 80000)
emp_2 = Employee('Jane', 'Doe', 90000)
# print(employ.first)

# # #one way of inserting data into database
# # cur.execute("INSERT INTO employees VALUES(?,?,?)",(employ.first, employ.last, employ.pay))
# # conn.commit()
# # #another way of inserting data into database
# # cur.execute("INSERT INTO employees VALUES(:first,:last,:pay)",
# #             {'first':employ_1.first, 'last': employ_1.last, 'pay':employ_1.pay})
# # conn.commit()
# cur.execute("SELECT * FROM employees WHERE last=?",('Rachel',))
# print(cur.fetchall())
# cur.execute("SELECT * FROM employees WHERE last=:last",{'last':'Enias'})
# print(cur.fetchall())
# conn.commit()
insert_emp(emp_1)
insert_emp(emp_2)
emps = get_emps_by_name('Doe')
print(emps)

update_pay(emp_2, 95000)
remove_emp(emp_1)

emps = get_emps_by_name('Doe')
print(emps)
conn.close()