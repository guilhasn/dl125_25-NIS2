---
title: "B.2 Análise e gestão de risco"
layout: default
parent: "B. Art. 27.º — Risco e ativos"
nav_order: 2
---

# B.2 Análise e gestão de risco

{: .note }
> **Grupo A** = autarquia com ≥ 250 trabalhadores  
> **Grupo B** = autarquia com 75-249 trabalhadores  
> (art. 7.º RJC — ver [A.2 Quem está abrangido]({% link 00-enquadramento/a2-quem-esta-abrangido.md %}))

{: .highlight }
> 📚 **Recurso CNCS complementar:** o CNCS publica o [**Guia para Gestão dos Riscos em Cibersegurança**](https://cncs.gov.pt/pt/gestao-de-risco/){:target="_blank"} — documento técnico oficial com metodologia detalhada por fases. Útil para aprofundar depois desta sessão. Ver também [Recursos do CNCS]({% link recursos/cncs.md %}).

Este é **o coração do Bloco B**. Quarenta e cinco minutos de exposição porque é aqui que se decide se a vossa autarquia tem uma postura defensável perante o CNCS ou apenas uma colecção de boas intenções. A análise de risco é o instrumento que **organiza todas as outras decisões** — qual o fornecedor mais crítico, que sistema merece backup duplicado, onde aplicar MFA primeiro, que formação é prioritária. Sem análise de risco, todas as escolhas a seguir são arbitrárias.

A subtileza para uma autarquia é esta: ao contrário do que acontece com entidades essenciais — que têm um artigo (o 26.º) e um anexo (o Anexo II do Aviso) integralmente dedicados ao tema —, **o Anexo IV não tem uma medida explícita "análise de risco"**. A gestão de risco para o Grupo B e Grupo A emerge **transversalmente** das medidas O, sobretudo do inventário de activos críticos. Esta página explica como construir, mesmo sem essa medida explícita, um processo de gestão de risco proporcional, documentado e defensável.

## O que a lei diz

O conjunto de normas relevante distribui-se por cinco artigos, três do DL e dois do Aviso:

> «As entidades essenciais e importantes são responsáveis por garantir a segurança das redes e dos sistemas de informação, tomando as medidas técnicas, operacionais e organizativas adequadas para gerir os riscos que se colocam à segurança das redes e dos sistemas de informação (...). As medidas (...) devem basear-se numa abordagem sistémica que abranja todos os riscos para as entidades (...).» — art. 26.º, n.os 1 e 2 do RJC

> «As medidas de ciberseguranca a adotar pelas entidades essenciais e importantes, tendo em consideração a matriz de risco em que estiverem inseridas (...), abrangem, designadamente, as seguintes áreas: a) Tratamento de incidentes (...).» — art. 27.º, n.º 1, al. a) do RJC

> «As entidades essenciais e importantes devem realizar uma análise e gestão de riscos em relação a todos os ativos que garantam a continuidade do funcionamento das redes e sistemas de informação que utilizam (...). Com base na análise (...), as entidades essenciais e importantes devem adotar as medidas de ciberseguranca adequadas e proporcionais (...). As entidades essenciais e importantes devem documentar a preparação, a execução e a apresentação dos resultados da análise dos riscos.» — art. 29.º, n.os 1-3 do RJC (gestão do risco residual)

> «A matriz de risco, aprovada no presente regulamento e constante do Anexo II, é o quadro referencial que estabelece os valores de risco para o conjunto de cenários de risco que recaem sobre um setor e subsetor de atividade (...). A matriz de risco é aplicável às entidades essenciais e importantes (...).» — arts. 28.º, n.º 1 e 29.º do Aviso 5146/2026/2

> «As entidades essenciais e importantes realizam a análise do risco residual com a seguinte periodicidade: a) Durante o planeamento e introdução de alteração ou substituição a ativo ou ativos (...). Após a ocorrência de um incidente com impacto significativo (...); b) Após a notificação, por parte do CNCS, de um risco, de uma ameaça ou de uma vulnerabilidade emergente (...).» — art. 31.º, n.º 2 do Aviso 5146/2026/2

**Constatação**: os arts. 26.º, 27.º, 29.º RJC e os arts. 28.º e 31.º Aviso dirigem-se literalmente **a entidades essenciais e importantes**. Para autarquias, o art. 33.º remete a definição das medidas para o regulamento — e o regulamento (Anexo IV) **não enumera uma medida "análise de risco" para Grupo B**. Há duas leituras possíveis: ou (i) a omissão é deliberada e o legislador entende que para autarquias basta o inventário de activos e a identificação de dependências; ou (ii) a omissão é uma lacuna que poderá vir a ser corrigida na versão final do Aviso (a consulta pública terminou em 22 de Abril de 2026; a versão final está em redacção pelo CNCS). Recomendamos tratar o tema **como se a análise de risco fosse exigida** — porque é metodologicamente impossível cumprir as restantes medidas do Anexo IV sem ela, e porque qualquer auditoria sensata vai pedi-la.

## Tradução para Grupo B — três requisitos mínimos

Para uma autarquia de Grupo B, a gestão de risco materializa-se em **três entregáveis** mínimos, todos cobríveis em ficheiros simples (uma folha Excel é suficiente):

1. **Inventário dos activos críticos** — Anexo IV medida [<abbr title="Inventariação de Activos Críticos">**O.IAC**</abbr>]({% link recursos/anexo-iv-aviso-5146.md %}#o-iac). Lista dos sistemas, equipamentos e aplicações sem os quais a câmara deixa de prestar serviço público (portal do munícipe, balcão único, SIG cadastral, contabilidade, GED, e-mail). Esta é a entrada do processo e tratamo-la em detalhe em [B.3]({% link 01-gestao-risco/b3-inventario-ativos.md %}).

2. **Identificação das ameaças relevantes** — para cada activo crítico, quais os cenários plausíveis que podem comprometer a sua disponibilidade, integridade ou confidencialidade. O art. 31.º, n.º 4 do Aviso enumera as cinco categorias-padrão (válidas como guia mesmo não aplicáveis literalmente à autarquia):

   | Categoria de ameaça | Exemplos típicos em autarquia |
   |---|---|
   | Falha de sistema | Bug no portal, falha de servidor, corrupção de base de dados |
   | Fenómeno natural | Inundação do datacenter, falha eléctrica prolongada, incêndio |
   | Erro humano | Apagar registos por engano, configuração errada de firewall, partilha indevida |
   | Ataque malicioso | Ransomware, phishing, exfiltração de dados, DDoS ao portal |
   | Falha de fornecedor | Indisponibilidade Medidata/AIRC/cloud, breach no fornecedor, descontinuação |

3. **Matriz probabilidade × impacto** — para cada par (activo, ameaça), avaliar de forma consistente. A escala usual é 1–5 nos dois eixos:
   - **Probabilidade**: 1 (muito improvável, < 1 vez em 5 anos) a 5 (quase certo, várias vezes por ano).
   - **Impacto**: 1 (insignificante, perda de algumas horas de produtividade) a 5 (catastrófico, paralisação de serviço público crítico, prejuízo financeiro substancial, dano reputacional grave).
   - **Risco bruto** = Probabilidade × Impacto. Resultados de 1 a 25; valores ≥ 15 exigem tratamento prioritário; valores 8–14 exigem plano de tratamento documentado; valores ≤ 7 são habitualmente aceites com monitorização.

Estes três entregáveis cabem num ficheiro Excel de uma só folha — é exactamente o que o template [`matriz-risco-nis2.xlsx`]({{ '/templates/matriz-risco-nis2.xlsx' | relative_url }}) faz.

## Tradução para Grupo A — requisitos adicionais

Para autarquias do Grupo A, o regime cumula (art. 30.º, n.º 3 do Aviso) e exige adicionalmente:

1. **Metodologia documentada** — política escrita que descreve **como** se faz a análise (escalas, critérios, periodicidade, intervenientes). Materializa-se num documento próprio, do tipo [`metodologia-avaliacao-riscos-nis2.docx`]({{ '/templates/metodologia-avaliacao-riscos-nis2.docx' | relative_url }}), aprovado pelo executivo. Sem este documento, a matriz parece arbitrária.

2. **Identificação de funções e activos críticos** (Anexo IV medida [<abbr title="Identificação de funções e activos críticos">**O.ID**</abbr>]({% link recursos/anexo-iv-aviso-5146.md %}#o-id)) — não basta inventariar; é preciso identificar **as funções ou actividades críticas** (atendimento ao munícipe, processo de licenciamento, gestão de águas, etc.) e a sua dependência das TIC. A análise de risco passa a estruturar-se por **processo de negócio**, não só por activo.

3. **Revisão periódica** — pelo menos anual, e adicionalmente nas três janelas previstas no art. 31.º, n.º 2 do Aviso (ver "Periodicidade", abaixo). Cada revisão produz registo datado.

4. **Aceitação formal do risco residual** — o **risco residual** é o que sobra depois de implementadas as medidas de tratamento. Tem de existir documento — tipicamente [`aceitacao-riscos-residuais-nis2.docx`]({{ '/templates/aceitacao-riscos-residuais-nis2.docx' | relative_url }}) — assinado pelo dirigente máximo, que declara que a entidade aceita conscientemente o risco que permanece. Esta assinatura é a contraparte explícita do art. 25.º para essenciais; em autarquias, o Anexo IV Grupo A consagra-a indirectamente pela exigência de **Política de Ciberseguranca (O.PSI)** aprovada pela gestão de topo.

## Metodologia recomendada — 5 passos

Independentemente do grupo, recomendamos a sequência que se segue. É essencialmente a abordagem do template [`metodologia-avaliacao-riscos-nis2.docx`]({{ '/templates/metodologia-avaliacao-riscos-nis2.docx' | relative_url }}), simplificada para o nível autárquico.

### Passo 1 — Identificar activos

Output: lista de **20–40 activos críticos** para uma autarquia média. Não tenta ser exaustivo (1.000 estações de trabalho não entram individualmente); foca-se em **activos primários** — sistemas, aplicações, bases de dados, dependências externas críticas. A página [B.3]({% link 01-gestao-risco/b3-inventario-ativos.md %}) trata este passo em pormenor e é o pré-requisito do passo seguinte.

### Passo 2 — Identificar ameaças por activo

Para cada activo do passo 1, percorrer as cinco categorias de ameaça (tabela acima) e listar os cenários plausíveis. Tipicamente cada activo terá entre 3 e 8 cenários relevantes. Resultado: uma matriz de 20–40 linhas × N cenários, ou (mais prático) **um cenário por linha** (activo + ameaça + descrição curta), totalizando 60–200 linhas de risco.

### Passo 3 — Avaliar probabilidade × impacto

Para cada linha, atribuir P (1–5) e I (1–5) — usando, sempre que possível, **dois avaliadores independentes** que depois concertam diferenças. A primeira iteração é a mais difícil; iterações subsequentes apenas actualizam. **Documentar a justificação** sumária de cada nota (uma frase basta). Sem justificação, números arbitrários.

### Passo 4 — Decidir tratamento

Para cada linha, decidir qual das quatro estratégias clássicas se aplica:

| Estratégia | Quando | Acção |
|---|---|---|
| **Mitigar** | Risco alto e existe controlo aplicável (a maior parte dos casos) | Implementar medida do Anexo IV ou medida adicional; documentar |
| **Transferir** | Risco financeiramente coberto por seguro ou contrato | Negociar cobertura cyber; cláusulas contratuais com fornecedor |
| **Aceitar** | Risco baixo (≤ 7) ou tratamento desproporcionadamente caro | Documentar a aceitação consciente; revisão periódica |
| **Evitar** | Activo prescindível ou substituível por alternativa segura | Descontinuar serviço, mudar fornecedor, eliminar dependência |

A maioria dos riscos será mitigada via medidas do Anexo IV — é a tradução natural entre as duas peças (matriz + medidas).

### Passo 5 — Documentar e rever

Output final: ficheiro Excel preenchido (a matriz) + breve nota interna (1 página) com conclusões, prioridades e plano de tratamento. Assinatura pelo dirigente. **Data e versão** no ficheiro. Rever na periodicidade definida (ponto seguinte).

## Periodicidade da revisão — o que diz o art. 31.º do Aviso

O art. 31.º, n.º 2 do Aviso, dirigido a essenciais/importantes mas adoptável como boa prática pelas autarquias, exige a revisão da análise de risco em **três janelas adicionais** à revisão regular:

1. **Antes de mudanças significativas**: planeamento e introdução de alteração ou substituição de activo. Tradução prática para autarquia: antes de mudar de fornecedor de software de gestão municipal, antes de subscrever cloud, antes de uma migração de servidor, **reavaliar o risco** dos activos afectados.
2. **Após incidente significativo**: depois de um incidente que atinja o limiar do art. 41.º do RJC. A análise pós-incidente alimenta a próxima iteração.
3. **Após notificação do CNCS**: o CNCS comunica ameaças e vulnerabilidades emergentes via plataforma electrónica; quando receberem essa notificação, **têm de reavaliar** dentro do prazo fixado.

Recomendação prática para Grupo B: **revisão anual** + as três janelas acima. Para Grupo A: o mesmo, mais semestre opcional sempre que mudanças organizacionais materiais o justifiquem.

## Em dupla qualificação

Para o **SMAS** ou empresa municipal qualificada como **entidade essencial**, a matriz de risco do *Anexo II do Aviso*{:.legal} aplica-se directamente, com os três níveis de conformidade do art. 28.º:

- **Básico**: medidas mínimas do nível B do Anexo III.
- **Substancial**: medidas do nível B + medidas adicionais S.
- **Elevado**: as anteriores + medidas adicionais E.

A atribuição do nível é feita pelo CNCS em função do sector (águas) e da dimensão da entidade. Para um SMAS pequeno (até 50 trabalhadores) tendencialmente nível B; SMAS médios (50–150) frequentemente S; grandes ou multimunicipais E. **Importante**: para o SMAS, o template **[`matriz-risco-setor-agua-potavel-nis2.xlsx`]({{ '/templates/matriz-risco-setor-agua-potavel-nis2.xlsx' | relative_url }})** já vem pré-preenchido com os cenários típicos do sector — usar como ponto de partida e não reinventar a roda.

## Templates aplicáveis

| Template | Grupo / Etiqueta | Notas |
|---|---|---|
| [`matriz-risco-nis2.xlsx`]({{ '/templates/matriz-risco-nis2.xlsx' | relative_url }}) | **Adaptar para Grupo B** | Folha base com colunas activo / ameaça / P / I / risco / tratamento. Aplicar tal-qual para Grupo B; estender para Grupo A. |
| [`metodologia-avaliacao-riscos-nis2.docx`]({{ '/templates/metodologia-avaliacao-riscos-nis2.docx' | relative_url }}) | **Adaptar para Grupo A** | Documento descritivo da metodologia. Obrigatório para Grupo A; recomendado para Grupo B. |
| [`aceitacao-riscos-residuais-nis2.docx`]({{ '/templates/aceitacao-riscos-residuais-nis2.docx' | relative_url }}) | **Adaptar para Grupo A** | Termo de aceitação formal assinado pelo dirigente. Grupo A: obrigatório. Grupo B: recomendado. |
| [`analise-impacto-negocio-nis2.xlsx`]({{ '/templates/analise-impacto-negocio-nis2.xlsx' | relative_url }}) | Referência | Análise de Impacto no Negócio (BIA). Complemento à matriz de risco — quantifica o impacto operacional e financeiro da indisponibilidade de cada activo. Útil sobretudo para Grupo A. |
| [`matriz-risco-setor-agua-potavel-nis2.xlsx`]({{ '/templates/matriz-risco-setor-agua-potavel-nis2.xlsx' | relative_url }}) | **Para SMAS** | Matriz pré-preenchida com cenários do sector águas. Usar apenas para a entidade SMAS, não para a câmara. |

Todos os templates ficam disponíveis para *download* a partir de 8 de Junho na página de [recursos]({% link recursos/templates.md %}).

## Recurso externo de consulta — EduRisk (guia ISO 27005)

A norma **ISO/IEC 27005** é a referência metodológica internacional para gestão de riscos de segurança da informação e está implícita na abordagem do Anexo IV. Para aprofundar a teoria por trás dos passos que aqui se propõem — categorias de ameaça, escalas de probabilidade, técnicas de avaliação — existe um **guia interactivo ISO 27005** acessível em:

> [edurisk-guia-iso-27005-…run.app](https://edurisk-guia-iso-27005-632691460370.us-west1.run.app/){:target="_blank"}

**Plataforma educacional de terceiros**, gratuita e aberta. Útil como **leitura complementar** ou como segunda opinião na construção da matriz de risco da vossa entidade. Não é exigida pela formação nem substitui os templates do manual digital — é apenas um recurso adicional para quem queira ir mais a fundo na metodologia.

## Exercício associado

[Exercício A2 — Matriz de risco da entidade]({% link exercicios/a2-matriz-risco.md %}) (15 min, individual) — cada formando identifica 3 riscos da sua autarquia, atribui P × I, decide o tratamento. Output: 3 linhas preenchidas na [`matriz-risco-nis2.xlsx`]({{ '/templates/matriz-risco-nis2.xlsx' | relative_url }}). Este é um dos exercícios mais importantes da formação, e o output fica convosco — ficareis com o **embrião da matriz de risco da vossa entidade**.

## Próximo passo

[B.3 Inventário e classificação de ativos →]({% link 01-gestao-risco/b3-inventario-ativos.md %})
