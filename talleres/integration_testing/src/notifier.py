"""
Módulo de notificaciones (simula envío de correo).
No debe llamarse realmente en los tests.
"""

class Notifier:
    def send(self, message):
        """
        Envía una notificación.
        En producción usaría SMTP; aquí simulamos una petición.
        Puede lanzar excepción.
        """
        # Simula que a veces falla (para pruebas de integración)
        import random
        if random.random() < 0.1:  # 10% de fallo aleatorio
            raise ConnectionError("No se pudo enviar la notificación")
        print(f"Notificación enviada: {message}")