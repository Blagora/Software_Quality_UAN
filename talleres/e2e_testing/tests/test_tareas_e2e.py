"""
test_tareas_e2e.py — Pruebas E2E iniciales (versión débil).

⚠️ ESTAS PRUEBAS SON INTENCIONALMENTE DÉBILES.
   Pasan aunque el sistema tenga errores graves.
   El estudiante deberá identificar sus limitaciones y mejorarlas.

Ejecutar:
    pytest tests/test_tareas_e2e.py -v
"""

import pytest


class TestPaginaPrincipal:
    """Pruebas débiles de la página principal."""

    def test_pagina_carga(self, page):
        """Verifica que la página responde (solo código HTTP 200)."""
        # Esta prueba pasa aunque la página esté completamente rota
        # siempre que no lance un error 500
        assert page.url is not None

    def test_titulo_visible(self, page):
        """Verifica que el título de la página existe."""
        # Aserción débil: solo verifica que el elemento existe, no su contenido
        title = page.locator("[data-testid='page-title']")
        assert title.count() >= 0  # Siempre pasa, incluso si no existe


class TestCrearTarea:
    """Pruebas débiles de creación de tareas."""

    def test_formulario_presente(self, page):
        """Verifica que el formulario existe en la página."""
        form = page.locator("[data-testid='form-nueva-tarea']")
        # Aserción débil: no verifica que el formulario funcione
        assert form.count() >= 0

    def test_agregar_tarea_no_lanza_error(self, page):
        """Verifica que agregar una tarea no lanza excepción de red."""
        page.fill("[data-testid='input-titulo']", "Mi tarea")
        page.click("[data-testid='btn-agregar']")
        # No verifica que la tarea realmente aparezca en la lista


class TestCompletarTarea:
    """Pruebas débiles de completar tareas."""

    def test_completar_tarea_no_lanza_error(self, page):
        """Verifica que el flujo completar no lanza error de red."""
        # Primero creamos una tarea
        page.fill("[data-testid='input-titulo']", "Tarea a completar")
        page.click("[data-testid='btn-agregar']")
        page.wait_for_load_state("networkidle")

        # Intentamos completarla (sin verificar el resultado)
        btn = page.locator("[data-testid='btn-completar']").first
        if btn.count() > 0:
            btn.click()
            page.wait_for_load_state("networkidle")
        # No verifica que la tarea quede marcada como completada
