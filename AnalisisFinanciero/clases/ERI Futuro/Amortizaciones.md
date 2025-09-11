Para las amortizaciones el análisis es muy similar al que se tiene en depreciaciones, por que al final las amortizaciones son depreciaciones sobre intangibles.  Aqui un parentesis. La depreciacion se realiza sobre activos que son fisicos. La amortizacion es como una depreciacion pero sobre activos intangibles. Y como las depreciaciones, su valor depende de leyes de cada pais sobre diferentes tipos de activos intangibles. 
$$Amortizaciones_{Supuesto(K)} = Amortizaciones Activos Diferidos e Intangibles Históricos_{Supuesto(K)} + Amortizaciones Activos Diferidos e Intangibles Nuevos_{Supuesto(K)} $$

Antes de estudiar esto se recomienda estudiar [[Depreciaciones]]

#### Amortizaciones Intangibles Historicos (Activos Diferidos e Intangibles)

Similar a las depreciaciones historicas, los intangibles también se deprecian en el tiempo.

$$\% Amortización del Período/Saldo_{Historico(K)} = \frac {Amortización del período_{Historico(K)}}{Activos Diferidos e Intangibles Histórico_{Historico(K)}}$$

Y 
$$\% Amortización del Período/Saldo_{Supuesto(K)} = Criterio$$
la amortización del periodo sobre el saldo no es mas que el criterio que se tome. 


Por tanto la amortización del periodo no es mas que el ultimo $Activos Diferidos e Intangibles Histórico_{Historico(K)}$ por la depreciacion del periodo comparado con el saldo de ese periodo K.

$$AmortizaciónDelPeriodo_{K}  = \% Amortización del Período | Saldo_{K} \cdot Ultimo Activos Diferidos e Intangibles Histórico_{Historico(K)}$$

Las amortizaciones de activos diferidos historicos vendrian siendo entonces
$$Amortizaciones Activos Diferidos e Intangibles Históricos_{Supuesto(K)} = Amortización del período_{Supuesto(K)}$$

#### Amortizaciones Intangibles Nuevos

Similar a las depreciaciones. 
$$Amortizaciones Activos Diferidos e Intangibles Nuevos_{Supuesto(K)} = AmortizaciónDelPeriodo_{Supuesto(K)}$$

$$AmortizaciónDelPeriodo_{Supuesto(K=2025)}=Amortización Gasto o Cargo Diferido Nuevo Año 2025$$
$$AmortizaciónDelPeriodo_{Supuesto(K=2026)}=Amortización Gasto o Cargo Diferido Nuevo Año 2025 + Amortización Gasto o Cargo Diferido Nuevo Año 2026$$
$$AmortizaciónDelPeriodo_{Supuesto(K=N)}=Amortización Gasto o Cargo Diferido Nuevo Año 2025 + Amortización Gasto o Cargo Diferido Nuevo Año 2026 + Amortización Gasto o Cargo Diferido Nuevo Año N$$

Y de manera similar se tienen entonces amortizaciones por año, que se depreciacian y se estudian de manera independiente..

![[{C1E69754-9D14-46CD-B67A-F5AA2ECF8416}.png]]

Y también se tiene
$$Amortización Gasto o Cargo Diferido Nuevo Año 2025 = Amortización 3 años + Amortización a 5 años + Amortización a 10 años + Amortización a 20 años$$

Se tiene items de $Amortización Gasto o Cargo Diferido Nuevo Año N$. Cada una de estas se compone de amortizaciones objetivos a varios años (3, 5, 7, 9). Que opera similar a las inversiones que se vieron en depreciaciones. 
Eg:
$$Gasto o Cargo Diferido Nuevo Amortizable = Activos Diferidos e Intangibles Nuevo$$
$$Gasto o Cargo Diferido Nuevo Amortizable = Activos Diferidos e Intangibles Nuevo 2025 = 6483$$
$$Gasto o Cargo Diferido Nuevo Amortizable a 20 años = 40\% * Gasto o Cargo Diferido Nuevo Amortizable 2025 = 2593$$

Y asi mismo existen diferentes para ese año a diferentes años
Y se tienen diferentes tasas de depreciacion que se analizan. 
Pero, de donde sale $ActivosDiferidoseIntagiblesNuevos2025$?

Hay varias opciones. Pueden salir como una porcion de los Activos Diferidos e Intangibles del año anterior, donde se contempla una parte para re inversión, o pueden salir como parte de ventas, o como porcentaje de depreciación, todo depende de lo que se desee. Para este caso, salen como una parte (digamos invertir el 7% de los activos diferidos e intangibles historicos del año pasado). Similar a como funcionaban en las inversiones
 $$ActivosDiferidoseIntagiblesNuevos2025 = 7\% \cdot Activos Diferidos e Intangibles_{K=2024}$$
Y asi, se van recalculando los de cada año, y se completa la matriz
![[{C1E69754-9D14-46CD-B67A-F5AA2ECF8416}.png]]

Con esto ya se tiene 
$$AmortizaciónDelPeriodo_{Supuesto(K=N)}$$
Y sabemos que 
$$Amortizaciones Activos Diferidos e Intangibles Nuevos_{Supuesto(K)} = AmortizaciónDelPeriodo_{Supuesto(K)}$$


## Ecuación Final

$$Amortizaciones_{Supuesto(K)} = Amortizaciones Activos Diferidos e Intangibles Históricos_{Supuesto(K)} + Amortizaciones Activos Diferidos e Intangibles Nuevos_{Supuesto(K)} $$

### Nota

Ver que $AmortizaciónDelPeriodo_{Supuesto(K=N)}$ no fue mas que una variable dummy para calcular las diferentes depreciaciones. A lo largo de reporte de suelen usar.