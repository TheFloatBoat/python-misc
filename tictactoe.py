class TicTacToe:
  def __init__(self):
    self.bodre=[
      ["","",""],
      ["","",""],
      ["","",""]]
  def set_number(self, location, user):
    if self.bodre[location // 3][location % 3] != "":
      print("Invalid location!")
    else:
        self.bodre[location // 3][location % 3] = user
      
  def check_winner(self):
    for i in range(3):
      if self.bodre[i][0] == self.bodre[i][1] == self.bodre[i][2] != "":
        return True, self.bodre[i][0]
      if self.bodre[0][i] == self.bodre[1][i] == self.bodre[2][i] != "":
        return True, self.bodre[0][i]
      if self.bodre[0][0] == self.bodre[1][1] == self.bodre[2][2] != "":
        return True, self.bodre[0][1]
      if self.bodre[0][2] == self.bodre[1][1] == self.bodre[2][0] != "":
        return True, self.bodre[0][2]
    return False, None
  def begin(self):
    while True:
      turn = int(input(">>>"))
      game.set_number(turn, "x")
      print(self.bodre[0])
      print(self.bodre[1])
      print(self.bodre[2])
      turn = int(input(">>>"))
      game.set_number(turn, "o")
      print(self.bodre[0])
      print(self.bodre[1])
      print(self.bodre[2])
game=TicTacToe()
game.begin()
