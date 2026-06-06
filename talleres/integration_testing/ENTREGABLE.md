# Taller: Pruebas de Integración – Más allá de los tests unitarios

## 🎯 Objetivo

Este taller tiene como propósito comprender la importancia de las pruebas de integración, aplicar los enfoques bottom‑up, top‑down, sandwich y big‑bang, y utilizar stubs y drivers para validar la colaboración entre módulos. Se busca desarrollar criterio para diseñar pruebas de integración robustas, que vayan más allá de simplemente obtener resultados "en verde".

## 📌 Modalidad de trabajo

Este taller se puede realizar de forma **individual** o en **grupos de máximo 3 personas**.

---

## 🧪 Parte 1 – Exploración inicial

1. Clona el repositorio base del taller (el enlace lo proporciona el profesor).
2. Instala las dependencias:

```bash
pip install -r requirements.txt
```

3. Ejecuta las pruebas existentes:

```bash
pytest tests/ -v
```

4. Observa el resultado general: todos los tests pasan.

---

## 🔍 Parte 2 – Análisis crítico de las pruebas

Responde en tu informe:

- ¿Las pruebas actuales verifican realmente que los módulos colaboran correctamente?
- ¿Qué interacciones entre módulos **no** están siendo validadas?
- ¿Qué fallos típicos de integración (errores de comunicación, excepciones no controladas, estados inconsistentes) podrían pasar desapercibidos?

---

## ⚠️ Parte 3 – El lado oscuro de las pruebas de integración

1. Abre `src/service.py` y localiza el método `add_task`.
2. Modifícalo para que **siempre** devuelva `True` sin llamar al almacenamiento ni al notificador.
3. Vuelve a ejecutar SOLO los tests de integración:

```bash
pytest tests/test_service_integration.py -v
```

4. Analiza el resultado.

Responde:

- ¿Las pruebas detectaron el error?
- ¿Por qué siguen pasando?
- ¿Qué debilidad fundamental tienen estas pruebas de integración?

---

## 🔧 Parte 4 – Aplicación de los enfoques de integración

Deberás escribir pruebas que implementen las siguientes estrategias. Apóyate en los notebooks para comprender los conceptos y ver ejemplos.

### 4.1 Enfoque Top‑Down

- Crea **stubs** para `Storage` y `Notifier`.
- Escribe pruebas en `tests/test_service_integration.py` (clase `TestTopDown`) que validen la lógica de `Service` de forma aislada.
- Asegúrate de verificar que las llamadas a los stubs ocurren con los parámetros correctos.

### 4.2 Enfoque Bottom‑Up

- Escribe un **driver** para probar directamente el módulo `Storage` sin depender de `Service`.
- Crea el archivo `tests/test_storage_driver.py` (si no existe) y añade al menos **4 pruebas** que cubran:
  - Archivo no existe (debe crearse con lista vacía).
  - Guardar y recuperar una tarea.
  - Guardar y recuperar múltiples tareas.
  - Intento de guardar un título vacío (define tú la política: ¿debe lanzar error o permitirlo?).
- No uses `Service` en estos tests; solo `TaskStorage`.

### 4.3 Enfoque Sandwich

- Combina un **stub** de `Notifier` con el `Storage` real.
- Escribe al menos **2 pruebas** (en `test_service_integration.py` o en un archivo nuevo) que verifiquen que `Service` persiste correctamente en `Storage` y que el notificador recibe la llamada adecuada.
- Asegúrate de que estas pruebas no dependan de la red ni envíen correos reales.

---

## 🔧 Parte 5 – Mejora de las pruebas de integración

Refactoriza y amplía las pruebas para que:

- Detecten la modificación maliciosa de la Parte 3 (es decir, que fallen si `add_task` no usa los módulos reales).
- Cubran escenarios de error, por ejemplo:
  - Fallo en el almacenamiento (simula una excepción en `storage.save` usando un stub que lance `IOError`).
  - Fallo en el notificador (simula que `notifier.send` lanza `ConnectionError`).
  - **Consistencia:** si el notificador falla, ¿la tarea queda guardada igual? Decide si eso es correcto o debe revertirse, y escribe pruebas que validen el comportamiento esperado.
- Incluyan casos extremos:
  - Agregar una tarea con título vacío (rechazarla o aceptarla, pero de forma explícita).
  - Agregar tareas duplicadas (debe retornar `False` y no duplicar).
  - Listar tareas cuando el archivo JSON está vacío o no existe.

---

## 📊 Parte 6 – Reflexión sobre cobertura de integración

Utiliza el notebook `04_lado_oscuro.ipynb` como guía y responde:

- ¿Qué diferencia hay entre cobertura de código (líneas ejecutadas) y cobertura de integración?
- ¿Por qué un 100% de cobertura unitaria no garantiza que el sistema integrado funcione correctamente?
- ¿Qué métricas o señales te indicarían que unas pruebas de integración son insuficientes?

---

## 🧠 Parte 7 – Reflexión final

Responde:

- ¿Qué aprendiste sobre las limitaciones de las pruebas unitarias frente a las de integración?
- ¿En qué situaciones reales usarías un enfoque bottom‑up y en cuáles top‑down? Justifica con base en la arquitectura del sistema.
- ¿Cómo aplicarías stubs y drivers en un proyecto con microservicios o con bases de datos externas?

---

## 📦 Entregable

Debes entregar **un Pull Request (PR)** desde tu rama hacia la rama principal del repositorio. Sigue estos pasos:

1. **Clona** el repositorio base proporcionado por el profesor.
2. **Crea una rama** con el nombre que identifique a los autores, según la modalidad de trabajo:
   - **Individual:** usa el formato `nombre_apellido1_apellido2`.  
     Ejemplo: `andres_julian_bermudez_garcia`.
   - **Grupal (máximo 3 personas):** usa los apellidos de todos los integrantes unidos por guiones bajos, en el orden que prefieran.  
     Ejemplo: `bermudez_perez_gomez`.  
     También pueden anteponer la palabra `grupo` si lo desean: `grupo_bermudez_perez_gomez`.
   ```bash
   git checkout -b nombre-de-la-rama
   ```
3. **Realiza todos los cambios** necesarios (código fuente corregido, nuevas pruebas, informe).
4. **Haz commit** de tus cambios con un mensaje descriptivo.
5. **Sube tu rama** al repositorio remoto:
   ```bash
   git push origin nombre-de-la-rama
   ```
6. **Abre un Pull Request** desde tu rama hacia `main` (o la rama que indique el profesor).
   - En la **descripción del Pull Request** deben aparecer los **nombres completos y códigos (o identificaciones)** de todos los integrantes del equipo.

### Contenido del PR

La rama debe incluir:

1. **Código fuente corregido** en `src/` (si encontraste errores de integración y los solucionaste).
2. **Tests mejorados** en `tests/`:
   - `test_service_integration.py` con pruebas top‑down y sandwich.
   - `test_storage_driver.py` con pruebas bottom‑up (mínimo 4).
3. **Informe** en formato PDF o Markdown (`informe.md` o `informe.pdf`) que contenga:
   - Respuestas a las preguntas de las Partes 2, 3, 6 y 7.
   - Explicación de los enfoques de integración que aplicaste.
   - Justificación de las decisiones de diseño de pruebas.
   - (Opcional) Capturas de pantalla de la ejecución de los tests antes y después de tus mejoras.
4. **Opcional** (suma puntos extra):
   - Un diagrama sencillo (puede ser ASCII) de la arquitectura y cómo integraste los módulos.
   - Pruebas adicionales basadas en *error guessing* que se te hayan ocurrido.

**No incluyas** la carpeta `tests_hidden/` ni modifiques los tests ocultos; esos son solo para evaluación del profesor.

---

## ⚠️ Nota importante (criterios de evaluación)

Se evaluará:

- **Detección de errores reales (30%):** tus pruebas deben fallar con la versión rota (Parte 3) y pasar con la versión corregida.
- **Uso correcto de stubs y drivers según el enfoque (25%):** top‑down con stubs, bottom‑up con drivers, sandwich combinado.
- **Cobertura de escenarios de error y casos extremos (20%):** títulos vacíos, duplicados, fallos simulados, consistencia.
- **Calidad del análisis escrito (15%):** profundidad, claridad, justificaciones.
- **Organización del PR y del código (10%):** rama con nombre correcto, commits limpios, estructura de archivos clara.

**¡No basta con que los tests pasen!** Deben demostrar que entiendes por qué pasan y que has validado las interacciones reales entre módulos.
