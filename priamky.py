from PIL import Image

obr = Image.new("RGB", (500, 500), 'white')
pixely = obr.load()

A = input("Zadaj mi 2 hodnoty: ")
B = input("Zadaj mi 2 hodnoty: ")
A = A.split(",")
B = B.split(",")

Ax = int(A[0])
Ay = int(A[1])
Bx = int(B[0])
By = int(B[1])

if Ax < Bx:
    k = (By - Ay) / (Bx - Ax)
    q = Ay - k * Ax
    for x in range(Ax, Bx):
        y = int(k * x + q)
        pixely[x, y] = (0, 0, 0)

elif Ax == Bx:
    if Ay == By:
        x = Ax
        y = Ay
        pixely[x, y] = (0, 0, 0)
    elif Ay < By:
        for y in range(Ay, By):
            x = Ax
            pixely[x, y] = (0, 0, 0)
    else:
        for y in range(By, Ay):
            x = Ax
            pixely[x, y] = (0, 0, 0)

else:
    k = (Ay - Ay) / (Ax - Bx)
    q = By - k * Bx
    for x in range(Bx, Ax):
        y = int(k * x + q)
        pixely[x, y] = (0, 0, 0)

obr.show()
