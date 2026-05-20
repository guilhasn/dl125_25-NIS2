---
title: "E.1 Supervisão ex post"
layout: default
parent: "E. Supervisão e roadmap"
nav_order: 1
---

# E.1 Supervisão *ex post*

{: .note }
> **Grupo A** = autarquia com ≥ 250 trabalhadores  
> **Grupo B** = autarquia com 75-249 trabalhadores  
> (art. 7.º RJC — ver [A.2 Quem está abrangido]({% link 00-enquadramento/a2-quem-esta-abrangido.md %}))

**Duração**: 5 min · **Base legal**: [*art. 55.º RJC*{:.legal}]({% link recursos/legislacao-dl-125-2025.md %}#art-55)

Uma autarquia não é supervisionada como uma entidade essencial. Não há auditoria periódica programada, não há obrigação de relatórios anuais ao CNCS, não há *peer review* sectorial. O que existe é **supervisão *ex post*** — o CNCS pode pedir contas **quando houver motivo**: a seguir a um incidente, perante uma denúncia, ou por amostragem aleatória. Esta página explica em que consiste e como se preparar.

{: .caso-pratico }
> **Caso prático 8 — Práticas sem dossier**
>
> Após um incidente de baixa gravidade, uma entidade pública relevante recebe pedido formal de informação em sede de supervisão *ex post* (*art. 55.º RJC*). A equipa explica oralmente que faz *backups* regulares, tem contactos de emergência dos fornecedores, dá orientações verbais aos utilizadores e revê o portal trimestralmente. O CNCS pede evidência documental.
>
> **Pergunta:** que vai acontecer? Onde está o problema — nas práticas ou na sua demonstração?

<details markdown="block">
<summary><strong>Ver resposta</strong></summary>

O problema **não é ausência de práticas** — é **ausência de prova organizada**. Em cibersegurança regulada, **o que não está documentado pode não existir** do ponto de vista do regulador. Sem matriz de risco aprovada, plano de resposta documentado, registos de testes de restauro, registos de formação ou actas de decisão, a entidade não consegue demonstrar diligência.

Antes de qualquer pedido de supervisão, manter **dossier mínimo de conformidade** sempre actualizado:

- Qualificação da entidade (Grupo, dupla qualificação se aplicável).
- Inventário de ativos críticos.
- Matriz de risco e plano de tratamento.
- Plano de resposta a incidentes.
- Registos de incidentes, testes de restauro e formação.
- Actas de decisão dos órgãos competentes.
- Contratos críticos e cláusulas de cibersegurança.

A **evidência é parte da própria conformidade**, não o relatório que se faz depois.
</details>

## O que a lei diz

> «O Centro Nacional de Cibersegurança exerce a supervisão das entidades públicas relevantes em momento posterior ao da prática dos atos ou da ocorrência dos factos, podendo aceder, designadamente: a) Aos sistemas, redes, instalações e equipamentos; b) Aos registos, documentos e demais informação considerada relevante; c) Às pessoas com funções na entidade.» — paráfrase do [*art. 55.º RJC*{:.legal}]({% link recursos/legislacao-dl-125-2025.md %}#art-55)

A figura distingue-se da **supervisão *ex ante*** (aplicável a essenciais — art. 53.º) em três pontos:

| Dimensão | Essenciais (art. 53.º) | **Públicas relevantes (art. 55.º)** |
|---|---|---|
| Periodicidade | Inspecções programadas + auditorias regulares | Apenas perante motivo |
| Pedido de informações | A todo o tempo, proactivamente | Reactivamente, mediante despacho fundamentado |
| Acesso físico | Acesso programado às instalações | Acesso só com motivo (incidente, denúncia, indício) |
| Custo da postura | Postura permanente de prontidão | Postura **defensável** quando solicitada |

## Quando se pode esperar uma inspecção

Três cenários típicos:

1. **Após incidente significativo notificado** — o CNCS pode pedir esclarecimentos adicionais, evidência forense, registo cronológico das decisões, comprovativo das medidas correctivas adoptadas. É a situação mais frequente. A vossa documentação interna do incidente serve aqui.

2. **Sequência de queixa, denúncia ou processo judicial** — um munícipe que sofreu prejuízo, um trabalhador que reportou má prática interna, ou um processo no Ministério Público envolvendo crimes informáticos contra a câmara.

3. **Por amostragem ou intuição da autoridade** — o CNCS pode escolher por amostra estatística ou por sinal indireto (ex.: divulgação pública de vulnerabilidade conhecida; *posts* em fóruns *underground* a vender dados de autarquias). Raro mas possível.

Em qualquer dos três casos, o pedido inicial chega tipicamente por **comunicação eletrónica** através do MyCiber, com prazo de resposta entre 5 e 30 dias úteis, conforme a urgência.

## O que o CNCS pode pedir

O *art. 55.º, n.º 1 do RJC*{:.legal} é abrangente. Em concreto, espere-se um pedido de:

- **Cópia das políticas em vigor** — segurança da informação, *backups*, controlo de acessos, formação. Quem não tem documento escrito, falha aqui.
- **Inventário de ativos** e lista de ativos publicamente acessíveis ([*art. 32.º do Aviso*{:.legal}]({% link recursos/legislacao-aviso-5146.md %}#art-32)).
- **Matriz de risco** atualizada (ver [B.2]({% link 01-gestao-risco/b2-analise-risco.md %})).
- **Registo do(s) incidente(s)** ocorrido(s), incluindo decisões tomadas, horas, responsáveis, comunicações externas.
- **Registo de presenças em formação** dos últimos 12 meses.
- **Comprovativos técnicos** — capturas de configurações de MFA, política de palavras-passe, *logs* de eventos relevantes.
- **Designação do ponto de contacto** comunicado ao CNCS na altura do registo.
- **Acta da última revisão pela gestão** sobre a postura de segurança da informação.

A norma habilita também o CNCS a deslocar-se às instalações e a falar com trabalhadores — mas, na prática, a maior parte das inspecções a autarquias resolve-se em **documental**, sem deslocação física.

## A postura defensável

Não é viável manter uma postura de "estaminé permanente" como entidade essencial. Mas é **viável e desejável** manter uma postura **defensável**: documentos prontos, decisões justificadas, evidência de **adaptação ativa** ao regime. Três princípios:

1. **Cada decisão importante deixa rasto** — política aprovada por despacho, acta da reunião de gestão, e-mail interno que confirma o argumentário.
2. **Cada incidente significativo tem registo** — registo cronológico completo, mesmo para incidentes sem necessidade de notificação. O CNCS pode pedir mais tarde.
3. **Cada ano produz evidência** — acta da revisão anual pela gestão, relatório de auditoria interna (mesmo informal), atualização da matriz de risco. Sem evidência anual, três anos sem incidentes parecem **inacção**.

## Sanções aplicáveis no contexto de supervisão

A própria supervisão não aplica sanções; aplica-se **a seguir** ao apuramento de incumprimento. O quadro de coimas e sanções acessórias está em [A.4 Prazos, sanções e amnistia]({% link 00-enquadramento/a4-prazos-sancoes.md %}) — recordar:

- Para autarquia **Grupo B**, infracção muito grave ([*art. 61.º RJC*{:.legal}]({% link recursos/legislacao-dl-125-2025.md %}#art-61)): **8.000 € a 350.000 €**.
- Para autarquia **Grupo A**: **16.000 € a 4.000.000 €**.
- **Dispensa de coima** transitória até ~3 de Abril de 2027 — [*art. 65.º RJC*{:.legal}]({% link recursos/legislacao-dl-125-2025.md %}#art-65).

A dispensa do [*art. 65.º RJC*{:.legal}]({% link recursos/legislacao-dl-125-2025.md %}#art-65) é **discricionária** e pressupõe que a entidade tem **plano de adaptação em curso documentado**. Sem evidência de atividade, a dispensa é indeferida.

## Em dupla qualificação

Para autarquias com **SMAS** ou empresa municipal qualificada como **entidade essencial**, o regime de supervisão da parte essencial é o do [*art. 53.º RJC*{:.legal}]({% link recursos/legislacao-dl-125-2025.md %}#art-53) — **supervisão *ex ante***. Implica:

- Inspecções periódicas programadas pelo CNCS.
- Obrigação de relatório anual.
- Acesso facilitado do CNCS aos sistemas e instalações.
- Designação formal de **RC** ([*art. 31.º RJC*{:.legal}]({% link recursos/legislacao-dl-125-2025.md %}#art-31)) e **PCP** ([*art. 32.º RJC*{:.legal}]({% link recursos/legislacao-dl-125-2025.md %}#art-32)).

A vossa câmara pode ser **simultaneamente** sob *ex post* (parte câmara) e *ex ante* (parte SMAS) — duas posturas administrativas distintas, dois canais de comunicação separados no MyCiber.

## Próximo passo

[E.2 Documentação mínima — checklist final →]({% link 04-supervisao-roadmap/e2-documentacao-minima.md %})
