class ChessPiece:
    def __init__(self, position):
        self.position = position

    def is_valid_position(self, position):
        return 0 <= position[0] < 8 and 0 <= position[1] < 8

class King(ChessPiece):
    def can_move(self, target):
        dx = abs(self.position[0] - target[0])
        dy = abs(self.position[1] - target[1])
        return max(dx, dy) == 1 and self.is_valid_position(target)

class Rook(ChessPiece):
    def can_move(self, target):
        dx = abs(self.position[0] - target[0])
        dy = abs(self.position[1] - target[1])
        return (dx == 0 or dy == 0) and self.is_valid_position(target)

# Пример использования
king = King((4, 4))
print(king.can_move((5, 5)))  # True
print(king.can_move((6, 6)))  # False

rook = Rook((0, 0))
print(rook.can_move((0, 5)))  # True
print(rook.can_move((5, 5)))  # False
