---
title: "A.2 Quem está abrangido"
layout: default
parent: "A. Enquadramento legal"
nav_order: 2
---

# A.2 Quem está abrangido

A pergunta nuclear de qualquer dirigente municipal ao ler o DL 125/2025 é simples: **"isto aplica-se à minha autarquia?"**. A resposta tem duas dimensões — **categoria** e **dimensão** — e em algumas autarquias multiplica-se (**dupla qualificação**). Esta página resolve a primeira pergunta e prepara o terreno para o **Exercício A1**, em que cada par vai classificar a sua própria entidade.

## O que a lei diz

> «O presente regime é aplicável (...) **à administração autónoma**.» — art. 3.º, n.º 3, al. e) do RJC (anexo ao DL 125/2025)

> «As entidades públicas relevantes referidas no n.º 1 (...) são classificadas em dois grupos, em função do número de trabalhadores: a) **Grupo A**: 250 ou mais trabalhadores; b) **Grupo B**: entre 75 e 249 trabalhadores.» — art. 7.º do RJC (paráfrase fiel)

O critério é o **número de trabalhadores no quadro de pessoal** da entidade. Não é o orçamento, não é a população do concelho, não é o número de freguesias. É o **headcount** da própria entidade.

### "Administração autónoma" — desambiguação

Este é o conceito que desconcerta: **nenhum dos dois diplomas usa as palavras "autarquia local"**. As autarquias caem na categoria de "**administração autónoma**" (art. 3.º, n.º 3, al. e) do RJC), que abrange três famílias:

- **Autarquias locais** (câmaras, juntas de freguesia) e seus serviços municipalizados.
- **Ordens profissionais** e associações públicas profissionais.
- **Universidades públicas** e outros institutos de ensino superior públicos.

Quando virem documentos ou notícias sobre a "administração autónoma" no contexto da NIS2, é deste grupo que se está a falar — e estão lá vocês.

## A vossa autarquia é uma "entidade pública relevante"

Esta é a primeira conclusão importante: **as autarquias são entidades públicas relevantes** (Grupo A ou Grupo B), **não entidades essenciais nem importantes** (as duas categorias mais exigentes do regime).

A consequência prática é decisiva:

| Categoria | Regime de obrigações | Regulamentação técnica |
|---|---|---|
| Entidade essencial | arts. 26.º–32.º do RJC | Anexo III do Aviso (níveis B/S/E) |
| Entidade importante | arts. 26.º–32.º do RJC (mais leves) | Anexo III do Aviso |
| **Entidade pública relevante** | **art. 33.º do RJC** | **Anexo IV do Aviso (Grupo A/B)** |

**Não tentem aplicar os arts. 26.º a 32.º a uma autarquia**. Esses artigos exigem coisas que a lei especificamente **não pede** a uma entidade pública relevante: um Responsável de Cibersegurança formalmente designado nos termos do art. 31.º, um Ponto de Contacto Permanente nos termos do art. 32.º, ou as 9 alíneas de medidas técnicas do art. 27.º. Mais à frente (Bloco B) veremos que **alguma coisa muito parecida** aparece no Anexo IV — mas a fonte legal e o grau de exigência são diferentes. Aplicar acriticamente templates desenhados para essenciais cria **sobre-conformidade**, que é dispendiosa e desnecessária.

## Árvore de decisão — Grupo A, Grupo B, ou fora?

Para a entidade-câmara (a entidade jurídica "Município de XPTO"):

```
Número de trabalhadores no quadro de pessoal?
│
├── ≥ 250
│   └── GRUPO A — entidade pública relevante
│       (ex.: grandes câmaras: Porto, Lisboa, Cascais, Sintra, Loures,
│        Coimbra, Braga, ...)
│
├── 75–249
│   └── GRUPO B — entidade pública relevante
│       (a maior parte das câmaras médias portuguesas)
│
└── < 75
    └── FORA DO REGIME OBRIGATÓRIO
        (muitas câmaras pequenas, juntas de freguesia)
        Recomendação CNCS: adoptar o QNRCS de forma voluntária.
```

**Nota sobre "fora do regime obrigatório"**: não é sinónimo de "não tem de fazer nada". O CNCS pode, por decisão fundamentada, qualificar uma entidade abaixo do limiar (art. 8.º, n.º 3 do RJC). Além disso, uma autarquia pequena que opere serviços críticos (ver dupla qualificação abaixo) cai nas exigências dessa actividade, independentemente do seu próprio Grupo.

## Dupla qualificação — quando uma autarquia tem dois chapéus

Esta é a parte menos óbvia e a que com mais frequência é mal interpretada. A **mesma autarquia** pode qualificar simultaneamente em **duas categorias diferentes**, com **dois conjuntos cumuláveis de obrigações**:

- A **câmara** em si (entidade central, com o seu quadro de pessoal): entidade pública relevante (Grupo A ou B).
- Um **serviço municipalizado** (SMAS) ou uma **empresa municipal** que opere um sector listado no Anexo I ou II do DL: entidade **essencial** ou **importante**, conforme dimensão e natureza do serviço.

Os sectores Anexo I (essenciais) que com mais frequência aparecem em autarquias:

- **Água potável** (operadores de abastecimento público).
- **Águas residuais**.
- **Gestão de serviços TIC B2B** (raro mas possível — empresa municipal de informática que presta serviço a outras entidades).
- **Transportes** (empresas municipais de transportes urbanos).

Os sectores Anexo II (importantes) com presença autárquica:

- **Resíduos** (empresas municipais de gestão de resíduos sólidos urbanos).

### Exemplo hipotético

Numa autarquia média tipo, com:

- Câmara Municipal com **180 trabalhadores** → **Grupo B** (entidade pública relevante).
- SMAS de Águas com **80 trabalhadores**, a operar abastecimento e tratamento de águas residuais → **potencialmente entidade essencial** (sector Anexo I).
- Empresa Municipal de Resíduos com **45 trabalhadores** → **potencialmente entidade importante** (sector Anexo II).

Esta autarquia tem **três qualificações distintas** e três cadernos de encargos parcialmente sobrepostos:

| Entidade operacional | Categoria | Regime | Regulamento técnico |
|---|---|---|---|
| Câmara Municipal | Pública relevante Grupo B | art. 33.º | Anexo IV — 14 medidas Grupo B |
| SMAS | Essencial | arts. 26.º–32.º | Anexo III, nível B/S/E |
| EM Resíduos | Importante | arts. 26.º–32.º (regime aliviado) | Anexo III |

As obrigações **acumulam**: a câmara é entidade pública relevante **e** dona/tutela da entidade essencial. As notificações de incidentes, os pedidos de qualificação, as auditorias, são feitos **por cada entidade operacional** distinta, ainda que na mesma plataforma electrónica do CNCS.

### Excepção qualificadora rara (art. 6.º, n.º 1, al. d) do RJC)

Há ainda uma porta aberta para que o CNCS qualifique uma autarquia como **entidade essencial**, mesmo sem operar sector Anexo I, se prestar "serviços nas áreas do desenvolvimento, manutenção e gestão de infraestruturas de TIC ou apresentar um grau particularmente elevado de integração digital na prestação dos seus serviços". Caso raro, decisão fundamentada do CNCS (art. 8.º, n.os 3-4). Sinalizar, mas não dimensionar a estratégia em função desta hipótese improvável.

## Pré-trabalho — informação que deveriam ter convosco

Para fazer o Exercício A1 com proveito, cada par precisa de ter à mão:

1. **Número de trabalhadores actuais do quadro de pessoal** da câmara (recursos humanos sabe).
2. **Lista completa das entidades operacionais autónomas** dependentes ou tuteladas pela câmara: SMAS, empresas municipais (EM, EIM), fundações municipais, agrupamentos.
3. **Número de trabalhadores de cada uma dessas entidades**.
4. **Sectores de actividade** dessas entidades (água, resíduos, transportes, cultura, desporto, etc.).

Se não trouxeram estes dados, façam o exercício com aproximações e completem na semana seguinte. **O importante é sair daqui com um inventário de qualificações e o caminho de obrigações claro para cada uma.**

## Templates aplicáveis

| Template | Etiqueta | Notas |
|---|---|---|
| `WS1_v2_Classificacao_Obrigacoes_H1_ComLegislacao.docx` | Aplicar tal-qual | Worksheet do exercício A1. Download disponível a partir de 8 Junho. |
| `avaliacao-maturidade-nis2.xlsx` | Adaptar Grupo A/B | Autodiagnóstico inicial. Download disponível a partir de 8 Junho. |
| `gap-analysis-nis2.xlsx` | Adaptar Grupo A/B | Comparação entre estado actual e Anexo IV. Download disponível a partir de 8 Junho. |

## Próximo passo

- [Exercício A1 — Classificação da vossa autarquia →]({% link exercicios/a1-classificacao.md %})
- Para quem identificou dupla qualificação: [Trilho essencial →]({% link trilho-essencial/index.md %})
- [A.3 Plataforma electrónica do CNCS →]({% link 00-enquadramento/a3-plataforma-cncs.md %})
