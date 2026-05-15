---
title: "A4 — Simulação de notificação"
layout: default
parent: "Exercícios A1–A5"
nav_order: 4
---

# A4. Simulação de notificação 24h

**Duração**: 25 min · **Bloco**: C.6 · **Materiais**: 4 fichas de cenário em PDF (descarregáveis, uma sorteada por formando em sessão) + [`notificacao-24h-nis2.docx`]({{ '/templates/notificacao-24h-nis2.docx' | relative_url }})

## Objectivo

Exercitar **uma vez** o que deve ser automático no dia em que acontecer a sério: receber um incidente real, decidir em **minutos** se atinge o limiar de significativo do art. 40.º, n.º 3 do RJC, identificar os canais aplicáveis (CNCS, CNPD, MP, art. 48.º), e preencher a notificação inicial dos 24h. É o exercício mais consequente do dia. Quando o incidente vier, terão **15 minutos** úteis — não horas.

## As 4 fichas de cenário

Em sessão, o formador atribui uma ficha por sorteio a cada formando (ou a um subconjunto, se a turma for grande). Os PDFs estão acessíveis a todos no hub — depois do exercício pode consultar os outros três:

| Nº | Cenário | PDF |
|---|---|---|
| 1 | **Ransomware no servidor de ficheiros** — registo civil + aprovisionamento bloqueados, ~40.000 ficheiros, indícios fortes de exfiltração | [`a4-ficha-cenario-1-ransomware.pdf`]({{ '/templates/a4-ficha-cenario-1-ransomware.pdf' | relative_url }}) |
| 2 | **Fornecedor de GED comprometido** — fornecedor confirma acessos não autorizados a servidores partilhados, dados de munícipes potencialmente expostos | [`a4-ficha-cenario-2-fornecedor.pdf`]({{ '/templates/a4-ficha-cenario-2-fornecedor.pdf' | relative_url }}) |
| 3 | **DDoS contra o Portal do Munícipe** — portal inacessível há 90 min, prazos legais a expirar, pressão política | [`a4-ficha-cenario-3-ddos.pdf`]({{ '/templates/a4-ficha-cenario-3-ddos.pdf' | relative_url }}) |
| 4 | **Phishing com fraude ao Vereador** — caixa de e-mail comprometida, 200 e-mails fraudulentos, tentativas de transferência bancária | [`a4-ficha-cenario-4-phishing.pdf`]({{ '/templates/a4-ficha-cenario-4-phishing.pdf' | relative_url }}) |

## Instruções (individual, 25 minutos)

**Fase 1 — Decisão (5 min).** Lendo a ficha, sozinho, responda mentalmente (ou em notas) a:

1. Este incidente atinge o **limiar de significativo** (art. 40.º, n.º 3 do RJC)? Justifique com 2-3 parâmetros concretos.
2. **Quando** começa a contar o prazo dos 24h — a hora de detecção ou a hora de verificação?
3. **Que canais** se accionam? CNCS sempre. CNPD se houver dados pessoais. MP se houver crime informático (Lei 109/2009). Art. 48.º (comunicação a destinatários) se aplicável.

**Fase 2 — Preenchimento (10 min).** Abra [`notificacao-24h-nis2.docx`]({{ '/templates/notificacao-24h-nis2.docx' | relative_url }}) (password da formação) e preencha pelo menos:

- Identificação da entidade.
- Hora de verificação (não hora de detecção genérica).
- Descrição sumária do incidente.
- Estimativa de impacto (serviços afectados, número aproximado de munícipes).
- Outras informações relevantes (suspeita de violação de dados, crime informático, etc.).

**Fase 3 — Discussão em plenária (10 min).** O formador convida **4 voluntários** — idealmente um de cada cenário — a partilhar brevemente (≈2 min cada):

- Decisão de notificação (sim/não) e justificação.
- Canais accionados.
- A **decisão mais difícil** que tomou (e porquê).
- O que ficou **por decidir** ao final dos 15 min (o que faltaria).

## Output esperado

Cada formando termina com **um rascunho de notificação inicial** parcialmente preenchido no seu computador. Não tem de estar completo — o que importa é que **as decisões fundamentais estejam tomadas**. O documento sai convosco como ponto de partida do **registo interno de incidentes** da entidade.

## Validação rápida (formador) — armadilhas comuns

| Armadilha | Correcção |
|---|---|
| Confundir hora de **detecção** com hora de **verificação** | O relógio dos 24h começa em **T1 (verificação)**, não em T0 (alerta vago). |
| Esquecer a CNPD em incidente com dados pessoais | NIS2 e RGPD são **paralelos**, não substitutos. 24h CNCS + 72h CNPD. |
| Comunicar à imprensa antes de notificar o CNCS | **Ordem matters**: regulador primeiro, comunicação depois (excepto risco iminente para o público). |
| Ficha 2 (fornecedor): «esperar pelo fornecedor» | A entidade responsável é a câmara. **Notificar mesmo sem confirmação** — art. 42.º permite incompletude inicial. |
| Ficha 3 (DDoS): notificar com 30 min de indisponibilidade | Decisão deve ser proporcional. 30 min não atinge limiar; 4h+ provavelmente sim. **Monitorizar** antes de decidir. |
| Notificação sem assinatura ou sem hora | Documento jurídico — falta um campo, falha a evidência de cumprimento. |

## Como continuar este trabalho na câmara

1. **Plano de resposta a incidentes formal** documentado, com fluxo de decisão, escalação e responsáveis — use [`plano-resposta-incidentes-nis2.docx`]({{ '/templates/plano-resposta-incidentes-nis2.docx' | relative_url }}).
2. **Simulação interna** semestral usando uma destas fichas (ou outra adaptada) — tabletop de 30 min com o gabinete, a informática e o DPO.
3. **Lista de contactos de emergência** (CNCS, CNPD, MP, fornecedores TIC, banco do município) afixada no gabinete TIC.
4. **Treino MFA + reset rápido** para todos os utilizadores com privilégios elevados — Vereadores incluídos.

## Templates relacionados

- [`notificacao-24h-nis2.docx`]({{ '/templates/notificacao-24h-nis2.docx' | relative_url }}) — formulário a preencher.
- [`registo-incidentes-nis2.xlsx`]({{ '/templates/registo-incidentes-nis2.xlsx' | relative_url }}) — registo interno cronológico.
- [`plano-resposta-incidentes-nis2.docx`]({{ '/templates/plano-resposta-incidentes-nis2.docx' | relative_url }}) — plano formal de resposta.
- [`matriz-escalacao-incidentes-nis2.docx`]({{ '/templates/matriz-escalacao-incidentes-nis2.docx' | relative_url }}) — matriz de escalação por severidade.
- [`playbook-ransomware-nis2.docx`]({{ '/templates/playbook-ransomware-nis2.docx' | relative_url }}) — útil para a Ficha 1.
- [`playbook-data-breach-nis2.docx`]({{ '/templates/playbook-data-breach-nis2.docx' | relative_url }}) — útil para as Fichas 1, 2 e 4.

## Ver também

- [C.2 Prazos PT vs NIS2]({% link 02-notificacao-incidentes/c2-prazos-pt-vs-nis2.md %}) — a página mais importante do hub.
- [C.3 Conteúdo de cada notificação]({% link 02-notificacao-incidentes/c3-conteudo-notificacao.md %}) — campos obrigatórios.
- [C.4 Cruzamento RGPD]({% link 02-notificacao-incidentes/c4-cruzamento-rgpd.md %}) — dois relógios paralelos.
- [C.6 Fichas de cenário]({% link 02-notificacao-incidentes/c6-cenarios-exercicio.md %}) — versão expandida com análise por ficha.
- [FAQ §4 — Notificação de incidentes]({% link recursos/faq.md %}#4-notificação-de-incidentes) — perguntas frequentes.
