n = int(input("Enter number: "))

row = 1

while row <= n:
    col = 1

    while col <= row:
        if row == n or col == 1 or col == row:
            print("*", end=" ")
        
        else:
            print("@", end=" ")
        col += 1

    print()
    row += 1