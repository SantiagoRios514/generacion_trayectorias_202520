from trayectoria_cuadratica import fn_trayectoria_recta_cuadratica
from trayectoria_cubica import fn_trayectoria_cubica
import matplotlib.pyplot as plt

# Inicialización de parámetros, según taller
q0 = 0.0
qf = 100.0
qdot0 = 0.0
qdotf = 0.0
t0 = 0.0
tf = 10.0
tspace = 0.001

qdotdot_d = float(input("Enter desired acceleration for quadratic trajectory: ")) # Aceleración deseada para la trayectoria cuadrática

# Cálculo de las trayectorias
q_cub, qdot_cub, qdotdot_cub, t_cub = fn_trayectoria_cubica(q0, qf, qdot0, qdotf, t0, tf, tspace)
q_cua, qdot_cua, qdotdot_cua, t_cua = fn_trayectoria_recta_cuadratica(q0, qf, qdotdot_d, tf, tspace)

# Crear subplots para tener todas las gráficas en una sola ventana
fig, ax = plt.subplots(3, 1, sharex=True, figsize=(8, 12))

# Gráfica posición vs tiempo
ax[0].plot(t_cub, q_cub, label = 'cubic spline', color = 'blue')
ax[0].plot(t_cua, q_cua, label = 'linear/quadratic', color = 'green')
ax[0].set_ylabel('Position (m)')
ax[0].set_title('Position vs Time')
ax[0].legend()
ax[0].grid()


# Gráfica velocidad vs tiempo
ax[1].plot(t_cub, qdot_cub, label = 'cubic spline', color = 'blue')
ax[1].plot(t_cua, qdot_cua, label = 'linear/quadratic', color = 'green')
ax[1].set_ylabel('Velocity ($m/s$)')
ax[1].set_title('Velocity vs Time')
ax[1].grid()


# Gráfica aceleración vs tiempo
ax[2].plot(t_cub, qdotdot_cub, label = 'cubic spline', color = 'blue')
ax[2].plot(t_cua, qdotdot_cua, label = 'linear/quadratic', color = 'green')
ax[2].set_xlabel('Time (s)')
ax[2].set_ylabel('Acceleration (m/s²)')
ax[2].set_title('Acceleration vs Time')
ax[2].grid()

plt.show()