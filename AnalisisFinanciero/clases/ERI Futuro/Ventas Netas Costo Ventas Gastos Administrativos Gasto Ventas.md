

### Ventas Netas

Para la proyeccion de las ventas, se debe primero de chequear como ha sido el incremento de ventas netas year over year. En teoria se espera crecer de manera positiva. Sobre ese crecimiento, se puede hacer un estimado de como ha sido el crecimiento en ventas cada year, y por ejemplo a futuro tener un criterio y decir si se va a crecer como el promedio de los ultimos years, o si se tienen ciertas metas, colocarlo. Pero siempre debe de justificarse.

$$IncrementoPorcentualVentasNetas_{Historico K}=(\frac{Ventas_{k}}{Ventas_{k-1}}-1)$$
$$IncrementoPorcentualVentasNetas_{Supuesto K}=Criterio$$

Con el incremento porcentual, se puede calcular el crecimiento a futuro:
$$VentasNetas_{k} = VentasNetas_{k-1} \cdot (1 + IncrementoPorcentialVentasNetas_{SupuestoK})$$

### Costo Ventas

Para el crecimeinto en costos, pueden haber varios criterios. Uno de los que se puede usar, es el porcentaje que representan los costos en el historico
$$CostoVentasSobreVentasNetas_{HistoricoK} =\frac{CostodeVentas_{k}}{VentasNetas_{k}}$$
Y de manera similar tener un criterio para los costos futuros
$$IncrementoPorcentualCostoVentas_{Supuesto K}=Criterio$$
Calculando el crecimiento a futuro
$$CostoVentas_{k} = VentasNetas_{k-1} \cdot IncrementoPorcentialCostoVentas_{SupuestoK}$$
Observar que esta ves el incremento porcentual costo ventas es menor a 1, mientras que en el anterior se calculaba 1 + incremento. La diferencia radica en que el analisis del costo de ventas parte de ser una fraccion de las ventas totales. 


### Gastos Administrativos

Los gastos de administracion son un poco mas curiosos. En el modelo los gastos de administracion contemplan los gastos de administracion + el canon de leasing operativo, que no es mas que una cuota o pago que una empresa o persona paga por usar un activo del que no es duenio. Y dado que los gastos de administracion no se mueven como los costos de ventas que se correlacionan mas con las ventas totales, los gastos de administracion se analizan de manera similar a las ventas netas.

$$IncrementoPorcentualGastosAdministracion_{Historico K}=(\frac{GastosAdministracion_{k}}{GastosDeAdministracion_{k-1}}-1)$$
Por supuesto, el valor futuro viene dado por 
$$GastosAdministrativos_{k} = GastosAdministrativos_{k-1} \cdot (1 + IncrementoPorcentialGastosAdministrativos_{SupuestoK})$$
Siendo el supuesto lo que se determine para el futuro (eg: el promedio, o una meta especifica)

### Gastos de Ventas

Los gastos de ventas si se calculan como los costos de venta, se asume correlacion, a mas ventas mas gatos de ventas.

$$GastoDeVentasSobreVentasNetas_{HistoricoK} =\frac{GastoDeVentas_{k}}{VentasNetas_{k}}$$
Calculando el crecimiento a futuro del gasto de ventas
$$GastoDeVentas_{k} = VentasNeta_{k-1} \cdot IncrementoPorcentialGastoDeVentasSobreVentasNetas_{SupuestoK}$$

