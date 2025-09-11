
Los ingresos financieros historicos son fáciles de calcular, ya lo vinos, vienen reportados por la compañia. Sin embargo, si se desea predecir estos ingreso al futuro, se puede realizar de muchas formas. Una de ellas es por ejemplo proyectado si se invierte todos el $Disponible e Inversiones Temporales$ del año anterior en por ejemplo en un depósito a término fijo, que sucedería.

$$Ingresos Financieros_{Supuesto(K)} = Disponible e Inversiones Temporales_{K-1} \cdot Rendimiento Promedio Anual DFT_{Supuesto(K)} $$
Por ejemplo, si se tuviera en el año 2024 $Disponible e Inversiones Temporales_{K=2024}=100$, y se tiene que para el 2025 el $Rendimiento Promedio Anual DFT_{Supuesto(2025)}=8\%$, para el 2025 se esperarían ingresos financieros de $Ingresos Financieros_{Supuesto(2025)} = 100 * 0.08 = 8$ , que serian los ingresos extras productos de esa inversión. 
Pero que son $Disponible e Inversiones Temporales_{K}$. Bueno, no es una pregunta tan difícil. El dispuesto en inversiones se compone de lo que se tiene disponible en efectivo mas las inversiones que se han hecho en ese año. A nivel histórico viene dado por el balance financiero

$$Disponible e Inversiones Temporales_{Historico(K)} = Disponible^{ActivosCorriente}_{Historico(K)} + Inversiones Temporales^{ActivosCorriente}_{Historico(K)}$$
Y aplica de manera similar para los supuestos. 

Concentremonos de donde proviene  $Disponible^{ActivosCorriente}_{Historico(K)}$.
$$Disponible^{ActivosCorriente}_{Historico(K)}=Reportado$$
pero que pasa en el futuro?
$$Disponible^{ActivosCorriente}_{Supuestos(K)}=\frac{Días de Ventas Netas_{Supuesto(K)}}{365} \cdot Ventas Netas_{Supuesto(K)}$$
Concentremonos un momento de donde sale  $Días de Ventas Netas_{(K)}$. Miremos de donde sale el termino historico. 
 $$Días de Ventas Netas_{Historico(K)} = \frac{Disponible^{ActivosCorrientes}_{Historico(K)}}{Ventas Netas_{Historico(K)}}*365$$
 ¿Cómo entender la ecuación anterior?. Tu puedes vender X cantidad. Pero puedes venderla con plazos de pago extendidos, no necesariamente van a pagarte inmediatamente. Ahora, si comparamos lo que te han pagado con lo que vendiste, y si estos valores son anuales, vas a tener un ratio de lo disponible con respecto a lo que vendiste en el año. Pero si eso lo divides por 365 tienes el ratio por dia. Por eso los dias ventas netas corresponde a los dias en que se demora en convertirse en efectivo esa venta. 

Ahora, para el futuro los días ventas netas depende del criterio que tomes. Ese criterio va a decidir la estrategia de la compañía con los compradores. 
 $$Días de Ventas Netas_{Supuesto(K)} = Criterio$$
 Ahora,  con esto ya resolvimos $Disponible^{ActivosCorriente}_{Supuestos(K)}$. Sabemos que
$$Disponible e Inversiones Temporales_{Historico(K)} = Disponible^{ActivosCorriente}_{Historico(K)} + Inversiones Temporales^{ActivosCorriente}_{Historico(K)}$$
y sabemos que 
$$Disponible e Inversiones Temporales_{Supuesto(K)} = Disponible^{ActivosCorriente}_{Supuesto(K)} + Inversiones Temporales^{ActivosCorriente}_{Supuesto(K)}$$
Ahora faltaría conocer el termino $Inversiones Temporales^{ActivosCorriente}_{Supuesto(K)}$

El histórico de inversiones temporales viene dado por la historia reportada
$$Inversiones Temporales^{ActivosCorriente}_{Historico(K)} = Historia$$
El futuro viene dado por 
$$Inversiones Temporales^{ActivosCorriente}_{Supuesto(K=2025)} = Caja Final_{Supuesto(K=2025)}$$

$$Caja Final_{Supuesto(K=2025)}=Flujo de Caja Generado_{K=2025} + Caja Inicial_{K=2025} - Dividendos_{K=2025}$$



Concentremonos en el primer termino. Flujo de caja generado.Que logica hay detrás de esto?, no lo sé.

$$Flujo de Caja Generado_{Supuesto(K=2025)}=Flujo de Caja Libre de la Compañía_{Supuesto(K=2025)} + Flujo de Caja Financiero_{Supuesto(K=2025)} + Otros pasivos LP_{Supuesto(K=22025)}$$

$$Flujo de Caja Libre de la Compañía_{Supuesto(K=2025)}=Flujo de Caja Operación_{Supuesto(K=2025)} + Flujo de Caja Inversión_{Supuesto(K=2025)}$$

$$Flujo de Caja Operación_{Supuesto(K=2025)} = Ebitda_{Supuesto(K=2025)} + Necesidades Netas de Capital de trabajo_{Supuesto(K=2025)} - Impuesto de Renta_{Supuesto(K=2025)}$$
$$Ebitda_{Supuesto(K=2025)}=Calculado$$

## Necesidades Netas de Capital de trabajo
$$Necesidades Netas de Capital de trabajo_{Supuesto(K=2025)} = Financiación ProveedMenosPas Corr_{(K=2025)} -  Inversión en Act Corrientes_{(K=2025)}$$


$Financiacion ProveedPas Menos Pas Corr_{(K=2025)}$ puede entenderse como el efecto de tener un pasivo corriente financiado por las deudas del proveedor comparado con los pasivos corrientes. La idea es apalancarse en los proveedores
$$Financiacion ProveedPas Menos Pas Corr_{(K=2025)} = (Proveedores_{K=2025}+Impuestos y Retenciones_{K=2025}+Obligaciones Laborales_{K=2025}+Otros Acreedores_{K=2025}+Otros Pasivos Corrientes_{K=2025})-(Proveedores_{K=2024}+Impuestos y Retenciones_{K=2024}+Obligaciones Laborales_{K=2024}+Otros Acreedores_{K=2024}+Otros Pasivos Corrientes_{K=2024})$$

$Inversión en Act Corrientes_{(K=2025)}$ puede entenderse como la inversión realizada de un año a otro en activos corrientes.
$$Inversión en Act Corrientes_{(K=2025)} =(Disponible_{K=2025}+Cuentas por Cobrar (Deudores)_{K=2025}+Otras Cuentas por Cobrar_{K=2025}+Inventarios_{K=2025}+Pagos x Anticipado_{K=2025}+Otros Activos Corrientes_{K=2025})-(Disponible_{K=2024}+Cuentas por Cobrar (Deudores)_{K=2024}+Otras Cuentas por Cobrar_{K=2024}+Inventarios_{K=2024}+Pagos x Anticipado_{K=2024}+Otros Activos Corrientes_{K=2024})$$
Con lo anterior entonces ya se tendría el termino de $Necesidades Netas de Capital de trabajo_{Supuesto(K=2025)}$, que no es mas que el efecto de lo que apalanca los proveedores vs el efecto de los activos corrientes. Si se tiene $Necesidades Netas de Capital de trabajo_{Supuesto(K)}$ positivo significa que se esta apalancando la operación a través de los proveedores, por eso el capital de trabajo. A veces el capital de trabajo se desea disminuir, pero a veces sirve para apalancarse.

