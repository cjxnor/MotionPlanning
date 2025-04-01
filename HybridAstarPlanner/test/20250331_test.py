import math
import numpy as np
import matplotlib.pyplot as plt

class C:  # Parameter config
    PI = math.pi

    XY_RESO = 2.0  # [m]
    YAW_RESO = np.deg2rad(15.0)  # [rad]
    MOVE_STEP = 0.4  # [m] path interporate resolution
    N_STEER = 20.0  # steer command number
    COLLISION_CHECK_STEP = 5  # skip number for collision check
    EXTEND_BOUND = 1  # collision check range extended

    GEAR_COST = 100.0  # switch back penalty cost 挡位切换的代价
    BACKWARD_COST = 5.0  # backward penalty cost
    STEER_CHANGE_COST = 5.0  # steer angle change penalty cost
    STEER_ANGLE_COST = 1.0  # steer angle penalty cost
    H_COST = 15.0  # Heuristic cost penalty cost

    RF = 4.5  # [m] distance from rear to vehicle front end of vehicle  后轴中心到车头的距离
    RB = 1.0  # [m] distance from rear to vehicle back end of vehicle   后轴中心到车尾的距离
    W = 3.0  # [m] width of vehicle
    WD = 0.7 * W  # [m] distance between left-right wheels
    WB = 3.5  # [m] Wheel base
    TR = 0.5  # [m] Tyre radius
    TW = 1  # [m] Tyre width
    MAX_STEER = 0.6  # [rad] maximum steering angle

def draw_car(x, y, yaw, steer, color='black'):
    car = np.array([[-C.RB, -C.RB, C.RF, C.RF, -C.RB],
                    [C.W / 2, -C.W / 2, -C.W / 2, C.W / 2, C.W / 2]])

    wheel = np.array([[-C.TR, -C.TR, C.TR, C.TR, -C.TR],
                      [C.TW / 4, -C.TW / 4, -C.TW / 4, C.TW / 4, C.TW / 4]])

    rlWheel = wheel.copy()
    rrWheel = wheel.copy()
    frWheel = wheel.copy()
    flWheel = wheel.copy()

    # 车辆旋转矩阵
    Rot1 = np.array([[math.cos(yaw), -math.sin(yaw)],
                     [math.sin(yaw), math.cos(yaw)]])

    # 前轮旋转矩阵
    Rot2 = np.array([[math.cos(steer), math.sin(steer)],
                     [-math.sin(steer), math.cos(steer)]])

    frWheel = np.dot(Rot2, frWheel)
    flWheel = np.dot(Rot2, flWheel)

    # 四个轮子相对于后轴中心的位置
    frWheel += np.array([[C.WB], [-C.WD / 2]])
    flWheel += np.array([[C.WB], [C.WD / 2]])
    rrWheel[1, :] -= C.WD / 2
    rlWheel[1, :] += C.WD / 2

    frWheel = np.dot(Rot1, frWheel)
    flWheel = np.dot(Rot1, flWheel)

    rrWheel = np.dot(Rot1, rrWheel)
    rlWheel = np.dot(Rot1, rlWheel)
    car = np.dot(Rot1, car)

    # 加上车辆后轴中心的坐标
    frWheel += np.array([[x], [y]])
    flWheel += np.array([[x], [y]])
    rrWheel += np.array([[x], [y]])
    rlWheel += np.array([[x], [y]])
    car += np.array([[x], [y]])

    plt.plot(car[0, :], car[1, :], color)
    plt.plot(frWheel[0, :], frWheel[1, :], color)
    plt.plot(rrWheel[0, :], rrWheel[1, :], color)
    plt.plot(flWheel[0, :], flWheel[1, :], color)
    plt.plot(rlWheel[0, :], rlWheel[1, :], color)
    # draw.Arrow(x, y, yaw, C.WB * 0.8, color)

draw_car(0.0, 0.0, -0.1, 0.0, 'dimgray')
plt.show()