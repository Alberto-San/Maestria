
## Para historia conocida y no proyeccion a futuro, el estado de resultados integrales (ERI)


$$ Utilidad Bruta = Ventas Netas - CostoDeVentas $$
$$MargenBruto = UtilidadBruta/VentasNetas$$
$$EBIT = UtilidadBruta - GastosAdministracion - GastosVenta - Depreciaciones - Amortizaciones$$

$$MargenOperacional = \frac{EBIT}{VentasNetas}$$
$$EBIDA=EBIT + Depreciaciones + Amortizaciones$$
$$MargenEbitda=\frac{EBITDA}{VentasNetas}$$
$$UtilidadesAntesDeImpuestos=EBIT + IngresosFinancieros + OtrosIngresos - EgresosFinancieros - OtrosEgresos$$
$$UtilidadNeta = UtilidadesAntesDeImpuestos - ImpuestoRenta$$

$$MargenNeto=UtilidadNeta/VentasNetas$$

## Para historia conocida y no proyeccion a futuro, el estado de situacion financiera (ESF)

### Activos Corrientes

$$ActivosCorrientes = Disponible + InversionesTemporales + CuentasPorCobrar_{Deudores} + OtrasCuentasPorCobrar + Inventarios + PagosxAnticipados + OtrosActivosCorrientes $$

### Activos Largo Plazo
$$PropiedadPlantayEquipo_{Neto}=PropiedadesPlantayEquipo_{PPE} + DepreciacionAcumulada$$
$$DiferidosEIntagibles_{Neto}=ActivosDiferidosEIntangibles - AmortizacionAcumulada$$
$$ActivosLargoPlazo = PropiedadPlantayEquipo_{Neto} + DiferidosEIntagibles_{Neto} + OtrosActivos + Valorizaciones + Inversiones$$
### Total Activos
$$TotalActivos = ActivosCorrientes + ActivosLargoPlazo$$

### Pasivos Corrientes

$$PasivosCorrientes = ObligacionesFinCortoPlazo + Proveedores + ImpuestosYRetenciones + ObligacionesLaborales + OtrosAcreedores + OtrosPasivosCorriente$$
### Pasivos Largo Plazo
$$PasivosLargoPlazo = ObligacionesFinDeLargoPlazo + OtrosPasivosDeLargoPlazo$$

### Total Pasivos
$$TotalPasivos = PasivosCorrientes + PasivosLargoPlazo$$

### Patrimonio
$$RevalorizacionesDelPatrimonio = RevalorizacionesDelPatrimonio_{original} - Valorizaciones$$
$$UtilidadesRetenidas = UtilidadesRetenidas_{original} - UtilidadesDelEjercicio$$
$$TotalPatrimonio = Capital + Reservas + RevalorizacionesDelPatrimonio + UtilidadesRetenidas + UtilidadesDelEjercicio + Valorizaciones$$

### Ecuacion de chequeo
$$TotalPasivos + Patrimonio = TotalActivos$$
# Proyecciones a futuro

## ERI

Para la proyeccion de las ventas, se debe primero de chequear como ha sido el incremento de ventas netas year over year. En teoria se espera crecer de manera positiva. Sobre ese crecimiento, se puede hacer un estimado de como ha sido el crecimiento en ventas cada year, y por ejemplo a futuro tener un criterio y decir si se va a crecer como el promedio de los ultimos years, o si se tienen ciertas metas, colocarlo. Pero siempre debe de justificarse.
$$IncrementoPorcentualVentasNetas_{Historico K}=(\frac{Ventas_{k}}{Ventas_{k-1}}-1)$$
$$IncrementoPorcentualVentasNetas_{Supuesto K}=Criterio$$

Con el incremento porcentual, se puede calcular el crecimiento a futuro:
$$VentasNetas_{k} = VentasNetas_{k-1} \cdot (1 + IncrementoPorcentialVentasNetas_{SupuestoK})$$
Para el crecimeinto en costos, pueden haber varios criterios. Uno de los que se puede usar, es el porcentaje que representan los costos en el historico
$$CostoVentasSobreVentasNetas_{HistoricoK} =\frac{CostodeVentas_{k}}{VentasNetas_{k}}$$
Y de manera similar tener un criterio para los costos futuros
$$IncrementoPorcentualCostoVentas_{Supuesto K}=Criterio$$
Calculando el crecimiento a futuro
$$CostoVentas_{k} = VentasNetas_{k-1} \cdot IncrementoPorcentialCostoVentas_{SupuestoK}$$
Observar que esta ves el incremento porcentual costo ventas es menor a 1, mientras que en el anterior se calculaba 1 + incremento. La diferencia radica en que el analisis del costo de ventas parte de ser una fraccion de las ventas totales. 

Los gastos de administracion son un poco mas curiosos. En el modelo los gastos de administracion contemplan los gastos de administracion + el canon de leasing operativo, que no es mas que una cuota o pago que una empresa o persona paga por usar un activo del que no es duenio. Y dado que los gastos de administracion no se mueven como los costos de ventas que se correlacionan mas con las ventas totales, los gastos de administracion se analizan de manera similar a las ventas netas.

$$IncrementoPorcentualGastosAdministracion_{Historico K}=(\frac{GastosAdministracion_{k}}{GastosDeAdministracion_{k-1}}-1)$$
Por supuesto, el valor futuro viene dado por 
$$GastosAdministrativos_{k} = GastosAdministrativos_{k-1} \cdot (1 + IncrementoPorcentialGastosAdministrativos_{SupuestoK})$$
Siendo el supuesto lo que se determine para el futuro (eg: el promedio, o una meta especifica)

Los gastos de ventas si se calculan como los costos de venta, se asume correlacion, a mas ventas mas gatos de ventas.

$$GastoDeVentasSobreVentasNetas_{HistoricoK} =\frac{GastoDeVentas_{k}}{VentasNetas_{k}}$$
Calculando el crecimiento a futuro del gasto de ventas
$$GastoDeVentas_{k} = VentasNeta_{k-1} \cdot IncrementoPorcentialGastoDeVentasSobreVentasNetas_{SupuestoK}$$


### Depreciaciones: Seccion Especial

Ahora, el tema de las depreciaciones si es un poco mas dificil. Las depreciaciones historicas son las que reporta la empresa. Sin embargo, para predecir las depreciaciones futuras, se tiene que tener en cuenta las depreciaciones de activos historicos y depreciones de activos nuevos.  Las depreciaciones de activos historicos a futuro, corresponde a la ultima Propiedad Planta y Equipo por la depreciacion del periodo (recordar que el equipo disminuye con el tiempo). Por supuesto la depreciacion del periodo no es gratuita. Se tienen las depreciacioens historicas, y con estas se puede calcular la depreacion sobre el PPE para obtener el porcentaje de depreciacion historico
$$\% Depreciación del Período | Saldo_{HistoricoK}=\frac{Depreciacion}{PPE}$$, y la depreciacion a futuro, no es mas que el criterio que se tome
$$\% DepreciacionDelPeriodo | Saldo {k}=Criterio$$

Por tanto la depreciacion del periodo no es mas que el ultimo PPE por la depreciacion del periodo comparado con el saldo de ese periodo K.

$$DepreciacionDelPeriodo_{K}  = \% Depreciación del Período | Saldo_{K} \cdot UltimoPPE$$
Y la depreciacion acumulada vendria siendo el % de depreciacion year over year. 


La depreciacion acumulada PPE historica vendria siendo la depreciacion acumulada PPE historica del year anterior + depreciacion del periodo (aprox).
$$DepreciacionAcumuladaPPEHistorica_{k}=DepreciacionAcumuladaPPEHistorica_{k-1} + DepreciacionDelPeriodo_{k}$$


Y las depreciaciones de activos historicos vendrian siendo
$$DepreciacionesActivosHistoricos_{K} = DepreciacionDelPeriodo_{K}$$

Observar que la depreacion de activos historicos nunca se calculo para los periodos donde la empresa reporto el balance. Porque la idea es como calcular de lo que existe hoy, como se va a depreciar ese PPE en el futuro. 

Ahora calcular la depreciacion para el llamado activos nuevos si es una locura. Y de nuevo solo tiene sentido para el futuro, no para el historico. 

Y las de activos nuevos
$$Depreciaciones Activos Nuevos = DepreciacionDelPeriodo$$
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

La cual, aunque la formula sea enrredada, no dice mas que se esta invirtiendo la depreciacion (Opcion 3, inversiones como % de depreciacion del 100%). En este caso ERI!H14 corresponde a la depreciacion en ese year. Por lo cual 
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
$$Depreciación Inversión Nueva Año2025{_K=2025} = DepreciacionInversionesDe_{t=20} + DepreciacionInversionesDe_{t=10} + DepreciacionInversionesDe_{t=5} + DepreciacionInversionesDe_{t=3} $$
Esta formula es enrredada, por eso es mejor verla desde su parte grafica. 



Finalmente ya podemos concluir que:

$$DepreciacionDelPeriodo_{K=N}=Depreciación Inversión Nueva Año 2025 + Depreciación Inversión Nueva Año 2026 + Depreciación Inversión Nueva Año 2027 + ... + Depreciación Inversión Nueva Año N$$

que vendrian siendo todas las depreciaciones, y que:

$$Depreciaciones Activos Nuevos = DepreciacionDelPeriodo$$

Y que 

$$Depreciaciones_{K} = DepreciacionesActivosHistoricos_{K} + DepreciacionesActivosNuevos_{K}$$
