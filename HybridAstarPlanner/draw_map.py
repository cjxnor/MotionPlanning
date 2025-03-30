import numpy as np
import matplotlib.pyplot as plt

def design_obstacles(x, y):
    ox, oy = [], []

    # range(x) 生成0到x-1的整数序列
    for i in range(x):
        for j in range(y):
            ox.append(i)
            oy.append(j)

    return ox, oy

def plot_grid(grid):
    if not hasattr(grid, "shape"):
        grid = np.array(grid)
        
    rows, cols = grid.shape
    plt.figure(figsize=(cols/4, rows/4))
    plt.imshow(grid, cmap="gray_r")  # 0（白色），1（黑色）
    
    # 绘制网格线
    for x in range(cols + 1):
        plt.axvline(x - 0.5, lw=1, color="black", alpha=0.5)
    for y in range(rows + 1):
        plt.axhline(y - 0.5, lw=1, color="black", alpha=0.5)

    plt.xticks([])
    plt.yticks([])
    plt.title("Grid Map")
    plt.show()


def main():
    x, y = 50, 30
    # ox, oy = design_obstacles(x, y)

    arr = np.zeros((30, 50))
    plot_grid(arr)

    # plt.plot(ox, oy, "sk")
    plt.show()


if __name__ == '__main__':
    main()