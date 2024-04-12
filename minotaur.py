import random
import maze


class Minotaur:
  """
  Represents the Minotaur in the Minotaur Maze game.
  Attributes:
    _row (int): The row position of the Minotaur.
    _col (int): The column position of the Minotaur.

  move_minotaur: Detects where the hero is and moves the minotaur towards the hero direction.
  """

  def __init__(self):
    while True:
      self.row = random.randint(0, len(maze.Maze()) - 1)
      self.col = random.randint(0, len(maze.Maze()[0]) - 1)
      if maze.Maze()[self.row][self.col] == " ":
        maze.Maze()[self.row][self.col] = "M"
        break

  def move_minotaur(self):
    hero_location = maze.Maze().search_maze("H")
    while True and hero_location is not None:
      if abs(hero_location[0] - self.row) >= abs(hero_location[1] - self.col):
        if hero_location[0] > self.row:
          self.row += 1
          if maze.Maze()[self.row][self.col] == " " or maze.Maze()[self.row][
              self.col] == "H":
            maze.Maze()[self.row - 1][self.col] = " "
            maze.Maze()[self.row][self.col] = "M"
            break
          else:
            self.row -= 1
            if hero_location[1] > self.col:
              self.col += 1
              if maze.Maze()[self.row][self.col] == " " or maze.Maze()[
                  self.row][self.col] == "H":
                maze.Maze()[self.row][self.col - 1] = " "
                maze.Maze()[self.row][self.col] = "M"
                break
              self.col -= 1
            else:
              self.col -= 1
              if maze.Maze()[self.row][self.col] == " " or maze.Maze()[
                  self.row][self.col] == "H":
                maze.Maze()[self.row][self.col + 1] = " "
                maze.Maze()[self.row][self.col] = "M"
                break
              self.col += 1
        else:
          self.row -= 1
          if maze.Maze()[self.row][self.col] == " " or maze.Maze()[self.row][
              self.col] == "H":
            maze.Maze()[self.row + 1][self.col] = " "
            maze.Maze()[self.row][self.col] = "M"
            break
          else:
            self.row += 1
            if hero_location[1] > self.col:
              self.col += 1
              if maze.Maze()[self.row][self.col] == " " or maze.Maze()[
                  self.row][self.col] == "H":
                maze.Maze()[self.row][self.col - 1] = " "
                maze.Maze()[self.row][self.col] = "M"
                break
              self.col -= 1
            else:
              self.col -= 1
              if maze.Maze()[self.row][self.col] == " " or maze.Maze()[
                  self.row][self.col] == "H":
                maze.Maze()[self.row][self.col + 1] = " "
                maze.Maze()[self.row][self.col] = "M"
                break
              self.col += 1
      else:
        if hero_location[1] > self.col:
          self.col += 1
          if maze.Maze()[self.row][self.col] == " " or maze.Maze()[self.row][
              self.col] == "H":
            maze.Maze()[self.row][self.col - 1] = " "
            maze.Maze()[self.row][self.col] = "M"
            break
          else:
            self.col -= 1
            if hero_location[0] > self.row:
              self.row += 1
              if maze.Maze()[self.row][self.col] == " " or maze.Maze()[
                  self.row][self.col] == "H":
                maze.Maze()[self.row - 1][self.col] = " "
                maze.Maze()[self.row][self.col] = "M"
                break
              self.row -= 1
            else:
              self.row -= 1
              if maze.Maze()[self.row][self.col] == " " or maze.Maze()[
                  self.row][self.col] == "H":
                maze.Maze()[self.row + 1][self.col] = " "
                maze.Maze()[self.row][self.col] = "M"
                break
              self.row += 1
        else:
          self.col -= 1
          if maze.Maze()[self.row][self.col] == " " or maze.Maze()[self.row][
              self.col] == "H":
            maze.Maze()[self.row][self.col + 1] = " "
            maze.Maze()[self.row][self.col] = "M"
            break
          else:
            self.col += 1
            if hero_location[0] > self.row:
              self.row += 1
              if maze.Maze()[self.row][self.col] == " " or maze.Maze()[
                  self.row][self.col] == "H":
                maze.Maze()[self.row - 1][self.col] = " "
                maze.Maze()[self.row][self.col] = "M"
                break
              self.row -= 1
            else:
              self.row -= 1
              if maze.Maze()[self.row][self.col] == " " or maze.Maze()[
                  self.row][self.col] == "H":
                maze.Maze()[self.row + 1][self.col] = " "
                maze.Maze()[self.row][self.col] = "M"
                break
              self.row += 1
      if maze.Maze()[self.row +
                     1][self.col] == " " or maze.Maze()[self.row +
                                                        1][self.col] == "H":
        self.row += 1
        maze.Maze()[self.row][self.col] = "M"
        maze.Maze()[self.row - 1][self.col] = " "
        break
      elif maze.Maze()[self.row -
                       1][self.col] == " " or maze.Maze()[self.row -
                                                          1][self.col] == "H":
        self.row -= 1
        maze.Maze()[self.row][self.col] = "M"
        maze.Maze()[self.row + 1][self.col] = " "
        break
      elif maze.Maze()[self.row][self.col +
                                 1] == " " or maze.Maze()[self.row][self.col +
                                                                    1] == "H":
        self.col += 1
        maze.Maze()[self.row][self.col] = "M"
        maze.Maze()[self.row][self.col - 1] = " "
        break
      elif maze.Maze()[self.row][self.col -
                                 1] == " " or maze.Maze()[self.row][self.col -
                                                                    1] == "H":
        self.col -= 1
        maze.Maze()[self.row][self.col] = "M"
        maze.Maze()[self.row][self.col + 1] = " "
        break
    if hero_location is not None:
      if self.row == hero_location[0] and self.col == hero_location[1]:
        return True
    else:
      return True
