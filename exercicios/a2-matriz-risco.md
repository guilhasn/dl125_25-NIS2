---
title: "A2 — Matriz de risco"
layout: default
parent: "Worksheets dos exercícios"
nav_order: 2
---

# A2. Matriz de risco da entidade

**Duração**: 15 min · **Bloco**: B.2 · **Materiais**: [`a2-matriz-risco-simplificada.xlsx`]({{ '/templates/a2-matriz-risco-simplificada.xlsx' | relative_url }})

## Objetivo

Construir o **embrião** da matriz de risco da vossa entidade — 3 riscos identificados, classificados por probabilidade × impacto, com tratamento decidido. É uma das peças mais importantes da formação: tudo o que vem depois (medidas técnicas, prioridade de implementação, alocação de orçamento) decorre desta matriz.

Não procuramos exaustividade. Procuramos **três decisões fundamentadas**. A versão exaustiva constrói-se em câmara, nas semanas seguintes, usando o template [`matriz-risco-nis2.xlsx`]({{ '/templates/matriz-risco-nis2.xlsx' | relative_url }}).

## Instruções (individual, 15 minutos)

1. Abra [`a2-matriz-risco-simplificada.xlsx`]({{ '/templates/a2-matriz-risco-simplificada.xlsx' | relative_url }}) (password da formação).
2. Apague a linha de exemplo.
3. Identifique **3 riscos reais** da sua autarquia. Não invente cenários — pense nas coisas que lhe tiram o sono.
   - Categorias típicas em autarquias: ransomware, indisponibilidade do portal do munícipe, exfiltração de dados de munícipes, fornecedor único comprometido, perda total do datacenter por incêndio/inundação, phishing bem-sucedido contra vereador ou tesouraria.
4. Para cada, indique:
   - **Ativo afetado** (cruzar com [Exercício A3]({% link exercicios/a3-inventario.md %}) ou com a sua noção informal).
   - **Probabilidade** (1=raro, 5=quase certo).
   - **Impacto** (1=irrelevante, 5=paralisação prolongada do serviço público).
   - **Nível P × I** (calculado automaticamente — 1-6 baixo, 8-12 médio, 15-25 alto).
   - **Tratamento**: Mitigar, Transferir, Aceitar ou Evitar.
   - **Ação concreta**: uma frase que descreva o que vai fazer. Sem isto, a decisão fica em papel.

## Output esperado

3 linhas preenchidas. Idealmente:

- 1 risco "técnico clássico" (ransomware, malware, indisponibilidade).
- 1 risco "humano" (phishing, erro de configuração, fuga interna).
- 1 risco "estrutural" (fornecedor único, dependência tecnológica, fim de vida útil de equipamento crítico).

## Validação rápida

A maior parte das equipas tende a:

- **Sobrestimar a probabilidade** dos ataques mediáticos (ransomware ao máximo, sempre 5). Olhar para a base histórica: 1-3 é mais realista para uma câmara média.
- **Subestimar o impacto** da indisponibilidade prolongada do portal do munícipe (vereadores, comunicação social, prazos legais perdidos).
- Tratar **tudo como "mitigar"**. Algumas dependências críticas inevitáveis (Microsoft, fornecedor único contratado) só admitem **transferir** (contrato robusto) ou **aceitar** (com plano de contingência) — não "mitigar".

## Como continuar este trabalho na câmara

1. Alargar de 3 para **15-25 riscos** num *workshop* de algumas horas com a equipa de informática + chefe de gabinete + DPO.
2. Documentar a **metodologia** usada (escala P/I, definição de níveis) com o template [`metodologia-avaliacao-riscos-nis2.docx`]({{ '/templates/metodologia-avaliacao-riscos-nis2.docx' | relative_url }}) (obrigatório para Grupo A).
3. Para riscos com P × I ≥ 15, exigir **acta de aceitação formal do risco residual** assinada pelo presidente — template [`aceitacao-riscos-residuais-nis2.docx`]({{ '/templates/aceitacao-riscos-residuais-nis2.docx' | relative_url }}).
4. **Revisão semestral** mínima, ou após qualquer incidente significativo, ou após nova vulnerabilidade comunicada pelo CNCS (art. 31.º Aviso).

## Templates relacionados

- [`matriz-risco-nis2.xlsx`]({{ '/templates/matriz-risco-nis2.xlsx' | relative_url }}) — versão completa (folha-mestra a usar em câmara).
- [`plano-tratamento-riscos-nis2.docx`]({{ '/templates/plano-tratamento-riscos-nis2.docx' | relative_url }}) — formaliza ações decididas.
- [`matriz-risco-setor-agua-potavel-nis2.xlsx`]({{ '/templates/matriz-risco-setor-agua-potavel-nis2.xlsx' | relative_url }}) — para SMAS com dupla qualificação.

## Recurso externo opcional

Para aprofundar a metodologia ISO 27005 (base teórica da gestão de riscos): [**EduRisk — Guia ISO 27005**](https://edurisk-guia-iso-27005-632691460370.us-west1.run.app/){:target="_blank"}. Plataforma educacional de terceiros, gratuita, útil como leitura complementar enquanto constrói a sua matriz.

## Ver também

- [B.2 Análise e gestão de risco]({% link 01-gestao-risco/b2-analise-risco.md %}) — base teórica.
- [FAQ §3.2 — A análise de risco está mesmo no Anexo IV?]({% link recursos/faq.md %}#32-a-análise-de-risco-está-mesmo-no-anexo-iv) — porque é que tratamos como obrigação mesmo sem menção explícita.
