---
title: "C.5 Demo: plataforma CNCS"
layout: default
parent: "C. Notificação de incidentes"
nav_order: 5
---

# C.5 Demo: plataforma CNCS

Este slot de 10 minutos é a parte mais visual do bloco. Mostra-se a **plataforma electrónica do CNCS** — o canal único e oficial de submissão de notificações, autoidentificação, qualificação e comunicações com a autoridade. Na sessão presencial, a demo é navegada ao vivo; aqui ficam as referências e o resumo do *workflow*.

## Plataforma electrónica do CNCS — canal oficial

Definida no **Cap. II do Aviso 5146/2026/2** (arts. 4.º a 19.º). É o **único canal oficial** de comunicação com a autoridade de ciberseguranca para autoidentificação, registo, comunicação de RC/PCP (não aplicável a autarquias), notificação de incidentes, relatório anual e recepção de notificações electrónicas do CNCS.

**Autenticação**: Cartão de Cidadão ou Chave Móvel Digital, com perfil de utilizador associado à entidade. Para autarquias, o secretário-geral ou o presidente designam por escrito quem pode actuar em nome da entidade.

### Workflow normal de submissão de incidente

1. **Login** com CC ou CMD.
2. **Área reservada da entidade** — escolher módulo «Notificação de incidentes».
3. **Tipo de notificação** — inicial (24h), actualização (72h), fim de impacto (24h após cessação), relatório final (30 dias úteis), intercalar (semanal).
4. **Preenchimento do formulário** — campos derivados directamente dos arts. 42.º a 44.º do RJC (ver [C.3]({% link 02-notificacao-incidentes/c3-conteudo-notificacao.md %})). Campos obrigatórios marcados; possibilidade de salvar rascunho e retomar.
5. **Anexos** — possibilidade de anexar relatórios técnicos, evidência, ficheiros de logs.
6. **Submissão** — confirmação com ID único da notificação. **Guardar o ID** para subsequentes notificações relacionadas (associação prevista no art. 22.º, n.º 2 do Aviso).
7. **Acknowledge** — recepção visível na área reservada; alertas automatizados quanto aos prazos seguintes podem ser disponibilizados (art. 22.º, n.º 3 do Aviso).

### Se a plataforma estiver indisponível em 15 de Junho de 2026

O Aviso 5146/2026/2 entrou em consulta pública em 10 de Março de 2026; a versão final e a entrada efectiva em funcionamento da plataforma podem não estar concluídas em meados de Junho. **Plano B na sessão**: usam-se **capturas de ecrã** das versões intermédias divulgadas e um **vídeo gravado** previamente (pré-trabalho da Fase 6 da produção do hub). O conteúdo conceptual — campos, fluxos, prazos — é o mesmo.

### Falência da plataforma — art. 17.º do Aviso

Cenário inverso, mais grave: a plataforma electrónica está formalmente em produção mas, no momento exacto do vosso incidente, **não responde** (sobrecarga, manutenção, ou — pior — porque o próprio ataque atingiu também a plataforma). O art. 17.º, n.os 1 e 2 do Aviso cobre o caso:

> «Nos casos em que ocorra uma situação de falência do funcionamento da plataforma eletrónica e as entidades não possam aguardar pela disponibilidade da mesma para prática de determinados actos ou submissão de informações, poderão remeter as mesmas para o correio eletrónico da autoridade de ciberseguranca competente ou contacto telefónico (...). Os actos praticados ou a informação submetida pelo endereço de correio electrónico (...) considera-se validamente submetida no momento da recepção da comunicação, para todos os efeitos.» — art. 17.º, n.os 1 e 2 do Aviso 5146/2026/2

**Contactos de emergência** a manter afixados no gabinete TIC e na matriz de escalação do plano de resposta (ver [C.1]({% link 02-notificacao-incidentes/c1-plano-resposta.md %})):

- E-mail: **`cncs@cncs.gov.pt`** (e endereço alternativo publicado pelo CNCS).
- Telefone do CERT.PT (disponibilizado no sítio do CNCS).

**Prova de submissão por canal alternativo**: guardar e-mail enviado com data/hora e qualquer acknowledge recebido. Capturas de ecrã da plataforma indisponível ajudam a fundamentar.

## Templates aplicáveis

Esta página é demonstrativa; os templates relevantes ao preenchimento das notificações estão em [C.3]({% link 02-notificacao-incidentes/c3-conteudo-notificacao.md %}). Recomenda-se ter sempre preparado:

| Template | Etiqueta | Notas |
|---|---|---|
| [`notificacao-24h-nis2.docx`]({{ '/templates/notificacao-24h-nis2.docx' | relative_url }}) | Adaptar | Rascunho a preencher offline se a plataforma falhar; copiar conteúdo para o e-mail ao CNCS. |
| [`registo-incidentes-nis2.xlsx`]({{ '/templates/registo-incidentes-nis2.xlsx' | relative_url }}) | Aplicar | Registar IDs das notificações submetidas (ou IDs internos se submissão por e-mail). |

## Próximo passo

[C.6 Fichas de cenário do exercício A4 →]({% link 02-notificacao-incidentes/c6-cenarios-exercicio.md %})
