$$Depreciaciones_{Supuesto(K)} = DepreciacionesActivosHistoricos_{Supuesto(K)} + DepreciacionesActivosNuevos_{Supuesto(K)}$$

### Depreciaciones de Activos Historicos (PPE)

Ahora, el tema de las depreciaciones si es un poco mas dificil. Las depreciaciones historicas son las que reporta la empresa. Sin embargo, para predecir las depreciaciones futuras, se tiene que tener en cuenta las depreciaciones de activos historicos y depreciones de activos nuevos.  Las depreciaciones de activos historicos a futuro, corresponde a la ultima Propiedad Planta y Equipo por la depreciacion del periodo (recordar que el equipo disminuye con el tiempo). Por supuesto la depreciacion del periodo no es gratuita. Se tienen las depreciacioens historicas, y con estas se puede calcular la depreacion sobre el PPE para obtener el porcentaje de depreciacion historico
$$\% Depreciación del Período | Saldo_{HistoricoK}=\frac{Depreciacion}{PPE}$$, y la depreciacion a futuro, no es mas que el criterio que se tome
$$\% DepreciacionDelPeriodo | Saldo_{(k)}=Criterio$$

Por tanto la depreciacion del periodo no es mas que el ultimo PPE por la depreciacion del periodo comparado con el saldo de ese periodo K.

$$DepreciacionDelPeriodo_{K}  = \% Depreciación del Período | Saldo_{K} \cdot UltimoPPE$$

La depreciacion acumulada PPE historica vendria siendo la depreciacion acumulada PPE historica del year anterior + depreciacion del periodo (aprox).
$$DepreciacionAcumuladaPPEHistorica_{k}=DepreciacionAcumuladaPPEHistorica_{k-1} + DepreciacionDelPeriodo_{k}$$


Y las depreciaciones de activos historicos vendrian siendo
$$DepreciacionesActivosHistoricos_{K} = DepreciacionDelPeriodo_{K}$$

Observar que la depreacion de activos historicos nunca se calculo para los periodos donde la empresa reporto el balance. Porque la idea es como calcular de lo que existe hoy, como se va a depreciar ese PPE en el futuro. 


### Depreciaciones de Activos Nuevos

Ahora calcular la depreciacion para el llamado activos nuevos si es una locura. Y de nuevo solo tiene sentido para el futuro, no para el historico. 

Y las de activos nuevos
$$Depreciaciones Activos Nuevos_{Supuesto(K)} = DepreciacionDelPeriodo_{Supuesto(K)}$$
$$DepreciacionDelPeriodo_{K=2025}=Depreciación Inversión Nueva Año 2025$$
$$DepreciacionDelPeriodo_{K=2026}=Depreciación Inversión Nueva Año 2025 + Depreciación Inversión Nueva Año 2026$$
$$DepreciacionDelPeriodo_{K=2027}=Depreciación Inversión Nueva Año 2025 + Depreciación Inversión Nueva Año 2026 + Depreciación Inversión Nueva Año 2027$$
$$DepreciacionDelPeriodo_{K=N}=Depreciación Inversión Nueva Año 2025 + Depreciación Inversión Nueva Año 2026 + Depreciación Inversión Nueva Año 2027 + ... + Depreciación Inversión Nueva Año N$$
pero aqui es donde la pita empieza a enrreddarse un poco,

![[Pasted image 20250909182359.png]]
Se observa que por ejemplo $Depreciación Inversión Nueva Año 2025$ cambia con el transcurrir de los years. Lo que significa que en realidad es una funcion de $k$ tambien, siendo el $k$ el year. Pero Que significa esto, por que?. Inspeccionemos un poco mas a profundidad este enrredo. Esta variable no es mas que producto de la suma de depreciaciones a diferentes anios, en este caso a 3,5, 10 y 20. 

$$Depreciación Inversión Nueva Año 2025 = Depreciación a 3 años + Depreciación a 5 años + Depreciación a 10 años + Depreciación a 20 años$$

Y la depreciacion a 3 anios no es mas que el producto de $Inversión Nueva Depreciable$ en ese mismo year. Pero que es $Inversión Nueva Depreciable$ ?, continua el trabalenguas. Pero antes de irnos tenemos que saber que 
$$Depreciación a 3 años = \frac {Inversión Nueva Depreciable_{InversionA3Years}} {3}$$
$Inversión Nueva Depreciable_{InversionA3Years}$ de donde viene? La respuesta es facil, una empresa puede hacer inversiones de multiples caracteristicas, algunas pueden ser depreciadas a 3 years, otras a 5 y asi mismo. Entonces la inversion total de ese year, no es mas que lo que se perfile para depreciarse en 3 years, 5, 10, y 20. 

$$Inversión Nueva Depreciable = Inversión Nueva Depreciable_{InversionA3Years} + Inversión Nueva Depreciable_{InversionA5Years} + Inversión Nueva Depreciable_{InversionA10Years} + Inversión Nueva Depreciable_{InversionA20Years}$$
Pero por supuesto, es la empresa quien decide cuanto se va a 3, 5, 10 y 20 years. Si asuminos que si en 2025 se hace una inversion total de 132102, y que el 20% de esa inversion se deprecia en 20 %years, el 50% en 10 years, el 20% en 5 years y el 10% en 3 years, entonces tendriamos que
$$Inversión Nueva Depreciable Total_{2025} = 132102$$
$$Inversión Nueva Depreciable {(InversionA3YearsEn)}{(k=2025)} = 132102*0.1=13210$$
$$Inversión Nueva Depreciable {(InversionA5YearsEn)}{(k=2025)} = 132102*0.2=26420$$
$$Inversión Nueva Depreciable {(InversionA10YearsEn)}{(k=2025)} = 132102*0.5=66051$$
$$Inversión Nueva Depreciable {(InversionA20YearsEn)}{(k=2025)} = 132102*0.20=26420$$

Lo que coincide con la informacion que se reporta
![[Pasted image 20250909203116.png]]

Pero lo mas curioso es de donde el profesor esta sacando  $Inversión Nueva Depreciable_{K=2025}$. Basicamente se tienen varias opciones. La primera es inversiones en millones de pesos. La segunda son inversiones como % de ventas y la tercera inversiones como % de depreciacion. Que quiere decir esto?. Pues claramente como el PPE se desvaloriza con el tiempo (los equipos se desgastan), se hace necesario inyectar capital en mantenimiento para manetener esos activos en el tiempo, esa seria la tercera opcion. O tambien se pueden tener inversiones como producto de las ventas, o inversiones fijas en milllones de pesos. Demas que existen otras opciones pero estas fueron las presentadas. Para este caso se escogio que fuera el porcentaje de la depreacion mas especificamente invertir en capital en los anios lo que se deprecia en el anio

![[Pasted image 20250909205327.png]]

La cual, aunque la formula sea enrredada, no dice mas que se esta invirtiendo la depreciacion (Opcion 3, inversiones como % de depreciacion del 100%). En este caso ERI!H14 corresponde a la depreciacion en ese year (hay una referencia circular aqui, porque la depreciacion del año depende de la depreacion de activos historicos mas los nuevos, pero excel tiene como resolver esto. Sin embargo, podria resolverse calculando inicialmente la depreacion de los histociso y colocandolo como la inversion nueva). Por lo cual 
$$Inversión Nueva Depreciable_{K=2025} = \beta_{inversionDepreciacion} \cdot Depreciaciones_{K=2025} = 100\% \cdot Depreciaciones_{K=2025} = Depreciaciones_{K=2025}  $$
Por lo cual en el criterio decidido
$$Inversión Nueva Depreciable_{K} = Depreciaciones_{K}  $$
Ahora ya sabemos de donde viene 
$$Inversión Nueva Depreciable Total_{2025}$$ y las demas.  

Ahora volvamos de nuevo a las depreciaciones

![[Pasted image 20250909222936.png]]

Que significan los datos anteriores?. Partamos por un momento de la columna 2026p (no partimos de 2025p por una cosa que veremos en un momento)
![[Pasted image 20250909223056.png]]
En 2026p lo que estamos viendo es que para la depreciacion Inversion Nueva Ano 2025p. Como su nombre lo dice se refiere en principio a la depreciacion sobre la inversion realizada en 2025, que recordemos fue 132102. Si usamos el metodo de depreacion de linea [recta](https://www.youtube.com/watch?v=En3wXoFffyA), partiriamos de depreciar el monto en partes totales en los years de depreacion, en este caso 20. Por eso el /20. Ahora, analizando la depreciacion, todas deberian de ser 1321, por que no es asi?. Simple, estamos asumiendo que la inversion se realizo a mitades del 2025, y estamos depreciando la mitad para el siguiente anio, por lo que habra un medio anio de gracia mas. Como se muestra por ejemplo en la depreacion en 5 anos, donde tanto el inicio como el final coinciden

![[Pasted image 20250909223702.png]]
Ahora, podemos repetir el mismo analisis para las depreaciones de las inversiones que se dieron en 2026 hasta 2034, que es lo que plantea la matriz
![[Pasted image 20250909222936.png]]
Que es el analisis de las depreciaciones de cada year individual, siendo las filas las inversiones individuales y las columnas las de cada anio correspondiente a las individuales. 
Y es por eso que la depreacion de la inversion que se hizo en 2025, corresponde a la depreacion de las inversiones que se deprecian a 3 mas 5 mas las de 10 mas las de 20, porque juntan forman la inversion total
$$Depreciación Inversión Nueva Año2025_{K=2025} = DepreciacionInversionesDe_{t=20} + DepreciacionInversionesDe_{t=10} + DepreciacionInversionesDe_{t=5} + DepreciacionInversionesDe_{t=3} $$
Esta formula es enrredada, por eso es mejor verla desde su parte grafica. 



Finalmente ya podemos concluir que:

$$DepreciacionDelPeriodo_{K=N}=Depreciación Inversión Nueva Año 2025 + Depreciación Inversión Nueva Año 2026 + Depreciación Inversión Nueva Año 2027 + ... + Depreciación Inversión Nueva Año N$$

que vendrian siendo todas las depreciaciones, y que:

$$Depreciaciones Activos Nuevos = DepreciacionDelPeriodo$$

Y que 

## Ecuación Final

$$Depreciaciones_{K} = DepreciacionesActivosHistoricos_{K} + DepreciacionesActivosNuevos_{K}$$

### Nota

Ver que $DepreciacionDelPeriodo$ no fue mas que una variable dummy para calcular las diferentes depreciaciones. A lo largo de reporte de suelen usar.