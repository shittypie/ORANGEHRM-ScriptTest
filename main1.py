from modules import *
from e2e.TC01_LogIn import Login
from e2e.TC02_AddEmployee import EmployeeManagement

import time


if __name__ == "__main__":
    l = Login() 
    l.setup()           
    l.login()        
    ne = EmployeeManagement(l.driver)
    ne.AddEmployee()