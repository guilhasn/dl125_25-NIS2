---
title: "Anexo III vs Anexo IV"
layout: default
parent: "Roteiro essencial (dupla qualificação)"
nav_order: 2
---

# Anexo III vs Anexo IV — comparação

{: .note }
> **Grupo A** = autarquia com ≥ 250 trabalhadores  
> **Grupo B** = autarquia com 75-249 trabalhadores  
> (art. 7.º RJC — ver [A.2 Quem está abrangido]({% link 00-enquadramento/a2-quem-esta-abrangido.md %}))

O Aviso 5146/2026/2 tem **dois anexos** de medidas:

- **Anexo III** — para **entidades essenciais e importantes**. Mais detalhado, com **três níveis de exigência**: Básico (B), Substancial (S), Elevado (E).
- **Anexo IV** — para **entidades públicas relevantes** (Grupo A e B). Lista das 27 medidas O/T/H aplicáveis a autarquias. Ver [Anexo IV — medidas O/T/H]({% link recursos/anexo-iv-aviso-5146.md %}).

Esta página compara os dois lado-a-lado para ajudar entidades em dupla qualificação a perceber o que **acumula** quando a parte essencial entra em jogo.

## Estrutura dos dois anexos

| Dimensão | Anexo III (essenciais/importantes) | Anexo IV (públicas relevantes) |
|---|---|---|
| Nº de medidas | ~40-50 medidas | 27 medidas |
| Granularidade | 3 níveis (B / S / E) por medida | 2 grupos (A / B) cumulativos |
| Famílias | O · T · H (mesma estrutura) | O · T · H (mesma estrutura) |
| Análise de risco | Medida explícita + matriz Anexo II | **Não enumerada explicitamente** — emerge do inventário |
| Plano de continuidade | Medida formal obrigatória | Implícita via medida [T.CS]({% link recursos/anexo-iv-aviso-5146.md %}#t-cs) |
| Auditoria externa | Recomendada (essenciais E) | Não exigida |
| RC + PCP designados | **Obrigatório** (arts. 31.º/32.º RJC) | Não exigido (apenas ponto de contacto leve) |

## Como se decide o nível B/S/E para essenciais?

O CNCS atribui o nível em função do **sector** e **dimensão** da entidade. Indicação geral:

| Nível | Aplicabilidade típica |
|---|---|
| **Básico (B)** | Entidades importantes; entidades essenciais de menor dimensão (50-100 trabalhadores). |
| **Substancial (S)** | Entidades essenciais médias (100-250 trabalhadores). SMAS multimunicipais. |
| **Elevado (E)** | Entidades essenciais críticas para o país: grandes operadores energéticos, operadores nacionais de água, transportadores ferroviários, infraestruturas digitais críticas. **Raríssimo** em SMAS municipal. |

Para um **SMAS de uma câmara média** (50-150 trabalhadores), o nível tipicamente atribuído é **Básico ou Substancial**. Para um **SMAS grande de capital** (Lisboa, Porto), pode chegar a **Substancial**.

## Mapa medida-a-medida — o que muda no SMAS face à câmara

A tabela seguinte mostra, para cada medida do Anexo IV (regime câmara), **o que muda** quando o regime aplicável é o Anexo III (regime SMAS essencial).

### O — Organizacionais

| Anexo IV (câmara) | Anexo III (SMAS essencial) | Δ |
|---|---|---|
| [O.CRI]({% link recursos/anexo-iv-aviso-5146.md %}#o-cri) — Ponto de contacto leve | RC formal designado (*art. 31.º RJC*{:.legal}) + PCP 24/7 (*art. 32.º RJC*{:.legal}) | **+ Formalização** |
| [O.PCN]({% link recursos/anexo-iv-aviso-5146.md %}#o-pcn) — PCN | PCN sectorial específico + BCP testado anualmente | **+ Periodicidade** |
| [O.PSF]({% link recursos/anexo-iv-aviso-5146.md %}#o-psf) — Inventário + contactos fornecedores | *art. 28.º RJC*{:.legal} integral — critérios de aceitação + monitorização contínua | **+ Cadeia** |
| [O.IAC]({% link recursos/anexo-iv-aviso-5146.md %}#o-iac) — Inventário activos críticos | Inventário **completo** incluindo OT (SCADA, telemetria) | **+ OT** |
| O.ID (só Grupo A no IV) | Identificação funções críticas — sempre obrigatória | **Sempre** |
| O.PSI (só Grupo A no IV) | Política classificação informação — sempre obrigatória | **Sempre** |
| (sem equivalente directo) | Política de gestão de crises (separada do plano de incidentes) | **Nova** |
| (sem equivalente directo) | Política de continuidade da actividade (BCM) | **Nova** |

### T — Técnicas

| Anexo IV (câmara) | Anexo III (SMAS essencial) | Δ |
|---|---|---|
| [T.AM]({% link recursos/anexo-iv-aviso-5146.md %}#t-am) — MFA acessos administrativos | MFA para **todos** os utilizadores; FIDO2 para SCADA | **+ Universalidade** |
| [T.CS]({% link recursos/anexo-iv-aviso-5146.md %}#t-cs) — Cópias de segurança | Backups mensais (B) → semanais (S) → diários (E); teste mensal; air-gap obrigatório | **+ Frequência** |
| [T.AR]({% link recursos/anexo-iv-aviso-5146.md %}#t-ar) — Acesso remoto seguro | Bastion host + zero trust para acesso a OT | **+ Arquitectura** |
| T.PEW — SPF/DKIM/DMARC | + DNSSEC + DANE + cabeçalhos HTTP de segurança completos | **+ Profundidade** |
| (sem equivalente directo no IV) | **Segregação rede TIC ↔ rede OT** — exigência arquitectural específica para água/SCADA | **Nova** |
| (sem equivalente directo no IV) | **Recolha centralizada de logs** (SIEM) com correlação | **Nova** |
| (sem equivalente directo no IV) | **Threat Intelligence** sectorial (subscrição feeds CNCS + sectoriais) | **Nova** |

### H — Humanas

| Anexo IV (câmara) | Anexo III (SMAS essencial) | Δ |
|---|---|---|
| [H.PF]({% link recursos/anexo-iv-aviso-5146.md %}#h-pf) — Formação anual | Formação **semestral** + formação específica OT/SCADA para operadores | **+ Periodicidade** |
| H.FIC — Onboarding/refresher | Idem + certificação obrigatória dos formadores (sectorial) | **+ Certificação** |
| H.EC — Phishing simulado (só A no IV) | Phishing simulado **trimestral** + exercícios de resposta a incidentes (tabletop) **anuais** | **+ Frequência** |

## O que acumula em dupla qualificação

Quando uma autarquia tem dupla qualificação (câmara Grupo B + SMAS essencial), o conjunto de obrigações **acumula**, mas **não duplica**. Cada entidade cumpre o seu regime; algumas peças partilham-se naturalmente.

### Peças que se partilham (com adaptação)

- **Política de segurança da informação** — comum, com secções específicas para parte SMAS.
- **Política de palavras-passe** — comum, com excepções para SCADA (geralmente mais restritiva).
- **Plano de formação anual** — comum, com módulos específicos para operadores OT.
- **Inventário de fornecedores TIC** — pode ser conjunto, marcando quais fornecedores servem cada entidade.
- **DPO** — pode ser o mesmo para câmara e SMAS, com mandato distinto formalizado.

### Peças que **não** se partilham

- **Inventário de activos** — separado: parte câmara (TIC corporativa) e parte SMAS (TIC + OT).
- **Matriz de risco** — separadas (a parte SMAS usa a matriz do Anexo II do Aviso, sectorial).
- **Plano de resposta a incidentes** — separados, com matrizes de escalação próprias.
- **Plano de continuidade** — separados, com cenários próprios (parte SMAS inclui falha de bombagem, contaminação da rede de águas, falha de telemetria).
- **Notificações de incidentes** — sempre separadas (cada entidade notifica em seu nome).
- **Registo no MyCiber** — sempre separados.

### Peças exclusivas da parte SMAS

- **Designação formal do RC** (*art. 31.º RJC*{:.legal}).
- **Designação formal do PCP** (*art. 32.º RJC*{:.legal}).
- **Relatório anual** ao CNCS.
- **Matriz de risco do Anexo II** preenchida.
- **Plano de continuidade sectorial** (águas) — articulado com a ERSAR.
- **Procedimentos OT/SCADA** documentados e auditados.

## Aceder ao texto completo dos Anexos

- **Anexo III completo**: [`legislacao-aviso-5146.md`#anexo-iii]({% link recursos/legislacao-aviso-5146.md %}#anexo-iii-aviso) — sumário com remissão para o DRE.
- **Anexo IV completo** (medidas para autarquias): [`recursos/anexo-iv-aviso-5146.md`]({% link recursos/anexo-iv-aviso-5146.md %}) — todas as 27 medidas com paráfrases e remissão a páginas do manual digital.

## Templates específicos para SMAS

Os templates da biblioteca relevantes para a parte essencial:

- [`matriz-risco-setor-agua-potavel-nis2.xlsx`]({{ '/templates/matriz-risco-setor-agua-potavel-nis2.xlsx' | relative_url }}) — matriz pré-preenchida com cenários do sector águas.
- [`checklist-setor-agua-potavel-nis2.docx`]({{ '/templates/checklist-setor-agua-potavel-nis2.docx' | relative_url }}) — checklist de conformidade para SMAS.
- [`plano-incidentes-setor-agua-potavel-nis2.docx`]({{ '/templates/plano-incidentes-setor-agua-potavel-nis2.docx' | relative_url }}) — plano de incidentes específico águas.

## Próximo passo

[Checklist específica SMAS →]({% link roteiro-essencial/smas-checklist.md %})
