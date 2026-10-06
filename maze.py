from stack import Stack
from cell import Cell

class Maze:
    def __init__(self, maze):
        self.currentCell = None
        self.exitCell = None
        self.entryCell = None
        self.mazeStack = Stack()
        self.exitMarker = "e"
        self.entryMarker = "m"
        self.visited = "."
        self.passage = "0"
        self.wall = "1"
        self.maze = maze

        for i in range(len(self.maze)):
            for j in range(len(self.maze[i])):

                if self.maze[i][j] == self.entryMarker:
                    self.entryCell = Cell(i, j)

                elif self.maze[i][j] == self.exitMarker:
                    self.exitCell = Cell(i, j)

        self.currentCell = self.entryCell

    def canMoveUp(self):

        x = self.currentCell.x - 1
        y = self.currentCell.y

        return self.maze[x][y] == self.passage or self.maze[x][y] == self.exitMarker

    def canMoveDown(self):

        x = self.currentCell.x + 1
        y = self.currentCell.y

        return self.maze[x][y] == self.passage or self.maze[x][y] == self.exitMarker

    def canMoveLeft(self):

        x = self.currentCell.x
        y = self.currentCell.y - 1

        return self.maze[x][y] == self.passage or self.maze[x][y] == self.exitMarker

    def canMoveRight(self):

        x = self.currentCell.x
        y = self.currentCell.y + 1

        return self.maze[x][y] == self.passage or self.maze[x][y] == self.exitMarker

    def exitMaze(self):

        self.mazeStack.push(self.currentCell)
        while not self.currentCell.equals(self.exitCell):
            linha = self.maze[self.currentCell.x]

            self.maze[self.currentCell.x] = (
                linha[:self.currentCell.y]
                + self.visited
                + linha[self.currentCell.y + 1:]
            )
            if self.canMoveUp():
                self.mazeStack.push(
                    Cell(
                        self.currentCell.x - 1,
                        self.currentCell.y
                    )
                )
            if self.canMoveDown():
                self.mazeStack.push(
                    Cell(
                        self.currentCell.x + 1,
                        self.currentCell.y
                    )
                )
            if self.canMoveLeft():
                self.mazeStack.push(
                    Cell(
                        self.currentCell.x,
                        self.currentCell.y - 1
                    )
                )
            if self.canMoveRight():
                self.mazeStack.push(
                    Cell(
                        self.currentCell.x,
                        self.currentCell.y + 1
                    )
                )
            if self.mazeStack.is_empty():
                print("Caminho não encontrado.")
                return
            self.currentCell = self.mazeStack.pop()


def inicializar_labirinto(linhas):

    mazeRows = Stack()
    maze = []
    quantidade_colunas = len(linhas[0])
    maze.append("1" * (quantidade_colunas + 2))

    for linha in linhas:
        linha = "1" + linha + "1"
        mazeRows.push(linha)

    while not mazeRows.is_empty():

        maze.append(mazeRows.pop())

    maze.append("1" * (quantidade_colunas + 2))
    return maze