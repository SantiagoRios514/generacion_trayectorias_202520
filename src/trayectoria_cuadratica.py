import numpy as np
from numpy import linalg as LA
import math
np.set_printoptions(threshold=np.inf, linewidth=200)


def fn_trayectoria_recta_cuadratica(q0, qf, qdotdot_d, tf, tspace):
    qh = (qf - q0) / 2
    th = tf / 2
    tb = tf / 2 - (math.sqrt(qdotdot_d**2 * tf**2 - 4 * qdotdot_d * (qf - q0)) / (2 * qdotdot_d)) if qdotdot_d >= (4 * (qf - q0) / tf**2) else 0
    qb = q0 + 0.5 * qdotdot_d * tb**2

    t_arr = []
    q_arr = []
    qdot_arr = []
    qdotdot_arr = []

    for i in np.arange(0, tf, tspace):
        t = i
        if t <= tb:
            q = q0 + 0.5 * qdotdot_d * t**2
            qdot = qdotdot_d * t
            qdotdot = qdotdot_d
        elif tb < t <= (tf - tb):
            q = (((qh - qb) / (th - tb)) * (t - tb)) + qb
            qdot = (qh - qb) / (th - tb)
            qdotdot = 0
        else:
            q = qf - (0.5 * qdotdot_d * (tf - t)**2)
            qdot = qdotdot_d * (tf - t)
            qdotdot = -qdotdot_d
        
        t_arr.append(t)
        q_arr.append(q)
        qdot_arr.append(qdot)
        qdotdot_arr.append(qdotdot)

    return q_arr, qdot_arr, qdotdot_arr, t_arr

if __name__ == "__main__":
    q0 = 0.0
    qf = 5.0
    qdotdot_d = 20
    tf = 10.0

    q, qdot, qdotdot, t = fn_trayectoria_recta_cuadratica(q0, qf, qdotdot_d, tf, 0.001)

    print("Position:", q)
    print("Velocity:", qdot)
    print("Acceleration:", qdotdot)
    print("Time:", t)