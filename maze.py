class Maze:
  """
  Represents the maze.
  Attributes: 
    _instance (Maze): The maze instance.
    _initialized (bool): A boolean to check if the maze has been initialized.
    _maze (list): A 2D list of strings representing the maze.

  __getitem__: Returns the row of the maze at the specified index.
  __len__: Returns the number of rows in the maze.
  __str__: Returns a string representation of the maze.
  search_maze: Searches for a character in the maze and returns its row and column
  """
  _instance = None
  _initialized = False

  def __new__(cls, *args):
    if cls._instance is None:
      cls._instance = super().__new__(cls)
    return cls._instance

  def __init__(self):
    if not Maze._initialized:
      with open('minomaze.txt', 'r') as file:
        lines = file.readlines()
        self._maze = []
        for line in lines:
          line = line.strip()
          chars = [char for char in line]
          self._maze.append(chars)
      Maze._initialized = True

  def __getitem__(self, row):
    return self._maze[row]

  def __len__(self):
    return len(self._maze)

  def __str__(self):
    return "\n".join("".join(row) for row in self._maze)

  def search_maze(self, ch):
    for row in range(len(self._maze)):
      for col in range(len(self._maze[row])):
        if self._maze[row][col] == ch:
          return [row, col]
