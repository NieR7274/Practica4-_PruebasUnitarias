
import pytest

from estacionamiento import Estacionamiento


@pytest.fixture
def sistema():
    """Preparación reutilizable para las pruebas."""
    return Estacionamiento()

# TODO:
# 1. Agregue casos normales.

def test_caso_Boleto_Perdido(sistema):
    # Arrage
    minutos = 1
    perdido = True

    #Act
    resultado = sistema.calcular_total(minutos, "normal", perdido)

    # Assert
    assert resultado == 300.00

def test_caso_Cero_Minutos(sistema):

    # Arrege
    minutos = 0

    # Act
    resultado = sistema.calcular_total(minutos, "normal", False)

    # Assert
    assert resultado == 0.00

# 2. Agregue casos frontera.

def test_caso_Frontera_16_Minutos(sistema):
    # Arrege
    minutos = 16

    # Act
    resultado = sistema.calcular_total(minutos, "normal", False)

    # Assert
    assert resultado == 20.00

    
# 3. Agregue entradas inválidas con pytest.raises.

def test_excepcion_Entrada_decimal(sistema):

    # Arrange
    minutos = 1.1

    # Act & Assert
    with pytest.raises(ValueError):
        sistema.calcular_total(minutos, "normal", False)

def test_excepcion_Entrada_negativa(sistema):

    # Arrange
    minutos = -1

    # Act & Assert
    with pytest.raises(ValueError):
        sistema.calcular_total(minutos, "normal", False)

def test_excepcion_Entrada_Nombre_Invalido(sistema):

    # Arrange
    minutos =  1

    # Act & Assert
    with pytest.raises(ValueError):
        sistema.calcular_total(minutos, "anormal", False)

# 4. Agregue casos parametrizados con @pytest.mark.parametrize.

# Casos intervalo gratuito
@pytest.mark.parametrize("minutos, esperado", [
    (1, 0.00),    # R1: frontera de $0.00
    (5, 0.00),    # R2: caso normal
    (10, 0.00),   # R3: caso normal
    (15, 0.00),   # R4: frontera de $0.00

])
def test_casos_frontera_minutos(sistema, minutos, esperado):
    # Act
    resultado = sistema.calcular_total(minutos, tipo_cliente="normal", boleto_perdido=False)

    # Assert
    assert resultado == esperado

# 5. Use pytest.approx cuando el resultado esperado tenga decimales.
# 6. Pruebe interacciones entre reglas.

def test_Boleto_Perdido_Descuento(sistema):

    # Arrange
    minutos = 1
    perdido = True

    # Act
    resultado = sistema.calcular_total(minutos, "frecuente", perdido)

    # Assert
    assert resultado == 300.00