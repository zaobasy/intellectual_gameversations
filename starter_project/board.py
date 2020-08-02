from cell import Cell

class Board:

  def __init__(self, Nx0, Ny0):
    
    self.Nx = Nx0
    self.Ny = Ny0

    self.row_header = [Cell(idx) for idx in range(self.Ny)]
    self.column_header = [Cell(idx) for idx in range(self.Nx)]

    self.game_board = [[Cell(" ") for idx in range(self.Nx)]
                        for idx in range(self.Ny)] 

    return
  
  def pretty_print(self):
    
    out_str = " "*len(str(self.row_header[0]))

    for cell in self.column_header:
      out_str += "{} ".format(cell)
    out_str += "\n"

    for iy, row in enumerate(self.game_board): 
      
      row_str = str(self.row_header[iy])
      und_str = " "*len(row_str)

      for cell in row:
        cell_str = str(cell)
        row_str += "{}|".format(cell_str)
        und_str += "-"*len(cell_str) + "|"
      
      row_str = row_str[:-1] + "\n"
      und_str = und_str[:-1] + "\n"

      out_str += row_str
    
      if iy != self.Ny - 1:
        out_str += und_str

    return out_str

  def change_cell(self, ix, iy, new_val):
    self.game_board[iy][ix].change_val(new_val)
    return

  def clear_board(self):
    self.__init__(self.Nx, self.Ny)
    return

  def __str__(self):
    return self.pretty_print()

if __name__ == "__main__":
  gb = Board(6,4)
  print(gb)
  gb.change_cell(3, 2, 'a')
  gb.change_cell(1,2,'c')
  print(gb)
  gb.clear_board()
  print(gb)