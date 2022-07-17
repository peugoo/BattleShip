from Ship_prop import Ship
from Field_prop import Field


Field1 = Field(10, 2)



ship1 = Ship(2, Field1)
ship1.set_pos('vert')
ship1.set_coord([1, 1])
Field1.add_ship(ship1)

ship2 = Ship(2, Field1)
ship2.set_pos('hor')
ship2.set_coord([3, 2])
Field1.add_ship(ship2)
while len(Field1.ships) != 0:
    a = input().split()
    a = [int(a[0]), int(a[1])]
    Field1.hit_and_print(a)
print('You won!')
