---
title: "C.2 Prazos PT vs NIS2"
layout: default
parent: "C. Notificação de incidentes"
nav_order: 2
---

# C.2 Prazos PT vs NIS2

Esta é, provavelmente, **a página mais importante de todo o manual digital** — e o ponto onde mais erros se cometem na prática. Quem leu a Directiva NIS2 em inglês (a maioria das publicações jurídicas internacionais e dos materiais de fornecedores) ficou com um esquema de prazos na cabeça: **24 horas para alerta inicial, 72 horas para notificação detalhada, 1 mês para relatório final**. Esse esquema **não é o esquema português**. O DL 125/2025 transpôs com diferenças materiais. Confundi-los pode significar perder um prazo legal e cair em contraordenação.

> **Aviso prático**: tudo o que se segue refere-se ao regime do DL português. Sempre que dúvida, **olhar para o DL 125/2025, arts. 41.º a 44.º**, não para a Directiva (UE) 2022/2555.

## Tabela comparativa — lado a lado

| Fase | NIS2 Directiva (UE) 2022/2555 art. 23.º | DL 125/2025 (RJC) | Artigo PT |
|---|---|---|---|
| **Alerta inicial** | 24h após detecção | 24h após **verificação** do incidente significativo | art. 42.º, n.º 1 |
| **Detalhe técnico** | 72h notificação obrigatória | 72h **actualização facultativa** («quando necessário») | art. 42.º, n.º 3 |
| **Fim de impacto significativo** | (não existe figura específica) | 24h após cessação do impacto | art. 43.º, n.º 1 |
| **Relatório final** | 1 mês após detecção | 30 dias úteis após **fim de impacto significativo** | art. 44.º, n.º 1 |
| **Relatório intercalar** | mensal/quando solicitado | semanal se o incidente persistir > 30 dias úteis | art. 44.º, n.º 3 |
| **Resolução em 2 horas** | (n/a) | dispensa da notificação inicial — só se envia a de fim de impacto | art. 41.º, n.º 2 |

**Cinco diferenças materiais** entre as duas colunas:

1. **Marco temporal do início do relógio** — a Directiva fala em «detecção» ou «awareness» (consciência). O DL fala em **«verificação do incidente significativo»** (art. 42.º, n.º 1): o ponto em que a entidade conclui que «existe, ou possa vir a existir, um incidente significativo». A diferença é importante: detectar uma anomalia é uma coisa; concluir que é significativo é outra (mais tarde). Esta janela analítica protege contra falsos positivos, mas não pode ser esticada artificialmente — em caso de dúvida, o CNCS interpretará contra a entidade.
2. **Actualização 72h é facultativa, não obrigatória** — «quando necessário» (art. 42.º, n.º 3). Só se envia se houver informação substancialmente nova ou correcção relevante à notificação inicial. Quem segue o modelo NIS2 puro envia sempre — o que não é erro, mas é trabalho desnecessário.
3. **Figura adicional "fim de impacto significativo"** — não existe na Directiva. É **invenção do legislador português** que cria uma terceira notificação obrigatória entre a inicial e o relatório final. O relógio dos 30 dias úteis para o relatório final **só começa a contar a partir desta notificação**, não a partir da detecção.
4. **Relatório final contado em dias úteis** — 30 dias úteis, não 30 dias corridos nem «um mês». Cerca de 6 semanas de calendário em condições normais. Conta-se desde o fim de impacto, não desde a detecção.
5. **Cláusula das 2 horas** — invenção exclusivamente portuguesa (art. 41.º, n.º 2). Se o incidente foi resolvido em menos de 2 horas após a detecção, **dispensa a notificação inicial**: a entidade envia apenas a notificação de fim de impacto significativo. Útil para incidentes contidos rapidamente; tem de ser usado com critério (a contagem é desde a detecção, e o impacto significativo tem de ter terminado dentro das 2h).

## Quando começa a contar o relógio — "verificação do incidente significativo"

A pergunta que tira o sono a qualquer responsável de TIC é: **a partir de que momento começam a correr as 24h?** O art. 42.º, n.º 1 do RJC responde: «**assim que a entidade (...) concluir que existe, ou possa vir a existir, um incidente significativo, sem demora injustificada e até 24 horas após essa verificação, salvo quando tal for incompatível com a mitigação ou a resolução do incidente**».

Três elementos materiais:

- **Conclusão**, não simples detecção. A equipa TIC pode ver alertas durante horas a fim de saber se são significativos; o relógio só começa quando alguém com responsabilidade decide que sim.
- **Sem demora injustificada** — não é facultativo aguardar pelas 24h se já se sabe na 1.ª hora. A janela é um tecto, não um direito.
- **Salvo quando tal for incompatível com a mitigação** — escape muito limitado. Aplica-se a casos extremos (incidente em curso a degradar-se em tempo real, equipa toda em contenção activa). Não cobre falta de tempo administrativo.

**Boa prática operacional**: registar internamente, com timestamp, o momento da decisão de qualificação como significativo. Esse registo é a vossa defesa em caso de fiscalização.

## Critérios de "incidente significativo" (art. 40.º, n.º 3)

A definição reside no art. 40.º, n.º 3 do RJC, com cinco parâmetros indicativos:

> «A fim de determinar se um incidente tem impacto significativo (...), as entidades em causa devem ter em consideração, designadamente, os seguintes parâmetros: a) Número de utilizadores afetados pela perturbação do serviço; b) Número total de utilizadores do serviço perturbado; c) A duração do incidente; d) O nível da gravidade da perturbação do funcionamento do serviço; e) A dimensão do impacto nas atividades económicas e sociais.»

Traduzido para uma autarquia, e na ausência ainda de **instrução técnica do CNCS** que fixe limiares numéricos (anunciada no art. 40.º, n.º 4 — pendente em Maio de 2026), recomendamos o seguinte conjunto de critérios práticos. Considere-se **incidente significativo** quando:

- **Mais de 4 horas** de indisponibilidade total de serviço público crítico (portal do munícipe, balcão único, sistema de licenciamento, contabilidade, e-mail institucional, atendimento ao público); **ou**
- **Comprometimento de dados pessoais** de munícipes/trabalhadores (acesso, exfiltração, alteração ou eliminação não autorizada); **ou**
- **Acesso não autorizado** confirmado a sistemas que suportam o exercício de poderes de autoridade pública (gestão urbanística, fiscalização, sistemas tributários); **ou**
- **Cifragem por ransomware** de servidores ou bases de dados, independentemente da duração; **ou**
- **Activação de exigência de resgate** ou contacto de extorsão; **ou**
- **Comprometimento da identidade institucional** (e-mail de presidente, conta oficial em redes sociais, página institucional desfigurada); **ou**
- **Impacto financeiro** estimado superior a 10.000 € (orçamento corrente) ou que afecte processos de receita/despesa em curso.

Este é um patamar **conservador**. Em caso de dúvida, **notificar**: o art. 40.º, n.º 2 do RJC garante que «o cumprimento da mera notificação não gera responsabilidade acrescida para a entidade notificante», e a notificação tardia configura contraordenação grave (art. 62.º).

## Sidebar — dupla qualificação

Para autarquias com **SMAS ou empresa municipal essencial**, os prazos são **exactamente os mesmos** (arts. 42.º a 44.º aplicam-se transversalmente). A diferença está noutro lado:

- **Canal único**: a plataforma electrónica do CNCS (art. 8.º, n.º 7 do RJC + art. 20.º do Aviso) — mas a entidade essencial **e** a entidade pública relevante submetem **notificações separadas** se ambas forem afectadas pelo mesmo incidente. Uma só pessoa pode submeter as duas (com autenticação na área reservada de cada qualificação), mas conceptualmente são reports distintos.
- **Critério de "significativo" mais apertado** para a parte essencial — o sector águas tem instruções técnicas próprias do CNCS (em desenvolvimento) que podem baixar o limiar.
- **Plano de Resposta a Incidentes formal exigido** pelo Anexo III GR.PL-2 (Plano de Resposta a Incidentes) — ver [C.1]({% link 02-notificacao-incidentes/c1-plano-resposta.md %}).

## Folha-resumo dos prazos (PDF imprimível)

A folha-resumo "Prazos PT vs NIS2" será disponibilizada como **PDF descarregável** antes do bloco C (formato A4 colorido, pronto a imprimir). Contém esta tabela em formato compacto, mais o telefone e o e-mail de emergência do CNCS. **Recomenda-se imprimir e afixar no gabinete TIC** — é a peça que mais difícil é ler de cabeça quando o incidente está em curso.

## Templates aplicáveis

Esta página é principalmente conceptual; os templates relevantes estão na página seguinte ([C.3]({% link 02-notificacao-incidentes/c3-conteudo-notificacao.md %})). Notar:

| Template | Grupo / Etiqueta | Notas |
|---|---|---|
| [`registo-incidentes-nis2.xlsx`]({{ '/templates/registo-incidentes-nis2.xlsx' | relative_url }}) | Aplicar | Registo interno de incidentes — com colunas para horas-chave: detecção, verificação significativa (início do relógio), notificação inicial submetida, fim de impacto, relatório final. Permite demonstrar cumprimento dos prazos. |

## Próximo passo

[C.3 Conteúdo de cada notificação →]({% link 02-notificacao-incidentes/c3-conteudo-notificacao.md %})
