

class Board:

  def __init__(self, Nx0, Ny0):
    
    self.Nx = Nx0
    self.Ny = Ny0

    self.game_board = [[" " for idx in range(self.Nx)]
                          for idx in range(self.Ny)] 

    return
  
  def pretty_print(self):
    
    out_str = ""

    for iy, row in enumerate(self.game_board): 
      
      row_str = ""
      und_str = ""

      for cell in row:
        row_str += " {} |".format(cell)
        und_str += "---|"
      
      row_str = row_str[:-1] + "\n"
      und_str = und_str[:-1] + "\n"

      out_str += row_str
    
      if iy != self.Ny - 1:
        out_str += und_str

    return out_str

  def __str__(self):
    return self.pretty_print()

if __name__ == "__main__":
  gb = Board(5,4)
  print(gb)