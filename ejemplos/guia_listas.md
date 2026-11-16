# Guía de estudio: listas

## Explicación

### ¿Qué es una lista y para qué sirve?

Una **lista** en Python es una estructura de datos que permite almacenar una colección ordenada de elementos (como números, textos u otras listas) en una sola variable. Los elementos de una lista pueden modificarse (son mutables), agregarse o eliminarse. 

Sirve para agrupar datos relacionados y trabajar con ellos fácilmente sin necesidad de crear una variable independiente para cada dato.

### Ejemplo de código

```python
# Creamos una lista de frutas
frutas = ["manzana", "banana", "naranja"]

# Accedemos al primer elemento (índice 0)
print(frutas[0])  # Imprime: manzana

# Agregamos una nueva fruta al final
frutas.append("pera")
print(frutas)  # Imprime: ['manzana', 'banana', 'naranja', 'pera']
```

### Error frecuente y cómo evitarlo

**El error:** Intentar acceder a un índice que no existe, lo que genera el error `IndexError: list index out of range`. 

Esto ocurre comúnmente porque en Python los índices empiezan a contar desde el **0** y no desde el 1. Si una lista tiene 3 elementos, sus índices válidos son `0`, `1` y `2`. Si intentas acceder al índice `3`, fallará.

**Cómo evitarlo:** Recuerda siempre que el último índice de una lista es igual a su tamaño menos 1. Si quieres acceder al último elemento sin contar, puedes usar el índice negativo `-1` (por ejemplo: `frutas[-1]`).

## Práctica

### Ejercicio de práctica: Lista de colores

Crea un programa en Python que gestione una lista de tus colores favoritos. Inicializa la lista con tres colores de tu elección. Luego, imprime el primer color de la lista, agrega un cuarto color utilizando el método `.append()`, y finalmente imprime en pantalla el nuevo último color que agregaste.

---

### Criterios de aceptación

1. La lista se inicializa con exactamente tres elementos de tipo texto (strings).
2. Se utiliza la función `.append()` para incorporar un cuarto color al final de la lista.
3. El programa imprime correctamente en la consola el primer elemento (usando el índice `0`) y el último elemento recién agregado.

---

### Pista

Recuerda que en Python las posiciones de las listas empiezan a contar desde el `0`. Si quieres acceder al último elemento que acabas de agregar sin preocuparte por la cantidad de elementos, ¡puedes usar el índice negativo `-1`!

## Revisión

- Se corrigió una errata tipográfica en el comentario dentro del bloque de código ("Crearmos" por "Creamos").
- Se verificó que las explicaciones, el código de ejemplo y los criterios del ejercicio concuerden adecuadamente entre sí.