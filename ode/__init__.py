# ode/__init__.py

""" Métodos númericos para resolver ODEs.

El modulo exportado con este paquete es:

    - ´ode´: Contiene los métodos númericos de Euler, RK2 y RK4, implementados en diferentes funciones, para resolver ODEs.

### Método de Euler

El método de Euler es muy sencillo, se basa en la expansión de Taylor de la función $x(t)$. Tenemos
$$
\\text{Expansión Taylor} \\Rightarrow x(t+h) = x(t) + h\\frac{dx}{dt} + \\overbrace{ \\frac{h^2}{2} \\frac{d^2x}{dt^2} } ^{\\epsilon} + O(h^3)
$$

Esto implica que para avanzar en el tiempo la función por un paso $h$, el cual suponemos que es lo suficientemente pequeño, basta con utilizar la ecuación
$$
x(t + h) = x(t) + hf(x,t)
$$

Existe un error asociado a la cantidad de veces que se divide el intervalo, este error suele ser más grande utilizando este método que con los demás presentados a continuación

### Método de Runge-Kutta 2$^{\\rm do}$ Orden (RK2)

La idea del método RK2 es utilizar el punto medio para evaluar el método de Euler, como se indica en la figura. Mientras que el método de Euler se aplica en el punto $t$ para evaluar la derivada para aproximar la función en el punto $x = t + h$, el método RK2 utiliza el punto medio $t + h/2$.

De esta forma, se alcanza una mejor aproximación para el mismo valor de $h$.

El método se deriva aplicando la serie de Taylor alrededor del punto medio $t + h/2$ para obtener el valor de la función en el punto $x(t + h)$. Tenemos

$$
x(t + h) = x\left(t + \\frac{h}{2}\\right) + \\frac{h}{2}\left(\\frac{{\\rm d}x}{{\\rm d}t}\\right)_{t+h/2} + \\frac{h^2}{8}\left(\\frac{{\\rm d}^2x}{{\\rm d}t^2}\\right)_{t+h/2} + O(h^3).
$$

Similarmente, podemos hacer lo mismo para $x(t)$, tal que

$$
x(t) = x\left(t + \\frac{h}{2}\\right) - \\frac{h}{2}\left(\\frac{{\\rm d}x}{{\\rm d}t}\\right)_{t+h/2} + \\frac{h^2}{8}\left(\\frac{{\\rm d}^2x}{{\\rm d}t^2}\\right)_{t+h/2} + O(h^3).
$$

Al sustraer ambas ecuaciones obtenemos

$$
x(t + h) = x(t) + h\left(\\frac{{\\rm d}x}{{\\rm d}t}\\right)_{t+h/2} + O(h^3)
$$

Finalmente,

$$
x(t + h) = x(t) + hf[x(t + h/2), t + h/2] + O(h^3)
$$

El término de orden $h^2$ desaparece y nuestra aproximación tiene un error de orden $h^3$. Recordemos que incrementar el orden del error por un orden de magnitud es muy beneficioso a nivel computacional.

El único problema es que requerimos conocer el valor de la función en el punto medio $x(t + h/2)$, el cual desconocemos.

Para aproximar este valor utilizamos el método de Euler con un paso $h/2$, $(x + h/2) = x(t) + \\frac{h}{2}f(x,t)$. De esta manera, obtenemos las ecuaciones del método RK2:

$$
k_1 = hf(x,t)
$$

$$
k_2 = hf\left(x + \\frac{k_1}{2},t + \\frac{h}{2}\\right)
$$

$$
x(t + h) = x(t) + k_2
$$

El error de aproximación de cada paso es de orden $O(h^3)$, mientras que el error global (con un análisis similar al que hicimos con el método de Euler) es de order $O(h^2)$.

Cabe recalcar que al utilizar el método de Euler para la primera parte de la aproximación, el error también es de $O(h^3)$ y por ende el error de aproximación se mantiene de $O(h^3)$.

### Método de Runge-Kutta de 4$^{\\rm to}$ Orden

La metodología anterior se puede aplicar aún a más puntos ubicados entre $x(t)$ y $x(t + h)$ realizando expansiones de Taylor. De esta forma se pueden agrupar términos de orden $h^3$, $h^4$, etc; para cancelar dichas expresiones.

El problema de hacer esto es que las expresiones se vuelven más complicadas conforme incrementamos el orden de aproximación.
En general, la regla de dedo es que el $4^{\\rm to}$ orden corresponde al mejor compromiso entre complejidad y error de aproximación. Este método es el más utilizado comunmente para resolver ODEs.

El álgebra para encontrar las ecuaciones de $4^{\\rm to}$ orden es tediosa, pero el resultado final es
$$
k_1 = hf(x, t)
$$

$$
k_2 = hf\left(x + \\frac{k_1}{2}, t+\\frac{h}2\\right)
$$

$$
k_3 = hf\left(x + \\frac{k_2}{2}, t+\\frac{h}2\\right)
$$

$$
k_4 = hf\left(x + k_3, t + h \\right)
$$

$$
x(t+h) = x(t) + \\frac{1}{6}(k_1 + 2 k_2 + 2k_3 + k_4)
$$

Para la mayoría de aplicaciones, el método RK4 es el método de-facto para obtener soluciones. Es fácil de programar y devuelve resultados precisos.

El error de aproximación es $O(h^5)$, mientras que el error global es aproximadamente del orden $O(h^4)$.

"""
