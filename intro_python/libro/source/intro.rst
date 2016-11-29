Introducción
============

Los objetivos de este texto es el de servir de referencia a un curso
de Python de no más de 20 horas sobre analítica de datos. No se trata
de una revisión exhaustiva del lenguaje, otras referencias cubren
mejor esta necesidad, sino una referencia mínima para poder utilizar
las herramientas que han convertido a Python en el lenguaje de moda
para esta función. En el momento en el que se empieza este texto, a
finales de 2016, la práctica del análisis de datos se mueve entre R y
Python. Alternativas propietarias como Matlab, SAS o SPSS están
perdiendo terrento lentamente. Ante la duda si utilizar Python o R, el
primero es claramente una mejor opción. Librerías como Pandas o
scikit-learn están en crecimiento constante tanto en funcionalidad
como en usuarios, mientras que R avanza a un ritmo significativamente
menor. Hay otros lenguajes en crecimiento orientados al cálculo
numérico y la analítica de datos que pueden ser interesantes en el
futuro como Lua o Julia, pero no están lo suficientemente establecidos
como para ser interesantes a nivel industrial.

La audiencia de este texto son profesionles y estudiantes que ya se
hayan iniciado en la programación. Aunque algunas de las estructuras
del lenguje se analizarán en detalle, los elementos más fundamentales
de la práctica de la programación (qué es una variable, qué es la
memoria, cómo se ejecuta un programa...) se asumirán como
conocidos.

Durante el texto se tratarán algunas librerías para el análisis de
datos como Numpy, Pandas o Matplotlib, pero no se tratarán en
detalle. Los manuales de cada uno de ellas se extienden cientos de
páginas, así que este texto se quedará en lo fundamental.

El lenguaje de programación Python
----------------------------------

Python fue creado por Guido van Rossum en el año 1991. Para poner una
referencia cronológica, es 4 años anterior a Java, con el que presenta
tanto semejanzas como diferencias. Si bien Java tuvo un fuerte
crecimiento a finales de los años 90 gracias al apoyo que tuvo de Sun
Microsystems, Python fue un lenguaje de programación con un nivel de
adopción medio hasta mediados de la década del 2000. A diferencia de
Java, que era el lenguaje de uso en entornos empresariales, Python se
implantó en muchos proyectos de software libre. Su popularidad actual
se debe al éxito de los proyectos que lo han utilizado como lenguaje
de programación, entre ellos Google.

Python se caracteriza por tener una sintaxis fácil de leer y por ser
relativamente accesible a principiantes. Es un lenguaje interpretado,
así que cualquier instalación de Python incluye un intérprete de
comandos con el que poder ensayar cualquier pieza de código. El
intérprete de Python es además muy ligero y portable. Uno puede
encontrar Python en el mayor superordenador del mundo y en un
microcontrolador con sólo 64 kiB de memoria RAM.

Es difícil citar una fecha o un proyecto a partir del cual Python se
pudo considerar un lenguaje maduro para el análisis de datos. Python
siempre ha contado con una gran popularidad entre científicos e
ingenieros, que empezaron a crear extensiones para su uso
personal. Primero llegó Numpy, que permite manipular vectores,
matrices y demás estructuras homogéneas de datos de manera
sencilla. Luego llegó Scipy, una colección de wrappers a librerías
científicas con una larga reputación. Matplotlib apareció como un
pequeño paquete que permitía crear gráficos para publicaciones con una
sintaxis parecida a Matlab, para convertirse poco después en una
extensa librería de representación gráfica usada por mútliples
proyectos y lenguajes. Scikit-learn vino cuando el ecosistema de
Python para Ciencia y análisis de datos ya estaba maduro, e incorpora
cientos de algoritmos para machine learning. El último en llegar,
Pandas, es una librería para tratamiento y análisis de datos inspirada
por el lenguaje de programación R. Todas estas librerías, unidas a un
lenguaje potente pero fácil de utilizar como Python, permiten analizar
grandes cantidades de datos de manera efectiva para obtener o aplicar
conocimiento de negocio.

Python 2 y 3
------------

En el momento de escribir este documento Python se encuentra
transicionando entre dos versiones incompatibles del lenguaje. Aunque
las diferencias no son muchas, no hay ninguna garantía que un programa
escrito para Python 2 funcione correctamente en Python 3 y
viceversa. Estas diferencias, aunque reales, no son dramáticas; hay
librerías que soportan las dos versiones con una misma base de código.

Python 2 se encuentra en modo de mantenimiento y no será actualizado
nunca más a no ser que algún grupo de desarrolladores haga un fork y
lo desarrolle independientemente de la Fundación Python, la
organización que se encarga de manejar la comunidad de
desarrolladores. La única versión que recibe actualizaciones es Python
3, así que para este documento se considerará únicamente la versión 3
del lenguaje.

Esto es en lo que respecta a la versión mayor, pero también hay
versiones menores. La última versión de Python 3 en noviembre de 2016
es la 3.5. Hay cierto consenso en que las versiones maduras de Python
3, las que justificaron la migración de muchos proyectos desde Pythoon
3, se iniciaron a partir de la 3.4. Las versiones menores no
introducen ningún cambio incompatible hacia atrás, sólo mejoras y
nuevas funcionalidades. Un código escrito para la versión 3.4
funcionará para la 3.5 y todas las que vengan en el futuro. La
consecuencia de esta evolución constante es que este documento no
tiene otro destino que terminar siendo obsoleto. Algunas
características interesantes de Python 3.6 que está en estos momentos
a punto de ser publicado, no entrarán en este texto.

Posibles equívocos causados por este documento
----------------------------------------------

Siendo este texto una introducción, los ejemplos son pequeños
programas o scripts cortos que cumplen una funcionalidad
específica. Esto puede llevar a la impresión errónea que Python es un
lenguaje de programación para proyectos pequeños, o que no cuenta con
las herramientas necesarias para el desarrollo a gran escala de
aplicaciones empresariales. La discusión de si Python es conveniente o
no para este tipo de desarrollos existe, pero no es tanto sobre las
herramientas, que existen y son maduras. Para poner un ejemplo, este
documento ha sido redactado con la herramienta para documentación
recomendada para documentar proyectos en Python, `Sphinx
<http://www.sphinx-doc.org/>`_.

Otro error que puede motivar este texto es que Python es un lenguaje
superficial que no esconde muchos atractivos para los usuarios
avanzados. Un ejemplo de esta *potencia escondida* es la clase
intrínseca :py:class:`type`, que abre las puertas de Python a la
práctica de la metaprogramación.


La estructura de este documento
-------------------------------

La primera sección incluye un pequeño manual sobre cómo debe
instalarse Python en función del sistema operativo. Las cuatro
secciones siguientes tratan sobre las estructuras fundamentales del
lenguaje: los tipos, los contenedores, el control de flujo y los
recursos de entrada/salida. A continuación tenemos varios capítulos
esenciales para entender cómo se estructura el código en Python, sobre
funciones, clases y módulos respectivamente. Finalmente entramos en en
los capítulos dedicados a las librerías para análisis de datos. La
primera es Numpy, para la manipulación de arrays numéricos, la segunda
es Matplotlib, que permite representar datos con prácticamente
cualquier tipo de gráfico. La tercera y última es Pandas, la navaja
suiza del análisis de datos moderno.
