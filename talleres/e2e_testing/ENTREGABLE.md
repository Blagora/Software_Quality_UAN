# Entregable del Taller de Pruebas E2E

## 📌 Modalidad de trabajo

Este taller se puede realizar de forma **individual** o en **grupos de máximo 3 personas**.

## 📦 Forma de entrega

Deben entregar **un Pull Request (PR)** desde su rama hacia la rama principal del repositorio. Sigan estos pasos:

1. **Clonen** el repositorio base proporcionado por el profesor.
2. **Creen una rama** con el nombre que identifique a los autores, según la modalidad de trabajo:
   - **Individual:** usen el formato `nombre_apellido1_apellido2`.  
     Ejemplo: `andres_julian_bermudez_garcia`.
   - **Grupal (máximo 3 personas):** usen los apellidos de todos los integrantes unidos por guiones bajos, en el orden que prefieran.  
     Ejemplo: `bermudez_perez_gomez`.  
     También pueden anteponer la palabra `grupo` si lo desean: `grupo_bermudez_perez_gomez`.
   ```bash
   git checkout -b nombre-de-la-rama
   ```
3. **Realicen todos los cambios** necesarios (código fuente, nuevas pruebas, informe).
4. **Hagan commit** de sus cambios con un mensaje descriptivo.
5. **Suban su rama** al repositorio remoto:
   ```bash
   git push origin nombre-de-la-rama
   ```
6. **Abran un Pull Request** desde su rama hacia `main` (o la rama que indique el profesor).
   - En la **descripción del Pull Request** deben aparecer los **nombres completos y códigos (o identificaciones)** de todos los integrantes del equipo.

## 📁 Archivos requeridos

### 1. Tests mejorados

- `tests/test_tareas_e2e.py` con:
  - `TestCrearTareaFuerte`: al menos 3 pruebas con aserciones sobre el estado de la UI.
  - `TestCompletarTareaFuerte`: verifica el badge y el tachado del título.
  - `TestEliminarTareaFuerte`: verifica desaparición de la lista.
  - `TestFlujoCompleto`: flujo crear → completar → eliminar en un solo test.
  - `TestCasosExtremos`: título vacío, duplicados, lista vacía.

- `tests/page_objects.py` con la clase `TaskPage` (Page Object Model).

### 2. Informe (PDF o Markdown)

El informe debe responder:

**Parte 2 — Análisis:**
- ¿Las pruebas iniciales verifican algo útil? ¿Por qué?
- ¿Qué interacciones de usuario no estaban cubiertas?

**Parte 3 — Sabotaje:**
- ¿Las pruebas iniciales detectaron la modificación maliciosa?
- ¿Qué debilidad fundamental expone este experimento?

**Parte 7 — Reflexión E2E:**
- Explica con tus palabras qué es un flaky test y da un ejemplo concreto.
- ¿Cómo garantizarías el aislamiento entre tests E2E?
- ¿Cuándo preferirías una prueba de integración sobre una E2E?
- ¿Cómo aplicarías Playwright o Selenium en un proyecto con microservicios?

## ✅ Criterios de evaluación

| Criterio | Peso |
|----------|------|
| Calidad de los locators (preferencia `data-testid`) | 15% |
| Robustez de aserciones (verifican estado, no solo ausencia de errores) | 25% |
| Implementación del Page Object Model | 20% |
| Aislamiento entre tests (sin contaminación de estado) | 20% |
| Profundidad del análisis crítico en el informe | 20% |

## ⚠️ Restricciones

- Las pruebas deben ejecutarse con `pytest tests/ -v` sin modificaciones al `conftest.py`.
- No se permite usar `time.sleep()` para esperas fijas; usa `wait_for_selector` o `expect()`.
- Cada test debe ser independiente: no asumir estado de tests anteriores.
