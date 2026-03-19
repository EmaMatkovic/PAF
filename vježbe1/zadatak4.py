def pravac(x1, y1, x2, y2):
    if x1 == x2:
        print(f"Pravac je vertikalan: x = {x1}")
    else:
        k = (y2 - y1) / (x2 - x1)  # nagib
        l = y1 - k * x1            # odsječak na y-osi
        print(f"Jednadžba pravca je: y = {k}x + {l}")
pravac(1, 2, 3, 4)