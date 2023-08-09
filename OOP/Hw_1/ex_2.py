class Chess:
  color = ''
  position = (int, int)

  def change_color(self):
    self.color = 'black' if self.color == 'white' else 'white'

  def change_position(self, new_postiton):
    if 0 <= new_position[0] <= 7 and 0 <= new_position[1] <= 7:
      self.position = new_position
    else:
      print('Invalid position')

  def is_can_move(self, new_position):
    pass

class Pawn(Chess):
  def is_can_move(self, new_position):
    x = self.position[0] - new_position[0]
    y = self.position[1] - new_position[1]

    if x == 1 and y == 0:
      return True
      
    return False

class Knight(Chess):
  def is_can_move(self, new_position):
    x = self.position[0] - new_position[0]
    y = self.position[1] - new_position[1]
    
    return (x == 1 and y == 2) or (x == 2 and y == 1)

class Bishop(Chess):
  def is_can_move(self, new_position):
    x = self.position[0] - new_position[0]
    y = self.position[1] - new_position[1]
    
    return x == y

class Rook(Chess):
  def is_can_move(self, new_position):
    return self.position[0] == new_position[0] or self.position[1] == new_position[1]

class Queen(Chess):
  def is_can_move(self, new_position):
    x = self.position[0] - new_position[0]
    y = self.position[1] - new_position[1]
    
    return self.position[0] == new_position[0] or self.position[1] == new_position[1] or x == y

class King(Chess):
  def is_can_move(self, new_position):
    x = self.position[0] - new_position[0]
    y = self.position[1] - new_position[1]
    
    return x <= 1 and y <= 1

def potential_moves(pieces, new_position):
    valid_pieces = []
    for piece in pieces:
        if piece.is_can_move(new_position):
            valid_pieces.append(piece)
    return valid_pieces

pawn = Pawn()
pawn.color = "white"
pawn.position = (1, 2)
knight = Knight()
knight.color = "white"
knight.position = (2, 1)
bishop = Bishop()
bishop.color = "white"
bishop.position = (5, 5)
rook = Rook()
rook.color = "black"
rook.position = (4, 2)
queen = Queen()
queen.color = "black"
queen.position = (0, 0)
king = King()
king.color = "black"
king.position = (7, 7)

chess_pieces = [pawn, knight, bishop, rook, queen, king]

new_position = (2, 2)
valid_moves = potential_moves(chess_pieces, new_position)
for piece in valid_moves:
    print(f"{piece.color} {piece.__class__.__name__} can move to {new_position}.")