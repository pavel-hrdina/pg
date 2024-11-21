from abc import ABC, abstractmethod


class Piece(ABC):
    """
    Abstraktní třída reprezentující šachovou figurku.

    """

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

    @staticmethod
    def is_position_on_board(position):
        return 1 <= position[0] <= 8 and 1 <= position[1] <= 8

    @property
    def color(self):
        return self.__color

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, new_postion):
        self.__position = new_postion

    def __str__(self):
        return f"Piece({self.color}) at position {self.position}"


#     Šachovnice odvozená od možných pohybů figurky Knight
#     Tvoří se z dvojrozměrného pole, kde každá pozice
#     obsahuje row a col souřadnice, kde se figurka může nacházet.
#
#     Figurka se nikdy nemůže pohybovat mimo šachovnici.
#
#     Pokud je figurka Knight na pozici (1, 2), může se pohybovat
#     na pozice (W) (3, 3), (3, 1) a (2, 4). To vyplývá z pravidel šachové hry.
#
#     8  .  .  .  .  .  .  .  .
#     7  .  .  .  .  .  .  .  .
#     6  .  .  .  .  .  .  .  .
#     5  .  .  .  .  .  .  .  .
#     4  .  W  .  .  .  .  .  .
#     3  .  .  W  .  .  .  .  .
#     2  K  .  .  .  .  .  .  .
#     1  .  .  W  .  .  .  .  .
#         1  2  3  4  5  6  7  8


class Pawn(Piece):
    def possible_moves(self):
        """
        Vrací všechny možné tahy pěšce. Pěšec se může pohybovat o jedno nebo
        dvě pole vpřed, to zde není implementováno, z důvodu jednoduchosti a
        zbytečnosti pro tento úkol.

        :return: Seznam možných pozic [(row, col), ...].
        """
        row, col = self.position
        # v závislosti na barvě pěšce se může pohybovat jinak
        if self.color == "white":
            moves = [(row + 1, col)]
            if row == 7:
                moves.append((row - 2, col))
        # blok else platí pro černého pěšce, kteý se pohybuje od 8 do 1
        else:
            moves = [(row - 1, col)]
            if row == 2:
                moves.append((row + 2, col))

        # Filtruje tahy, které jsou mimo šachovnici
        final_moves = []
        for move in moves:
            if self.is_position_on_board(move):
                final_moves.append(move)
        return final_moves

    def __str__(self):
        return f"Pawn({self.color}) at position {self.position}"


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
        final_moves = []
        for move in moves:
            if self.is_position_on_board(move):
                final_moves.append(move)
        return final_moves

    def __str__(self):
        return f"Knight({self.color}) at position {self.position}"


class Bishop(Piece):
    """
    Vrací všechny možné tahy střelce. střelec se ze své pozice může pohybovat po
    diagonálách šachovnice. Pokud se nachází na pozici (4, 4), může se pohybovat
    na pozice (1, 1), (2, 2), (3, 3), (5, 5), (6, 6), (7, 7), (8, 8), (1, 7),
    (2,6), (3, 5), (5, 3), (6, 2), (7, 1).

    Pohyby střelce jsou symetrické podle diagonál šachovnice. To znamená, že
    stačí implementovat pohyby pro jednu diagonálu a ostatní diagonály se
    získají rotací a zrcadlením. To zde není implementováno, z důvodu
    jednoduchosti
    """

    def possible_moves(self):
        """
        Vrací všechny možné tahy střelce.

        :return: Seznam možných pozic [(row, col), ...].
        """
        row, col = self.position
        # střelec se může pohybovat po diagonálách šachovnice
        moves = []
        for i in range(1, 9):
            moves.append((row + i, col + i))
            moves.append((row - i, col - i))
            moves.append((row + i, col - i))
            moves.append((row - i, col + i))

        final_moves = []
        for move in moves:
            if self.is_position_on_board(move):
                final_moves.append(move)
        return final_moves

    def __str__(self):
        return f"Bishop({self.color}) at position {self.position}"


class Rook(Piece):
    """
    Vrací všechny možné tahy věže. Věž se může pohybovat po řádcích a sloupcích
    šachovnice. Pokud se nachází na pozici (4, 4), může se pohybovat na pozice
    (1, 4), (2, 4), (3, 4), (5, 4), (6, 4), (7, 4), (8, 4), (4, 1), (4, 2),
    (4, 3), (4, 5), (4, 6), (4, 7), (4, 8).
    """

    def possible_moves(self):
        """
        Vrací všechny možné tahy věže.

        :return: Seznam možných pozic [(row, col), ...].
        """
        row, col = self.position
        moves = []
        # nemůže se pohnout na pozici, na které se nachází
        for i in range(1, 9):
            if i != row:
                moves.append((row, i))
                moves.append((i, col))

        final_moves = []
        for move in moves:
            if self.is_position_on_board(move):
                final_moves.append(move)
        return final_moves

    def __str__(self):
        return f"Rook({self.color}) at position {self.position}"


class Queen(Piece):
    """
    Vrací všechny možné tahy královny. Královna je kombinací střelce a věže.
    Královna se může pohybovat po diagonálách, řádcích a sloupcích šachovnice.
    Z pozice (4, 4) se může pohybovat na pozice (1, 1), (2, 2), (3, 3), (5, 5),
    (6, 6), (7, 7), (8, 8), (1, 7), (2, 6), (3, 5), (5, 3), (6, 2), (7, 1),
    (1, 4), (2, 4), (3, 4), (5, 4), (6, 4), (7, 4), (8, 4), (4, 1), (4, 2),
    (4, 3), (4, 5), (4, 6), (4, 7), (4, 8).
    """

    def possible_moves(self):
        """
        Vrací všechny možné tahy královny.

        :return: Seznam možných pozic [(row, col), ...].
        """
        row, col = self.position
        moves = []
        for i in range(1, 9):
            moves.append((row + i, col + i))
            moves.append((row - i, col - i))
            moves.append((row + i, col - i))
            moves.append((row - i, col + i))
            moves.append((row, i))
            moves.append((i, col))

        final_moves = []
        for move in moves:
            if self.is_position_on_board(move):
                final_moves.append(move)
        return final_moves

    def __str__(self):
        return f"Queen({self.color}) at position {self.position}"


class King(Piece):
    """
    Vrací všechny možné tahy krále. Král se může pohybovat o jedno pole
    ve všech směrech. Z pozice (4, 4) se může pohybovat na pozice (3, 3),
    (3, 4), (3, 5), (4, 3), (4, 5), (5, 3), (5, 4), (5, 5).
    """

    def possible_moves(self):
        """
        Vrací všechny možné tahy krále.

        :return: Seznam možných pozic [(row, col), ...].
        """
        row, col = self.position
        moves = [
            (row + 1, col),
            (row + 1, col + 1),
            (row + 1, col - 1),
            (row - 1, col),
            (row - 1, col + 1),
            (row - 1, col - 1),
            (row, col + 1),
            (row, col - 1),
        ]
        final_moves = []
        for move in moves:
            if self.is_position_on_board(move):
                final_moves.append(move)
        return final_moves

    def __str__(self):
        return f"King({self.color}) at position {self.position}"


if __name__ == "__main__":
    knight = Knight("black", (1, 2))
    rock = Rook("white", (4, 4))
    print(rock.possible_moves())
    print(knight)
    print(knight.possible_moves())
