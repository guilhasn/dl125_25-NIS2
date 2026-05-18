---
title: "B.1 Panorama do art. 27.º"
layout: default
parent: "B. Art. 27.º — Risco e ativos"
nav_order: 1
---

# B.1 Panorama do art. 27.º

{: .note }
> **Grupo A** = autarquia com ≥ 250 trabalhadores  
> **Grupo B** = autarquia com 75-249 trabalhadores  
> (art. 7.º RJC — ver [A.2 Quem está abrangido]({% link 00-enquadramento/a2-quem-esta-abrangido.md %}))

{: .highlight }
> 📚 **QNRCS v2 — referencial nacional:** aprovado pelo Anexo I do Aviso 5146/2026/2 (art. 23.º). Estrutura em **6 objetivos** (Gerir · Identificar · Proteger · Detetar · Responder · Recuperar) e **3 níveis cumulativos** (Básico ⊂ Substancial ⊂ Elevado). É o referencial de onde o Anexo IV foi derivado para autarquias. Ver [Recursos / QNRCS v2]({% link recursos/qnrcs.md %}) e [auto-avaliação E.2.1]({% link 04-supervisao-roadmap/e2-1-autoavaliacao-qnrcs.md %}).

O art. 27.º do RJC é o **catálogo nuclear das medidas de gestão de riscos de cibersegurança** previstas pela transposição portuguesa da NIS2. É também a origem de uma confusão recorrente: lê-se na lei, copia-se para o caderno de encargos da câmara, e em poucas semanas os fornecedores estão a propor implementações desenhadas para entidades essenciais a uma autarquia que **não está obrigada a aplicá-lo diretamente**. Esta página resolve essa confusão e prepara o terreno para os 90 minutos do bloco: o que o art. 27.º exige, **a quem**, e **como se traduz** no Anexo IV do Aviso — o regulamento que efectivamente vincula as autarquias.

## O que a lei diz

> «As medidas de cibersegurança a adotar pelas **entidades essenciais e importantes**, tendo em consideração a matriz de risco em que estiverem inseridas nos termos do artigo anterior, **abrangem, designadamente, as seguintes áreas**:
>
> **a)** Tratamento de incidentes;
>
> **b)** Continuidade das atividades, como a gestão de cópias de segurança e a recuperação de desastres, e gestão de crises;
>
> **c)** Segurança da cadeia de abastecimento, incluindo aspetos de segurança respeitantes às relações entre cada entidade e os respetivos fornecedores ou prestadores de serviços diretos;
>
> **d)** Segurança na aquisição, desenvolvimento e manutenção das redes e sistemas de informação, incluindo o tratamento e a divulgação de vulnerabilidades;
>
> **e)** Políticas e procedimentos para avaliar a eficácia das medidas de gestão dos riscos de cibersegurança;
>
> **f)** Práticas básicas de ciber-higiene e formação em cibersegurança, incluindo os titulares de órgãos máximos de gestão e trabalhadores;
>
> **g)** Políticas e procedimentos relativos à utilização de criptografia e, se for caso disso, de cifragem (...);
>
> **h)** Segurança dos recursos humanos, políticas seguidas em matéria de controlo do acesso e gestão de ativos;
>
> **i)** Utilização de autenticação multifator ou de autenticação contínua, comunicações seguras e sistemas seguros de comunicações de emergência no seio da entidade.»
>
> — *art. 27.º, n.º 1 do RJC* (anexo ao DL 125/2025)

Nove alíneas, da a) à i). Não dez. **Esta é a primeira diferença operacional a fixar**, porque a diretiva NIS2 (art. 21.º) enumera dez medidas — o legislador português optou por **fundir três medidas distintas da diretiva numa única alínea h)**: "segurança dos recursos humanos", "controlo do acesso" e "gestão de ativos". Quem citar "as 10 medidas do art. 27.º" está a invocar a diretiva, não o decreto-lei. Em audição com o CNCS é o art. 27.º **com 9 alíneas** que vale.

## NIS2 art. 21.º vs DL 125/2025 art. 27.º — correspondência

| NIS2 art. 21.º | DL 125/2025 art. 27.º | Tema |
|---|---|---|
| (a) Análise de risco | (implícita no art. 26.º — sistema de gestão de riscos) | Política de risco |
| (b) Tratamento de incidentes | al. a) | Resposta |
| (c) Continuidade e gestão de crises | al. b) | PCN/DR |
| (d) Segurança da cadeia de abastecimento | al. c) (+ art. 28.º) | Fornecedores |
| (e) Aquisição, desenvolvimento, manutenção | al. d) | DevSecOps, vulnerabilidades |
| (f) Avaliação da eficácia | al. e) | Auditoria interna |
| (g) Ciber-higiene e formação | al. f) | Sensibilização |
| (h) Criptografia | al. g) | Cifragem |
| (i) Segurança RH + controlo acesso + gestão de ativos | **al. h) (3-em-1)** | Pessoas, acessos, inventário |
| (j) MFA + comunicações seguras | al. i) | Autenticação |

A fusão na al. h) é uma decisão portuguesa: politicamente faz sentido tratar pessoas, acessos e ativos como uma só área governativa; operacionalmente significa que três conjuntos de controlos coexistem dentro do mesmo "guarda-chuva" jurídico.

## A questão central: o art. 27.º **não é o vosso artigo**

Esta é a leitura crítica de todo o bloco B, e é a leitura que distingue o dirigente que **sabe** o regime do dirigente que **copiou** o regime.

> «As medidas de cibersegurança a adotar pelas entidades **essenciais e importantes** (...)» — art. 27.º, n.º 1, alínea de abertura

O art. 27.º **dirige-se exclusivamente a entidades essenciais e importantes**. Para as autarquias, que (como vimos em [A.2]({% link 00-enquadramento/a2-quem-esta-abrangido.md %})) são **entidades públicas relevantes**, a norma aplicável é o [*art. 33.º RJC*{:.legal}]({% link recursos/legislacao-dl-125-2025.md %}#art-33):

> «As entidades públicas relevantes devem cumprir com as medidas de cibersegurança estabelecidas pelo CNCS (...) através de regulamento, (...) em termos proporcionais e adequados ao grupo a que pertencem.» — art. 33.º, n.os 1-2 do RJC

A consequência é decisiva: **não copiem o art. 27.º para o vosso caderno de encargos**. O artigo que vos diz **o que** tem de ser implementado é o **Anexo IV do Aviso 5146/2026/2**, em **medidas operacionais** já decompostas por área, e em dois grupos distintos: Grupo A (≥250 trabalhadores) e Grupo B (75–249). Aplicar o art. 27.º acriticamente cria três problemas:

1. **Sobre-conformidade**: produz documentação que a lei não exige (RC formalmente designado nos termos do art. 31.º, relatório anual nos termos do art. 30.º, ponto de contacto permanente 24/7 nos termos do art. 32.º — nenhum destes obriga uma autarquia).
2. **Erro de fonte**: o tribunal/CNCS, em fiscalização, pergunta-vos pelo Anexo IV — não pelo art. 27.º. Apresentar evidências que não mapeiam ao Anexo IV é mau sinal.
3. **Custo desproporcional**: implementar a totalidade das medidas pensadas para essenciais multiplica o orçamento previsível.

{: .caso-pratico }
> **Caso prático 3 — Caderno de encargos sem análise de risco**
>
> Câmara lançou procedimento para nova plataforma interna de gestão documental. O caderno de encargos copiou de forma acrítica um conjunto extenso de medidas de cibersegurança, sem qualificar previamente a entidade, o sistema ou o risco do serviço. O fornecedor respondeu com proposta inflacionada — incluindo Responsável de Cibersegurança formal, Ponto de Contacto Permanente 24/7 e relatório anual de essencial — todas medidas desproporcionadas ao âmbito real. O custo final triplicou em relação ao orçamento estimado. A equipa percebeu tarde que tinha confundido boa conformidade com acumulação indiscriminada de requisitos.
>
> **Lição:** sem gestão de risco própria, a entidade não tem critério para distinguir requisito necessário de requisito excessivo — e fica refém do caderno-tipo ou do fornecedor.
>
> **Como deveria ter sido feito:** antes do procedimento de contratação, fazer uma análise de risco sumária do sistema a contratar (que dados trata, que serviços suporta, que criticidade tem). Só essa análise dá à entidade base própria para triar requisitos em obrigatórios / recomendáveis / desajustados. Sem ela, o caderno só pode ser maximalista.

## Mapa de correspondência — art. 27.º DL → Anexo III (essencial) → Anexo IV (autarquia)

Esta é a tabela mais importante do bloco. Ela diz, para cada alínea do art. 27.º, **qual a medida equivalente que recai sobre a vossa câmara** no Anexo IV — e qual a medida equivalente que recairia se fossem entidade essencial (útil para quem tem dupla qualificação, ver 'Em dupla qualificação').

📄 **[Mapa art. 27.º → Anexo IV (PDF, A4 paisagem)]({{ '/templates/mapa-art27-anexo-iv.pdf' | relative_url }})** — versão imprimível desta tabela para afixar no gabinete TIC.

| Alínea art. 27.º | Tema | Anexo III (essencial, níveis B/S/E) | Anexo IV Grupo B | Anexo IV Grupo A (cumulativo) |
|---|---|---|---|---|
| a) Tratamento de incidentes | Plano de resposta | medidas O e T dedicadas | [<abbr title="Comunicação e Resposta a Incidentes">**O.CRI**</abbr>]({% link recursos/anexo-iv-aviso-5146.md %}#o-cri) (ponto de contacto para incidentes) | adiciona políticas formais |
| b) Continuidade, backups, DR | PCN + DR | medidas O.PCN + T.CS + T.RAR | [<abbr title="Cópias de Segurança">**T.CS**</abbr>]({% link recursos/anexo-iv-aviso-5146.md %}#t-cs) (cópias de segurança) + [<abbr title="Registo e Auditoria de Registos">**T.RAR**</abbr>]({% link recursos/anexo-iv-aviso-5146.md %}#t-rar) (registos) | adiciona segregação de backups |
| c) Cadeia de abastecimento | Fornecedores | medidas dedicadas | [<abbr title="Política de Segurança da cadeia de Fornecimento">**O.PSF**</abbr>]({% link recursos/anexo-iv-aviso-5146.md %}#o-psf) (inventário + contactos) | **O.PSF** completa (política + critérios de aceitação) |
| d) Aquisição, desenvolvimento, vulnerabilidades | DevSecOps, patches | medidas dedicadas | [<abbr title="Actualizações de Segurança">**T.AS**</abbr>]({% link recursos/anexo-iv-aviso-5146.md %}#t-as) (atualizações de segurança) + [<abbr title="Gestão de Patches">**T.GPT**</abbr>]({% link recursos/anexo-iv-aviso-5146.md %}#t-gpt) | adiciona [<abbr title="Segurança das Comunicações">**T.SC**</abbr>]({% link recursos/anexo-iv-aviso-5146.md %}#t-sc) (hardening) |
| e) Avaliação da eficácia | Auditoria interna | medidas dedicadas | (Grupo B não tem medida específica) | (Grupo A indiretamente via O.GMO) |
| f) Ciber-higiene e formação | Sensibilização | medidas H dedicadas | [<abbr title="Plano de Formação e Sensibilização">**H.PF**</abbr>]({% link recursos/anexo-iv-aviso-5146.md %}#h-pf) (plano sensibilização/formação) + [<abbr title="Formação Inicial e Contínua">**H.FIC**</abbr>]({% link recursos/anexo-iv-aviso-5146.md %}#h-fic) (fontes) | adiciona [<abbr title="Exercícios Controlados">**H.EC**</abbr>]({% link recursos/anexo-iv-aviso-5146.md %}#h-ec) (exercícios de phishing) |
| g) Criptografia | Cifragem | medidas T dedicadas | [<abbr title="Proteção de Correio Eletrónico e Web">**T.PEW**</abbr>]({% link recursos/anexo-iv-aviso-5146.md %}#t-pew) (correio/web, SPF/HTTPS) | adiciona HSTS, cabeçalhos, DKIM |
| h) Seg. RH + acessos + ativos | Pessoas, acessos, inventário | medidas O e H dedicadas | [<abbr title="Inventariação de Ativos Críticos">**O.IAC**</abbr>]({% link recursos/anexo-iv-aviso-5146.md %}#o-iac) (inventário ativos críticos) + [<abbr title="Gestão de Acessos e Privilégios">**O.GAP**</abbr>]({% link recursos/anexo-iv-aviso-5146.md %}#o-gap) (gestão acessos) + [<abbr title="Gestão de Mudanças nas Operações">**O.GMO**</abbr>]({% link recursos/anexo-iv-aviso-5146.md %}#o-gmo) (gestão equipamentos) | adiciona [<abbr title="Política de Acessos e Privilégios">**O.PAP**</abbr>]({% link recursos/anexo-iv-aviso-5146.md %}#o-pap), [<abbr title="Política de Utilização Aceitável">**O.PUA**</abbr>]({% link recursos/anexo-iv-aviso-5146.md %}#o-pua), [<abbr title="Política de Palavras-Passe">**O.PP**</abbr>]({% link recursos/anexo-iv-aviso-5146.md %}#o-pp), [<abbr title="Gestão de Eventos de Cibersegurança">**O.GEC**</abbr>]({% link recursos/anexo-iv-aviso-5146.md %}#o-gec), [<abbr title="Identificação de funções e ativos críticos">**O.ID**</abbr>]({% link recursos/anexo-iv-aviso-5146.md %}#o-id) |
| i) MFA + comunicações seguras | Autenticação | medidas T dedicadas | [<abbr title="Autenticação Multi-fator">**T.AM**</abbr>]({% link recursos/anexo-iv-aviso-5146.md %}#t-am) (MFA aplicações críticas) + [<abbr title="Acesso Remoto seguro">**T.AR**</abbr>]({% link recursos/anexo-iv-aviso-5146.md %}#t-ar) (acesso remoto seguro) + [<abbr title="Proteção de Acessos a Sistemas">**T.PAS**</abbr>]({% link recursos/anexo-iv-aviso-5146.md %}#t-pas) + [<abbr title="Monitorização e Alertas">**T.MA**</abbr>]({% link recursos/anexo-iv-aviso-5146.md %}#t-ma) | adiciona [<abbr title="Gestão técnica de Palavras-passe">**T.GP**</abbr>]({% link recursos/anexo-iv-aviso-5146.md %}#t-gp) (gestão palavras-passe) + [<abbr title="Privilégios Administrativos Diferenciados">**T.PAD**</abbr>]({% link recursos/anexo-iv-aviso-5146.md %}#t-pad) (privilégios diferenciados) |

Sem entrar ainda no detalhe (que percorremos nas próximas três páginas), retenham três leituras desta tabela:

- O **Anexo IV não cobre uma medida explícita "análise de risco"** equivalente ao art. 26.º do RJC. A gestão de risco para autarquias **emerge transversalmente** das medidas O — em particular do inventário de ativos críticos (O.IAC) e da identificação de funções/ativos críticos (O.ID, Grupo A). É essa a abordagem que vamos seguir em [B.2]({% link 01-gestao-risco/b2-analise-risco.md %}).
- A **estrutura O / T / H** do Anexo IV é a chave organizativa de toda a vossa documentação futura. **O** é organizacional (políticas, processos, gestão), **T** é tecnológico (controlos técnicos), **H** é humano (formação, sensibilização). Quando o CNCS pedir evidências, vai pedir por estas categorias.
- O Grupo A **cumula** medidas: tudo o que se exige ao Grupo B aplica-se também ao Grupo A, **mais** as medidas específicas do Grupo A (art. 30.º, n.º 3 do Aviso).

## A estrutura O / T / H do Anexo IV — visão de conjunto

O Anexo IV organiza as medidas em três famílias, identificadas por prefixo:

- **O — Organizacional**: políticas escritas, procedimentos, governação, gestão de fornecedores, inventário de ativos, gestão de acessos. É a **camada documental** — quando o CNCS pedir "evidências", as evidências organizacionais são tipicamente políticas aprovadas, actas, listas, registos de aprovação.
- **T — Tecnológico**: configurações, controlos técnicos, antivírus, MFA, atualizações, cópias de segurança, hardening, proteção perimetral. É a **camada técnica** — as evidências são tipicamente prints de configuração, relatórios de ferramentas, logs.
- **H — Humano**: formação, sensibilização, exercícios de phishing, canais de informação sobre ameaças. As evidências são planos de formação, registos de presença, relatórios de exercícios.

Para o **Grupo B**, o Anexo IV define **5 medidas O + 11 medidas T + 2 medidas H** (16 medidas no total). Para o **Grupo A**, acumulam-se mais medidas O (9 medidas O adicionais), T adicionais e H adicionais. A página [B.3]({% link 01-gestao-risco/b3-inventario-ativos.md %}) trabalha a primeira medida O concreta — o inventário de ativos.

## Em dupla qualificação

Se a vossa autarquia opera **SMAS ou empresa municipal em sector Anexo I** (água potável, águas residuais), essa entidade operacional **é classificada como essencial** e aplica-se-lhe o *Anexo III*{:.legal} completo, com os **três níveis Básico/Substancial/Elevado** definidos no art. 28.º do Aviso. As 9 alíneas do art. 27.º **aplicam-se diretamente** a essa entidade — e o regulamento que decompõe cada uma delas em medidas mínimas é o Anexo III, não o Anexo IV.

Em termos práticos, isto significa para uma autarquia com SMAS:

- **A câmara** segue o regime desta página: Anexo IV, Grupo B ou A.
- **O SMAS** segue um regime paralelo: art. 27.º do RJC + Anexo III com o nível B/S/E que lhe for atribuído pelo CNCS em função da matriz de risco do sector águas (art. 28.º do Aviso).

Ver [Anexo III vs Anexo IV]({% link roteiro-essencial/anexo-iii-vs-anexo-iv.md %}) para o detalhe comparado das medidas que se acumulam.

## Próximo passo

[B.2 Análise e gestão de risco →]({% link 01-gestao-risco/b2-analise-risco.md %})
