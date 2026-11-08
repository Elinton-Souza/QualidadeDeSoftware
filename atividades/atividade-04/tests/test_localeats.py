#Arquivo responsável pelo teste funcional via Playwright
#testando o fluxo "pesquisar um restaurante" diretamente no
#LocalEats.

""" Teste funcional (Playwright) do fluxo de busca do LocalEats. """

import os
from playwright.sync_api import Page, expect

BASE_URL = "https://local-eats-unisenac.vercel.app/"

def login(page: Page) -> None:
    """Faz login no LocalEats usando credenciais vindas de variaveis de ambiente."""
    email = os.environ["LOCALEATS_EMAIL"]
    senha = os.environ["LOCALEATS_PASSWORD"]

    page.goto(BASE_URL)
    page.get_by_placeholder("teste@teste.com").fill(email)
    page.get_by_placeholder("Sua senha secreta").fill(senha)
    page.get_by_placeholder("Sua senha secreta").press("Enter")
    page.wait_for_selector("#searchInput")
    page.wait_for_selector("#restaurantGrid .rest-card")


# Responsavel: Elinton
def test_busca_por_termo_inexistente_nao_retorna_restaurantes(page: Page) -> None:
    # Arrange
    login(page)
    termo_inexistente = "termoinexistentezzz999"

    # Act
    page.locator("#searchInput").fill(termo_inexistente)
    page.locator("#searchBtn").click()

    # Assert
    expect(page.locator("#restaurantGrid")).to_contain_text("Nenhum restaurante encontrado.")
    expect(page.locator("#restaurantGrid .rest-card")).to_have_count(0)
