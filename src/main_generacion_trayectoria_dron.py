from trayectoria_cuadratica import fn_trayectoria_recta_cuadratica
from trayectoria_cubica import fn_trayectoria_cubica
import matplotlib.pyplot as plt
import numpy as np

q0 = 0.0
qf = 100.0
qdot0 = 0.0
qdotf = 0.0
t0 = 0.0
tf = 10
tspace = 0.001

qdotdot_d = 5.0 # VALOR CAMBIABLE

q_cub, qdot_cub, qdotdot_cub, t_cub = fn_trayectoria_cubica(q0, qf, qdot0, qdotf, t0, tf, tspace)
q_cua, qdot_cua, qdotdot_cua, t_cua = fn_trayectoria_recta_cuadratica(q0, qf, qdotdot_d, tf, tspace)

t_cub = np.array(t_cub)
q_cub = np.array(q_cub)
qdot_cub = np.array(qdot_cub)
qdotdot_cub = np.array(qdotdot_cub)
t_cua = np.array(t_cua)
q_cua = np.array(q_cua)
qdot_cua = np.array(qdot_cua)
qdotdot_cua = np.array(qdotdot_cua)


# Gráfica posición vs tiempo
plt.figure()
plt.plot(t_cub, q_cub, label = 'cubic spline', color = 'blue')
plt.plot(t_cua, q_cua, label = 'linear/quadratic', color = 'green')
plt.xlabel('Time (s)')
plt.ylabel('Position (m)')
plt.title('Position vs Time')
plt.legend()
plt.grid()


# Gráfica velocidad vs tiempo
plt.figure()
plt.plot(t_cub, qdot_cub, label = 'cubic spline', color = 'blue')
plt.plot(t_cua, qdot_cua, label = 'linear/quadratic', color = 'green')
plt.xlabel('Time (s)')
plt.ylabel('Velocity (m/s)')
plt.title('Velocity vs Time')
plt.legend()
plt.grid()


# Gráfica aceleración vs tiempo
plt.figure()
plt.plot(t_cub, qdotdot_cub, label = 'cubic spline', color = 'blue')
plt.plot(t_cua, qdotdot_cua, label = 'linear/quadratic', color = 'green')
plt.xlabel('Time (s)')
plt.ylabel('Acceleration (m/s^2)')
plt.title('Acceleration vs Time')
plt.legend()
plt.grid()


plt.show()