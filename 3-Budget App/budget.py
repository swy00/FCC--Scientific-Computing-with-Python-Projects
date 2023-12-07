class Category:
  #Constructor
  def __init__(self, nombre):
    self.name: str = nombre
    self.ledger: list = []
    self.balance: float = 0

  #Metodos de la clase
  def deposit(self, amount, description=""):
    self.balance += amount
    self.ledger.append({"amount": amount, "description": description})

  def withdraw(self, amount, description=""):
    if not (self.check_funds(amount)):
      return False
    else:
      self.ledger.append({"amount": (-1 * amount), "description": description})
      self.balance = self.balance - amount
      return True

  def get_balance(self):
    return self.balance

  def transfer(self, amount, category):
    if not (self.check_funds(amount)):
      return False
    else:
      self.withdraw(amount, "Transfer to " + category.name)
      category.deposit(amount, "Transfer from " + self.name)
      return True

  def check_funds(self, amount):
    if amount > self.balance:
      return False
    else:
      return True

  def __str__(self):
    bgt = [self.name.center(30, "*")]
    for i in self.ledger:
      desc = i["description"][0:23]
      bgt.append("{:<23}{:>7.2f}".format(desc, i["amount"]))
    bgt.append("Total: {}".format(self.balance))
    return "\n".join(bgt)

  def spent(self):
    b = 0
    for t in self.ledger:
      amount = t["amount"]
      if amount < 0:
        b += amount
    return -b

#El String quilombo
def create_spend_chart(category_list):
  spend_lst = []
  perc_spend = []
  chart = []
  s = ""

  chart.append("Percentage spent by category")

  for i in range(len(category_list)):
    spend = 0
    for j in range(len(category_list[i].ledger)):
      if category_list[i].ledger[j]["amount"] < 0:
        spend = spend + category_list[i].ledger[j]["amount"]
    spend_lst.append(abs(spend))
  total_spend = sum(spend_lst)

  for i in range(len(spend_lst)):
    perc_spend.append((spend_lst[i] / total_spend) * 100)
#Parte del porcentaje usado
  for i in reversed(range(0, 110, 10)):
    s = ("{:>3}| ".format(i))
    for j in range(len(perc_spend)):
      if perc_spend[j] >= i:
        s += "o  "
      else:
        s += "   "
    chart.append(s)
  chart.append(4 * " " + (3 * len(category_list)) * "-" + "-")
#Parte final de los nombres en vertical
  length_name = 0
  for j in range(len(category_list)):
    if len(category_list[j].name) > length_name:
      length_name = len(category_list[j].name)
  names = [c.name for c in category_list]
  for j in range(length_name):
    s = 4 * " "
    for name in names:
      s += " "
      if len(name) > j:
        s += name[j]
      else:
        s += " "
      s += " "
    chart.append(s + " ")
  return "\n".join(chart)
