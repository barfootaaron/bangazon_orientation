from departments import *
from departments import Department
from employees import *
from employees import Employee


if __name__ == '__main__':
  
  #########################################################################
  ## Create an instance of each class that derives from Department class ##
  #########################################################################
  hr_dept = HumanResources("Human Resources", "Dr. Feelgood", 45)

  it_dept = InformationTechnology("Information Technology", "Bill Gates", 30)

  sales_dept = Sales("Sales", "Michael Scott", 50)

  marketing_dept = Marketing("Marketing", "Mr. Charismatic", 20)

  #################################################
  ## Print names of department instances created ##
  #################################################
  print(hr_dept.name, 'led by', hr_dept.supervisor)
  print(it_dept.name, 'led by', it_dept.supervisor)
  print(sales_dept.name, 'led by', sales_dept.supervisor)
  print(marketing_dept.name, 'led by', marketing_dept.supervisor)
  
  print("---------------------------")

  ####################################################
  ## Print meeting instructions for each department ##
  ####################################################
  HumanResources.meet()
  InformationTechnology.meet()
  Sales.meet()
  Marketing.meet()
  
  print("---------------------------")

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
  
  print("---------------------------")

  #####################################################################
  ## Create insance of Employee and test all eat() method signatures ##
  #####################################################################
  kobe = Employee("Kobe", "Bryant")
  shaq= Employee("Shaq", "O'Neal")
  kevin = Employee("Kevin", "Durant")
  steph = Employee('Steph', 'Curry')

  steph.eat()

  steph.eat(food="sandwich")

  steph.eat(companions=[kobe.fn, shaq.fn, kevin.fn])

  steph.eat("cheeseburger ", [kobe.fn, shaq.fn, kevin.fn])

  print("---------------------------")

  ######################################################################
  ## Create insance of a WearhouseEmployee and HumanResourcesEmployee ##
  ######################################################################
  klay = HumanResourcesEmployee('Klay', 'Thompson')
  draymond = WarehouseEmployee('Draymond', 'Green')

  print("Klay works", klay.hours_per_week, "hours per week")
  print("Draymond works", draymond.hours_per_week, "hours per week")

  print("---------------------------")

  #########################
  ## Test add_employee() ##
  #########################
  hr_dept.add_employee(klay)
  hr_dept.add_employee(kobe)
  hr_dept.add_employee(shaq)
  # print(hr_dept.employees)

  ############################
  ## Test remove_employee() ##
  ############################
  # hr_dept.remove_employee(kobe)
  # print(hr_dept.employees)

  ##########################
  ## Test get_employees() ##
  ##########################
  hr_dept.get_employees()




