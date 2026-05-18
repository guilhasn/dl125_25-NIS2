---
title: "QNRCS v2"
layout: default
parent: "Recursos"
nav_order: 6
---

# QNRCS v2 — Quadro Nacional de Referência para a Cibersegurança

{: .highlight }
> 📋 **Base legal:** art. 23.º + Anexo I do Aviso n.º 5146/2026/2. Aprovado como **instrumento estruturante** da segurança do ciberespaço (art. 22.º do RJC).

O **Quadro Nacional de Referência para a Cibersegurança (QNRCS)** é o referencial nacional de controlos e medidas de cibersegurança publicado pelo CNCS. A versão atualmente em vigor é a **versão 2 (QNRCS v2)**, constante do **Anexo I do Aviso n.º 5146/2026/2** que regulamenta o Decreto-Lei n.º 125/2025.

A versão anterior (QNRCS 2019, ainda disponível em PDF público no sítio do CNCS) está desatualizada. **Toda a referência a "QNRCS" no presente manual respeita à v2**, salvo indicação em contrário.

## O que mudou da versão 2019 para a v2

| Aspeto | QNRCS 2019 | QNRCS v2 (Anexo I) |
|---|---|---|
| **Objetivos** | 5 (Identificar · Proteger · Detetar · Responder · Recuperar) | **6** — acrescenta **Gerir** |
| **Níveis** | 3 (Inicial · Intermédio · Avançado) | **3 cumulativos**: Básico ⊂ Substancial ⊂ Elevado |
| **Alinhamento internacional** | NIST CSF 1.x · ISO 27001:2013 | NIST CSF 2.0 · ISO 27001/27002:2022 · CIS v8.1 · NIST SP 800-53 Rev.5 · CyberFundamentals |

## Os 6 objetivos do QNRCS v2

| Objetivo | Sigla | Propósito |
|---|---|---|
| **Gerir** *(novo)* | GR | Condições transversais de governação: contexto, estratégia, funções, políticas, supervisão, cadeia de abastecimento. |
| **Identificar** | ID | Conhecimento da entidade: ativos, riscos, melhoria contínua. |
| **Proteger** | PR | Salvaguardas operacionais: identidades/acessos, formação, dados, plataformas, infraestrutura. |
| **Detetar** | DE | Capacidade de identificar eventos e incidentes: monitorização, anomalias. |
| **Responder** | RS | Ação perante incidente: gestão, análise, notificação, mitigação. |
| **Recuperar** | RC | Restabelecimento pós-incidente: plano de recuperação e comunicação. |

## As 22 categorias

| Objetivo | Categorias |
|---|---|
| GR — Gerir | GR.CO Contexto · GR.GR Estratégia de Risco · GR.FR Funções/Responsabilidades · GR.PP Políticas · GR.SP Supervisão · GR.CA Cadeia de Abastecimento |
| ID — Identificar | ID.GA Gestão de Ativos · ID.AR Avaliação do Risco · ID.MC Melhoria Contínua |
| PR — Proteger | PR.GA Identidades/Acessos · PR.FC Formação · PR.SD Dados · PR.SP Plataformas · PR.RI Resiliência Infra |
| DE — Detetar | DE.MC Monitorização Contínua · DE.AE Anomalias e Eventos |
| RS — Responder | RS.GI Gestão · RS.AI Análise · RS.NC Notificação · RS.MI Mitigação |
| RC — Recuperar | RC.PR Plano de Recuperação · RC.CO Comunicação |

Cada categoria contém múltiplos **controlos** (códigos como `GR.CO-1`, `PR.GA-3`). O QNRCS v2 tem **~107 controlos no total**.

## Os 3 níveis cumulativos

O QNRCS v2 define para cada controlo medidas em **três níveis cumulativos**:

- **Básico** — mínimo exigível.
- **Substancial** — pressupõe o Básico cumprido + medidas adicionais.
- **Elevado** — pressupõe o Substancial cumprido + medidas avançadas.

Para **autarquias** (entidades públicas relevantes, Grupo A/B), o objetivo realista é **Básico em todos os controlos relevantes** do Anexo IV. Substancial e Elevado são patamares aspiracionais — ou aplicáveis à parte SMAS/empresa municipal qualificada como entidade essencial (que segue o Anexo III com os mesmos níveis B/S/E).

## QNRCS vs Anexo IV — qual usar?

| | QNRCS v2 (Anexo I) | Anexo IV |
|---|---|---|
| **Natureza** | Referencial nacional completo de cibersegurança | Catálogo de medidas mínimas para autarquias |
| **Universo** | Todas as entidades (essenciais, importantes, públicas relevantes) | Apenas entidades públicas relevantes Grupo A/B |
| **Estrutura** | 6 objetivos · 22 categorias · ~107 controlos · 3 níveis | 27 medidas O/T/H, por Grupo |
| **Origem** | Derivado de NIST CSF 2.0, ISO 27001:2022, etc. | Derivado do QNRCS, adaptado a autarquias |
| **Função pedagógica** | Mapa completo, referencial de maturidade | "Currículo mínimo" obrigatório |

O Anexo IV é o **currículo mínimo** que a autarquia tem de cumprir. O QNRCS é o **referencial maior** de onde o Anexo IV foi derivado — útil para perceber o contexto, mapear com NIST/ISO, e medir maturidade para além do mínimo legal.

## Mapeamento com referenciais internacionais

Cada controlo do QNRCS v2 indica explicitamente, no texto do Anexo I, os controlos equivalentes em NIST CSF 2.0, ISO/IEC 27001:2022, ISO/IEC 27002:2022, NIST SP 800-53 Rev.5, CIS CSC 8.1 e CyFun 2025. Útil para:

- Câmaras com fornecedores que trabalham com referenciais internacionais.
- Câmaras com pessoal técnico certificado em NIST/ISO que prefere navegar por esses códigos.
- Auditorias cruzadas com normas internacionais.

## Auto-avaliação de maturidade — dois instrumentos

Para usar o QNRCS v2 como ferramenta ativa de auto-avaliação na vossa câmara, ver [**E.2.1 — Auto-avaliação de maturidade QNRCS**]({% link 04-supervisao-roadmap/e2-1-autoavaliacao-qnrcs.md %}). Existem **duas versões** do Excel:

| Versão | Ficheiro | Controlos | Tempo de preenchimento | Para quem |
|---|---|---|---|---|
| **Reduzida** *(recomendada)* | [`avaliacao-maturidade-qnrcs.xlsx`]({{ '/templates/avaliacao-maturidade-qnrcs.xlsx' | relative_url }}) | **26** seleccionados dos ~107 | ~2h em equipa | Todas as câmaras Grupo A/B — ponto de partida. Alinhada com Anexo IV. |
| **Completa** *(opcional)* | [`avaliacao-maturidade-qnrcs-completa.xlsx`]({{ '/templates/avaliacao-maturidade-qnrcs-completa.xlsx' | relative_url }}) | **107** integrais | ~6-8h em equipa | Câmaras Grupo A · Câmaras com SMAS qualificado como essencial · Grupo B com maturidade já consolidada que queira aprofundar. |

Recomendação: **começar pela reduzida** (cobre o essencial e dá perfil de maturidade utilizável). A completa é o passo seguinte para câmaras que já têm os 26 mapeados e querem cobrir o referencial inteiro. Não é necessário fazer as duas em paralelo.

## Documento integral

- **Anexo I do Aviso (texto integral):** [DRE](https://diariodarepublica.pt/dr/detalhe/aviso/5146-2026-1069935643){:target="_blank"} — 85 páginas no total, Anexo I cobre páginas 17-85.
- **QNRCS 2019 (versão anterior, desatualizada):** [PDF CNCS](https://www.cncs.gov.pt/docs/cncs-qnrcs-2019.pdf){:target="_blank"} — referência histórica apenas.
- **NIST CSF 2.0:** [nist.gov/cyberframework](https://www.nist.gov/cyberframework){:target="_blank"}
- **ISO/IEC 27001:2022:** [iso.org/standard/27001](https://www.iso.org/standard/27001){:target="_blank"}

## Ver também

- [Recursos do CNCS]({% link recursos/cncs.md %}) — catálogo geral de recursos.
- [Anexo IV — medidas O/T/H]({% link recursos/anexo-iv-aviso-5146.md %}) — catálogo das medidas para autarquias.
- [B.1 Panorama do art. 27.º]({% link 01-gestao-risco/b1-art27-panorama.md %}) — onde o QNRCS é introduzido na sequência da formação.
