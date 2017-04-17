###########################
## Base Department Class ##
###########################
class Department(object):
  """Parent class for all departments

  Methods: __init__, get_name(), get_supervisor(), meet(), get_budget(),
  add_employee(), remove_employee(), get_employees()
  """

  def __init__(self, name, supervisor, employee_count):
      self.name = name
      self.supervisor = supervisor
      self.size = employee_count
      self.employees = []
      # Department.budget serves as the base budget for derived Department classes
      Department.budget = 10000

  def get_name(self):
    """Returns the name of the department"""

    return self.name

  def get_supervisor(self):
    """Returns the name of the supervisor"""
    return self.supervisor

  def meet():
    """ Provides instructions regarding meetings for employees """
    print("Everyone meet in {}'s office".format(self.supervisor))  

  
  def get_budget(self):
    """Returns the budget for respective Department instance"""
    return self.budget


  def add_employee(self, employee):
    """Adds an employee to the set, employee accepts existing instances of employee"""
    self.employees.append(employee)
    return self.employees


  def remove_employee(self, employee):
    """Removes an employee to the set, employee accepts existing instances of employee""" 
    self.employees.remove(employee)
    return self.employees 


  def get_employees(self):
    """Returns the set of employees for the department instance"""  
    print("Department:", self.name)
    for employee in self.employees:
      print("   ", employee.fn, employee.ln)


#########################
## HR Department Class ##
#########################
class HumanResources(Department):
  """Class for representing Human Resources department

  Methods: __init__, add_policy, get_policy, meet(), get_budget, etc.
  """

  def __init__(self, name, supervisor, employee_count):
    super().__init__(name, supervisor, employee_count)
    self.policies = {}


  def add_policy(self, policy_name, policy_text):
    """Adds a policy, as a tuple, to the set of policies

    Arguments:
      policy_name (string)
      policy_text (string)
    """
    self.policies.add((policy_name, policy_text)) 

  def meet():
    """ This overrides the base meet() class completely """  
    print("All HR professionals please meet in the Human Resources Conference Room")

  def get_budget(self):
    """Returns the budget for respective Department instance"""
    
    self.budget = Department.budget + 2000
    return self.budget 


#########################
## IT Department Class ##
#########################
class InformationTechnology(Department):
  """Class for representing IT department

  Methods: __init__, add_security_policy, get_security_policy, add_tech_manual, get_tech_manual, meet(), get_budget()
  """

  def __init__(self, name, supervisor, employee_count):
    super().__init__(name, supervisor, employee_count)
    self.security_policies = {}
    self.tech_manuals = {}

  def add_security_policy(self, policy_name, policy_text):
    """Adds a security policy, as a tuple, to the set of policies

    Arguments:
      policy_name (string)
      policy_text (string)
    """
    self.security_policies.add((policy_name, policy_text)) 

  def add_tech_manual(self, manual_name, manual_text):
    """Adds a tech manual, as a tuple, to the set of manuals

    Arguments:
      manual_name (string)
      manual_text (string)
    """
    self.tech_manuals.add((manual_name, manual_text))   

  def meet():
    """ This overrides the base meet() class completely """  
    print("IT staff meet in the IT conference room")  

  def get_budget(self):
    """Returns the budget for respective Department instance"""
    
    self.budget = Department.budget + 15000
    return self.budget 


############################
## Sales Department Class ##
############################
class Sales(Department):
  """Class for representing Sales department

  Methods: __init__, add_sales_policy, get_sales_policy, add_sales_presentation, 
  get_sales_presentation, meet, get_budget
  """

  def __init__(self, name, supervisor, employee_count):
    super().__init__(name, supervisor, employee_count)
    self.sales_policies = {}
    self.sales_presentations = {}

  def add_sales_policy(self, policy_name, policy_text):
    """Adds a policy, as a tuple, to the set of sales policies

    Arguments:
      policy_name (string)
      policy_text (string)
    """
    self.policies.add((policy_name, policy_text))

  def add_sales_presentation(self, presentation_name, presentation_text):
    """Adds a presentation, as a tuple, to the set of sales presentations

    Arguments:
      presentation_name (string)
      presentation_text (string) """
    
    self.sales_presentation.add((presentation_name, presentation_text))  

  def meet():
    """ This overrides the base meet() class completely """  
    print("All Salespeople meet in the Parking Lot")  

  def get_budget(self):
    """Returns the budget for respective Department instance"""
    
    self.budget = Department.budget + 7000
    return self.budget 


################################
## Marketing Department Class ##
################################
class Marketing(Department):
  """Class for representing Marketing department

  Methods: __init__, add_advertising_policy, get_advertising_policy, add_advertiser,
  get_advertiser etc.
  """

  def __init__(self, name, supervisor, employee_count):
    super().__init__(name, supervisor, employee_count)
    self.advertising_policies = {}
    self.advertisements = {}
    self.advertisers = {}

  def add_advertising_policy(self, policy_name, policy_text):
    """Adds a policy, as a tuple, to the set of advertising policies

    Arguments:
      policy_name (string)
      policy_text (string)
    """
    self.policies.add((policy_name, policy_text))

  def add_advertisement(self, advertisement_name, advertisement_text):
    """Adds an advertisement, as a tuple, to the set of advertisements

    Arguments:
      advertisement_name (string)
      advertisement_text (string)
    """
    self.advertisements.add((advertisement_name, advertisement_text))  

  def add_advertiser(self, advertisor_name, advertiser_contact):
    """Adds an advertiser, as a tuple, to the set of advertisers

    Arguments:
      advertiser_name (string)
      advertiser_contact (string)
    """
    self.advertisers.add((advertisor_name, advertiser_contact))      

  def meet():
    """ This overrides the base meet() class completely """  
    print("All Marketing employees meet in the Social Media War Room")

  def get_budget(self):
    """Returns the budget for respective Department instance"""
    
    self.budget = Department.budget + 11000
    return self.budget 



