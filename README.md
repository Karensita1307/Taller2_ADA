## Taller 2 de ADA
---

## Integrantes del grupo

| Nombre Completo                | Código     | Rol           | Correo Electrónico                        |
|--------------------------------|------------|---------------|-------------------------------------------|
| Karen Sofía López Botero       | 202459519  | Colaborador   | karen.sofia.lopez@correounivalle.edu.co   |
| Laura Sofía Echeverry González | 202477067  | Colaborador   | echeverry.laura@correounivalle.edu.co     |

---

# Problema 1
## Estructura de datos implementada
Estructura de datos de pila.

En este problema se implementó una pila para simular el comportamiento de un editor de texto con opción de deshacer. La pila permite que la última palabra escrita sea la primera en eliminarse, siguiendo el principio LIFO (Last In, First Out).

- La operación `ESCRIBIR palabra` agrega una palabra al texto usando `push`.
- La operación `DESHACER` elimina la última palabra escrita usando `pop`, siempre que la pila no esté vacía.
- La operación `MOSTRAR` imprime todas las palabras en el orden en que fueron escritas, o `VACIO` si no hay ninguna palabra almacenada.

Esta estructura fue adecuada porque el comando de deshacer siempre actúa sobre el elemento más reciente ingresado.

---

# Problema 2
## Estructura de datos implementada
Estructura de datos de cola.

En este problema se implementó una cola para simular el comportamiento de una sala de urgencias, donde los pacientes son atendidos en el mismo orden en que llegan.
 La cola permite que la primera persona que entra sea la primera en atenderse.

- La operación `LLEGA nombre` agrega un paciente al final de la cola.
- La operación `ATIENDE` atiende y elimina al primer paciente de la cola.
- La operación `SIGUIENTE` muestra el nombre del próximo paciente a atender.

Esta estructura fue adecuada porque el comando de atiende siempre actúa sobre el elemento que primero se ingresó.

---

# Problema 3
## Estructura de datos implementada
....

---

# Problema 4
## Estructura de datos implementada
Estructura de datos de tabla hash.

En este problema se implementó una tabla hash para registrar y consultar la cantidad de productos vendidos durante el día. La tabla hash permite asociar cada producto con la cantidad total vendida, usando el nombre del producto como clave y la cantidad como valor.

- La operación `VENDER producto cantidad` actualiza la cantidad acumulada del producto en la tabla hash.
- La operación `CONSULTAR producto` busca el producto y muestra su cantidad vendida; si no existe, imprime `0`.
- La operación `TOTAL` recorre la tabla hash y suma todas las cantidades almacenadas.

Esta estructura fue adecuada porque permite buscar, insertar y actualizar productos de forma eficiente, incluso cuando hay varios productos distintos registrados.

---
