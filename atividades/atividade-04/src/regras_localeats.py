""" Regras de Negócio do LocalEats. """

def pedido_atingiu_valor_minimo(valor_do_pedido: float) -> bool:
  """ Verifica se o pedido atingiu o valor mínimo para entrega.
  
  Regra:
  - pedidos de R$ 30,00 ou mais retornam True.
  - pedidos abaixo de R$ 30,00 retornam False.
  - valores negativos geram ValueError.
  """
  
  if valor_do_pedido < 0:
    raise ValueError("O valor do pedido não pode ser negativo.")
  
  return valor_do_pedido >= 30