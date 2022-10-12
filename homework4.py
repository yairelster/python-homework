size = 9
print(                                   )
for row in range(size):
    for col in range(size):
        if row == 0:
            print("X", end=" ")
        elif row == 8:
            print("X", end=" ")
        elif col == 8:
            print("X", end=" ")
        elif col == 0:
            print("X", end=" ")
        elif col == row:
            print("V", end=" ")
        elif col + row == size - 1:
            print("V", end=" ")
        else:
            print("0", end=" ")
    print()

print(                                   )

height = 9
width = 16
for row in range(height):
    for col in range(width):
        if col == (row * 2):
            print("x", end=" ")
        elif col == width-1 and row == height-1:
            print("x", end=" ")
        else:
            print("0", end=" ")
    print()

#    0,0 1,2 2,4 3,6