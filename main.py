# Name - Krisha Hemani
#      - Justin Ha
# Program - Practice
# Date - 04/09/2024
# Module 9 - Singleton
# Purpose - A game where the user navigates through a maze to find the exit without being caught by the Minotaur.

import maze
import hero
import minotaur


def main():
  """The main function"""
  m = maze.Maze()
  h = hero.Hero()
  mt = minotaur.Minotaur()
  result = ""
  lose = False

  while True:
    print(m)
    direction = str.upper(
        input(
            "Enter direction (W/A/S/D) to move the Hero left,right, up and down:"
        ))
    if direction == "W":
      result = h.go_up()
      lose = mt.move_minotaur()
    elif direction == "S":
      result = h.go_down()
      lose = mt.move_minotaur()
    elif direction == "A":
      result = h.go_left()
      lose = mt.move_minotaur()
    elif direction == "D":
      result = h.go_right()
      lose = mt.move_minotaur()
    else:
      print("Invalid Direction")
      print("Please enter W, A, S or D")
      continue

    if result == "Win":
      print(m)
      print("You found the exit! You win!")
      break
    if lose or result == "Lose":
      print(m)
      print("You got caught by the Minotaur! Game Over!")
      break


main()
