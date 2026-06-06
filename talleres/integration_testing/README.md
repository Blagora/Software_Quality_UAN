# Taller: Pruebas de Integración – Más allá de los tests unitarios

## 🎯 Objetivo

Comprender la importancia de las pruebas de integración, aplicar enfoques (bottom‑up, top‑down, sandwich, big‑bang) y utilizar stubs y drivers para validar la interacción entre módulos.

## 📦 Estructura del proyecto

- `src/`: código del sistema (módulos con errores de integración).
- `tests/`: pruebas iniciales (débiles, pasan pero no detectan fallos reales).
- `tests_hidden/`: pruebas ocultas (solo para evaluación del profesor).
- `notebooks/`: guías interactivas sobre conceptos clave.
- `data/`: archivo de ejemplo para el almacenamiento.

## 🧪 Parte 1 – Instalación y ejecución inicial

1. Clona o descarga el proyecto.
2. Instala las dependencias:

pip install -r requirements.txt

3. Ejecuta las pruebas existentes:

pytest tests/ -v

4. Observa el resultado: todos los tests pasan.

## 🔍 Parte 2 – Análisis crítico de las pruebas

Responde en un documento:

- ¿Las pruebas actuales verifican realmente que los módulos colaboran correctamente?
- ¿Qué interacciones entre módulos no están siendo validadas?
- ¿Qué fallos típicos de integración (errores de comunicación, excepciones no controladas, estados inconsistentes) podrían pasar desapercibidos?

## ⚠️ Parte 3 – El lado oscuro de las pruebas de integración

1. Abre src/service.py y localiza el método add_task.
2. Modifícalo para que siempre devuelva True sin llamar al almacenamiento ni al notificador.
3. Vuelve a ejecutar los tests de integración:

pytest tests/test_service_integration.py -v

4. Analiza el resultado.

Responde:

- ¿Los tests detectaron el error?
- ¿Por qué siguen pasando?
- ¿Qué debilidad fundamental tienen estas pruebas de integración?

## 🔧 Parte 4 – Aplicación de enfoques de integración

En esta parte utilizarás los notebooks y escribirás pruebas que implementen diferentes estrategias de integración.

### 4.1 Enfoque Top‑Down

- Usa un stub para storage y notifier y prueba la lógica de service.py de forma aislada.
- Escribe los tests en tests/test_service_integration.py (sección TestTopDown).

### 4.2 Enfoque Bottom‑Up

- Escribe un driver que pruebe directamente el módulo storage.py (sin pasar por service).
- Crea el archivo tests/test_storage_driver.py y escribe al menos 3 pruebas que verifiquen operaciones de lectura/escritura en el archivo JSON.

### 4.3 Enfoque Sandwich

- Combina stubs (para notifier) con el módulo real de storage y prueba el flujo completo de agregar una tarea desde service, verificando que el storage se actualiza correctamente.

## 🔧 Parte 5 – Mejora de las pruebas de integración

Refactoriza y amplía las pruebas para que:

- Detecten la modificación maliciosa de la Parte 3.
- Cubran escenarios de error:
  - Fallo en el almacenamiento (simula una excepción en storage.save).
  - Fallo en el notificador (simula que notifier.send lanza excepción).
  - Verifica que el sistema mantiene la consistencia (si falla la notificación, la tarea no debe quedar guardada a medias, o debe manejarse adecuadamente).
- Incluyan casos extremos:
  - Agregar una tarea con título vacío (debe ser rechazada).
  - Agregar tareas duplicadas.
  - Listar tareas cuando el archivo está vacío o no existe.

## 📊 Parte 6 – Reflexión sobre cobertura de integración

Utiliza el notebook notebooks/04_lado_oscuro.ipynb y responde:

- ¿Qué diferencia hay entre cobertura de código y cobertura de integración?
- ¿Por qué un 100% de cobertura unitaria no garantiza que el sistema integrado funcione correctamente?

## 🧠 Parte 7 – Reflexión final

Responde:

- ¿Qué aprendiste sobre las limitaciones de las pruebas unitarias frente a las de integración?
- ¿En qué situaciones usarías un enfoque bottom‑up y en cuáles top‑down?
- ¿Cómo aplicarías stubs y drivers en un proyecto real para desacoplar dependencias externas?

## 📦 Entregable

Sigue las instrucciones detalladas en ENTREGABLE.md.

## ⚠️ Nota importante

Se evaluará:

- La calidad de las pruebas de integración (aserciones, cobertura de escenarios).
- La correcta aplicación de stubs y drivers según el enfoque elegido.
- La capacidad de detectar errores de integración reales.
- La profundidad del análisis crítico en el informe.