---
title: "C.1 Plano de resposta a incidentes"
layout: default
parent: "C. Notificação de incidentes"
nav_order: 1
---

# C.1 Plano de resposta a incidentes

{: .note }
> **Grupo A** = autarquia com ≥ 250 trabalhadores  
> **Grupo B** = autarquia com 75-249 trabalhadores  
> (art. 7.º RJC — ver [A.2 Quem está abrangido]({% link 00-enquadramento/a2-quem-esta-abrangido.md %}))

{: .highlight }
> 📚 **Recursos CNCS complementares:** o CNCS publica dois materiais centrais para o plano de resposta a incidentes:
> - [**Referencial de Comunicação de Risco e de Crise**](http://www.cncs.gov.pt/pt/referencial-de-comunicacao/){:target="_blank"} — 3 fases: preparar · responder · melhorar.
> - [**Reacção a Incidentes: Capacidades Mínimas**](http://www.cncs.gov.pt/pt/certpt/roadmap/){:target="_blank"} — capacidades técnicas, humanas e procedimentais para AP. Inclui [modelo de maturidade](https://www.cncs.gov.pt/docs/ir-modelo-maturidade-pt-2018pdf.pdf){:target="_blank"} para avaliação.
>
> Ver [Recursos do CNCS]({% link recursos/cncs.md %}).

Este bloco abre com a questão que mais ansiedade gera em qualquer câmara: **quando acontecer um incidente — e vai acontecer —, quem faz o quê, em que ordem, com que prazos**. Esta página fixa a estrutura mínima de um plano de resposta a incidentes adaptado à dimensão e ao regime das autarquias. Não pretende substituir um manual técnico de tratamento de incidentes (esse é o trabalho da equipa de TIC); pretende garantir que, no momento em que o relógio dos 24 horas começa a contar, ninguém na vossa autarquia ficar parado por não saber se é a si que cabe agir.

A subtileza para Grupo A e Grupo B é esta: o **Anexo IV do Aviso 5146/2026/2 não exige formalmente um Plano de Resposta a Incidentes** com a estrutura desenvolvida que se exige a entidades essenciais. A única medida explícita do Anexo IV nesta matéria, para Grupo B, é a [<abbr title="Comunicação e Resposta a Incidentes">**O.CRI**</abbr>]({% link recursos/anexo-iv-aviso-5146.md %}#o-cri) — identificação de um ponto de contacto para resposta a incidentes. Para Grupo A nem essa medida figura nominalmente. **Mas isto é uma armadilha**: sem plano formal, é impossível cumprir os deveres de notificação dos arts. 40.º a 44.º do RJC dentro do prazo, e qualquer auditoria do CNCS ao abrigo do art. 55.º (supervisão *ex post*) vai pedi-lo. Recomendamos construir um plano proporcional **em todos os casos**.

## O que a lei diz

> «As medidas de cibersegurança a adotar pelas entidades essenciais e importantes (...) abrangem, designadamente, as seguintes áreas: a) Tratamento de incidentes (...).» — art. 27.º, n.º 1, al. a) do RJC

> «As entidades essenciais, importantes e públicas relevantes notificam qualquer incidente significativo à autoridade de cibersegurança competente.» — art. 40.º, n.º 1 do RJC

> «O.CRI — Identificação de ponto de contacto para resposta a incidentes. A entidade deve identificar um ponto de contacto para resposta a incidentes. A pessoa identificada deve ser capaz de responder a eventuais solicitações externas, e, caso seja necessário, ter disponibilidade para contactos de emergência fora do horário de expediente.» — Anexo IV do Aviso 5146/2026/2, Grupo B

> «GR.PL-2 — O Plano de Resposta a Incidentes é definido, comunicado, mantido e melhorado.» — Anexo III do Aviso 5146/2026/2 (essenciais e importantes)

**Constatação**: o *art. 27.º, al. a)*{:.legal} (tratamento de incidentes) é uma medida para essenciais e importantes — o art. 33.º remete a definição para o regulamento, e o Anexo IV apenas concretiza a medida **O.CRI** (Grupo B). A obrigação formal de ter um **Plano de Resposta a Incidentes** consta do Anexo III (GR.PL-2 e RS.MI-2) e dirige-se a essenciais e importantes. Para autarquias, o plano não é exigido nominalmente — mas o **cumprimento dos prazos de notificação** dos arts. 42.º a 44.º **exige** organização prévia equivalente a um plano.

## Estrutura mínima de um plano — cinco peças

Independentemente do grupo, um plano de resposta minimamente defensável tem cinco componentes. Não interessa o nome do documento; interessa que estas cinco respostas existam por escrito.

### 1. Papéis e responsabilidades

Três funções têm de estar atribuídas, nominalmente, antes do incidente:

| Papel | Quem | Decisão típica |
|---|---|---|
| **Decisor** | Dirigente máximo do serviço ou seu substituto (presidente de câmara, vereador com pelouro, diretor do DIM) | Ativa o plano; autoriza comunicação externa; decide envolvimento de fornecedor/peritos. |
| **Executor técnico** | Responsável de TIC ou equivalente; em câmaras pequenas, responsável funcional do sistema afetado | Contém o incidente; preserva evidência; coordena recuperação. |
| **Comunicador** | Pessoa designada (gabinete de comunicação, secretaria-geral) | Submete notificações na plataforma do CNCS; gere comunicação a destinatários (art. 48.º) e, se aplicável, CNPD, MP e órgãos de comunicação social. |

Em Grupo B com equipa pequena, **uma só pessoa pode acumular funções** — mas tem de estar nominalmente designada como **O.CRI** (ponto de contacto para resposta a incidentes), tem de estar registada na plataforma eletrónica do CNCS e tem de ter substituto designado para garantir cobertura fora de horas.

{: .caso-pratico }
> **Caso prático 4 — Escalação às 17h30**
>
> Quinta-feira, 17h30. A equipa TIC detecta instabilidade no serviço de autenticação e sinais de credenciais comprometidas. Tecnicamente sabe o que fazer — isolar contas, rever *logs*, repor serviço. Mas ninguém sabe quem pode **declarar incidente significativo**, **autorizar comunicação externa** ou **accionar o fornecedor de *cloud*** com a cláusula contratual de emergência. A decisão sobe de técnico para chefe de divisão TIC, depois vereador, depois presidente. Cada nível pede informação adicional. Quando o presidente autoriza contenção e contacto externo, são 23h30.
>
> **Pergunta:** o que falhou? Era um problema técnico — ou um problema de plano?

<details markdown="block">
<summary><strong>Ver resposta</strong></summary>

Era um problema de **plano de resposta inexistente ou não testado**. Tecnicamente a equipa sabia o que fazer; faltou a **cadeia de decisão pré-definida** — quem declara, quem autoriza, quem comunica, com substitutos para fora de horas.

Definir antecipadamente, **por escrito e antes do incidente**: decisor, executor técnico, comunicador, substitutos nomeados e contactos pessoais testados. O plano não é burocracia — é a diferença entre agir em 30 minutos ou discutir durante seis horas quem tem competência para decidir. **Durante** o incidente já é tarde para esse debate.
</details>

### 2. Critérios de activação e escalação

Dois patamares: **alerta interno** (suspeita de incidente, equipa TIC analisa) e **activação formal do plano** (incidente confirmado, decisor avisado, relógio do art. 42.º começa). O critério-chave é a chegada ao limiar de **"incidente significativo"** definido no art. 40.º, n.º 3 do RJC — número de utilizadores afetados, duração, gravidade da perturbação, dimensão do impacto. Esta avaliação é detalhada em [C.2 — Critérios de "incidente significativo"]({% link 02-notificacao-incidentes/c2-prazos-pt-vs-nis2.md %}).

A escalação fixa: quem avisa quem, em que prazo, por que canal (telefone primeiro, e-mail confirmatório). Para uma câmara média, três níveis bastam: técnico → responsável TIC → dirigente máximo. Cada um com **número de telemóvel pessoal registado e testado**.

### 3. Comunicação externa

O plano lista **antecipadamente** a quem se notifica e com que prazo:

- **CNCS** — plataforma eletrónica, 24h após verificação do incidente significativo (art. 42.º, n.º 1).
- **Fornecedor crítico** — se a causa estiver na cadeia, accionado em paralelo com o CNCS.
- **CNPD** — se houver violação de dados pessoais, 72h (RGPD art. 33.º). Detalhado em [C.4]({% link 02-notificacao-incidentes/c4-cruzamento-rgpd.md %}).
- **Ministério Público** — se houver indícios de crime informático nos termos da Lei 109/2009. Sem prazo fixo no DL, mas «sem demora».
- **Destinatários dos serviços** (munícipes, contribuintes) — art. 48.º do RJC: comunicação «sem demora injustificada» quando o incidente seja susceptível de os afetar negativamente.
- **Órgãos de comunicação social** — não há obrigação legal, mas porta-voz e linha de comunicação devem estar designados antes.

### 4. Logging e preservação de evidência

Desde o momento da deteção, o executor técnico tem de **registar tudo**: horas exatas dos eventos, decisões, snapshots, hash de ficheiros relevantes, dumps de memória se possível. O plano define que ferramentas usar (foro digital simples — Excel com timestamps + pasta partilhada com cópias) e onde guardar. Esta evidência é a base do **relatório final dos 30 dias úteis** (art. 44.º) e, se houver crime, da participação ao MP.

### 5. Critérios de encerramento e revisão

O plano fixa **quando se declara o incidente resolvido** — não é arbitrário. O Anexo III do Aviso (medida RS.MI-2) exige que «o Plano de Resposta a Incidentes deve conter critérios para declarar pela conclusão da resolução do incidente». Isto traduz-se em duas linhas no vosso documento: serviço restabelecido + ausência de atividade anómala confirmada + comunicação de fim de impacto significativo submetida (art. 43.º). Após encerramento, **revisão pós-incidente obrigatória** com lições aprendidas — alimenta a revisão da matriz de risco (ver [B.2]({% link 01-gestao-risco/b2-analise-risco.md %})).

## Em dupla qualificação

Para autarquias que operam **serviços essenciais** (SMAS, empresa municipal qualificada como essencial), o regime acumula:

- **Plano de Resposta a Incidentes formal obrigatório** — Anexo III GR.PL-2.
- **Responsável de Cibersegurança (RC)** obrigatório — art. 31.º do RJC. Pessoa singular com responsabilidades específicas, comunicada ao CNCS pela plataforma eletrónica.
- **Ponto de Contacto Permanente (PCP)** obrigatório — art. 32.º do RJC. Pode ser a mesma pessoa do RC, mas a função é distinta.

Para a parte autárquica (câmara em sentido estrito), a O.CRI do Anexo IV basta. Resultado prático para quem tem SMAS: **dois pontos de contacto distintos** registados na plataforma (um para a parte essencial, outro para a parte pública relevante), com planos próprios.

## Templates aplicáveis

| Template | Grupo / Etiqueta | Notas |
|---|---|---|
| [`plano-resposta-incidentes-nis2.docx`]({{ '/templates/plano-resposta-incidentes-nis2.docx' | relative_url }}) | **Adaptar Grupo B** | Documento-base com as cinco peças. Versão Grupo B simplifica funções acumuladas; versão Grupo A separa decisor / executor / comunicador. |
| [`matriz-escalacao-incidentes-nis2.docx`]({{ '/templates/matriz-escalacao-incidentes-nis2.docx' | relative_url }}) | **Adaptar** | Quadro de uma página com nomes, telemóveis, horários, suplentes. Imprimir e afixar no gabinete TIC e na receção do edifício principal. |
| [`playbook-ransomware-nis2.docx`]({{ '/templates/playbook-ransomware-nis2.docx' | relative_url }}) | Referência | Playbook específico para o cenário mais provável. Recomendado mesmo para Grupo B. |
| [`playbook-data-breach-nis2.docx`]({{ '/templates/playbook-data-breach-nis2.docx' | relative_url }}) | Referência | Playbook para violação de dados pessoais — articula NIS2 + RGPD. |
| [`template-post-incident-review-nis2.docx`]({{ '/templates/template-post-incident-review-nis2.docx' | relative_url }}) | Adaptar | Revisão pós-incidente. Aplicar quando se fecha qualquer incidente acima do limiar de significativo. |

Todos os templates ficam disponíveis a partir de 8 de Junho na página de [recursos]({% link recursos/templates.md %}).

## Exercício associado

[Exercício A4 — Notificação 24h]({% link exercicios/a4-notificacao.md %}) (25 min, dentro de C.6) — cada formando recebe uma ficha de cenário sorteada e simula, individualmente, a activação do plano + preenchimento da notificação inicial. As fichas e as instruções estão em [C.6 — Fichas de cenário]({% link 02-notificacao-incidentes/c6-cenarios-exercicio.md %}).

## Próximo passo

[C.2 Prazos PT vs NIS2 →]({% link 02-notificacao-incidentes/c2-prazos-pt-vs-nis2.md %})
