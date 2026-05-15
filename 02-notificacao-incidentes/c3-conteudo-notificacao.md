---
title: "C.3 Conteúdo de cada notificação"
layout: default
parent: "C. Notificação de incidentes"
nav_order: 3
---

# C.3 Conteúdo de cada notificação

Esta página é o **manual de preenchimento** das três notificações obrigatórias (mais a actualização facultativa de 72h) que o DL 125/2025 prevê no Cap. V. Para cada uma, listam-se os **campos mínimos** exigidos pela lei, o que costuma faltar na primeira tentativa, e o template a usar. Os formulários definitivos da plataforma electrónica do CNCS são pendentes de **instrução técnica** prevista no art. 41.º, n.º 4 do RJC; até essa publicação, os templates do hub servem para preparação prévia, num formato ligeiramente mais conservador que o mínimo legal.

## 1. Notificação inicial — art. 42.º (24h)

Submetida na plataforma electrónica do CNCS «**sem demora injustificada e até 24 horas após (...) verificação**» (art. 42.º, n.º 1).

**Conteúdo mínimo obrigatório** (art. 42.º, n.º 2 do RJC):

| Campo | Conteúdo |
|---|---|
| a) Representante da entidade | Nome, telefone e e-mail de uma pessoa para contacto pela autoridade — pode ser o PCP do art. 32.º ou pessoa diferente. |
| b) Início ou detecção | Data e hora do início do incidente; em alternativa, da detecção (se o início não for determinável). |
| c) Descrição do incidente | Breve descrição, com **categoria da causa** e **efeitos produzidos** segundo a taxonomia do CNCS, sempre que possível. |
| d) Estimativa de impacto | Número de utilizadores afectados, duração, distribuição geográfica (incluindo impacto transfronteiriço), outra informação relevante. |

**O que costuma faltar na primeira tentativa** — e bloqueia a submissão:

- **Identificação da entidade** com NIF e número de qualificação atribuído pelo CNCS (aparece automaticamente se a notificação for feita na área reservada da plataforma).
- **Hora exacta de verificação** — registar internamente desde o primeiro momento (ver [C.2]({% link 02-notificacao-incidentes/c2-prazos-pt-vs-nis2.md %})).
- **Distinção entre início e detecção** — campos diferentes, datas diferentes. Em incidentes longos (compromisso de fornecedor há semanas, descoberto hoje), os valores divergem muito.
- **Categoria da causa** segundo a taxonomia — até à publicação da instrução técnica do CNCS, usar as cinco categorias-padrão do art. 31.º, n.º 4 do Aviso: «falha de sistema, fenómeno natural, erro humano, ataque malicioso, falha de fornecedor».

**Template**: [`notificacao-24h-nis2.docx`]({{ '/templates/notificacao-24h-nis2.docx' | relative_url }}) — preencher offline em rascunho (especialmente útil quando a plataforma estiver indisponível, ver art. 17.º do Aviso) e depois transcrever para a plataforma. Manter o rascunho como evidência de cumprimento atempado.

## 2. Actualização da notificação inicial — art. 42.º, n.º 3 (72h, facultativa)

«**Quando necessário**, a entidade (...) envia (...) uma actualização da notificação inicial até 72 horas após a verificação do incidente significativo, revendo a informação referida no número anterior e fornecendo uma avaliação inicial do incidente significativo, incluindo da sua gravidade e do seu impacto, bem como, se disponíveis, dos indicadores de exposição a riscos.» — art. 42.º, n.º 3 do RJC.

**Quando enviar**:

- Houve informação substancialmente nova entre as 24h e as 72h (extensão do impacto descoberta, novo vector confirmado, dados pessoais previamente não identificados como comprometidos).
- A notificação inicial continha informação inexacta que precisa de correcção.
- A autoridade pediu informação adicional (mais comum: pedido específico do CERT.PT/CNCS).

**Quando NÃO enviar**:

- A situação não evoluiu materialmente — a actualização passa a ser ruído.

**Template**: [`notificacao-72h-nis2.docx`]({{ '/templates/notificacao-72h-nis2.docx' | relative_url }}) — mais leve que a inicial, focado em **delta** (o que mudou).

## 3. Notificação de fim de impacto significativo — art. 43.º (24h após cessação)

Esta notificação **não existe na Directiva NIS2** — é figura específica do DL português. Submeter «sem demora injustificada e dentro do prazo de 24 horas após o fim do impacto» (art. 43.º, n.º 1). Note-se que o relógio é o **fim do impacto significativo**, não a resolução completa do incidente.

**Conteúdo mínimo obrigatório** (art. 43.º, n.º 2 do RJC):

| Campo | Conteúdo |
|---|---|
| a) Actualização à inicial | Apenas se houver elementos a corrigir/completar. |
| b) Medidas adoptadas | Breve descrição das acções de mitigação executadas. |
| c) Situação no momento do fim de impacto | Número de utilizadores afectados, duração total, distribuição geográfica, tempo estimado para recuperação total dos serviços. |

**Subtileza importante**: «fim de impacto significativo» pode ocorrer **antes** da plena recuperação. Exemplo: portal do munícipe restabelecido em modo de leitura ao fim de 8 horas (impacto significativo cessou); recuperação das funcionalidades de submissão demora mais 3 dias (esses dias já não contam para o relógio dos 30 dias úteis, que começou no momento do fim de impacto significativo).

**Para incidentes resolvidos em 2h** (art. 41.º, n.º 2): a entidade fica **dispensada da notificação inicial** e envia **apenas** esta notificação de fim de impacto significativo, dentro das 24h após o fim do impacto.

## 4. Relatório final — art. 44.º (30 dias úteis)

Submetido «**no prazo de 30 dias úteis a contar da data da notificação do fim de impacto significativo**» (art. 44.º, n.º 1) — não da detecção, não da notificação inicial. É o documento mais substancial.

**Conteúdo mínimo obrigatório** (art. 44.º, n.º 2 do RJC):

| Campo | Conteúdo |
|---|---|
| a) Início do impacto significativo | Data e hora em que o incidente assumiu impacto significativo. |
| b) Fim do impacto significativo | Data e hora em que perdeu impacto significativo. |
| c) Impacto efectivo | Número de utilizadores, duração, distribuição geográfica, descrição com categoria de causa e efeitos. |
| d) Medidas adoptadas | Indicação das medidas para mitigar o incidente. |
| e) Situação residual | Utilizadores ainda afectados, distribuição, tempo estimado para recuperação total, **indicação de notificações cruzadas** (ao MP, CNPD, outras autoridades sectoriais), outra informação relevante. |

**O que torna um relatório final defensável**:

- **Cronologia detalhada** — não basta «entre dia X e dia Y». Lista de eventos com horas: T0 detecção, T1 verificação significativa, T2 notificação inicial, T3 contenção, T4 erradicação, T5 fim de impacto, T6 notificação de fim de impacto, recuperação por fases.
- **Causa raiz** identificada — não confundir com causa próxima. Phishing bem-sucedido tem causa próxima (clique no link) mas causa raiz na ausência de MFA ou na formação insuficiente. A análise de causa raiz é também input para a revisão da matriz de risco (ver [B.2]({% link 01-gestao-risco/b2-analise-risco.md %})).
- **Medidas correctivas adoptadas** (já feitas) e **preventivas planeadas** (com prazos). Sem prazos, é wishlist.
- **Indicação de notificações cruzadas** — se houve violação de dados pessoais e notificou-se a CNPD, **referir explicitamente**. Articula com art. 40.º, n.º 5 do RJC.

**Template**: [`notificacao-30d-nis2.docx`]({{ '/templates/notificacao-30d-nis2.docx' | relative_url }}).

## 5. Relatório intercalar — art. 44.º, n.º 3 (semanal se persistir)

«**Na hipótese de, decorrido o prazo para apresentação do relatório final, o incidente ainda se encontrar em curso, a entidade (...) deve apresentar relatório intercalar (...) com periodicidade semanal até ao momento da apresentação do relatório final.**» — art. 44.º, n.º 3 do RJC.

Aplica-se em incidentes longos (compromisso persistente, recuperação muito prolongada). Conteúdo (art. 44.º, n.º 4) é análogo ao da notificação de fim de impacto: actualização à inicial, medidas adoptadas, situação de impacto, estimativa de recuperação. Em síntese: **se o incidente ainda não terminou ao fim de 30 dias úteis, semanalmente a entidade tem de actualizar o CNCS**.

## 6. Comunicação aos destinatários — art. 48.º

Em paralelo às notificações ao CNCS, o art. 48.º do RJC impõe **comunicação aos destinatários dos serviços** (munícipes) «**sem demora injustificada**» quando o incidente seja susceptível de os afectar negativamente. Esta é uma **obrigação distinta** da notificação ao CNCS e materializa-se em comunicado público, posts em sítio institucional, ou comunicações individualizadas se aplicável. A informação «deve ser prestada de forma gratuita e em linguagem facilmente compreensível» (art. 48.º, n.º 4) — sem juridiquês.

**Template**: [`notificacao-incidente-destinatarios-nis2.docx`]({{ '/templates/notificacao-incidente-destinatarios-nis2.docx' | relative_url }}) — modelo de comunicado público para incidente com impacto a munícipes (exemplo: indisponibilidade prolongada do portal, comprometimento de dados pessoais).

## Templates aplicáveis

| Template | Etiqueta | Quando usar |
|---|---|---|
| [`notificacao-24h-nis2.docx`]({{ '/templates/notificacao-24h-nis2.docx' | relative_url }}) | Adaptar | Notificação inicial (e como rascunho durante o incidente). |
| [`notificacao-72h-nis2.docx`]({{ '/templates/notificacao-72h-nis2.docx' | relative_url }}) | Adaptar | Actualização facultativa às 72h. |
| [`notificacao-30d-nis2.docx`]({{ '/templates/notificacao-30d-nis2.docx' | relative_url }}) | Adaptar | Relatório final aos 30 dias úteis. |
| [`notificacao-incidente-destinatarios-nis2.docx`]({{ '/templates/notificacao-incidente-destinatarios-nis2.docx' | relative_url }}) | Referência | Comunicação a munícipes (art. 48.º). |
| [`registo-incidentes-nis2.xlsx`]({{ '/templates/registo-incidentes-nis2.xlsx' | relative_url }}) | Aplicar | Registo interno de horas-chave e estado de cada notificação submetida. |

Todos os templates estão disponíveis a partir de 8 de Junho na página de [recursos]({% link recursos/templates.md %}).

## Exercício associado

[Exercício A4 — Notificação 24h]({% link exercicios/a4-notificacao.md %}) (25 min, em C.6) — cada formando preenche, individualmente para a ficha de cenário sorteada, a notificação inicial usando [`notificacao-24h-nis2.docx`]({{ '/templates/notificacao-24h-nis2.docx' | relative_url }}). Ver [C.6]({% link 02-notificacao-incidentes/c6-cenarios-exercicio.md %}).

## Próximo passo

[C.4 Cruzamento RGPD →]({% link 02-notificacao-incidentes/c4-cruzamento-rgpd.md %})
