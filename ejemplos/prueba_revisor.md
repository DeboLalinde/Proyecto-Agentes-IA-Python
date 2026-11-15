# Prueba del agente revisor

# Caso 1: borrador coherente

# Guía de estudio: listas de Python

## Explicación

**¿Qué es y para qué sirve?**
Una lista en Python es una colección ordenada y modificable (mutable) de datos. Sirve para almacenar múltiples elementos en una sola variable, como listas de números, nombres o cualquier otro tipo de objeto.

**Ejemplo:**
```python
frutas = ["manzana", "banana", "naranja"]

# Acceder al primer elemento
print(frutas[0])  # Muestra: manzana

# Agregar un nuevo elemento
frutas.append("pera")
print(frutas)  # Muestra: ['manzana', 'banana', 'naranja', 'pera']
```

**Error frecuente:**
El error `IndexError: list index out of range`. Ocurre cuando intentas acceder a una posición (índice) que no existe en la lista. 

*¿Cómo evitarlo?* Recuerda que las listas en Python empiezan a contar desde el índice `0`. Si una lista tiene 3 elementos, sus índices son `0`, `1` y `2`. Puedes usar la función `len(tu_lista)` para verificar la cantidad de elementos antes de acceder a un índice.

## Práctica

**Ejercicio de práctica: Mi lista de colores**

Crea una lista llamada `colores` que contenga tres nombres de colores de tu elección. Después, agrega un cuarto color a la lista utilizando el método `.append()`. Por último, imprime en pantalla el primer color de la lista y la cantidad total de elementos que contiene la lista.

---

**Criterios de aceptación:**
1. La variable `colores` se inicializa como una lista de 3 elementos y posteriormente pasa a tener 4 elementos mediante el uso de `.append()`.
2. Se imprime en consola el primer elemento de la lista haciendo uso del índice `0`.
3. Se muestra en consola el número total de elementos presentes en la lista utilizando la función `len()`.

---

**Pista:**
Recuerda que en Python las posiciones de las listas comienzan en `0` para el primer elemento, y que la función `len(tu_lista)` te devuelve un número entero con la cantidad actual de ítems.

## Revisión

No se requirieron cambios importantes.

# Caso 2: borrador contradictorio

# Guía de estudio: listas de Python

## Explicación

**¿Qué es y para qué sirve?**
Una lista en Python es una colección ordenada y modificable (mutable) de datos. Sirve para almacenar múltiples elementos en una sola variable, como listas de números, nombres o cualquier otro tipo de objeto.

**Ejemplo:**
```python
frutas = ["manzana", "banana", "naranja"]

# Acceder al primer elemento
print(frutas[0])  # Muestra: manzana

# Agregar un nuevo elemento
frutas.append("pera")
print(frutas)  # Muestra: ['manzana', 'banana', 'naranja', 'pera']
```

**Error frecuente:**
El error `IndexError: list index out of range`. Ocurre cuando intentas acceder a una posición (índice) que no existe en la lista. 

*¿Cómo evitarlo?* Recuerda que las listas en Python empiezan a contar desde el índice `0`. Si una lista tiene 3 elementos, sus índices son `0`, `1` y `2`. Puedes usar la función `len(tu_lista)` para verificar la cantidad de elementos antes de acceder a un índice.

## Práctica

Crea una lista con tres elementos, agrega un nuevo elemento al final usando `.append()` e imprime cada uno de los elementos de la lista utilizando un bucle `for`.

## Revisión

- Se corrigió la sección "Práctica", reemplazando el ejercicio sobre diccionarios por uno enfocado en el uso y recorrido de listas para mantener la coherencia con el tema de la guía.
