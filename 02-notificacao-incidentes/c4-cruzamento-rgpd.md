---
title: "C.4 Cruzamento RGPD"
layout: default
parent: "C. Notificação de incidentes"
nav_order: 4
---

# C.4 Cruzamento RGPD

A maior parte dos incidentes que vão ocorrer numa autarquia **afecta dados pessoais de munícipes**. Quando isso acontece, o relógio NIS2 não corre sozinho: corre **em paralelo** com o relógio do RGPD. Os dois regimes têm prazos diferentes, autoridades diferentes, e por agora ainda **canais de notificação diferentes**. Esta página explica como gerir essa coexistência sem perder nenhuma das duas obrigações.

## Dois canais paralelos

| Regime | Autoridade | Prazo | Quando se aplica |
|---|---|---|---|
| **NIS2 / DL 125/2025** | CNCS | 24h após verificação | Qualquer incidente significativo de ciberseguranca (com ou sem dados pessoais). |
| **RGPD / Lei 58/2019** | CNPD | 72h após conhecimento | Apenas violações de dados pessoais que envolvam «risco para os direitos e liberdades das pessoas singulares» (art. 33.º RGPD). |

A intersecção é grande: a maior parte dos incidentes acima do limiar de significativo do art. 40.º, n.º 3 do RJC (ver [C.2]({% link 02-notificacao-incidentes/c2-prazos-pt-vs-nis2.md %})) **também envolverá dados pessoais**, porque a actividade nuclear de uma autarquia é o tratamento de dados de munícipes (urbanismo, fiscalidade, acção social, identificação civil, registos).

## Mecanismo "uma só notificação" — art. 40.º, n.º 7 do RJC

O legislador português antecipou o problema:

> «Às entidades essenciais, importantes e públicas relevantes é assegurada a possibilidade de notificar um incidente, simultaneamente, à autoridade de ciberseguranca competente, às autoridades especiais de ciberseguranca, bem como às entidades previstas no n.º 5, através da plataforma prevista no n.º 7 do artigo 8.º, **nos termos a definir por protocolo outorgado entre as referidas autoridades**.» — art. 40.º, n.º 7 do RJC

«Entidades previstas no n.º 5» inclui, entre outras, o **Ministério Público**, a **Polícia Judiciária**, a **CNPD**, a **Entidade Fiscalizadora do Segredo de Estado** e o **GNS** (art. 40.º, n.º 5 do RJC).

A ideia é elegante: uma só submissão na plataforma electrónica do CNCS encaminharia automaticamente para todas as autoridades relevantes. **Mas há um problema operacional**: o mecanismo **depende do protocolo entre autoridades**, que **ainda não foi publicado** em Maio de 2026. Sem protocolo, a notificação cruzada automática não funciona. Submeter uma notificação NIS2 no CNCS **não é equivalente** a cumprir a obrigação RGPD junto da CNPD.

## Recomendação prática durante a transição

Até à publicação do protocolo, **duas notificações paralelas**, na mesma equipa, com timestamps próprios e referência cruzada:

1. **CNCS — 24h após verificação** do incidente significativo (NIS2 / DL 125/2025).
2. **CNPD — 72h após conhecimento** da violação de dados pessoais (RGPD art. 33.º + Lei 58/2019), através do formulário electrónico no sítio da CNPD.

Boas práticas operacionais:

- **Mesma pessoa, dois reports**: o comunicador (ver [C.1]({% link 02-notificacao-incidentes/c1-plano-resposta.md %})) trata dos dois canais. Manter conteúdo factual consistente entre as duas notificações.
- **Referência cruzada explícita**: na notificação RGPD à CNPD, indicar que foi também submetida notificação ao CNCS em data X com referência Y; e vice-versa.
- **Mesma análise de causa raiz** para os dois relatórios finais — para evitar contradições que possam ser exploradas em fiscalização.
- **Quem é o controlador**: para fins RGPD, o responsável pelo tratamento é a câmara em sentido próprio (ou o SMAS, se for sistema do SMAS). Não confundir com a qualificação NIS2 da entidade.

## Cenário concreto — ransomware com exfiltração

Vai ser o cenário mais comum. **Ransomware em servidor de ficheiros da câmara**, com indícios fortes de **exfiltração prévia** de pastas com dados de munícipes (pedidos de licenciamento, processos de acção social).

Resposta articulada:

1. **T0 — Detecção** (madrugada de 2.ª feira, alerta da equipa TIC).
2. **T1 — Verificação significativa** (07:00, equipa confirma encriptação e indícios de exfiltração). Inicia-se relógio NIS2 (24h) e relógio RGPD (72h).
3. **T2 — Notificação CNCS** (até 24h depois): notificação inicial do art. 42.º, indicando categoria «ataque malicioso», impacto provável em serviços públicos, suspeita de violação de dados pessoais (campo «outra informação relevante»).
4. **T3 — Notificação CNPD** (até 72h após T1): notificação RGPD do art. 33.º, indicando natureza da violação (confidencialidade), categorias e número aproximado de titulares e de registos, possíveis consequências, medidas em curso. Referência cruzada à notificação CNCS feita em T2.
5. **T4 — Comunicação aos titulares** (RGPD art. 34.º e RJC art. 48.º, em paralelo): se o risco for elevado, comunicado público + comunicações individuais aos titulares afectados, em linguagem clara. Coordenar com gabinete de comunicação.
6. **T5 — Participação ao MP** (Lei 109/2009 — Lei do Cibercrime), pelo facto de o ataque ser crime informático (acesso ilegítimo, sabotagem). O DL 125/2025 acrescenta o art. 8.º-A à Lei 109/2009.
7. **T6 — Notificação fim de impacto significativo** ao CNCS (24h após fim) + relatórios finais aos 30 dias úteis (CNCS) e nas datas próprias da CNPD.

## Cibercrime — triângulo NIS2 + RGPD + Lei 109/2009

Se o incidente foi causado por **acto doloso** (ataque malicioso), há **terceiro canal**: notificação ao **Ministério Público** ao abrigo da **Lei n.º 109/2009 (Lei do Cibercrime)**. O DL 125/2025 introduziu o **art. 8.º-A** na Lei do Cibercrime, expressamente endereçado a este cruzamento. O art. 40.º, n.º 5 do RJC enumera o MP entre as autoridades cuja obrigação de notificação «não é dispensada» pelo cumprimento do DL.

**Em dupla qualificação**: para autarquias com SMAS qualificado como entidade essencial, a parte essencial pode ter ainda **obrigações sectoriais específicas** (ERSAR para águas) que se somam. O quadrante de coordenação passa de triângulo a quadrilátero.

## Quem decide se o incidente é "violação de dados pessoais"

A decisão é do **Encarregado de Protecção de Dados (DPO)** da câmara, em articulação com o comunicador do plano de resposta NIS2 (ver [C.1]({% link 02-notificacao-incidentes/c1-plano-resposta.md %})). O DPO já está identificado em todas as autarquias (obrigação RGPD anterior). O plano de resposta a incidentes **tem de incluir o nome e contacto do DPO** entre os papéis activáveis. Sem este passo, a articulação NIS2-RGPD não funciona no dia do incidente.

## Templates aplicáveis

| Template | Etiqueta | Notas |
|---|---|---|
| [`playbook-data-breach-nis2.docx`]({{ '/templates/playbook-data-breach-nis2.docx' | relative_url }}) | Referência | Playbook específico para violação de dados — articula NIS2 e RGPD, com checklist dupla. |
| [`aipd-nis2.docx`]({{ '/templates/aipd-nis2.docx' | relative_url }}) | Referência | Avaliação de Impacto sobre a Protecção de Dados — não é resposta a incidente, mas ajuda a fundamentar o risco prévio. |
| [`politica-violacoes-dados-nis2.docx`]({{ '/templates/politica-violacoes-dados-nis2.docx' | relative_url }}) | Adaptar | Política interna que liga a notificação NIS2 à notificação RGPD; define quem decide o quê. |

## Próximo passo

[C.5 Demo: plataforma CNCS →]({% link 02-notificacao-incidentes/c5-demos.md %})
