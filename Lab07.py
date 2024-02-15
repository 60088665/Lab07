#shouq al-sheeb
#60088665
'''
You will create a Employee Management System that is capable of the following:
Done -Create a new employee with the following details: name:string, age:int, id:int, department:string
Done -Retrieve employee information by id 
Done -Delete an employee given his id
Done -Your program will use a list to save the employees. Each employee is saved as an Object that has the required information.
'''

class Employee:
    def __init__(self , id , name ,age ,dept): #objects for easy data manipulation
        self.id = id
        self.name = name
        self.age = age
        self.dept = dept


class EmployeeManagementSystem:
    def __init__ (self): #identifying self
        self.employees = []


    def adding_employee(self, id , name , age , dep):

        #checking age
        if (type(age) == int):

            #limitation
            if age > 20 and age < 45:
                result = "valid"
            else:
                #print("this job is for people age 25 to 45")
                return False
            
        else:
            #print("the age type is invalid")
            return False

        #duplicate id
        if (type(id) == int):
            for employee in self.employees:
                if id == employee.id:
                    #print("this id already exist")
                    return False

        else:
            #print("the id type is invalid")
            return False

        #string limit
        if type(name) == str and len(name) < 10:
            result = "valid"

        else:
            #print("invalid name type or length")
            return False

        #dept checking
        if type(dep) == str and len(dep) < 200:
            result = "valid"

        else:
            #print("invalid dep type or length")
            return False
        
        employee = Employee(int(id) , name ,int(age),dep)
        self.employees.append(employee)
        return True


    def all_employees(self):

        for employee in ems.employees:
            print(f"id: {employee.id}, name: {employee.name}, age: {employee.age}, dept: {employee.dept} ")

    def employee_details(self, employee_id):
        if type(employee_id) == int:           
            for employee in self.employees:
                if (int(employee_id) == employee.id):

                    obj_employee = {
                        "id" : employee.id,
                        "name" : employee.name,
                        "age" : employee.age,
                        "dept": employee.dept
                    }

                    #print(f"id: {employee.id}, name: {employee.name}, age: {employee.age}, dept: {employee.dept} ")
                    return obj_employee
        
        else:
            #print("the id type is invalid")
            return None
        
        #print("id doesnt exist")
        return None

    
    def delete_employee(self, employee_id):
        #mismatched type
        if type(employee_id) == int:           
            for employee in self.employees:
                if (int(employee_id) == employee.id):
                    self.employees.remove(employee)
                    return True
        
        else:
            #print("the id type is invalid")
            return False
        
        #print("id doesnt exist")
        return False

ems = EmployeeManagementSystem()      
#adding employees
#ems.adding_employee(1, "dalal" , 34 , "IT")
#ems.adding_employee("5", "dalal" , 24 , "IT")
#ems.adding_employee(2, "farah" , 26 , "Medical")
#ems.adding_employee(3, "sarah" , 34 , "Business")
#ems.adding_employee(4, "sbeeka" , 60 , "Lawyer")

#ems.all_employees()
#ems.employee_details(2)
ems.delete_employee(3)
#ems.all_employees()

