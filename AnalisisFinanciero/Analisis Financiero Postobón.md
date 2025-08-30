
He descargado la siguiente información de la Superintendencia de Supersociedades. La información corresponde a la del año 2024 de la empresa Postobón, empresa de Colombia. 

La idea es convertir todo a json, verdad?. Una de las cosas que acabo de analizar es en relación a como procesar la información. Siempre existen espacios en blanco que son los que determinan el nivel de profundidad de las filas (espacios en blanco a la derecha), y el nivel de profundidad de las columnas. Sobre eso ya se puede empezar a procesar la información y formatearla para que se tenga una sola representación. 
![[Pasted image 20250829134218.png]]
Para el ejemplo, se tiene una profundidad de jerarquia de columnas de 3, y una profundidad de jerarquia de filas de 5. 
Como sería el algoritmo?

1. Detectar profundidad a nivel de columnas y filas.
2. Detectar donde se encuentra la información. 
3. Formatear filas y columnas. Obedeciendo a una jerarquia separada por punto. Para las filas claramente se empieza en el ejemplo por "Estados de cambio en el patrimonio [sinopsis].Estados de cambios en el patrimonio [partidas].Patrimonio al comiendo del periodo" hasta dejar todo en terminos de 1 sola columna. Lo mismo las columnas que contienen a otras. 
4. Una vez realizado esto se reconfiguran las columnas, y se pega el contenido en el nuevo esquema. 

Eduard realizó el código.

se tiene que correr en orden

python3 AnalisisFinanciero\procesador_inicial_superintendencia\flatten_excel.py --input_dir AnalisisFinanciero\data --output_subdir flattened --keep_all_columns --verbose

python3 AnalisisFinanciero\transformador_superintendencia\main.py --input_dir "AnalisisFinanciero\postobon\flattened" --output_dir "AnalisisFinanciero\postobon\transform" --verbose

python3 AnalisisFinanciero\main.py --input_dir "AnalisisFinanciero\data\transform" --output_dir "AnalisisFinanciero\data\json"