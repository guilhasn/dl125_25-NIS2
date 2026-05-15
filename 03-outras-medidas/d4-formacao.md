---
title: "D.4 Formação e sensibilização"
layout: default
parent: "D. Outras medidas do art. 27.º"
nav_order: 4
---

# D.4 Formação e sensibilização — meta-ironia

> 💡 **Grupo A** = autarquia com ≥ 250 trabalhadores  
> **Grupo B** = autarquia com 75-249 trabalhadores  
> (art. 7.º RJC — ver [A.2 Quem está abrangido]({% link 00-enquadramento/a2-quem-esta-abrangido.md %}))

**Duração**: 10 min · **Base legal**: art. 27.º al. g) RJC + Anexo IV [<abbr title="Plano de Formação e Sensibilização">**H.PF**</abbr>]({% link recursos/anexo-iv-aviso-5146.md %}#h-pf) (Práticas e Formação).

A meta-ironia: estamos numa formação a discutir a obrigação de fazer formação. Mas a ironia é apropriada — esta é uma das medidas com **maior retorno relativo** do Anexo IV. Os utilizadores formados clicam menos em phishing, escolhem senhas melhores, comunicam incidentes mais cedo, fazem menos erros de configuração. Sem formação, nenhuma das outras medidas técnicas resiste ao primeiro clique errado.

## O que a lei diz

> «As entidades essenciais e importantes (...) adoptam medidas relativas à formação e sensibilização em matéria de ciberseguranca de todos os colaboradores.» — art. 27.º, n.º 1, al. g) RJC (paráfrase)

> «A entidade assegura a formação periódica em ciberseguranca de todos os trabalhadores, dirigentes e prestadores de serviços, com registo documentado da participação e da avaliação.» — Anexo IV, medida **H.PF** (paráfrase aplicável a Grupos A e B)

## Os 3 entregáveis mínimos

1. **Plano anual de formação** documentado, com perfis (administrativos, dirigentes, técnicos TIC, autarcas) e conteúdos adequados a cada perfil. Template: [`plano-formacao-anual-nis2.xlsx`]({{ '/templates/plano-formacao-anual-nis2.xlsx' | relative_url }}).
2. **Programa pedagógico** das 3-6 sessões anuais — conteúdos, metodologia, materiais. Template: [`programa-formacao-sensibilizacao-nis2.docx`]({{ '/templates/programa-formacao-sensibilizacao-nis2.docx' | relative_url }}).
3. **Registo de presenças** com data, conteúdo, formador, lista de participantes assinada — evidência de cumprimento. Template: [`registo-presencas-formacao-nis2.xlsx`]({{ '/templates/registo-presencas-formacao-nis2.xlsx' | relative_url }}).

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
- **Dirigentes**: mais frequente em momentos de actualização legal ou após incidente.
- ***Refresher* curto** (15-30 min) trimestral ou semestral via vídeo gravado ou e-mail temático — manter o tema vivo entre as sessões anuais.

## Para Grupo A — exercícios de phishing (H.EC)

Para o Grupo A, o Anexo IV introduz a medida [<abbr title="Exercícios Controlados">**H.EC**</abbr>]({% link recursos/anexo-iv-aviso-5146.md %}#h-ec) (Exercícios Controlados) — campanhas internas de **phishing simulado**, periódicas, com medição da taxa de cliques e *follow-up* educativo para os que caem.

**Operacionalização**:

1. **Trimestralmente** — campanha de simulação a uma amostra ou universo de trabalhadores.
2. **Não punitiva** — quem clica recebe automaticamente uma página de aprendizagem (não denúncia interna, não advertência formal).
3. **Métrica acompanhada**: taxa de cliques ao longo do tempo. Objectivo é descer a curva, não punir.
4. **Conteúdos crescentemente sofisticados** — começar com phishing simples, evoluir para *spear phishing* dirigido a dirigentes (com cuidado).

Ferramentas: Microsoft Attack Simulator (incluído no M365 Business Premium), KnowBe4, Proofpoint, GoPhish (*open source*).

Para Grupo B é boa prática mas não exigência directa do Anexo IV.

## Sidebar — dupla qualificação

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

## Templates aplicáveis

| Template | Grupo / Etiqueta | Notas |
|---|---|---|
| [`plano-formacao-anual-nis2.xlsx`]({{ '/templates/plano-formacao-anual-nis2.xlsx' | relative_url }}) | **Aplicar — Grupo B e A** | Folha de cálculo do plano anual por perfil. |
| [`programa-formacao-sensibilizacao-nis2.docx`]({{ '/templates/programa-formacao-sensibilizacao-nis2.docx' | relative_url }}) | **Adaptar — Grupo B e A** | Programa pedagógico das sessões anuais. |
| [`registo-presencas-formacao-nis2.xlsx`]({{ '/templates/registo-presencas-formacao-nis2.xlsx' | relative_url }}) | **Aplicar — Grupo B e A** | Registo obrigatório de presenças. |
| [`guia-ciber-higiene-nis2.docx`]({{ '/templates/guia-ciber-higiene-nis2.docx' | relative_url }}) | **Aplicar — Grupo B e A** | Guia de bolso para distribuir. |

## Próximo passo

[Voltar ao índice do Bloco D ←]({% link 03-outras-medidas/index.md %}) ou [Bloco E — Supervisão e roadmap →]({% link 04-supervisao-roadmap/index.md %})
