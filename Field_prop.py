from aux_func import cross_ship
from aux_func import calc_cross_coord

class Field:

    #
    def __init__(self, _lenght, _ship_count):
        self.lenght = _lenght
        self.ship_count = _ship_count
        self.ships = []
        self.field = [['-' for _ in range(_lenght)] for _ in range(_lenght)]

    #
    def add_ship(self, _ship):
        f = 1
        for i in self.ships:
            if cross_ship(_ship, i, self.lenght):
                f = 0
                break
        if f == 1:
            self.ships.append(_ship)

    #
    def del_ship(self, _ship):
        self.ships.pop(self.ships.index(_ship))

    #
    def hit_and_print(self, _xy):
        oneten = [i for i in range(1, self.lenght + 1)]
        if _xy[0] in oneten and _xy[1] in oneten:
            if self.field[_xy[0] - 1][_xy[1] - 1] == '-':
                for i in self.ships:
                    if _xy in i.deck_coord:
                        i.status[i.deck_coord.index(_xy)] = 1
                        self.field[_xy[0] - 1][_xy[1] - 1] = 'x'
                        if i.status.count(1) == len(i.status):
                            cross_coord = calc_cross_coord(i, self.lenght)
                            for t in cross_coord:
                                self.field[t[0] - 1][t[1] - 1] = 'o'
                            for t in i.deck_coord:
                                self.field[t[0] - 1][t[1] - 1] = 'w'
                            self.del_ship(i)
                            print('Killed!')
                            for j in self.field:
                                print(j)
                            print()
                            return True
                        print('Hit!')
                        for j in self.field:
                            print(j)
                        print()
                        return True
                self.field[_xy[0] - 1][_xy[1] - 1] = 'o'
                print('Missed!')
                for j in self.field:
                    print(j)
                print()
                return False
            else:
                print('You already hit that place!')
