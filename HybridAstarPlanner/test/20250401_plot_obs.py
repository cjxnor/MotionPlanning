import matplotlib.pyplot as plt

def design_obstacles(x, y):
    ox, oy = [], []

    # 垂直车位
    for i in range(0, 24):
        ox.append(i)
        oy.append(5)
    for i in range(5, -1, -1):
        ox.append(23)
        oy.append(i)
    for i in range(23, 27):
        ox.append(i)
        oy.append(0)
    for i in range(0, 6):
        ox.append(26)
        oy.append(i)
    for i in range(26, x):
        ox.append(i)
        oy.append(5)
    for i in range(5, y):
        ox.append(x - 1)
        oy.append(i)
    for i in range(0, x):
        ox.append(i)
        oy.append(y - 1)
    for i in range(5, y):
        ox.append(0)
        oy.append(i)

    # print(ox)
    # print(oy)
    return ox, oy

x, y = 51, 31
ox, oy = design_obstacles(x, y)
plt.plot(ox, oy, "sk")
plt.show()