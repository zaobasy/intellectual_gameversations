class Cell:
  
  def __init__(self, val):
    self.val = val
    return

  def __str__(self):
    return " {} ".format(self.val)

  def change_val(self, new_val):
    self.val = new_val 
    return