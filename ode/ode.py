# ode/ode.py

""" ##Métodos númericos para resolver ODEs.

Este módulo permite al usuario resolver ODEs con distintos métodos matemáticos.

El módulo contiene las siguientes funciones:

    - Euler: Utiliza el Método de Euler para resolver la ODE.
    - RK2: Utiliza el Método de RK2 para resolver la ODE.
    - RK4: Utiliza el Método de RK4 para resolver la ODE.

"""

def Euler(f,xi,ti,tf,N):

    """Utiliza el Método de Euler para resolver la ODE.

    Examples:

    Args:
        f (función): Función de la ecuación a resolver.
        xi (float): Valor inicial para la variable dependiente.
        ti (float): Valor inicial para la variable independiente.
        tf (float): Valor final para la variable independiente.
        N (int): Número de particiones entre el rango de variables independientes.

    Returns:
        x (arreglo): un vector para la variable dependiente 'x'
        t (arreglo): un vector para la variable dependiente 't'
"""
    t = np.linspace(ti,tf,N)
    x = np.zeros(t.size)
    x[0] = xi
    h = t[1] - t[0]
    for i in range(t.size - 1):
        x[i+1] = x[i] + h*f(x[i],t[i])
    return t,x

def RK2(f,xi,ti,tf,N):
    """Utiliza el Método de RK2 para resolver la ODE.

    Examples:

    Args:
        f (función): Función de la ecuación a resolver.
        xi (float): Valor inicial para la variable dependiente.
        ti (float): Valor inicial para la variable independiente.
        tf (float): Valor final para la variable independiente.
        N (int): Número de particiones entre el rango de variables independientes.

    Returns:
        x (arreglo): un vector para la variable dependiente 'x'
        t (arreglo): un vector para la variable dependiente 't'
"""

    t = np.linspace(ti,tf,N)
    x = np.zeros(t.size)
    x[0] = xi
    h = t[1] - t[0]
    for i in range(t.size-1):
        k1 = h*f(x[i],t[i])
        k2 = h*f(x[i] + (k1/2), t[i] + (h/2))
        n = x[i] + (h/2)*f(x[i],t[i])
        x[i+1] = x[i] + h*f(n, t[i] + h/2)
    return x,t


def RK4(f,xi,ti,tf,N):

    """Utiliza el Método de RK4 para resolver la ODE.

    Examples:

    Args:
        f (función): Función de la ecuación a resolver.
        xi (entero): Valor inicial para la variable dependiente.
        ti (entero): Valor inicial para la variable independiente.
        tf (entero): Valor final para la variable independiente.
        N (entero): Número de particiones entre el rango de variables independientes.

    Returns:
        x (arreglo): un vector para la variable dependiente 'x'
        t (arreglo): un vector para la variable dependiente 't'
"""

    t = np.linspace(ti,tf,N)
    x = np.zeros(t.size)
    x[0] = xi
    h = t[1] - t[0]
    for i in range(t.size-1):
        k1 = h*f(x[i],t[i])
        k2 = h*f(x[i] + (k1/2), t[i] + (h/2))
        k3 = h*f(x[i] + (k2/2), t[i] + (h/2))
        k4 = h*f(x[i] + k3, t[i] + h)
        x[i+1] = x[i] + (1/6)*(k1 + 2*k2 + 2*k3 + k4)
    return x,t
