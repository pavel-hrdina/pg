from abc import ABC, abstractmethod


class Piece(ABC):
    def __init__(self, color, position):
        """
        Inicializuje šachovou figurku.

        :param color: Barva figurky ('white' nebo 'black').
        :param position: Aktuální pozice na šachovnici jako tuple (row, col).
        """
        self.__color = color
        self.__position = position

    @abstractmethod
    def possible_moves(self):
        """
        Vrací všechny možné pohyby figurky.
        Musí být implementováno v podtřídách.

        :return: Seznam možných pozic [(row, col), ...].
        """
        pass

    @property
    @abstractmethod
    def symbol(self):
        pass

    @property
    def color(self):
        return self.__color

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, new_position):
        """
        Nastaví novou pozici figurky.
        """
        self.__position = new_position

    def __str__(self):
        return f"{self.__class__.__name__}({self.symbol}) at position {self.position}"


class Pawn(Piece):
    def possible_moves(self):
        """
        Vrací všechny možné tahy pěšce.

        :return: Seznam možných pozic [(row, col), ...].
        """
        row, col = self.position
        moves = []

        direction = 1 if self.color == "white" else -1
        moves.append((row + direction, col))

        if (self.color == "white" and row == 2) or (self.color == "black" and row == 7):
            moves.append((row + 2 * direction, col))

        return [(r, c) for r, c in moves if 0 < r <= 8 and 0 < c <= 8]

    @property
    def symbol(self):
        return "♟" if self.color == "black" else "♙"

    def __str__(self):
        return f"Pawn({self.symbol}) at position {self.position}"


class Knight(Piece):
    def possible_moves(self):
        """
        Vrací všechny možné tahy jezdce.

        :return: Seznam možných pozic [(row, col), ...].
        """
        row, col = self.position
        moves = [
            (row + 2, col + 1),
            (row + 2, col - 1),
            (row - 2, col + 1),
            (row - 2, col - 1),
            (row + 1, col + 2),
            (row + 1, col - 2),
            (row - 1, col + 2),
            (row - 1, col - 2),
        ]
        # Filtruje tahy, které jsou mimo šachovnici
        return [(r, c) for r, c in moves if 0 < r <= 8 and 0 < c <= 8]

    @property
    def symbol(self):
        return "♞" if self.color == "black" else "♘"

    def __str__(self):
        return f"Knight({self.symbol}) at position {self.position}"


class Bishop(Piece):
    def possible_moves(self):
        """
        Vrací všechny možné tahy střelce.

        :return: Seznam možných pozic [(row, col), ...].
        """
        row, col = self.position
        moves = []

        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

        for dr, dc in directions:
            for i in range(1, 8):
                new_row, new_col = row + i * dr, col + i * dc
                if 0 < new_row <= 8 and 0 < new_col <= 8:
                    moves.append((new_row, new_col))
                else:
                    break

        return moves

    @property
    def symbol(self):
        return "♝" if self.color == "black" else "♗"

    def __str__(self):
        return f"Bishop({self.symbol}) at position {self.position}"


class Rook(Piece):
    def possible_moves(self):
        """
        Vrací všechny možné tahy věže.

        :return: Seznam možných pozic [(row, col), ...].
        """
        row, col = self.position
        moves = []

        for i in range(1, 8):
            # Horizontal moves
            moves.append((row, col + i))
            moves.append((row, col - i))
            # Vertical moves
            moves.append((row + i, col))
            moves.append((row - i, col))

        return [(r, c) for r, c in moves if 0 < r <= 8 and 0 < c <= 8]

    @property
    def symbol(self):
        return "♜" if self.color == "black" else "♖"

    def __str__(self):
        return f"Rook({self.symbol}) at position {self.position}"


class Queen(Piece):
    def possible_moves(self):
        """
        Vrací všechny možné tahy dámy.

        :return: Seznam možných pozic [(row, col), ...].
        """
        row, col = self.position
        moves = []

        # Diagonal, horizontal, and vertical moves
        for i in range(1, 8):
            # Horizontal moves
            moves.append((row, col + i))
            moves.append((row, col - i))
            # Vertical moves
            moves.append((row + i, col))
            moves.append((row - i, col))
            # Diagonal moves
            moves.append((row + i, col + i))
            moves.append((row + i, col - i))
            moves.append((row - i, col + i))
            moves.append((row - i, col - i))

        # Filter out moves that go outside the board
        return [(r, c) for r, c in moves if 0 < r <= 8 and 0 < c <= 8]

    @property
    def symbol(self):
        return "♛" if self.color == "black" else "♕"

    def __str__(self):
        return f"Queen({self.symbol}) at position {self.position}"


class King(Piece):
    def possible_moves(self):
        """
        Vrací všechny možné tahy krále.

        :return: Seznam možných pozic [(row, col), ...].
        """
        row, col = self.position
        moves = [
            (row + 1, col),
            (row - 1, col),
            (row, col + 1),
            (row, col - 1),
            (row + 1, col + 1),
            (row + 1, col - 1),
            (row - 1, col + 1),
            (row - 1, col - 1),
        ]

        # Filter out moves that go outside the board
        return [(r, c) for r, c in moves if 0 < r <= 8 and 0 < c <= 8]

    @property
    def symbol(self):
        return "♚" if self.color == "black" else "♔"

    def __str__(self):
        return f"King({self.symbol}) at position {self.position}"


if __name__ == "__main__":
    piece = Knight("white", (1, 2))
    print(piece)
    print(piece.possible_moves())

    pawn = Pawn("black", (7, 2))
    print(pawn)
    print(pawn.possible_moves())

    # Test other pieces
    bishop = Bishop("white", (4, 4))
    print(bishop)
    print(bishop.possible_moves())

    rook = Rook("black", (5, 5))
    print(rook)
    print(rook.possible_moves())

    queen = Queen("white", (3, 3))
    print(queen)
    print(queen.possible_moves())

    king = King("black", (8, 8))
    print(king)
    print(king.possible_moves())
