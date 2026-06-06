"""
Módulo de almacenamiento en archivo JSON.
Contiene errores sutiles que afectan la integración.
"""

import json
import os

class TaskStorage:
    def __init__(self, filepath):
        self.filepath = filepath
        if not os.path.exists(filepath):
            with open(filepath, 'w') as f:
                json.dump([], f)

    def load(self):
        """Carga la lista de tareas. Retorna lista vacía si el archivo no existe."""
        with open(self.filepath, 'r') as f:
            return json.load(f)

    def save(self, tasks):
        """Guarda la lista de tareas en el archivo."""
        # Error de integración: no maneja excepciones de escritura
        with open(self.filepath, 'w') as f:
            json.dump(tasks, f, indent=2)