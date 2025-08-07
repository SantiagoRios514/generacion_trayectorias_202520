import numpy as np
from numpy import linalg as LA

def fn_trayectoria_cubica(q0, qf, qdot0, qdotf, t0, tf, tspace):
    # Definición de la matriz de coeficientes y el vector de términos independientes
    mat_coeficientes = np.array([[1, t0, t0**2, t0**3], 
                                  [1, tf, tf**2, tf**3], 
                                  [0, 1, 2*t0, 3*t0**2], 
                                  [0, 1, 2*tf, 3*tf**2]])
    vec_independientes = np.array([[q0], 
                                    [qf], 
                                    [qdot0], 
                                    [qdotf]])
    
    # Solución del sistema de ecuaciones
    a0, a1, a2, a3 = LA.solve(mat_coeficientes, vec_independientes)

    # Generación del vector de tiempo
    t = np.arange(t0, tf, tspace)

    # Cálculo de los vectores de posición, velocidad y aceleración
    q = a0 + a1 * t + a2 * t**2 + a3 * t**3
    qdot = a1 + 2 * a2 * t + 3 * a3 * t**2
    qdotdot = 2 * a2 + 6 * a3 * t

    # Retorno de los resultados como listas (vectores)
    return q, qdot, qdotdot, t

if __name__ == "__main__":
    q0 = 0.0
    qf = 5.0
    qdot0 = 0.0
    qdotf = 0.0
    t0 = 0.0
    tf = 1

    q, qdot, qdotdot, t = fn_trayectoria_cubica(q0, qf, qdot0, qdotf, t0, tf, 0.001)

    print("Position:", q)
    print("Velocity:", qdot)
    print("Acceleration:", qdotdot)
    print("Time:", t)