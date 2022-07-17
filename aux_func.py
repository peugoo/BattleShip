#
def cross_ship(_ship1, _ship2, _field_lenght):
    #
    calc_ship2 = calc_cross_coord(_ship2, _field_lenght)
    for i in _ship1.deck_coord:
        if i in calc_ship2:
            return True
    return False

#
def calc_cross_coord(_ship, _field_lenght):
        cross_coord = []
        oneten = [i for i in range(1, _field_lenght + 1)]
        y0, y1 = _ship.deck_coord[0][1] - 1, _ship.deck_coord[-1][1]
        x0, x1 = _ship.deck_coord[0][0] - 1, _ship.deck_coord[-1][0]
        for i in range(y0, y1 + 2):
            for j in range(x0, x1 + 2):
                if i in oneten and j in oneten:
                    cross_coord.append([j, i])
        return cross_coord
