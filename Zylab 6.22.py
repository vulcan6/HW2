#Erick Jimenez
#PSID: 1463639
#Zylab 6.22

def main():
    x1 = int(input())
    y1 = int(input())
    z1 = int(input())

    x2 = int(input())
    y2 = int(input())
    z2 = int(input())

    solution_found = False

    for x in range(-10, 11):
        for y in range(-10, 11):
            if x1 * x + y1 * y == z1 and x2 * x + y2 * y == z2:
                print(x, y)
                solution_found = True

    if not solution_found:
        print("No solution")


if __name__ == '__main__':
    main()
