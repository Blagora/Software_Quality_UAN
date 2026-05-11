# Respuestas al Taller: Pruebas Unitarias – Más allá del verde

## Parte 2 – Análisis crítico de las pruebas

### ¿Las pruebas actuales garantizan que el código es correcto?
Creo que **no**. Las pruebas que vi solo revisan cosas muy básicas:
1. Si el resultado es un número con decimales (float)
2. Si pongo una lista vacía que devuelva None
3. Si no truena con una lista de un solo número

Pero nunca preguntaron "este promedio está bien?" Por ejemplo, si yo pongo [1,2,3] el promedio debería ser 2

### ¿Qué aspectos del comportamiento NO están siendo validados?
- **El cálculo del promedio:** No revisan si el número que sale es el correcto matemáticamente
- **Números negativos:** Nunca probamos qué pasa con números negativos como [-2, -4]
- **Más casos:** Solo probamos listas pequeñitas, no muchos números diferentes

### ¿Qué tipo de errores podrían pasar desapercibidos?
- Si alguien pone que siempre devuelva 3.14, los tests lo aprobarían
- Errores en la suma o división del promedio
- Problemas con números negativos o cero
- Cálculos que no sean exactos

---

## Parte 3 – El lado oscuro de las pruebas

### Experimento: `calcular_promedio` modificado para retornar siempre 3.14

**Lo que pasó:**
- El test del tipo "float" **pasó** (3.14 es un float, así que está bien)
- El test de lista vacía **falló** (3.14 no es None)
- El test de "que no falle" **pasó** (no se daña, así que está bien)

¡Me parece increíble que casi nadie detectara el error!

### ¿Las pruebas detectaron el error?
**Solo uno.** El de la lista vacía lo detectó. Pero cuando probé con [1,2,3] que debería dar 2, el test pasó igual porque nunca revisó el número exacto.

### ¿Por qué siguen pasando?
Porque los tests son muy bàsicos en sus revisiones:
1. Solo ven que es un float, no si es el float correcto
2. Solo ven que no se rompe, no si calcula bien

### ¿Qué debilidad tienen estos tests?
- Las verificaciones son muy débiles, como revisar solo que algo existe pero no que esté bien
- No preguntan si el algoritmo hace lo que debe
- No tienen muchos casos para probar diferentes situaciones

---

## Parte 4 – Mejora de pruebas

Yo agregué más tests para que sean más fuertes:

| Caso              | Lo que revisa                   |
|-------------------|---------------------------------|
| Lista vacía       | Que no se rompa y devuelva None |
| Un solo número    | Que el promedio de [5] sea 5.0  |
| Muchos números    | Que [1,2,3,4,5] de 3.0          |
| Números negativos | Que [-2,-4] de -3.0             |
| El valor exacto   | Que el cálculo esté correcto    |

---

## Parte 5 – Pruebas con mocks

La verdad es que me costó entender los mocks al principio. Me imaginé que para probar `analizar_texto` había que conectarse a internet

Pero con los mocks puedo simular todo sin salir a internet:

1. **Éxito:** Simulo que la página responde bien con texto
2. **Error y luego éxito:** Simulo que falla una vez y luego funciona (como cuando el wifi se corta y vuelve)
3. **Error total:** Simulo que siempre falla y devuelve un error
4. **Vacío:** Simulo una página sin texto

No hice ni una sola llamada real a internet, todo fue simulado.

---

## Parte 6 – Reflexión sobre cobertura

### ¿Qué diferencia hay entre cobertura y calidad de pruebas?
- **Cobertura:** Es como ver qué líneas del código "miré" cuando hago los tests
- **Calidad:** Es si esos tests de verdad detectarían errores

Un 100% de cobertura con tests malos es como tener un termo lleno de agua... pero es agua de lluvia sucia. Sí sirve, pero no es lo que necesitas.

### ¿Por qué 100% coverage no garantiza corrección?
Imagínense una función que divide números. Si el test solo revisa que devuelva un número, un test pasa aunque la función siempre devuelva 0

---

## Parte 7 – Reflexión final

### ¿Qué aprendiste sobre las limitaciones de las pruebas unitarias?
Que las pruebas pueden pasar y el código estar mal. Un test que pasa solo dice "este test pasó", no "mi programa está bien". Hay que aprender a hacer tests que digan "si hay un error, yo te lo detecto".

### ¿Qué significa realmente que "los tests pasen"?
Significa que el código hizo lo que el test le pidió. Pero si el test le pidió algo fácil (como "solo no te rompas"), un código malo también lo pasa.

### ¿Cómo evitarías falsas confianzas en un proyecto real?
1. Que los tests revisen valores exactos, no solo tipos
2. Usar herramientas como hypothesis para probar muchos casos
3. Revisar cada test y preguntarme si esto detectaría un error
4. Cuando encuentre un bug, escribir un test que lo detecte
5. No creerse "todo bien" solo porque los tests pasan