name = 'Dan'
age = 99
job = "QA"
salary = 65000.75

print(name, age, job, salary)
print("Name is: ",name)
print("Age is: ",age)
print("Actual Job: ",job)
print("Salary is in Euro: ",salary)

# in one single line
# %s --> string , %d --> int , %g --> decimal , %b --> boolean
print("Name:%s Age:%d Salary:%g Job:%s" %(name,age,salary,job))
print("Age:%d Job:%s Name:%s Job:%s" %(age,salary,name,job))

# approach with *args {}
print("Name::{} Age::{} Salary::{} Job::{}" .format(name,age,salary,job))
print("name->{0} age->{1} salary->{2} job->{3}".format(name,age,salary,job))



