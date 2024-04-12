import maze


class Hero:
  """
  Represents the Hero in the Maze game.
  Attributes:
    _row (int): The row position of the Hero.
    _col (int): The column position of the Hero.

  go_up: Moves the Hero up one row if it is not a wall.
  go_down: Moves the Hero down one row if it is not a wall.
  go_left: Moves the Hero left one column if it is not a wall.
  go_right: Moves the Hero right one column if it is not a wall.
  """
  def __init__(self):
    self.row = 1
    self.col = 1
    maze.Maze()[self.row][self.col] = "H"

  def go_up(self):
    self.row -= 1
    if maze.Maze()[self.row][self.col] == "*":
      self.row += 1
      print("You ran into a wall!")
    elif maze.Maze()[self.row][self.col] == "f":
      maze.Maze()[self.row][self.col] = "H"
      maze.Maze()[self.row + 1][self.col] = " "
      return "Win"
    elif maze.Maze()[self.row][self.col] == "M":
      maze.Maze()[self.row + 1][self.col] = " "
      return "Lose"
    else:
      maze.Maze()[self.row][self.col] = "H"
      maze.Maze()[self.row + 1][self.col] = " "
    print()

  def go_down(self):
    self.row += 1
    if maze.Maze()[self.row][self.col] == "*":
      self.row -= 1
      print("You ran into a wall!")
    elif maze.Maze()[self.row][self.col] == "f":
      maze.Maze()[self.row][self.col] = "H"
      maze.Maze()[self.row - 1][self.col] = " "
      return "Win"
    elif maze.Maze()[self.row][self.col] == "M":
      maze.Maze()[self.row - 1][self.col] = " "
      return "Lose"
    else:
      maze.Maze()[self.row][self.col] = "H"
      maze.Maze()[self.row - 1][self.col] = " "
    print()

  def go_left(self):
    self.col -= 1
    if maze.Maze()[self.row][self.col] == "*":
      self.col += 1
      print("You ran into a wall!")
    elif maze.Maze()[self.row][self.col] == "f":
      maze.Maze()[self.row][self.col] = "H"
      maze.Maze()[self.row][self.col + 1] = " "
      return "Win"
    elif maze.Maze()[self.row][self.col] == "M":
      maze.Maze()[self.row][self.col + 1] = " "
      return "Lose"
    else:
      maze.Maze()[self.row][self.col] = "H"
      maze.Maze()[self.row][self.col + 1] = " "
    print()

  def go_right(self):
    self.col += 1
    if maze.Maze()[self.row][self.col] == "*":
      self.col -= 1
      print("You ran into a wall!")
    elif maze.Maze()[self.row][self.col] == "f":
      maze.Maze()[self.row][self.col] = "H"
      maze.Maze()[self.row][self.col - 1] = " "
      return "Win"
    elif maze.Maze()[self.row][self.col] == "M":
      maze.Maze()[self.row][self.col - 1] = " "
      return "Lose"
    else:
      maze.Maze()[self.row][self.col] = "H"
      maze.Maze()[self.row][self.col - 1] = " "
    print()
