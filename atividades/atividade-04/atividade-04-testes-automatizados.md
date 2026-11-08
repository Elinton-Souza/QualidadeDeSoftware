# Atividade 4: Testes Automatizados do LocalEats

## 1. Identificação

- **Nome:** Elinton Souza
- **Curso:** Análise e Desenvolvimento de Sistemas (ADS), 4º semestre
- **Disciplina:** Qualidade de Software
- **Data:** 07/11/2026
- **Repositório:** https://github.com/Elinton-Souza/QualidadeDeSoftware (pasta `atividades/atividade-04`)

## 2. Integrantes e responsabilidades

Trabalho individual.

| Integrante | Responsabilidades |
|---|---|
| Elinton Souza | TU01 (teste unitário 1), TU02 (teste unitário 2), TF01 (teste funcional 1) |

## 3. Testes unitários

**Regra de negócio escolhida:** Regra 1, `pedido_atingiu_valor_minimo` (verifica se um pedido atingiu o valor mínimo de R$ 30,00 para entrega).

| Teste | Entrada | Resultado esperado | Responsável |
|---|---|---|---|
| `test_pedido_atinge_valor_minimo` | valor_do_pedido = 50 | Retorna `True` | Elinton |
| `test_pedido_valor_negativo_gera_valueerror` | valor_do_pedido = -10 | Lança `ValueError` | Elinton |
| `test_pedido_com_valor_exatamente_no_minimo` | valor_do_pedido = 30 (caso de borda) | Retorna `True` | Elinton |

## 4. Aplicação do TDD

Segui o ciclo **Red-Green-Refactor** para os dois testes unitários:

1. **Red:** escrevi o teste `test_pedido_atinge_valor_minimo` antes de criar a função `pedido_atingiu_valor_minimo`. Ao rodar, obtive `ModuleNotFoundError`, confirmando que o teste realmente dependia do código ainda não escrito.
2. **Green:** criei a função em `src/regras_localeats.py` com a lógica mínima (`return valor_do_pedido >= 30`), e o teste passou.
3. **Red novamente:** escrevi o segundo teste (`test_pedido_valor_negativo_gera_valueerror`), usando `pytest.raises(ValueError)`. Ele falhou com `Failed: DID NOT RAISE ValueError`, já que a função ainda não validava valores negativos.
4. **Green novamente:** adicionei a validação (`if valor_do_pedido < 0: raise ValueError(...)`) antes da lógica principal, e os dois testes passaram.
5. **Teste de caso de borda:** acrescentei um terceiro teste (`test_pedido_com_valor_exatamente_no_minimo`), com `valor_do_pedido = 30` (exatamente o limite da regra). Esse teste passou direto, sem fase Red, já que o código já tratava esse caso corretamente (`>= 30`). Mesmo assim, é um teste valioso: ele protege esse comportamento contra uma futura alteração acidental (por exemplo, trocar `>=` por `>`).

## 5. Testes funcionais com Playwright

**Fluxo escolhido:** Pesquisar um restaurante (busca por um termo inexistente, confirmando a mensagem "Nenhum restaurante encontrado.").

Durante a construção do teste, encontrei três problemas reais ao rodar contra o site de verdade:

1. **Ambiguidade de locator:** o seletor `get_by_role("button", name="Entrar")` encontrava 2 elementos (o botão de alternar aba de login e o botão de submit do formulário). Corrigido restringindo a busca ao formulário: `page.locator("#loginForm").get_by_role(...)`.
2. **Condição de corrida:** a busca disparava antes da lista inicial de restaurantes terminar de carregar, fazendo o teste ver a lista completa em vez da mensagem de "nenhum resultado". Corrigido adicionando `page.wait_for_selector("#restaurantGrid .rest-card")` logo após o login, antes de buscar.
3. **Timeout/instabilidade ao clicar no botão de login:** mesmo escopado ao formulário, o clique no botão "Entrar" por vezes não era reconhecido como uma ação completa pelo Playwright (timeout de 30s, ou até `TargetClosedError`), apesar do login acontecer visualmente. Resolvido trocando o clique no botão por `page.get_by_placeholder("Sua senha secreta").press("Enter")`, uma forma mais robusta e estável de submeter o formulário de login.

## 6. Resultado da execução

- **Data:** 07/11/2026
- **Total de testes:** 4
- **Aprovados:** 4
- **Reprovados:** 0

Todos os testes foram aprovados. Resultado completo salvo em `relatorio-pytest.txt`.

## 7. Explicações individuais

Segui o ciclo Red-Green-Refactor nos testes unitários.
Primeiro escrevi o teste, sem nenhum código por trás (fase Red), e rodei o pytest pra confirmar a falha. Isso prova que o teste testa algo real, não é decorativo. Só depois escrevi o código mínimo pra passar (fase Green). Repeti o ciclo duas vezes: uma pra regra principal (`valor >= 30`) e outra pra validação de valor negativo (`ValueError`). Não fiz uma etapa de Refactor separada porque o código já saiu simples nas duas vezes. Essa etapa existiria pra melhorar a organização do código sem mudar o comportamento, sempre com os testes como garantia.

A estrutura AAA (Arrange-Act-Assert) organiza todos os testes, unitários e funcional, em três partes: preparo o cenário (Arrange: definir o valor do pedido, ou fazer login no site), executo a ação (Act: chamar a função, ou clicar em buscar) e verifico o resultado (Assert). Isso deixa cada teste fácil de ler, porque segue sempre a mesma lógica, mesmo quando o que está sendo testado muda.

Testes de caixa-branca e caixa-preta são diferentes na prática. Os testes unitários (`test_regras_localeats.py`) são caixa-branca: testam uma função do meu código por dentro, isolada, sem depender de nada externo. Sei exatamente o que a função faz e testo sua lógica interna. O teste funcional (`test_localeats.py`) é caixa-preta: testa o LocalEats por fora, como um usuário real: abre o navegador, preenche campos, clica em botões. Não importa como o código do site foi escrito, só o comportamento final visível pra quem usa. Essa diferença ficou clara nos bugs do teste funcional: ambiguidade do botão, condição de corrida, timeout no clique. Nenhum teste unitário pegaria esses erros. Não têm acesso à interface real da aplicação.



## 8. Uso de inteligência artificial

Utilizei o Claude como mentor ao longo de toda a atividade, mas escrevi todo o código eu mesmo, linha por linha, no VS Code. A IA explicava cada conceito e cada passo antes de eu digitar, e eu tirei prints de cada etapa do processo (ciclos de TDD, erros reais encontrados e suas correções) para registrar meu próprio processo de aprendizado e poder revisar depois.

Todos os prints estão na pasta [`evidencias/`](./evidencias/), organizados em ordem cronológica:

- `evidencia-00-estrutura-final-projeto.png`: estrutura final do projeto.
- `evidencia-01-tdd-teste1-red.png` e `evidencia-02-tdd-teste1-green.png`: ciclo Red-Green do primeiro teste unitário.
- `evidencia-03-tdd-teste2-red.png` e `evidencia-04-tdd-teste2-green.png`: ciclo Red-Green do segundo teste unitário.
- `evidencia-05-funcional-red-ambiguidade.png` e `evidencia-05b-funcional-red-ambiguidade-codigo.png`: primeiro bug real do teste funcional (botão ambíguo).
- `evidencia-06-funcional-red-race-condition.png`: segundo bug real (condição de corrida).
- `evidencia-07-funcional-green-confirmado-visual.png` e `evidencia-07b-funcional-green-codigo-final.png`: confirmação visual do login funcionando e código final.
- `evidencia-08-relatorio-pytest-gerado.png`: geração do relatório oficial de testes.
- `evidencia-09-tdd-teste3-borda.png`: terceiro teste unitário (caso de borda), passando direto (4 passed).

**Sugestões que precisaram ser corrigidas após execução real:**
- A primeira sugestão de locator para o botão de login (`get_by_role("button", name="Entrar")` sem escopo) causou um erro de ambiguidade real no site, só percebido ao rodar o teste de verdade.
- A primeira versão do teste funcional não previa a condição de corrida entre o carregamento inicial da lista de restaurantes e a busca. Esse problema só apareceu na execução real, e foi corrigido com uma espera explícita.
- A abordagem de clicar no botão de login (mesmo corrigida a ambiguidade) ainda apresentava timeout/instabilidade; a solução foi trocar para o envio do formulário via tecla Enter, uma técnica mais robusta.

Esses três casos mostram que os testes automatizados pegaram problemas reais de interação com a aplicação. Nenhum deles seria percebido sem rodar o teste de verdade contra o site.

## 9. Diferenciais opcionais

Marque somente os diferenciais realmente implementados e inclua ao lado os respectivos links.

- [x] Terceiro teste unitário para caso de borda. ([`tests/test_regras_localeats.py`](./tests/test_regras_localeats.py))
- [x] Uso de `pytest.raises` para verificar exceção. ([`tests/test_regras_localeats.py`](./tests/test_regras_localeats.py))
- [ ] Parametrização com `pytest.mark.parametrize`.
- [ ] Cenário BDD em Gherkin.
- [ ] Automação com `pytest-bdd`.
- [ ] Organização com Page Object Model.
- [ ] Segundo teste funcional pelo mesmo integrante.
- [ ] Execução em mais de um navegador.
- [ ] Screenshot, vídeo ou trace do Playwright.
- [x] Registro de uma falha encontrada e corrigida. ([`evidencias/`](./evidencias/) e Seção 8)

### Descrição dos diferenciais

- **Terceiro teste unitário para caso de borda:** `test_pedido_com_valor_exatamente_no_minimo`, em `tests/test_regras_localeats.py`, testa o valor exatamente no limite da regra (R$ 30,00), garantindo que a comparação `>=` está correta.
- **Uso de `pytest.raises` para verificar exceção:** implementado no teste `test_pedido_valor_negativo_gera_valueerror`, em `tests/test_regras_localeats.py`, que verifica se a função `pedido_atingiu_valor_minimo` lança `ValueError` para valores negativos.
- **Registro de uma falha encontrada e corrigida:** documentado na Seção 8 (Uso de inteligência artificial) e na pasta [`evidencias/`](./evidencias/). Três problemas reais foram encontrados ao rodar o teste funcional contra o site de verdade (ambiguidade de locator, condição de corrida, e instabilidade no clique do botão de login), todos com prints de antes (Red) e depois (Green) de cada correção.
