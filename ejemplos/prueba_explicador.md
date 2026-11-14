# Prueba del agente explicador

## Tema 1: listas

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

## Tema 2: funciones

### ¿Qué es una función y para qué sirve?

Una **función** en Python es un bloque de código con un nombre que realiza una tarea específica. 

Sirve para **reutilizar código** sin tener que escribirlo varias veces, organizar tu programa en partes más pequeñas y hacer que sea más fácil de leer y mantener.

---

### Ejemplo de código

```python
def saludar(nombre):
    return f"¡Hola, {nombre}!"


# Llamamos a la función
mensaje = saludar("Ana")
print(mensaje)
```

---

### Error frecuente y cómo evitarlo

**El error:** Olvidar la instrucción `return` cuando necesitas que la función devuelva un valor. Si no usas `return` (o solo usas `print` dentro de la función), Python devolverá automáticamente `None`.

```python
# Incorrecto (devuelve None)
def sumar(a, b):
    print(a + b)


resultado = sumar(3, 5)  # Muestra 8 en pantalla, pero 'resultado' vale None
```

**Cómo evitarlo:** Si vas a guardar o usar el resultado de una función más adelante, asegúrate de finalizarla devolviendo el dato con `return`.
