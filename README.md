JAVA
1. *insertarVentas(String departamento, int mes, double venta)*:
    - Qué hace: Inserta una venta en la matriz de ventas para un departamento y mes específico.
    - Cómo funciona: 
        - Primero, se busca el índice del departamento en el arreglo departamentos usando Arrays.asList(departamentos).indexOf(departamento). Si el departamento existe, se obtiene el índice.
        - Luego, verifica si el mes está dentro del rango válido (entre 1 y 12).
        - Si todo es correcto, almacena la venta en la posición correspondiente dentro de la matriz ventas en la fila del departamento y la columna del mes.

2. buscarVenta(String departamento, int mes):
    - Qué hace: Busca y devuelve la venta de un departamento en un mes específico.
    - Cómo funciona:
        - Similar al método de inserción, primero encuentra el índice del departamento en el arreglo departamentos.
        - Verifica que el mes sea válido.
        - Si los datos son correctos, devuelve el valor almacenado en la matriz ventas en la fila del departamento y la columna del mes.

3. eliminarVenta(String departamento, int mes):
   Qué hace: Elimina la venta de un departamento en un mes específico (poniendo el valor a 0).
   Cómo funciona:
   Encuentra el índice del departamento en el arreglo departamentos.
   Verifica que el mes esté dentro del rango adecuado.
   Si todo está bien, asigna 0 a la posición correspondiente en la matriz ventas.

PYTHON

1. insertar_ventas(departamento, mes, venta):
   Qué hace: Inserta una venta en la matriz de ventas para un departamento y mes específico.
   Cómo funciona:
        - Se busca el índice del departamento dentro de la lista departamentos usando self.departamentos.index(departamento).
        - Se verifica que el mes esté entre 1 y 12.
        - Si todo es correcto, se guarda la venta en la matriz ventas en la fila correspondiente al departamento y la columna del mes (restando 1 al mes porque el índice empieza en 0).

2. buscar_venta(departamento, mes):
   Qué hace: Busca y devuelve la venta de un departamento en un mes específico.
   Cómo funciona:
        - Primero, se encuentra el índice del departamento en la lista departamentos.
        - Verifica si el mes está dentro del rango permitido.
        - Si todo es válido, retorna el valor almacenado en la matriz ventas en la fila del departamento y la columna del mes.

3. eliminar_venta(departamento, mes):
   Qué hace: Elimina la venta de un departamento en un mes específico, colocando el valor en 0.
   Cómo funciona:
        - Encuentra el índice del departamento en la lista departamentos.
        - Verifica que el mes esté en el rango correcto.
        - Si todo está bien, asigna 0 a la posición correspondiente en la matriz ventas en la fila del departamento y la columna del mes.

Diferencias entre Java y Python:
1. Sintaxis:
    - Java: es necesario declarar los tipos de datos de los parámetros y el retorno de los métodos. Además, el manejo de arreglos requiere de la clase Arrays para funciones como indexOf.
    - Python: los tipos no se especifican explícitamente en las funciones, y la lista y matriz se manipulan más fácilmente.
2. Manejo de Índices:
    - En ambos lenguajes, los meses se almacenan en posiciones del 0 al 11, aunque para el usuario se presentan como del 1 al 12. En ambos casos, se ajusta el mes restando 1 para acceder al índice correcto
3. Mensajes de error:
    - Ambos programas incluyen comprobaciones de error cuando se ingresa un departamento o mes no válido, pero la forma en que se manejan los mensajes es distinta (uso de System.out.println en Java frente a print en Python).
