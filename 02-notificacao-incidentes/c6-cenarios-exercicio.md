---
title: "C.6 Cartões de cenário do exercício A4"
layout: default
parent: "C. Notificação de incidentes"
nav_order: 6
---

# C.6 Cartões de cenário do exercício A4

Os 25 minutos finais do bloco C são **prática**. Quatro cartões de cenário, distribuídos pelos pares de formandos: a tarefa é, em **15 minutos**, decidir se notifica o CNCS, preencher a notificação inicial dos 24h, identificar canais paralelos (RGPD? MP?) e justificar as decisões. Os restantes 10 minutos são para apresentação rápida (≈1 min/par) das decisões-chave e debate.

Esta página apresenta os cenários e as instruções. Os cartões físicos (PDF A5, um por par, plastificados) são gerados na **Fase 4** da produção do hub e ficam disponíveis para *download* na página de [recursos]({% link recursos/templates.md %}) antes do dia 15.

## Instruções gerais

**Formação dos pares**: na sessão presencial, os formandos trabalham em pares com colega da própria autarquia sempre que possível (ou da mesma dimensão se vierem sozinhos).

**Distribuição dos cartões**: 4 cartões, atribuídos por sorteio ou por escolha das autarquias (uma autarquia que tenha sofrido recentemente um incidente análogo pode escolher um cenário distinto para evitar replicar a experiência).

**Tarefa**: 15 minutos para cada par produzir:

1. **Decisão de notificação**: este incidente atinge o limiar de «significativo» (art. 40.º, n.º 3 do RJC)? Justificar com 2-3 parâmetros concretos. Ver [C.2]({% link 02-notificacao-incidentes/c2-prazos-pt-vs-nis2.md %}).
2. **Canais accionados**: CNCS? CNPD? Ministério Público? Comunicação a destinatários (art. 48.º)? Ver [C.4]({% link 02-notificacao-incidentes/c4-cruzamento-rgpd.md %}).
3. **Notificação inicial dos 24h** parcialmente preenchida no template `notificacao-24h-nis2.docx` — pelo menos: identificação, hora de verificação, descrição sumária, estimativa de impacto (ver [C.3]({% link 02-notificacao-incidentes/c3-conteudo-notificacao.md %})).
4. **Decisão de comunicação externa**: comunicado público? Sim/não, e quando.

**Apresentação**: cada par tem **1 minuto** para apresentar:

- Decisão de notificação (sim/não, prazo).
- Canais accionados.
- A decisão mais difícil que tomou.

**Output esperado**: cada par sai com **um rascunho de notificação inicial** parcialmente preenchido — material levado para casa, ponto de partida do registo de incidentes da entidade.

## Templates a usar

| Template | Etiqueta | Quando |
|---|---|---|
| `notificacao-24h-nis2.docx` | Preencher | Notificação inicial — saída do exercício. |
| `registo-incidentes-nis2.xlsx` | Registar | Linha de registo posterior — opcional dentro do exercício, recomendado para casa. |
| `playbook-ransomware-nis2.docx` | Referência | Útil para o Cartão 1 e para complementar o Cartão 4. |
| `playbook-data-breach-nis2.docx` | Referência | Útil para os Cartões 1, 2 e 4 (todos com dimensão de violação de dados pessoais). |

## Cartão 1 — Ransomware

> **Hoje, 15h32.** O técnico de informática reporta que três servidores (incluindo o que aloja o registo civil e o aprovisionamento) estão a apresentar mensagem de bloqueio com pedido de resgate em criptomoeda. Cópias de segurança são *offline* mas ainda não testadas. Aproximadamente 40.000 ficheiros afectados. Vereador exige saber em 30 min se notifica imprensa local.

**Pistas para análise**: impacto significativo (sim — vários servidores críticos, dados pessoais provavelmente afectados, paragem de serviços). Canais: CNCS (24h), CNPD (72h — suspeita forte de violação de dados pessoais), MP (Lei 109/2009 — crime informático), comunicação a munícipes (art. 48.º — quando se confirmar âmbito). Decisão sobre imprensa: gestão de comunicação distinta da obrigação legal — coordenar com comunicação interna; **prematuro** ao fim de minutos da detecção.

## Cartão 2 — Fornecedor comprometido

> **Hoje, 09h15.** O fornecedor da aplicação de Gestão Documental envia comunicado a todos os clientes: foram detectados acessos não autorizados a servidores partilhados na semana passada. Não confirma se dados dos vossos munícipes foram acedidos. A empresa investiga.

**Pistas para análise**: o incidente é do fornecedor — mas a entidade pública relevante é **a vossa câmara**, e o responsável pelo tratamento dos dados é a vossa câmara. **Hora de verificação**: a partir do momento em que recebem o comunicado — relógio dos 24h CNCS começa agora. Notificar mesmo sem confirmação de exfiltração («possa vir a existir um incidente significativo» — art. 42.º, n.º 1). RGPD pode aguardar confirmação, mas iniciar análise de impacto desde já. Activar cláusula contratual com o fornecedor (informação detalhada, evidência preservada). Distinção causa próxima (fornecedor) vs responsabilidade legal (a câmara é quem notifica).

## Cartão 3 — DDoS no portal do munícipe

> **Hoje, 11h00.** Portal do Munícipe e formulários digitais inacessíveis há 90 min. Tráfego anormal a partir de IPs estrangeiros. Munícipes não conseguem submeter requerimentos urgentes. Vereador da modernização administrativa pergunta «quando volta?».

**Pistas para análise**: indisponibilidade > 90 min — atravessou o limiar conservador das 4h? Ainda não, **mas a tendência é negativa**. Decisão: monitorizar 30-60 min mais — se persistir, **notificar como provavelmente significativo**. Sem dimensão de violação de dados pessoais (DDoS é negação de serviço, não acesso). CNPD: provavelmente não. MP: depende da motivação do atacante — pedido de resgate à parte, dificilmente. Comunicação a munícipes (art. 48.º): **sim**, na 1.ª hora, na página institucional alternativa e nas redes sociais — «portal indisponível, requerimentos urgentes por e-mail para X».

## Cartão 4 — Phishing com fraude ao vereador

> **Hoje, 14h00.** Detectado movimento anómalo na caixa de e-mail de um Vereador: 200 e-mails enviados com pedidos de transferência bancária para fornecedores municipais, falsificando assinatura. Já se sabe que dois fornecedores tentaram efectuar transferências; bancos suspenderam.

**Pistas para análise**: incidente significativo (sim — compromisso de identidade institucional, tentativa de fraude, dimensão financeira). Canais: CNCS (24h), CNPD (72h — caixa de e-mail do vereador contém dados pessoais de munícipes em correspondência), MP (Lei 109/2009 — falsificação informática), comunicação aos fornecedores potencialmente afectados (todos os 200 destinos do *spear-phishing* têm de ser avisados — art. 48.º aplicado em sentido lato). Acção imediata: bloquear conta, reset de credenciais, MFA obrigatório, análise forense da caixa (o que esteve acessível ao atacante?).

## Critérios de avaliação dos outputs (uso do formador)

Não há classificação numérica. Os critérios qualitativos para *feedback* na apresentação:

- A decisão de notificar foi **justificada** com referência aos parâmetros do art. 40.º, n.º 3?
- A hora de verificação foi **fixada** com precisão (não vaga)?
- Foram identificados **todos os canais** aplicáveis (CNCS, CNPD se aplicável, MP se aplicável, art. 48.º se aplicável)?
- A notificação inicial preenchida tem os 4 grupos de campos do art. 42.º, n.º 2?
- A decisão de comunicação externa foi **proporcional** ao momento (1 hora vs 1 dia vs 1 semana)?

## Próximo passo

Após o exercício, fechamento do bloco e pausa antes do Bloco D. Voltar a [índice do bloco C ←]({% link 02-notificacao-incidentes/index.md %}).
