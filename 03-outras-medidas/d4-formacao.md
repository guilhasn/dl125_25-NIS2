---
title: "D.4 Formação e sensibilização"
layout: default
parent: "D. Outras medidas do art. 27.º"
nav_order: 4
---

# D.4 Formação e sensibilização — meta-ironia

{: .highlight }
> 📚 **Recursos CNCS complementares — reutilização direta:**
> - [**Guia para campanha de sensibilização em 5 passos**](https://www.cncs.gov.pt/pt/guia-para-realizar-uma-campanha-de-sensibilizacao/){:target="_blank"} — roteiro para preparar uma campanha interna.
> - [**Recursos para Sensibilização**](http://www.cncs.gov.pt/pt/recursos-para-sensibilizacao/){:target="_blank"} — **slides, vídeos e conteúdos prontos** para reutilizar no plano anual de formação da câmara.
>
> Ver [Recursos do CNCS]({% link recursos/cncs.md %}).

**Duração**: 10 min · **Base legal**: art. 27.º al. g) RJC + Anexo IV [<abbr title="Plano de Formação e Sensibilização">**H.PF**</abbr>]({% link recursos/anexo-iv-aviso-5146.md %}#h-pf) (Práticas e Formação).

A meta-ironia: estamos numa formação a discutir a obrigação de fazer formação. Mas a ironia é apropriada — esta é uma das medidas com **maior retorno relativo** do Anexo IV. Os utilizadores formados clicam menos em phishing, escolhem senhas melhores, comunicam incidentes mais cedo, fazem menos erros de configuração. Sem formação, nenhuma das outras medidas técnicas resiste ao primeiro clique errado.

## O que a lei diz

> «As entidades essenciais e importantes (...) adoptam medidas relativas à formação e sensibilização em matéria de cibersegurança de todos os colaboradores.» — art. 27.º, n.º 1, al. g) RJC (paráfrase)

> «A entidade assegura a formação periódica em cibersegurança de todos os trabalhadores, dirigentes e prestadores de serviços, com registo documentado da participação e da avaliação.» — Anexo IV, medida **H.PF** (paráfrase aplicável a Grupos A e B)

## Os 3 entregáveis mínimos

1. **Plano anual de formação** documentado, com perfis (administrativos, dirigentes, técnicos TIC, autarcas) e conteúdos adequados a cada perfil. Template: [`plano-formacao-anual-nis2.xlsx`]({{ '/templates/plano-formacao-anual-nis2.xlsx' | relative_url }}).
2. **Programa pedagógico** das 3-6 sessões anuais — conteúdos, metodologia, materiais. Template: [`programa-formacao-sensibilizacao-nis2.docx`]({{ '/templates/programa-formacao-sensibilizacao-nis2.docx' | relative_url }}).
3. **Registo de presenças** com data, conteúdo, formador, lista de participantes assinada — evidência de cumprimento. Template: [`registo-presencas-formacao-nis2.xlsx`]({{ '/templates/registo-presencas-formacao-nis2.xlsx' | relative_url }}).

{: .caso-pratico }
> **Caso prático 7 — Palestra anual não é programa de formação**
>
> Câmara cumpre a "formação anual de cibersegurança" com uma palestra de 30 minutos no início de Janeiro, a cargo do responsável de TIC, com *slides* preparados na véspera. Os trabalhadores assistem, fazem algumas perguntas e regressam aos postos. Não há programa pedagógico anual, registo formal de presenças, segmentação por perfis de risco, avaliação de aprendizagem nem qualquer campanha de reforço durante o ano.
>
> **Pergunta:** esta prática cumpre a medida H.PF (formação periódica) do Anexo IV? O que falta para passar de "ação pontual" a "programa"?

<details markdown="block">
<summary><strong>Ver resposta</strong></summary>

Não cumpre. **Sensibilização não é uma palestra anual** — é um **plano** com registos, recorrência e adaptação aos perfis de risco. A medida `H.PF` do Anexo IV exige programa estruturado, não boa intenção.

O mínimo a ter:

- **Plano anual** com 3–4 ações segmentadas por perfil (utilizadores gerais, atendimento, TIC, dirigentes).
- **Registos de presença** assinados, com data, conteúdo e formador.
- **Avaliação simples** de aprendizagem (quiz curto, exercício prático).
- **Calendarização** que cubra o ano, não apenas Janeiro.

Notar ainda: o *art. 27.º, al. f) RJC* exige expressamente formação **dos órgãos máximos de gestão** (presidente, vereadores, dirigentes). Sem evidência da formação destes titulares, a fragilidade em supervisão *ex post* é tipicamente das primeiras a aparecer.
</details>

{: .important }
> **Formação dos órgãos máximos de gestão — obrigação legal, não opcional.** O *art. 27.º, al. f) RJC*{:.legal} — alinhado com o art. 20.º, n.º 2 da Diretiva NIS2 — exige expressamente formação em cibersegurança "**incluindo os titulares de órgãos máximos de gestão e trabalhadores**". Para autarquias, a medida `H.PF` do Anexo IV deriva desta alínea: a formação do presidente, vereadores e dirigentes máximos do serviço **não é boa prática facultativa, é exigência regulamentar**. A ausência de evidência documentada da formação destes titulares é uma das principais fragilidades em supervisão *ex post* (art. 55.º) — agrava a responsabilidade pessoal prevista nos arts. 61.º e 62.º (ver [A.4 Prazos e sanções]({% link 00-enquadramento/a4-prazos-sancoes.md %})).

## Conteúdos mínimos por perfil

Não basta convocar para uma sessão genérica. **Conteúdos diferenciados** por perfil aumentam a relevância e a retenção:

| Perfil | Conteúdos prioritários |
|---|---|
| **Administrativos** (atendimento, secretaria) | Phishing, palavras-passe e MFA, classificação de informação, reportar incidentes. |
| **Técnicos TIC** | Hardening, *patching*, *backups*, MFA, resposta a incidentes, ferramentas de monitorização. |
| **Dirigentes** (chefias, divisões) | Responsabilidade pessoal NIS2, decisão de notificação, articulação com o gabinete, comunicação a vereadores. |
| **Autarcas** (vereadores, presidente) | NIS2 como obrigação institucional, sanções, comunicação a munícipes em crise, articulação com gabinete de comunicação. |
| **Trabalhadores em geral** | Ciber-higiene básica, phishing, palavras-passe, reportar suspeitas. |

**Guia distribuído** a todos: [`guia-ciber-higiene-nis2.docx`]({{ '/templates/guia-ciber-higiene-nis2.docx' | relative_url }}) — guia de bolso (4-6 páginas) para entrega no *onboarding* e nas sessões periódicas.

## Periodicidade

- **Geral**: **anual** mínimo, com registo.
- **Dirigentes**: mais frequente em momentos de atualização legal ou após incidente.
- ***Refresher* curto** (15-30 min) trimestral ou semestral via vídeo gravado ou e-mail temático — manter o tema vivo entre as sessões anuais.

## Para Grupo A — exercícios de phishing (H.EC)

Para o Grupo A, o Anexo IV introduz a medida [<abbr title="Exercícios Controlados">**H.EC**</abbr>]({% link recursos/anexo-iv-aviso-5146.md %}#h-ec) (Exercícios Controlados) — campanhas internas de **phishing simulado**, periódicas, com medição da taxa de cliques e *follow-up* educativo para os que caem.

**Operacionalização**:

1. **Trimestralmente** — campanha de simulação a uma amostra ou universo de trabalhadores.
2. **Não punitiva** — quem clica recebe automaticamente uma página de aprendizagem (não denúncia interna, não advertência formal).
3. **Métrica acompanhada**: taxa de cliques ao longo do tempo. Objetivo é descer a curva, não punir.
4. **Conteúdos crescentemente sofisticados** — começar com phishing simples, evoluir para *spear phishing* dirigido a dirigentes (com cuidado).

Ferramentas: Microsoft Attack Simulator (incluído no M365 Business Premium), KnowBe4, Proofpoint, GoPhish (*open source*).

Para Grupo B é boa prática mas não exigência direta do Anexo IV.

## Em dupla qualificação

Para o **SMAS** qualificado como **entidade essencial**, o regime exige:

- **Formação específica para operadores de OT** (SCADA, telemetria, sistemas de bombagem) — conteúdos técnicos próprios.
- **Periodicidade reforçada** — geralmente semestral para operadores técnicos.
- **Certificação** dos formadores em sectores regulados (ERSAR pode emitir orientações).

## Operacionalização para uma câmara pequena (Grupo B com 80-150 trabalhadores)

A formação não tem de ser organizada inteiramente em casa. Opções económicas:

- **Aproveitar a formação ANFUP, AMA, CNCS** — cursos gratuitos ou subsidiados, dirigidos a staff de administração pública. Contam para o registo.
- **Convidar formador externo** uma vez por ano (3-4 horas), depois reciclar conteúdos internamente.
- **Vídeos curtos do CNCS** (Cibersegurança Pessoal, *Stay Safe*) — alimentar *intranet* e e-mail temático.
- **Esta formação** (DL 125/2025) — cumpre a obrigação para dirigentes e técnicos. Documentar e arquivar o registo de presenças.

## 💬 Micro-exercício (3 min)

Antes de avançar para o Bloco E, **rascunhem 1 perfil** do vosso plano anual de formação. Escolham um dos cinco perfis-tipo da tabela acima (administrativos, técnicos TIC, dirigentes, autarcas, trabalhadores em geral) e respondam, em 3 linhas:

1. **Perfil escolhido**: ________
2. **Conteúdos prioritários** para este perfil na vossa autarquia: ________
3. **Cadência sugerida** (anual / semestral / trimestral): ________

Não é exercício formal — é **um arranque** para o plano anual. O que sair pode ser ampliado depois, em câmara, com o template [`plano-formacao-anual-nis2.xlsx`]({{ '/templates/plano-formacao-anual-nis2.xlsx' | relative_url }}).

## Templates aplicáveis

| Template | Grupo / Etiqueta | Notas |
|---|---|---|
| [`plano-formacao-anual-nis2.xlsx`]({{ '/templates/plano-formacao-anual-nis2.xlsx' | relative_url }}) | **Aplicar — Grupo B e A** | Folha de cálculo do plano anual por perfil. |
| [`programa-formacao-sensibilizacao-nis2.docx`]({{ '/templates/programa-formacao-sensibilizacao-nis2.docx' | relative_url }}) | **Adaptar — Grupo B e A** | Programa pedagógico das sessões anuais. |
| [`registo-presencas-formacao-nis2.xlsx`]({{ '/templates/registo-presencas-formacao-nis2.xlsx' | relative_url }}) | **Aplicar — Grupo B e A** | Registo obrigatório de presenças. |
| [`guia-ciber-higiene-nis2.docx`]({{ '/templates/guia-ciber-higiene-nis2.docx' | relative_url }}) | **Aplicar — Grupo B e A** | Guia de bolso para distribuir. |

## Revisão do Bloco D — 8 perguntas

**1.** Em qual destes pontos é que se deve activar MFA com prioridade máxima numa autarquia?

<details markdown="block">
<summary><strong>Ver resposta</strong></summary>

**Em todos, sem exceção** — Microsoft 365, VPN, acessos administrativos a servidores/firewall, AD, aplicações financeiras. MFA bloqueia 99% dos ataques baseados em credenciais. A pergunta correta não é "onde activar primeiro" mas "porque é que ainda não está ativo em todos". Ver [D.3 Acessos, MFA e palavras-passe]({% link 03-outras-medidas/d3-acessos-mfa.md %}).
</details>

**2.** A câmara tem *backups* diários para uma pasta partilhada na rede. Isto é suficiente?

<details markdown="block">
<summary><strong>Ver resposta</strong></summary>

**Não.** Dois problemas: (1) **não há registo de testes** — *backups* existentes mas nunca testados frequentemente não funcionam quando precisam; (2) **estão na rede acessível** — ransomware moderno procura *backups* primeiro e encripta-os. Precisam de pelo menos uma cópia ***air-gapped*** (offline). Ver [D.2 Continuidade, backups e recuperação]({% link 03-outras-medidas/d2-continuidade-backups.md %}).
</details>

**3.** A câmara contrata um fornecedor de gestão documental. O incidente é deles. A notificação ao CNCS é deles?

<details markdown="block">
<summary><strong>Ver resposta</strong></summary>

**Não. A notificação é da câmara.** O fornecedor é responsável pelo facto técnico, mas a entidade qualificada perante o CNCS (entidade pública relevante) é a **câmara**. O contrato com o fornecedor **tem de exigir comunicação atempada** (24-72h) para a câmara poder cumprir o prazo de 24h do *art. 42.º RJC*. Ver [D.1 Cadeia de fornecimento]({% link 03-outras-medidas/d1-cadeia-fornecimento.md %}).
</details>

**4.** Política de palavras-passe moderna (NIST 2017): quanto tempo deve durar uma palavra-passe antes de ser obrigatória rotação?

<details markdown="block">
<summary><strong>Ver resposta</strong></summary>

**Não há rotação obrigatória** — exceto após suspeita de compromisso. Rotações forçadas levam os utilizadores a padrões previsíveis (`Verao2025!` → `Verao2026!`). Foco atual: **comprimento ≥ 12 caracteres**, validação contra listas de senhas vazadas, gestores de palavras-passe institucionais. Ver [D.3]({% link 03-outras-medidas/d3-acessos-mfa.md %}).
</details>

**5.** Um fornecedor TIC acede a dados pessoais de munícipes. Que cláusula contratual mínima é obrigatória?

<details markdown="block">
<summary><strong>Ver resposta</strong></summary>

**Contrato escrito com cláusulas do art. 28.º, n.º 3 do RGPD** — o fornecedor é **subcontratante de tratamento**. Mínimo: notificação de violação à câmara em prazo curto, direito de auditoria pela câmara, retenção e devolução/destruição de dados no fim do contrato, sigilo das pessoas envolvidas. Cumulativamente, **cláusula NIS2** de notificação atempada de incidentes (24-72h). Ver [D.1]({% link 03-outras-medidas/d1-cadeia-fornecimento.md %}).
</details>

**6.** Qual a diferença entre **PCN** e **DRP**?

<details markdown="block">
<summary><strong>Ver resposta</strong></summary>

**PCN — Plano de Continuidade de Negócio**: resposta **organizacional** — como continua a câmara a funcionar com sistemas em baixo (quem dispara, atendimento em modo degradado, comunicação a vereadores). É sobre **pessoas e processos**. <br/>
**DRP — Disaster Recovery Plan**: resposta **técnica** — como repõem os sistemas (ordem de restauro, RTO/RPO por sistema, procedimentos). <br/>
Para Grupo B podem fundir num documento único; para Grupo A separam-se. Ver [D.2]({% link 03-outras-medidas/d2-continuidade-backups.md %}).
</details>

**7.** Para Grupo B, qual a periodicidade mínima de **teste de restauro de backup**?

<details markdown="block">
<summary><strong>Ver resposta</strong></summary>

**Trimestral**, com registo escrito. Pelo menos uma sessão anual completa (restauro integral de um sistema crítico). Para Grupo A: **mensal**, com restauro completo semestral. Os testes são a **evidência principal** que o CNCS pede em supervisão pós-incidente — *backups* existentes sem testes documentados não contam. Template: [`procedimento-testes-pcn-nis2.docx`]({{ '/templates/procedimento-testes-pcn-nis2.docx' | relative_url }}).
</details>

**8.** A medida **H.EC** (exercícios de phishing simulado) é obrigatória para todos os grupos?

<details markdown="block">
<summary><strong>Ver resposta</strong></summary>

**Não.** É obrigatória para **Grupo A** (e essenciais/importantes). Para **Grupo B** é boa prática recomendada mas não exigência direta do Anexo IV. Independentemente do grupo, vale a pena fazer **trimestralmente** uma campanha não-punitiva, com página de aprendizagem para quem clica e métrica de taxa de cliques ao longo do tempo. Ferramenta gratuita do M365: Attack Simulator. Ver [D.4 Formação e sensibilização]({% link 03-outras-medidas/d4-formacao.md %}).
</details>

## Próximo passo

[Voltar ao índice do Bloco D ←]({% link 03-outras-medidas/index.md %}) ou [Bloco E — Supervisão e roadmap →]({% link 04-supervisao-roadmap/index.md %})
