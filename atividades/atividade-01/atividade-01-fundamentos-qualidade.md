# Atividade 1: Fundamentos e Características da Qualidade no LocalEats

## 1. Identificação

**Turma:** QS_Noite  
**Equipe:** Individual  
**Data:** 22/09/2026

### Integrantes

| Nome | Usuário no GitHub |
|---|---|
| Elinton | @Elinton-Souza |

**Elemento de Competência:** Compreender os fundamentos de qualidade de software e sua aplicação no desenvolvimento de sistemas.

**Aplicação:** <https://local-eats-unisenac.vercel.app/>

---

## 2. Tarefa 1: Fundamentos da qualidade

### 2.1 Necessidades explícitas e implícitas

| Tipo | Necessidade | Interessado | Consequência se não for atendida |
|---|---|---|---|
| Explícita | O úsuário deve conseguir criar uma conta | Pessoa que ainda não possui cadastro | Frustração em ter que repetir o processo ou desistir de usar o app |
| Explícita | O usuário deve conseguir buscar por um restaurante específico e encontrar exatamente esse restaurante | Usuário logado que já sabe o nome do restaurante que procura | Ele desiste de encontrar o restaurante pela busca e precisa navegar manualmente por toda a lista | 
| Implícita | Os favoritos e o histórico de pedidos devem continuar salvos depois que o usuário sai do sistema e entra novamente | Usuário logado que já usou o app antes | Frustração e perda de confiança no aplicativo, tendo que refazer favoritos e pedidos |
| Implícita | A aplicação deve funcionar corretamente em telas de tamanhos diferentes, sem precisar girar o aparelho ou dar zoom | Usuário que acessa pelo smartphone | Ele desiste de usar o app pelo celular e passa a usar só pelo computador |


### 2.2 Questão sobre os fundamentos da qualidade

**Um sistema que implementa todas as funcionalidades explicitamente solicitadas pode, ainda assim, apresentar baixa qualidade? Justifiquem utilizando pelo menos uma necessidade implícita identificada pela equipe.**

Sim, um sistema pode implementar corretamente todas as funcionalidades pedidas e, mesmo assim, ter baixa qualidade. No LocalEats, por exemplo, mesmo que o layout esteja perfeitamente visível no computador, se eu precisar girar o smartphone ou dar zoom para conseguir usar os botões principais, essa experiência revela um problema de qualidade — mesmo que a funcionalidade em si esteja tecnicamente funcionando. Isso mostra que qualidade não é só ter as funcionalidades implementadas: é atender expectativas que o usuário tem mesmo quando ninguém escreveu isso em nenhum requisito.

---


## 3. Tarefa 2: Exploração da aplicação

| Integrante | Funcionalidade | O que foi realizado | O que foi observado | Evidência |
|---|---|---|---|---|
| Elinton | Pesquisar restaurantes por especialidade ou localização | Busquei pelo termo de categoria real "Italiana" (uso esperado, uma busca por categoria existente) e, em seguida, busquei pelo nome exato de um restaurante que eu sabia existir, "Restaurante Sabor 0" (uso alternativo, buscando por um item específico já conhecido) | Nos dois casos o sistema retornou "Nenhum restaurante encontrado", mesmo a categoria "Italiana" e o restaurante "Restaurante Sabor 0" existindo e aparecendo normalmente na tela inicial (o restaurante inclusive já estava favoritado por mim) | [busca por "Italiana"](evidencias/elinton-busca-italiana-resultado.png) e [busca por "Restaurante Sabor 0"](evidencias/elinton-busca-restaurante-sabor-0-resultado.png) |

---


## 4. Tarefa 3: Requisitos e características de qualidade

| Integrante | Requisito de Qualidade | Característica ou subcaracterística | Justificativa | Como avaliar |
|---|---|---|---|---|
| Elinton | A busca por restaurantes deve retornar corretamente os restaurantes que correspondem ao termo pesquisado, seja o nome de um restaurante ou uma categoria existente no sistema | Adequação Funcional (Corretude Funcional) | Nas duas buscas realizadas (por categoria "Italiana" e pelo nome exato "Restaurante Sabor 0") o sistema não retornou o resultado correto, mesmo os dados pesquisados existindo e estando visíveis na tela inicial. Isso é justamente o que a Corretude Funcional avalia: se o sistema entrega resultados corretos e precisos | Buscar por todas as categorias mostradas nos filtros (4 no total) e por pelo menos 5 nomes exatos de restaurantes exibidos na tela inicial, contando quantas buscas retornam o resultado esperado. Critério proposto para esta atividade (não é requisito oficial do LocalEats): pelo menos 9 das 9 buscas devem retornar o restaurante correto |

---


## 5. Uso de inteligência artificial

**Ferramenta utilizada:**  
Gemini (assistente de IA do Google) e Claude (Anthropic)

**Como foi utilizada:**  
Usei o Gemini para entender melhor as características de qualidade da norma ISO/IEC 25010, já que o enunciado exige relacionar as situações analisadas a uma característica ou subcaracterística predominante. Usei o Claude para me ajudar a reorganizar minhas respostas (necessidades explícitas/implícitas, exploração da aplicação e evidências) dentro do template atual da atividade, que havia sido simplificado pelo professor em relação a uma versão anterior que eu já tinha preenchido.

**Como as respostas foram verificadas:**  
Comparei a explicação do Gemini sobre a ISO/IEC 25010 com o material da disciplina antes de aplicar a classificação de "Adequação Funcional" à situação analisada, para confirmar que fazia sentido. As necessidades identificadas, os testes realizados na aplicação e as evidências (prints) são meus, de quando explorei o LocalEats por conta própria; revisei e reescrevi o texto final com minhas próprias palavras antes de colar no repositório.