# ¡Bienvenid@!

Este sitio contiene la documentación para implementar diferentes métodos númericos para resolver ODEs. A continuación una breve introducción sobre la matématica detras de estos métodos.  

### Método de Euler

El método de Euler, se basa en la expansión de Taylor de la función x(t). Tenemos:

![expansion de taylor](https://quicklatex.com/cache3/6e/ql_97cc5a36e4a55ae689a1e51cd669176e_l3.png)

Esto implica que para avanzar en el tiempo la función por un paso $h$, el cual suponemos que es lo suficientemente pequeño, basta con utilizar la ecuación

![hpequeño](https://quicklatex.com/cache3/e3/ql_f942e46ae0ef22d93a070b0ee3115ee3_l3.png)

El error asociado con la aproximación **está ligado a la cantidad de veces que hagamos la aproximación**, es decir, al número de pasos en el tiempo que utilicemos en nuestra solución. Lo podemos estimar de la siguiente forma

\sum\epsilon = \sum_{k=0}^{N-1}\frac{h^2}{2}\left. \frac{d^2x}{dt^2} \right|_{x_k, t_k} = \frac{h}{2}\sum_{k=0}^{N-1}h\left.\frac{df}{dt}\right|_{x_k, t_k}\\
\approx \frac{h}2\int_a^b\frac{df}{dt}d t = \frac{h}{2}\left[f_b - f_a\right]

Realizado por:
Anaité Chaves Ramirez
