from departments import *
from departments import Department
from employees import *
from employees import Employee

##################################################################################
## Create an instance of each class that derives from original Department class ##
##################################################################################
if __name__ == '__main__':
  # Create Department Instances
  hr_dept = HumanResources("Human Resources Department", "Dr. Feelgood", 45)
  it_dept = InformationTechnology("Information Technology Department", "Bill Gates", 30)
  sales_dept = Sales("Sales Department", "Michael Scott", 50)
  marketing_dept = Marketing("Marketing Department", "Mr. Charismatic", 20)

  #################################################
  ## Print names of department instances created ##
  #################################################
  print(hr_dept.name, 'led by', hr_dept.supervisor)
  print(it_dept.name, 'led by', it_dept.supervisor)
  print(sales_dept.name, 'led by', sales_dept.supervisor)
  print(marketing_dept.name, 'led by', marketing_dept.supervisor)

  ####################################################
  ## Print meeting instructions for each department ##
  ####################################################
  HumanResources.meet()
  InformationTechnology.meet()
  Sales.meet()
  Marketing.meet()

  ###############################################
  ## Print budget for each Department instance ##
  ###############################################
  hr_dept.get_budget()
  print("HR Department Budget = $", hr_dept.budget)

  it_dept.get_budget()
  print("IT Department Budget = $", it_dept.budget)

  sales_dept.get_budget()
  print("Sales Department Budget = $", sales_dept.budget)

  marketing_dept.get_budget()
  print("Marketing Department Budget = $", marketing_dept.budget)

  ## Create insance of Employee and test eat() method
  bill = Employee('Bill', 'Barfoot')
  bill.eat()



