class Ship:

    #
    def __init__(self, _lenght, _field):
        self.lenght = _lenght
        self.pos = 'hor'
        self.coord = [1, 1]
        self.deck_coord = [0] * _lenght
        self.status = [0] * _lenght
        self.field = _field

    #
    def check_ship(self, _new_coord, _new_pos, _field):
        oneten = [i for i in range(1, _field.lenght + 1)]
        x, y = _new_coord[0], _new_coord[1]
        if x in oneten and y in oneten:
            if _new_pos == 'hor':
                dx, dy = 1, 0
                x -= 1
            else:
                dx, dy = 0, 1
                y -= 1
            if x + dx * self.lenght in oneten and y + dy * self.lenght in oneten:
                return True
        return False

    #
    def generate_deck(self, _xy, _pos):
        x, y = _xy[0], _xy[1]
        if _pos == 'hor':
            dx, dy = 1, 0
            x -= 1
        else:
            dx, dy = 0, 1
            y -= 1
        for i in range(self.lenght):
            x, y = x + dx, y + dy
            self.deck_coord[i] = [x, y]

    #
    def set_coord(self, _xy):
        if self.check_ship(_xy, self.pos, self.field):
            self.coord = _xy
        self.generate_deck(self.coord, self.pos)

    #
    def set_pos(self, _new_pos):
        if self.check_ship(self.coord, _new_pos, self.field):
            if _new_pos == 'hor':
                self.pos = 'vert'
            else:
                self.pos = 'hor'
        self.generate_deck(self.coord, self.pos)

    #
