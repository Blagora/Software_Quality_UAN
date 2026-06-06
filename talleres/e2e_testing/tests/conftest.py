"""
conftest.py — Fixtures compartidas para el taller E2E.

Este archivo es cargado automáticamente por pytest antes de ejecutar cualquier test.
Define:
  - `live_server`: levanta la app Flask en un hilo de fondo y la detiene al finalizar.
  - `page`: abre un navegador Playwright y navega a la URL base.
  - `base_url`: URL base del servidor de pruebas.
"""

import os
import sys
import threading
import time

import pytest
from playwright.sync_api import sync_playwright

# Aseguramos que src/ esté en el path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.app import app as flask_app
from src.models import TaskRepository

# Puerto dedicado para tests (distinto al de desarrollo)
TEST_PORT = 5099
BASE_URL = f"http://localhost:{TEST_PORT}"
TEST_TASKS_FILE = "data/tasks_test.json"


@pytest.fixture(scope="session")
def live_server():
    """
    Levanta la aplicación Flask en un hilo daemon.
    Scope 'session': se crea una sola vez para toda la suite de tests.
    """
    # Apuntamos a un archivo de tareas exclusivo para tests
    os.environ["TASKS_FILE"] = TEST_TASKS_FILE

    # Importamos set_repo para usar repositorio de tests
    from src.app import set_repo
    set_repo(TaskRepository(filepath=TEST_TASKS_FILE))

    server = threading.Thread(
        target=lambda: flask_app.run(port=TEST_PORT, use_reloader=False, debug=False),
        daemon=True,
    )
    server.start()

    # Esperamos a que el servidor esté listo
    for _ in range(20):
        try:
            import urllib.request
            urllib.request.urlopen(f"{BASE_URL}/health")
            break
        except Exception:
            time.sleep(0.3)

    yield BASE_URL

    # El hilo daemon se cierra automáticamente al terminar la sesión


@pytest.fixture(scope="session")
def browser_context(live_server):
    """Crea un contexto de navegador Playwright compartido en la sesión."""
    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=True)
        context = browser.new_context()
        yield context
        context.close()
        browser.close()


@pytest.fixture
def page(browser_context, live_server):
    """
    Abre una nueva página para cada test.
    Limpia el estado (tareas) antes de cada test para garantizar aislamiento.
    """
    # Limpiar estado antes de cada test
    import urllib.request
    urllib.request.urlopen(
        urllib.request.Request(f"{live_server}/tasks/clear", method="POST")
    )

    page = browser_context.new_page()
    page.goto(live_server)
    yield page
    page.close()
