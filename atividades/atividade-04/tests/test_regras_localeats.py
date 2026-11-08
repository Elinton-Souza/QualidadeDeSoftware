#Arquivo responsável pela parte mais importante (Red-Freen-Refactor) para a Regra 1 "pedido_atingiu_valor_minimo"
# TDD - deve-se escreve o teste primeiro, antes do código que ele teste

import pytest
from src.regras_localeats import pedido_atingiu_valor_minimo

# Primeiro teste
def test_pedido_atinge_valor_minimo():
  # Arrange
  valor_do_pedido = 50
  
  #Act
  resultado = pedido_atingiu_valor_minimo(valor_do_pedido)
  
  #Assert
  assert resultado == True
  
  
  
# Segundo teste
def test_pedido_valor_negativo_gera_valueerror():
  # Arrange
  valor_do_pedido = -10
  
  #Act/#Assert
  with pytest.raises(ValueError):
    pedido_atingiu_valor_minimo(valor_do_pedido)




# Terceiro teste (caso de borda)
def test_pedido_com_valor_exatamente_no_minimo():
    # Arrange
    valor_do_pedido = 30

    # Act
    resultado = pedido_atingiu_valor_minimo(valor_do_pedido)

    # Assert
    assert resultado == True