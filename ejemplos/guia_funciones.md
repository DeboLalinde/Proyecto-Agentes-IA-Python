# Guía de estudio: funciones

## Explicación

**¿Qué es y para qué sirve?**

Una **función** en Python es un bloque de código reutilizable que realiza una tarea específica. Se define utilizando la palabra clave `def`.

Sirve para organizar el programa en partes más pequeñas, evitar repetir código (principio DRY: *Don't Repeat Yourself*) y hacer que tus scripts sean más fáciles de entender y mantener.

---

**Ejemplo de código:**

```python
def saludar(nombre):
    return f"¡Hola, {nombre}!"


# Llamamos a la función
mensaje = saludar("Ana")
print(mensaje)
```

---

**Error frecuente y cómo evitarlo:**

* **Olvidar usar `return` (o confundirlo con `print`):** 
  Si dentro de la función usas `print()` en lugar de `return`, la función mostrará el texto en pantalla, pero devolverá el valor especial `None`. Esto provocará errores si intentas guardar el resultado de la función en una variable para usarlo después.

* **Cómo evitarlo:** Si necesitas que tu función le entregue un valor o resultado al resto del programa, asegúrate de terminar la función con la instrucción `return`.

## Práctica

**Ejercicio de práctica: El cuadrado de un número**

Crea una función llamada `calcular_cuadrado` que reciba un número como parámetro y devuelva el resultado de elevar dicho número al cuadrado. Después, llama a la función pasando el número `5` como argumento, guarda el resultado obtenido en una variable e imprímelo en la consola.

---

**Criterios de aceptación:**

1. La función debe llamarse `calcular_cuadrado` y recibir exactamente un parámetro.
2. La función debe utilizar la instrucción `return` para devolver el resultado matemático (no debe usar `print` dentro del cuerpo de la función).
3. Se debe almacenar el resultado de ejecutar `calcular_cuadrado(5)` en una variable y luego mostrar esa variable con `print()`.

---

**Pista:**
Recuerda que para elevar un número al cuadrado en Python puedes usar el operador `**` (por ejemplo, `n ** 2`). Asegúrate de que tu función entregue el valor calculado usando la palabra clave `return`.

## Revisión
No se requirieron cambios importantes.