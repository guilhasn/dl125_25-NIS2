---
title: "C. Notificação de incidentes"
layout: default
nav_order: 4
has_children: true
---

# C. Notificação de incidentes

**Duração**: 90 minutos (14:00–15:30) · **6 sub-páginas**

Este é **o maior bloco do dia** — e o bloco onde, na prática, mais erros são cometidos. Os capítulos sobre notificação de incidentes do DL 125/2025 (arts. 38.º a 51.º) e do Aviso 5146/2026/2 (arts. 20.º a 22.º) são curtos, mas escondem um regime que **difere materialmente** da Directiva NIS2 original. Quem trouxer da memória os prazos «24h + 72h + 1 mês» da Directiva irá perder pelo menos um prazo. Atenção redobrada nas próximas seis páginas.

A tarde começa, portanto, pela parte mais operacional do regime: o que fazer **antes** (plano e ponto de contacto), **no momento** (decidir, qualificar, notificar), **a seguir** (comunicar destinatários, articular com RGPD e cibercrime), e **depois** (relatório final, lições aprendidas). Fecha com 25 minutos de exercício prático individual, sobre quatro cenários realistas, seguido de discussão em plenária.

## Objectivos do bloco

Ao final do bloco, cada formando deve ser capaz de:

1. **Decidir, em tempo real, se um incidente exige notificação e em quantas vias** — distinguir o limiar de «significativo» do art. 40.º, n.º 3, identificar quando se acumulam canais NIS2, RGPD e cibercrime.
2. **Distinguir os prazos PT dos prazos da Directiva NIS2 «pura»** — em particular, perceber a figura adicional de «fim de impacto significativo», a actualização facultativa de 72h e a regra das 2 horas.
3. **Preencher correctamente uma notificação inicial** segundo os campos obrigatórios do art. 42.º, n.º 2 — e perceber porque o «início do relógio» (verificação) não é o mesmo que «detecção».
4. **Articular NIS2 + RGPD + Lei do Cibercrime** — saber a quem notificar, em que prazo, e como fazer referência cruzada nas três comunicações.

## Sub-páginas

1. [C.1 Plano de resposta a incidentes]({% link 02-notificacao-incidentes/c1-plano-resposta.md %}) (15 min) — Estrutura mínima do plano: papéis (decisor / executor / comunicador), critérios de activação, escalação, comunicação externa, logging, encerramento. **Subtileza importante**: o Anexo IV não exige plano formal para autarquias — só exige o ponto de contacto (O.CRI) —, mas sem plano não há como cumprir os prazos. Sidebar dupla qualificação (RC e PCP obrigatórios para essenciais — arts. 31.º e 32.º).
2. [C.2 Prazos PT vs NIS2]({% link 02-notificacao-incidentes/c2-prazos-pt-vs-nis2.md %}) (15 min) — **A página crítica do bloco**. Tabela lado-a-lado, cinco diferenças materiais, marco temporal de início do relógio, critérios de «incidente significativo» do art. 40.º, n.º 3. **Folha-resumo dos prazos (PDF) disponível para download antes do bloco.**
3. [C.3 Conteúdo de cada notificação]({% link 02-notificacao-incidentes/c3-conteudo-notificacao.md %}) (15 min) — Manual de preenchimento dos cinco documentos: notificação inicial (24h, art. 42.º), actualização facultativa (72h, art. 42.º, n.º 3), fim de impacto significativo (24h, art. 43.º), relatório final (30 dias úteis, art. 44.º), intercalar (semanal, art. 44.º, n.º 3) + comunicação aos destinatários (art. 48.º).
4. [C.4 Cruzamento RGPD]({% link 02-notificacao-incidentes/c4-cruzamento-rgpd.md %}) (10 min) — Dois canais paralelos (CNCS 24h, CNPD 72h); o mecanismo «uma só notificação» do art. 40.º, n.º 7 pende de protocolo; recomendação prática de **dupla notificação** durante a transição; cenário concreto de ransomware com exfiltração; triângulo NIS2 + RGPD + Lei 109/2009.
5. [C.5 Demo: plataforma CNCS]({% link 02-notificacao-incidentes/c5-demos.md %}) (10 min) — Demonstração ao vivo (ou capturas) da plataforma electrónica oficial; *workflow* completo de submissão; art. 17.º do Aviso e contactos de emergência se a plataforma falhar.
6. [C.6 Fichas de cenário do exercício A4]({% link 02-notificacao-incidentes/c6-cenarios-exercicio.md %}) (25 min) — Exercício prático individual com 4 fichas: ransomware, fornecedor comprometido, DDoS portal, phishing ao vereador. *Output*: notificação inicial preenchida + discussão em plenária com voluntários.

## Após este bloco

Saem com **três peças concretas**: o esboço do plano de resposta da entidade (mesmo que de meia página), a folha-resumo dos prazos PT em PDF (para imprimir e afixar no gabinete TIC ou na recepção) e uma notificação inicial preenchida sobre um cenário simulado (rascunho de referência para o dia real). Saem também com a noção operacional de que, em caso de incidente significativo, o ritmo é o ritmo do CNCS — não o ritmo administrativo habitual.

## Exercícios associados

- [Exercício A4 — Simulação de notificação 24h]({% link exercicios/a4-notificacao.md %}) (25 min, dentro de C.6).

## Roteiro paralelo

Para autarquias com **dupla qualificação** (SMAS, empresa municipal em sector Anexo I/II): os prazos são iguais, mas a notificação de fim de impacto significativo, o plano de resposta formal e os papéis RC/PCP (arts. 31.º e 32.º) aplicam-se com mais rigor à parte essencial. Acompanhar [Anexo III vs Anexo IV]({% link roteiro-essencial/anexo-iii-vs-anexo-iv.md %}) em paralelo. **Importante**: uma só pessoa pode submeter as notificações de ambas as qualificações na plataforma electrónica, mas as notificações são **distintas** se ambas as entidades forem afectadas.

## Aviso final

Este é, por consenso dos profissionais que já lidam com incidentes em entidades públicas, **o bloco onde mais erros são cometidos** — pela combinação de pressão temporal (24h passam depressa), exigência probatória (cada hora tem de estar documentada) e cruzamento de regimes (NIS2 + RGPD + cibercrime). **Atenção redobrada**: relêem as páginas no fim de semana antes de irem para a sessão. A folha-resumo dos prazos vai com vocês para o gabinete TIC.
