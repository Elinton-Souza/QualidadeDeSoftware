# Atividade 2: Organização da Qualidade no LocalEats

## 1. Identificação

**Turma:** QS_Noite  
**Equipe:** Individual  
**Data:** 22/09/2026

### Integrantes

| Nome | Usuário no GitHub |
|---|---|
| Elinton | @Elinton-Souza |

**Elemento de Competência:** Identificar papéis, responsabilidades e competências relacionadas às atividades de qualidade e testes.

---

## 2. Tarefa 1: Diagnóstico da situação

### 2.1 Problemas organizacionais

| Problema identificado | Possível consequência para o produto ou para a equipe |
|---|---|
| Não está claro quem pode aprovar a disponibilização de uma nova versão | Uma versão com defeitos pode ser lançada sem que ninguém tenha formalmente decidido que ela estava pronta, ou o lançamento pode atrasar porque ninguém se sente autorizado a aprovar |
| Alguns integrantes acreditam que somente o QA deve testar | Desenvolvedores não testam o próprio código antes de entregar, sobrecarregando o QA e permitindo que defeitos simples cheguem tarde no processo, ou até ao usuário final |
| Defeitos são identificados, mas nem sempre são registrados ou acompanhados | O mesmo defeito pode reaparecer, ser esquecido, ou ser corrigido sem que a equipe tenha visibilidade de quantos problemas existem ou de sua prioridade |

### 2.2 Responsabilidade pela qualidade

**A qualidade do LocalEats deve ser responsabilidade exclusiva do profissional de QA? Justifiquem.**

Não. A qualidade resulta de decisões tomadas em várias etapas do desenvolvimento: quem define os requisitos decide o que é esperado, quem implementa decide como construir, e quem aprova a versão decide se ela está pronta. Se só o QA fosse responsável, os testes só aconteceriam no fim do processo, quando já é mais caro corrigir problemas, e o resto da equipe deixaria de se preocupar em prevenir defeitos. O papel do QA é planejar e organizar os testes, mas a qualidade é resultado do trabalho de todos os papéis envolvidos.

---

## 3. Tarefa 2: Papéis e competências

| Integrante | Papel analisado | Responsabilidades relacionadas à qualidade | Competências técnicas | Competências comportamentais |
|---|---|---|---|---|
| Elinton | Desenvolvedor | Implementar as funcionalidades seguindo os requisitos definidos; testar o próprio código antes de entregar; corrigir defeitos identificados em sua área | Conhecimento da linguagem e do framework usados no LocalEats; capacidade de escrever testes unitários | Atenção a detalhes; disposição para testar o próprio trabalho antes de entregar; comunicação clara ao reportar problemas |
| Elinton | QA / Analista de Qualidade | Planejar e executar testes do sistema; registrar e acompanhar defeitos; ajudar a definir critérios de aceitação junto com o time | Conhecimento de técnicas de teste (particionamento de equivalência, tabela de decisão etc.); uso de ferramentas de registro de defeitos | Pensamento crítico; comunicação para relatar problemas sem gerar conflito; organização para acompanhar o status dos defeitos |
| Elinton | Líder técnico | Revisar código antes da integração; definir padrões técnicos; ajudar a priorizar a correção de defeitos | Experiência ampla no sistema; capacidade de revisar código de outras pessoas; visão de arquitetura | Capacidade de dar feedback construtivo; mediar decisões técnicas; liderança sem impor decisões arbitrariamente |
| Elinton | Responsável pelo produto | Definir e revisar requisitos; aprovar a disponibilização de uma nova versão; priorizar funcionalidades | Entendimento do domínio de negócio (restaurantes, pedidos); capacidade de escrever critérios de aceitação claros | Comunicação com usuários e equipe; capacidade de tomar decisões mesmo com informação incompleta; priorização |

---

## 4. Tarefa 3: Matriz de responsabilidades

Utilizem:

- **R:** responsável por executar a atividade;
- **A:** aprovador ou responsável final;
- **C:** consultado antes da execução ou decisão;
- **I:** informado sobre o resultado.

| Atividade de qualidade | Desenvolvedor | QA | Líder técnico | Responsável pelo produto |
|---|:---:|:---:|:---:|:---:|
| Definir critérios de aceitação | I | C | C | R/A |
| Revisar requisitos | I | C | R | A |
| Implementar a funcionalidade | R/A | I | C | I |
| Revisar o código | C | I | R/A |  |
| Criar testes unitários | R/A | C | I |  |
| Planejar e executar testes do sistema | C | R/A | I | I |
| Registrar e acompanhar defeitos | C | R/A | I | I |
| Priorizar a correção dos defeitos | C | C | R | A |
| Aprovar a disponibilização da versão | I | C | R | A |

### 4.1 Lacuna ou conflito encontrado

**Lacuna ou conflito:**  
Na atividade "Implementar a funcionalidade", o próprio Desenvolvedor é R e A ao mesmo tempo, sem nenhuma consulta formal ao QA ou ao Líder técnico antes de considerar o trabalho concluído.

**Consequência:**  
Isso se conecta diretamente ao primeiro problema identificado na Tarefa 1: funcionalidades chegam aos usuários com defeitos, porque a implementação é validada apenas pela mesma pessoa que a escreveu, sem uma segunda perspectiva antes de avançar para a revisão de código.

### 4.2 Práticas de QA recomendadas

| Prática recomendada | Problema que ajuda a resolver | Papéis envolvidos |
|---|---|---|
| Revisão de código obrigatória antes de qualquer merge (pull request review) | Reduz a concentração de "Implementar a funcionalidade" só no Desenvolvedor, trazendo o Líder técnico para dentro do processo antes da entrega | Desenvolvedor, Líder técnico |
| Reunião curta e periódica de triagem de defeitos, com critérios de severidade definidos | Resolve o problema de defeitos identificados mas não registrados ou acompanhados, dando visibilidade e prioridade combinada | QA, Desenvolvedor, Responsável pelo produto |

---

## 5. Uso de inteligência artificial

**Ferramenta utilizada:**  
Claude (Anthropic).

**Como foi utilizada:**  
Usei o Claude para me ajudar a organizar minhas respostas dentro da estrutura oficial exigida pelo template da atividade (divisão em tarefas, tabelas e seções), no mesmo formato do exemplo do repositório do professor.

**Como as respostas foram verificadas:**  
Os problemas organizacionais, a análise dos papéis, a distribuição da matriz RACI e as práticas recomendadas são minhas, baseadas no contexto descrito no enunciado da atividade. Conferi o enunciado oficial e o template do GitHub do professor para garantir que a estrutura e as colunas das tabelas estavam corretas antes de considerar a atividade pronta.