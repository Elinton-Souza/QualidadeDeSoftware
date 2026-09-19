# Atividade 3: Estratégia e Projeto de Testes do LocalEats

## 1. Identificação

**Turma:** QS_Noite  
**Equipe:** Individual  
**Data:** 22/09/2026

### Integrantes

| Nome | Usuário no GitHub |
|---|---|
| Elinton | @Elinton-Souza |

**Elemento de Competência:** Planejar e projetar testes selecionando técnicas adequadas.

**Aplicação:** <https://local-eats-unisenac.vercel.app/>

---

## 2. Tarefa 1: Planejamento dos testes

### 2.1 Objetivo dos testes

Verificar se a funcionalidade de busca de restaurantes do LocalEats retorna corretamente os resultados esperados para diferentes tipos de entrada (categoria existente e nome exato), já que essa funcionalidade apresentou falhas durante a exploração realizada na Atividade 1.

### 2.2 Escopo

#### Funcionalidades incluídas

| Integrante | Funcionalidade incluída | O que será verificado |
|---|---|---|
| Elinton | Pesquisar restaurantes por especialidade ou localização | Se a busca retorna corretamente os restaurantes correspondentes ao termo digitado, seja uma categoria ou um nome exato |

#### Funcionalidade não incluída

| Funcionalidade não incluída | Justificativa |
|---|---|
| Fazer pedido | Não foi explorada nas atividades anteriores e não há evidências prévias sobre seu comportamento; testá-la exigiria levantar um novo conjunto de cenários que não cabe no tempo disponível para esta atividade individual |

### 2.3 Abordagem

| Item | Decisão da equipe | Justificativa |
|---|---|---|
| Níveis de teste | Teste de sistema | A busca foi avaliada como uma funcionalidade completa, através da interface, sem acesso ao código-fonte |
| Tipos de teste | Teste funcional | O objetivo é verificar se a busca retorna os resultados corretos, não desempenho ou segurança |
| Perspectiva caixa-preta ou caixa-branca | Caixa-preta | Não há acesso ao código da busca; os testes se baseiam apenas nas entradas e saídas observadas pela interface |
| Técnicas de teste | Particionamento de equivalência | As entradas da busca (categoria válida, nome exato válido, termo inexistente) podem ser agrupadas em classes que deveriam ter o mesmo comportamento |

### 2.4 Ambiente e responsabilidades

| Item | Definição |
|---|---|
| Ambiente necessário | Navegador (Chrome), acesso à aplicação LocalEats publicada em produção, conta de usuário já cadastrada |
| Responsáveis pelo planejamento | Elinton |
| Responsáveis pela especificação dos casos | Elinton |
| Responsáveis pela futura execução | Elinton |

### 2.5 Critérios

| Critério | Definição da equipe |
|---|---|
| Entrada | A aplicação estar acessível e existir ao menos um restaurante cadastrado em cada categoria mostrada nos filtros |
| Saída | Os três casos de teste planejados terem sido executados e seus resultados registrados |
| Suspensão | Se a aplicação ficar indisponível ou apresentar um erro que impeça a navegação até a tela de busca |

---

## 3. Tarefa 2: Riscos e técnicas de teste

### 3.1 Análise dos riscos

| ID | Integrante | Funcionalidade | Risco | Consequência | Probabilidade | Impacto | Prioridade | Justificativa |
|---|---|---|---|:---:|:---:|:---:|:---:|---|
| R01 | Elinton | Pesquisar restaurantes | A busca por uma categoria existente não retorna os restaurantes correspondentes | O usuário acredita que não há restaurantes daquela categoria e desiste de usar o aplicativo | Alta | Alto | Alta | Comportamento já evidenciado na Atividade 1 (busca por "Italiana" retornou nenhum resultado, mesmo a categoria existindo) |
| R02 | Elinton | Pesquisar restaurantes | A busca por um nome exato de restaurante existente não retorna esse restaurante | O usuário não encontra um restaurante que já conhece, mesmo ele estando disponível na tela inicial | Alta | Médio | Alta | Mesmo comportamento evidenciado na Atividade 1 (busca por "Restaurante Sabor 0" não retornou resultado) |

### 3.2 Aplicação das técnicas

#### Análise do integrante 1

**Integrante:** Elinton  
**Funcionalidade:** Pesquisar restaurantes por especialidade ou localização  
**Risco relacionado:** R01 e R02  
**Técnica escolhida:** Particionamento de equivalência

**Por que a técnica foi escolhida:**  
A busca recebe um texto como entrada e pode ser dividida em classes que deveriam se comportar de forma parecida (categoria válida, nome exato válido, termo sem correspondência). O particionamento de equivalência permite organizar essas classes e escolher um representante de cada uma para testar, em vez de testar todos os restaurantes e categorias possíveis um por um.

**Aplicação da técnica:**

| Classe de equivalência | Exemplo de entrada | Resultado esperado |
|---|---|---|
| Categoria existente | "Italiana" | Retornar os restaurantes cadastrados nessa categoria |
| Nome exato de restaurante existente | "Restaurante Sabor 0" | Retornar o restaurante correspondente |
| Termo sem correspondência no sistema | "xyzabc123" | Retornar "Nenhum restaurante encontrado", sem erro |

**Casos derivados:** CT01, CT02 e CT03

---

## 4. Tarefa 3: Casos de teste e rastreabilidade

### 4.1 Casos de teste

### CT01: Busca por categoria existente retorna os restaurantes correspondentes

**Integrante responsável:** Elinton  
**Funcionalidade:** Pesquisar restaurantes por especialidade ou localização  
**Risco ou requisito relacionado:** R01  
**Técnica utilizada:** Particionamento de equivalência (classe: categoria existente)

**Pré-condição:**  
Aplicação carregada na tela inicial, com ao menos um restaurante cadastrado na categoria "Italiana".

**Dados de entrada:**  
"Italiana"

**Passos:**

1. Acessar a tela inicial do LocalEats.
2. Digitar "Italiana" no campo de busca.
3. Clicar em "Buscar".

**Resultado esperado:**  
A lista de resultados exibe todos os restaurantes cadastrados na categoria "Italiana".

---

### CT02: Busca por nome exato de restaurante existente retorna o restaurante correspondente

**Integrante responsável:** Elinton  
**Funcionalidade:** Pesquisar restaurantes por especialidade ou localização  
**Risco ou requisito relacionado:** R02  
**Técnica utilizada:** Particionamento de equivalência (classe: nome exato existente)

**Pré-condição:**  
Aplicação carregada na tela inicial, com o restaurante "Restaurante Sabor 0" visível na lista.

**Dados de entrada:**  
"Restaurante Sabor 0"

**Passos:**

1. Acessar a tela inicial do LocalEats.
2. Digitar "Restaurante Sabor 0" no campo de busca.
3. Clicar em "Buscar".

**Resultado esperado:**  
O resultado exibe o "Restaurante Sabor 0".

---

### CT03: Busca por termo sem correspondência não apresenta erro nem resultado incorreto

**Integrante responsável:** Elinton  
**Funcionalidade:** Pesquisar restaurantes por especialidade ou localização  
**Risco ou requisito relacionado:** Requisito de qualidade formulado na Atividade 1 (corretude da busca)  
**Técnica utilizada:** Particionamento de equivalência (classe: termo sem correspondência)

**Pré-condição:**  
Aplicação carregada na tela inicial.

**Dados de entrada:**  
"xyzabc123" (termo que não corresponde a nenhum restaurante ou categoria cadastrada)

**Passos:**

1. Acessar a tela inicial do LocalEats.
2. Digitar "xyzabc123" no campo de busca.
3. Clicar em "Buscar".

**Resultado esperado:**  
O sistema exibe a mensagem "Nenhum restaurante encontrado", sem apresentar erro.

---

### 4.2 Matriz de rastreabilidade

| Integrante | Funcionalidade | Risco ou requisito | Técnica utilizada | Casos de teste |
|---|---|---|---|---|
| Elinton | Pesquisar restaurantes por especialidade ou localização | R01 | Particionamento de equivalência | CT01 |
| Elinton | Pesquisar restaurantes por especialidade ou localização | R02 | Particionamento de equivalência | CT02 |
| Elinton | Pesquisar restaurantes por especialidade ou localização | Requisito de qualidade (Atividade 1) | Particionamento de equivalência | CT03 |

---

## 5. Uso de inteligência artificial

**Ferramenta utilizada:**  
[preencher você]

**Como foi utilizada:**  
[preencher você]

**Uma sugestão que precisou ser alterada ou rejeitada:**  
[preencher você]

**Como as respostas foram verificadas:**  
[preencher você]