---
title: "E.2.1 Auto-avaliação QNRCS"
layout: default
parent: "E. Supervisão e roadmap"
nav_order: 2.5
---

# E.2.1 Auto-avaliação de maturidade QNRCS v2

{: .note }
> **Grupo A** = autarquia com ≥ 250 trabalhadores  
> **Grupo B** = autarquia com 75-249 trabalhadores  
> (art. 7.º RJC — ver [A.2 Quem está abrangido]({% link 00-enquadramento/a2-quem-esta-abrangido.md %}))

**Duração**: ~10 min na sessão · ~2h em câmara (em equipa) · **Base legal**: art. 23.º + Anexo I do Aviso 5146/2026/2.

O QNRCS v2 (ver [Recursos / QNRCS v2]({% link recursos/qnrcs.md %})) é o referencial obrigatório aprovado pelo Anexo I do Aviso. Mas para uma câmara, ler o referencial não basta — é preciso **medir onde se está**. Esta sub-página apresenta um instrumento prático de auto-avaliação que cobre **26 controlos seleccionados** dos ~107 totais do QNRCS v2, alinhados com as medidas do Anexo IV para Grupo A/B.

O instrumento produz, em ~2 horas de trabalho em equipa, um **perfil de maturidade da câmara** com gráfico radar nos 6 objetivos do QNRCS v2 e uma lista de controlos em défice que alimenta diretamente o roadmap dos 6 meses ([E.3]({% link 04-supervisao-roadmap/e3-roadmap-6-meses.md %})).

## Porquê auto-avaliar

1. **Operacionaliza o regime.** Sai-se da fase "ler o regime" para "medir a entidade". Evidência concreta em mãos.
2. **Alimenta o roadmap E.3.** Os controlos com pontuação mais baixa tornam-se prioridades automáticas.
3. **Cria evidência documental.** Demonstra diligência na adaptação ao regime (relevante para o art. 65.º — dispensa de coima exige mérito demonstrado, não declaração tardia).
4. **Compara entidades e momentos.** Câmara pode comparar a sua maturidade com benchmark interno (ano após ano) ou — anonimamente — com outras autarquias.

## O instrumento

📥 **[`avaliacao-maturidade-qnrcs.xlsx`]({{ '/templates/avaliacao-maturidade-qnrcs.xlsx' | relative_url }})** — Excel protegido com password (mesma do resto dos templates, comunicada em sessão).

**Estrutura:**

| Aba | Conteúdo |
|---|---|
| **Instruções** | Guia de preenchimento (~1 página A4) |
| **GR** — Gerir | 6 controlos · contexto, estratégia, funções, políticas, supervisão, cadeia |
| **ID** — Identificar | 4 controlos · ativos + risco + melhoria contínua |
| **PR** — Proteger | 7 controlos · identidades, formação, dados, plataformas, infra |
| **DE** — Detetar | 3 controlos · monitorização + anomalias |
| **RS** — Responder | 4 controlos · gestão, análise, notificação, mitigação |
| **RC** — Recuperar | 2 controlos · plano + comunicação |
| **Dashboard** | Resumo tabular + gráfico radar + recomendações |

**Total: 26 controlos.** Cada controlo testa-se contra o **nível Básico** (mínimo Grupo B). Câmaras com SMAS qualificado podem usar o mesmo instrumento aspirando a Substancial nas medidas correspondentes do Anexo III.

## Como preencher — cronograma sugerido

**Sessão 1 (1h, em câmara, equipa de 3 pessoas — TIC, DPO, RH/jurídico):**

- **00:00-00:15** — Kick-off. Apresentar instrumento à equipa, ler aba "Instruções", esclarecer dúvidas.
- **00:15-00:55** — Preenchimento conjunto das 6 abas. Para cada controlo, decidir em equipa:
  - **Coluna C — Estado atual**: Não / Parcial / Sim.
  - **Coluna D — Nível atingido**: Não cumpre / Básico / Substancial / Elevado (cumulativo).
  - **Coluna G — Evidência existente**: documento, template, registo. Obrigatório se C=Sim.
- **00:55-01:00** — Sair com 5-10 evidências em falta para procurar/produzir antes da sessão 2.

**Trabalho intercalar (~3-5 dias):**

- Cada membro procura/produz as evidências em falta na sua área.
- TIC valida coluna G com prints, configurações ou referências a templates já preenchidos.

**Sessão 2 (45 min, em câmara, mesma equipa):**

- **00:00-00:30** — Consolidar respostas, fechar evidências, refinar coluna D (níveis B/S/E).
- **00:30-00:40** — Ir à aba Dashboard. Ler o gráfico radar. Identificar os 2-3 objetivos com maturidade mais baixa.
- **00:40-00:45** — Listar os controlos individuais marcados como "Não" — são candidatos diretos ao roadmap E.3.

## Interpretação do dashboard

O dashboard mostra:

- **Tabela resumo** — 6 linhas, uma por objetivo, com totais Sim/Parcial/Não + % maturidade calculada.
- **% Maturidade** — fórmula `(Sim × 1.0 + Parcial × 0.5) / Total`. Varia entre 0% (nada cumprido) e 100% (todos os controlos do objetivo cumpridos).
- **Gráfico radar** — visualização dos 6 objetivos. Áreas "afundadas" são as prioridades.
- **Recomendação** — caixa amarela com a regra geral: priorizar para o roadmap os controlos "Não" com mapeamento Anexo IV.

**Leitura típica de uma câmara em fase inicial:**

- **Proteger** tende a estar mais alto (MFA, antivirus, backups existem, ainda que parcialmente).
- **Gerir** tende a estar mais baixo (faltam políticas escritas, actas, supervisão formal).
- **Detetar / Responder / Recuperar** dependem muito de existir plano de resposta documentado.

A leitura mais útil **não é a média global** — é o **objetivo mais baixo**. Esse é o que entra primeiro no roadmap.

## Como alimenta o roadmap E.3

Os controlos marcados como **"Não"** com **Mapeamento Anexo IV não-vazio** são candidatos imediatos a entradas do roadmap dos 6 meses ([E.3]({% link 04-supervisao-roadmap/e3-roadmap-6-meses.md %})). Regra prática:

1. **Listar os "Nãos"** com Mapeamento Anexo IV (campo E do Excel).
2. **Ordenar por prioridade** — controlos do objetivo Gerir (políticas, funções) e do objetivo Identificar (inventário, risco) costumam vir antes, porque servem de base aos restantes.
3. **Cada controlo torna-se uma entrada do roadmap** com responsável, prazo (mês 1 / 2 / 3 / 4 / 5 / 6) e output esperado (documento, registo, configuração).

Exemplo — se a câmara marcar `GR.PP-1` (políticas) como "Não" e `ID.GA-1` (inventário) como "Parcial":

- Mês 1: aprovar despacho com política de cibersegurança (`GR.PP-1`).
- Mês 2: completar inventário de ativos críticos (`ID.GA-1` → "Sim"), usando o template adequado da página [Templates]({% link recursos/templates.md %}).

## Periodicidade

A auto-avaliação **repete-se anualmente**, em paralelo com a revisão do [dossier mínimo de conformidade]({% link 04-supervisao-roadmap/e2-documentacao-minima.md %}). Guardar a fotografia de cada ano dá uma curva de progressão — útil internamente para a câmara e como evidência defensável em supervisão *ex post*.

## Versão completa (opcional, 107 controlos)

Para câmaras com maturidade alta, Grupo A, ou com SMAS qualificado como entidade essencial, existe uma **versão completa** do instrumento que cobre os 107 controlos do QNRCS v2 (em vez dos 26 seleccionados):

📥 **[`avaliacao-maturidade-qnrcs-completa.xlsx`]({{ '/templates/avaliacao-maturidade-qnrcs-completa.xlsx' | relative_url }})** — versão integral, mesma estrutura (6 abas + dashboard), com coluna "Estado" a aceitar também `N/A` (não aplicável) para controlos fora do escopo Grupo B. Mapeamento Anexo IV é explícito nos 26 controlos do Excel reduzido e heurístico (por categoria) nos restantes 81. Tempo de preenchimento estimado: **6-8h em equipa** (vs. ~2h da versão reduzida).

**Recomendação:** começar pela versão reduzida. Avançar para a completa apenas depois de ter os 26 controlos mapeados e querer aprofundar.

## Templates aplicáveis

| Template | Etiqueta | Notas |
|---|---|---|
| [`avaliacao-maturidade-qnrcs.xlsx`]({{ '/templates/avaliacao-maturidade-qnrcs.xlsx' | relative_url }}) | **Aplicar — Grupo B e A** | Instrumento de auto-avaliação reduzido (26 controlos). Password comunicada em sessão. |
| [`avaliacao-maturidade-qnrcs-completa.xlsx`]({{ '/templates/avaliacao-maturidade-qnrcs-completa.xlsx' | relative_url }}) | Referência — Grupo A · SMAS | Versão completa (107 controlos). Opcional. |

## Ver também

- [Recursos / QNRCS v2]({% link recursos/qnrcs.md %}) — explicação completa do referencial.
- [E.2 Documentação mínima]({% link 04-supervisao-roadmap/e2-documentacao-minima.md %}) — onde a auto-avaliação se inclui como uma das peças do dossier.
- [E.3 Roadmap 6 meses]({% link 04-supervisao-roadmap/e3-roadmap-6-meses.md %}) — destino natural dos controlos em défice.

## Próximo passo

[E.3 Roadmap 6 meses →]({% link 04-supervisao-roadmap/e3-roadmap-6-meses.md %})
