import mysql.connector

con = mysql.connector.connect(host='localhost',user='root',passwd='Rohit@123',database='db')
emps = con.cursor()

# emps.execute('select emp.id,emp.name,dept.name "dept" from emp,dept\
# 				where emp.deptid = dept.deptid\
# 				order by id')

# data = emps.fetchall()
# for id,name,dept in data:
# 	print(f'Id : {id} , Name : {name} , DeptName : {dept}')



# data = emps.fetchmany(3)
# for id,name,dept in data:
# 	print(f'Id : {id} , Name : {name} , DeptName : {dept}')



# data = emps.fetchone()
# print(f'Id : {data[0]} , Name : {data[1]} , DeptName : {data[2]}')


emps.execute('select emp.id,emp.name,dept.name "dept" from emp,dept\
				where emp.deptid = dept.deptid\
				order by id')
print('\n----------------------------------------------------------------\n')
print('Before Insertion : ')
print('\n----------------------------------------------------------------\n')
for id,name,dept in emps:
	print(f'Id : {id} , Name : {name} , DeptName : {dept}')
print('\n----------------------------------------------------------------\n')
id = int(input('Enter Id : '))
name = input('Enter Name : ')
deptid = int(input('Enter DeptId : '))
emps.execute(f"insert into emp values({id},'{name}',{deptid})")
con.commit()
print('\n----------------------------------------------------------------\n')
print('\n>>>>>>>>>>>   Inserted Successfully   <<<<<<<<<<<<<')
print('\n----------------------------------------------------------------\n')
print('After Insertion : ')
print('\n----------------------------------------------------------------\n')
emps.execute('select emp.id,emp.name,dept.name "dept" from emp,dept\
				where emp.deptid = dept.deptid\
				order by id')
for id,name,dept in emps:
	print(f'Id : {id} , Name : {name} , DeptName : {dept}')



