class Ball:
  def __init__(self, x0, y0, r0):
    self.x = x0
    self.y = y0
    self.r = r0

    return

  def distance(self, x0, y0):
    return ((self.x-x0)**2. + (self.y-y0)**2.)**(0.5)
  
  def distance_from_origin(self):
    
    return self.distance(0,0)

  def __str__(self):
    out_str = "Radius = {}\n".format(self.r)
    out_str += "Position = ({},{})".format(self.x, self.y)
    return out_str


if __name__ == "__main__":
  ball = Ball(3, 4, 3)
  dist = ball.distance_from_origin()
  print(ball)
