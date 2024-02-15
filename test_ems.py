from Lab07 import Employee, EmployeeManagementSystem
import unittest



class ems_test(unittest.TestCase):
    def setUp (self):
        self.ems = EmployeeManagementSystem()
        
    def test_adding_employee(self):
        self.assertTrue(self.ems.adding_employee(1 , "tala" , 26 , "IT")) # valid input
        self.assertTrue(self.ems.adding_employee(2,"tala" , 44 , "IT")) # duplicate
        self.assertFalse(self.ems.adding_employee(2,"tala" , 44 , "IT")) # duplicate
        self.assertFalse(self.ems.adding_employee("01","tala" , 42 , "IT")) # mismatched type
        self.assertFalse(self.ems.adding_employee(8,"tala" , 400 , "IT")) # imaginary age , age max and min
        self.assertFalse(self.ems.adding_employee(9,"tala" , 2 , "IT")) # imaginary age , age max and min
        self.assertFalse(self.ems.adding_employee(10,"tala" , -1 , "IT")) # not a valid integer
        self.assertFalse(self.ems.adding_employee(11,"talaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" , 35 , "IT")) # string limit



    def test_remove_employee(self):
        self.ems.adding_employee(1,"tala" , 44 , "IT")
        self.assertTrue(self.ems.delete_employee(1)) # valid
        self.assertFalse(self.ems.delete_employee("1")) # mismatched type 
        self.assertFalse(self.ems.delete_employee(100)) # non existed ID


    def test_detail_employee(self):
        self.ems.adding_employee(9,"tala" , 44 , "IT")
        self.ems.adding_employee(99,"tala" , 44 , "IT")
        
        self.assertEqual(self.ems.employee_details(9) , 
                        {
                        "id" : 9,
                        "name" : "tala",
                        "age" : 44,
                        "dept": "IT"
                        })  # valid id
        
        self.assertIsNone(self.ems.employee_details("2"))   # non existing id
    
        self.assertIsNone(self.ems.employee_details(20))   # non existing id


if __name__ == "__main__":
        #adding_employee()
        #remove_employee()
        #detail_employee()
    unittest.main()
    print("All tests passed!")