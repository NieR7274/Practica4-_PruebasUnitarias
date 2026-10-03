# Version Python

## Ejecutar

    python -m pip install -r requirements.txt
    pytest -v

El archivo test_estacionamiento.py contiene unicamente un ejemplo inicial.
La actividad consiste en disenar la suite completa a partir del modelo de la practica.

## Preguntas de Analisis

### 1. Que diferencia hay entre un caso normal y un caso frontera?
Un caso normal prueba el comportamiento del sistema en situaciones tipicas y seguras.
Un caso frontera prueba los limites exactos donde las reglas cambian de estado para asegurar que la transicion entre comportamientos no falle.

### 2. Cual de sus pruebas considera mas importante y por que?
Considero que todas las pruebas son importantes, ya que cada una detecta fallos que no deberian ocurrir bajo ninguna circunstancia. Sin embargo, si tuviera que jerarquizarlas por orden de prioridad, seria el siguiente:

1. Las pruebas de excepciones y entradas invalidas: Son las mas criticas porque evitar que el sistema colapse o lance un error no controlado (TypeError, Crash) es prioridad.
2. Los casos frontera: Porque son los puntos donde la logica cambia de estado. Si una frontera falla, el sistema empieza a cobrar de mas o de menos a muchisimos usuarios.
3. Casos normales e interacciones: Las pruebas de flujo comun, que aseguran que el negocio calcule correctamente los descuentos y las tarifas del dia a dia.

### 3. Encontro algun comportamiento de la implementacion que no coincida con el modelo?
Si, la implementacion original contenia varios fallos graves respecto al modelo:

* R1 (Tipado): No valida que los minutos sean enteros, permitiendo decimales sin lanzar error, y si recibe texto arroja un TypeError no controlado en lugar de ValueError.
* R5 (Limite de gracia): Usaba `< 15` en lugar de `<= 15`, cobrando a los 15 minutos exactos cuando debia ser $0.00.
* R7 (Horas adicionales): Usaba la division entera `// 60`, fallando al cobrar la hora iniciada (61 min cobraba $20 en lugar de $35; 121 min cobraba $35 en lugar de $50).
* R8 (Descuento inapropiado): Le aplicaba el 10% de descuento de cliente frecuente a la tarifa de boleto perdido ($270 en lugar de los $300 fijos).

### 4. Una suite con 100% de pruebas aprobadas demuestra que el programa es correcto? Explique.
No. Que todas las pruebas pasen solo demuestra que el programa responde bien a los escenarios que decidimos probar. Por ejemplo, de los 17 casos que disenamos en el cuadro pasaron todas las pruebas, pero si colocabamos un dato no numerico en el argumento de minutos, por el orden de la validacion intentaba evaluar si era menor a 0 y rompia el programa.

### 5. Si una IA generara automaticamente 50 pruebas, que tendria que revisar una persona antes de confiar en ellas?


