# terrain generator
import random, math
def create_new(index, side):
    global region
    tile = ' '
    region = open("layout_lvl" + str(index) + ".txt", "w")
    # nested tile writing
    for y in range(0, 5):
        region.write('\n')
        for x in range(0, 52):
            if y == 1:
                tile = ' '
                if side == 'left' and x == 4:
                    tile = 'L'
                if side == 'right' and x == 48:
                    tile = 'L'
            if y == 2:
                tile = 'G'
            if y == 3:
                tile = 'D'
            if y == 4:
                tile = 'T'
            region.write(tile)
    region.close()
