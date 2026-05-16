---
title: "Checklist específica SMAS"
layout: default
parent: "Roteiro essencial (dupla qualificação)"
nav_order: 3
---

# Checklist específica SMAS — entidade essencial

{: .note }
> **Grupo A** = autarquia com ≥ 250 trabalhadores  
> **Grupo B** = autarquia com 75-249 trabalhadores  
> (art. 7.º RJC — ver [A.2 Quem está abrangido]({% link 00-enquadramento/a2-quem-esta-abrangido.md %}))

Esta checklist é a **versão SMAS** da [E.2 Documentação mínima]({% link 04-supervisao-roadmap/e2-documentacao-minima.md %}). Acrescenta as peças que decorrem da qualificação como **entidade essencial** (Anexo I — água potável / águas residuais) e que **não estão** na checklist da câmara.

Use em conjunto com a checklist principal. As peças aqui marcadas com **(SMAS)** **não substituem** as da câmara — **acumulam-se**.

## Designação formal — diferença-chave face à câmara

| Peça | Forma | Base legal |
|---|---|---|
| ☐ **(SMAS) Designação do Responsável de Cibersegurança (RC)** | Despacho do conselho de administração do SMAS | *art. 31.º RJC*{:.legal} |
| ☐ **(SMAS) Designação do Ponto de Contacto Permanente (PCP)** | Despacho + acordo de disponibilidade 24/7 | *art. 32.º RJC*{:.legal} |
| ☐ **(SMAS) Despacho de formação obrigatória do RC** | Comprovativo de formação + recertificação periódica | art. 31.º, n.º 4 RJC |

**Nota**: a designação tem de ser **pessoa singular**, com **mandato escrito** e **comunicada ao CNCS** via MyCiber. A pessoa pode acumular outras funções no SMAS, mas tem de ter **independência funcional** face à cadeia operacional.

## Análise de risco — uso da matriz sectorial

| Peça | Forma | Base |
|---|---|---|
| ☐ **(SMAS) Matriz de risco preenchida com cenários do Anexo II do Aviso** | Folha Excel sectorial | *art. 28.º do Aviso*{:.legal} + Anexo II |
| ☐ **(SMAS) Análise específica para sistemas OT** (SCADA, telemetria, bombagem) | Documento separado | Boa prática sectorial |
| ☐ **(SMAS) Aceitação de risco residual** assinada pelo conselho de administração | Documento formal | *art. 29.º RJC*{:.legal} |
| ☐ **(SMAS) Revisão da matriz após incidente** (mesmo não-significativo) | Acta de revisão | *art. 31.º do Aviso*{:.legal} |

**Template específico**: [`matriz-risco-setor-agua-potavel-nis2.xlsx`]({{ '/templates/matriz-risco-setor-agua-potavel-nis2.xlsx' | relative_url }}).

## Inventário de activos com componente OT

| Peça | Forma | Notas |
|---|---|---|
| ☐ **(SMAS) Inventário separado de activos OT** | Folha Excel | SCADA, PLCs, sensores telemetria, equipamentos de bombagem, válvulas controladas, contadores inteligentes |
| ☐ **(SMAS) Mapa de dependências OT ↔ TIC corporativa** | Diagrama | Identificar onde as duas redes se tocam (estação de gestão SCADA, exportação para tarifário, etc.) |
| ☐ **(SMAS) Lista de fornecedores OT** | Folha Excel | Distinto da lista de fornecedores TIC. Fornecedores SCADA são tipicamente especializados (Schneider, Siemens, ABB, Endress+Hauser) |

## Arquitectura de rede

| Peça | Forma | Critério |
|---|---|---|
| ☐ **(SMAS) Diagrama de segregação rede TIC ↔ rede OT** | Diagrama de rede | Sem rota directa entre TIC corporativa e OT. Ponte unidireccional (data diode) ou firewall industrial dedicado |
| ☐ **(SMAS) Política de acessos a OT** | Documento | FIDO2 obrigatório, sem acessos remotos não-controlados, jump host obrigatório |
| ☐ **(SMAS) Auditoria semestral das permissões OT** | Relatório | Para Grupo A e SMAS Substancial+ |

## Notificação de incidentes — adaptações sectoriais

| Peça | Forma | Notas |
|---|---|---|
| ☐ **(SMAS) Plano de resposta a incidentes sectorial** | Documento aprovado | Inclui cenários sectoriais: contaminação química/biológica, falha de tratamento, falha de bombagem, perda de telemetria, ataque à infra-estrutura SCADA |
| ☐ **(SMAS) Articulação com ERSAR** | Procedimento documentado | A ERSAR (Entidade Reguladora dos Serviços de Águas e Resíduos) tem competências próprias em incidentes que afectem a qualidade do serviço. Aviso paralelo ao CNCS |
| ☐ **(SMAS) Articulação com a Saúde Pública** | Procedimento documentado | Em incidentes com risco para a saúde pública (contaminação da rede), aviso à Direcção-Geral de Saúde e ARS regional |

**Template específico**: [`plano-incidentes-setor-agua-potavel-nis2.docx`]({{ '/templates/plano-incidentes-setor-agua-potavel-nis2.docx' | relative_url }}).

## Relatório anual ao CNCS

| Peça | Forma | Cadência |
|---|---|---|
| ☐ **(SMAS) Relatório anual de cumprimento** | Submetido no MyCiber | Anual, no aniversário da qualificação |
| ☐ **(SMAS) Plano de adaptação plurianual** | Documento aprovado pela administração | Anual, com revisão |
| ☐ **(SMAS) Registo de não-conformidades** identificadas em auditoria | Folha Excel | Permanente |

## Formação e sensibilização específicas

| Peça | Forma | Cadência |
|---|---|---|
| ☐ **(SMAS) Programa de formação para operadores OT** | Programa pedagógico | **Semestral** (mais frequente que para câmara) |
| ☐ **(SMAS) Exercícios de phishing simulado** ([H.EC]({% link recursos/anexo-iv-aviso-5146.md %}#h-ec)) | Relatórios | **Trimestral** |
| ☐ **(SMAS) Tabletop exercise sectorial anual** | Acta com participantes | Cenários específicos do sector — preferível com participação da ERSAR |

## Continuidade — exigências adicionais

| Peça | Forma | Notas |
|---|---|---|
| ☐ **(SMAS) Plano de continuidade com RTO/RPO sectoriais** | Documento aprovado | RTO mais apertado para serviços críticos (abastecimento de água em pressão) — tipicamente 4-12h |
| ☐ **(SMAS) Acordo de cooperação com operador vizinho** | Protocolo escrito | Em caso de falha grave, prever fornecimento em emergência através de operador adjacente |
| ☐ **(SMAS) Backup *air-gapped* obrigatório** | Configuração documentada | Para Substancial: backups imutáveis na cloud. Para Elevado: + cópia offline em cofre |
| ☐ **(SMAS) Testes de restauro mensais com cenário sectorial** | Relatórios | Inclui restauro de configurações SCADA e validação operacional |

## Supervisão *ex ante* — a diferença fundamental

A parte SMAS está sob **supervisão *ex ante*** (*art. 53.º RJC*{:.legal}) — ao contrário da câmara que está em *ex post*. Implica:

- **Inspecções programadas** pelo CNCS (anual ou bianual, conforme nível).
- **Acesso facilitado** do CNCS aos sistemas e instalações.
- **Auditoria de relatórios anuais** com possibilidade de pedidos de clarificação.
- **Avaliação periódica do nível B/S/E** atribuído.

Implicação prática: o SMAS tem de manter **postura permanente de prontidão**, ao contrário do "defensável quando solicitado" da câmara.

## Sanções — referência rápida

| Categoria SMAS | Muito graves | Graves |
|---|---|---|
| **Essencial** (Anexo III nível S) | até **10.000.000 €** (ou 2 % do volume de negócios) | até **5.000.000 €** |
| **Importante** (Anexo III nível B) | até **7.000.000 €** (ou 1,4 % do volume) | até **3.500.000 €** |

Atenção: para um SMAS com volume anual de 10-30 M€, 2 % representa 200-600 mil € — limiar superior em muitos casos.

A **dispensa de coima do *art. 65.º RJC*{:.legal}** aplica-se também aqui durante os primeiros 12 meses, mediante pedido fundamentado.

## Síntese — peças exclusivas SMAS além da checklist principal

Resumindo, em relação à checklist da câmara, o SMAS acrescenta:

1. **2 designações formais** — RC + PCP.
2. **2 documentos sectoriais** — matriz de risco do Anexo II + plano de incidentes sectorial.
3. **3 arquitecturas técnicas** — segregação TIC/OT + acesso controlado a OT + backups com nível mais alto.
4. **1 relatório anual** ao CNCS.
5. **Articulações externas** — ERSAR e Saúde Pública.
6. **Formação reforçada** — semestral para operadores OT + phishing trimestral + tabletop anual sectorial.

**Cerca de 15 peças adicionais** acima das ~15 da câmara. Total para uma autarquia em dupla qualificação: **~30 peças documentais**.

## Próximo passo

[← Voltar ao Roteiro essencial]({% link roteiro-essencial/index.md %}) · [Anexo IV — medidas O/T/H]({% link recursos/anexo-iv-aviso-5146.md %})
