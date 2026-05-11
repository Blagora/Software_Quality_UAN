import pytest
from unittest.mock import Mock, patch, MagicMock
from requests.exceptions import RequestException
import src.analizador


class TestAnalizarTexto:
    def test_respuesta_exitosa(self, mocker):
        mock_response = Mock()
        mock_response.text = "linea1\nlinea2\nlinea3"
        mock_response.raise_for_status = Mock()
        
        mocker.patch('src.analizador.requests.get', return_value=mock_response)
        
        lineas, caracteres = src.analizador.analizar_texto("http://ejemplo.com/texto.txt")
        
        assert lineas == 3
        assert caracteres == 18

    def test_fallo_seguido_de_exito_retorna_exito(self, mocker):
        mock_response_exitoso = Mock()
        mock_response_exitoso.text = "hola\nmundo"
        mock_response_exitoso.raise_for_status = Mock()
        
        mocker.patch('src.analizador.requests.get', side_effect=[
            RequestException("Error de red"),
            mock_response_exitoso
        ])
        
        lineas, caracteres = src.analizador.analizar_texto("http://ejemplo.com/texto.txt")
        
        assert lineas == 2
        assert caracteres == 9

    def test_fallo_total_lanza_excepcion(self, mocker):
        mocker.patch('src.analizador.requests.get', side_effect=RequestException("Error"))
        
        with pytest.raises(RuntimeError) as exc_info:
            src.analizador.analizar_texto("http://ejemplo.com/texto.txt")
        
        assert "No se pudo acceder a la URL" in str(exc_info.value)

    def test_respuesta_vacia(self, mocker):
        mock_response = Mock()
        mock_response.text = ""
        mock_response.raise_for_status = Mock()
        
        mocker.patch('src.analizador.requests.get', return_value=mock_response)
        
        lineas, caracteres = src.analizador.analizar_texto("http://ejemplo.com/vacio.txt")
        
        assert lineas == 1
        assert caracteres == 0