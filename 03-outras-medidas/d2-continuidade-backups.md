---
title: "D.2 Continuidade e backups"
layout: default
parent: "D. Outras medidas do art. 27.º"
nav_order: 2
---

# D.2 Continuidade, *backups* e recuperação

{: .note }
> **Grupo A** = autarquia com ≥ 250 trabalhadores  
> **Grupo B** = autarquia com 75-249 trabalhadores  
> (art. 7.º RJC — ver [A.2 Quem está abrangido]({% link 00-enquadramento/a2-quem-esta-abrangido.md %}))

**Duração**: 15 min · **Base legal**: art. 27.º al. b) RJC + Anexo IV [<abbr title="Cópias de Segurança">**T.CS**</abbr>]({% link recursos/anexo-iv-aviso-5146.md %}#t-cs) (Continuidade e Salvaguarda).

A maior parte dos incidentes que afectam uma autarquia não é exfiltração espectacular de dados — é **indisponibilidade**: o portal cai, a base de dados fica encriptada, o servidor de e-mail bloqueia. Quando isso acontece, a diferença entre **6 horas paradas** e **6 semanas paradas** está em **duas coisas**: ter *backups* que **funcionam** e ter um **plano de continuidade** que toda a gente saiba executar. Nenhuma destas duas é técnica — são organizacionais. O Anexo IV exige ambas.

## O que a lei diz

> «As entidades essenciais e importantes (...) adoptam medidas de continuidade do negócio, incluindo a gestão de cópias de segurança, recuperação de desastres e gestão de crises.» — art. 27.º, n.º 1, al. b) RJC (paráfrase)

> «A entidade deve assegurar a continuidade dos seus serviços críticos, incluindo a manutenção de cópias de segurança regularmente testadas e a existência de planos de recuperação documentados e exercitados.» — Anexo IV, medida **T.CS** (paráfrase aplicável a Grupos A e B)

A medida T.CS combina **três peças** que andam juntas e que vamos tratar em sequência: ***backups*, plano de continuidade (PCN), plano de recuperação de desastres (DRP)**.

## A regra principal: *backups* não testados não contam

Esta é a frase mais importante de toda esta página. Em auditoria, a primeira pergunta que vão receber sobre *backups* não é «existem?» — é «**testaram-nos quando?**». A diferença é enorme:

- *Backups* **existentes mas nunca testados** → falsa segurança. Em ransomware, descobre-se que estavam corrompidos, incompletos ou impossíveis de restaurar à hora certa.
- *Backups* **testados regularmente** → evidência de funcionamento, *Recovery Time Objective* (RTO) e *Recovery Point Objective* (RPO) conhecidos, pessoas treinadas a restaurar.

**Periodicidade recomendada**:

| Grupo | Teste de restauro |
|---|---|
| **Grupo B** | **Trimestral** mínimo, com registo escrito. Pelo menos uma sessão anual completa (restauro integral de um sistema crítico). |
| **Grupo A** | **Mensal** mínimo. Restauro completo semestral. Inclusão de cenário de *disaster recovery* (perda total do datacenter) anualmente. |

Template aplicável: [`procedimento-testes-pcn-nis2.docx`]({{ '/templates/procedimento-testes-pcn-nis2.docx' | relative_url }}).

## *Backups* offline (*air-gapped*) — protecção contra ransomware

O ransomware moderno **procura os *backups* primeiro**. Encripta os ficheiros, encripta os *snapshots* online, encripta os *backups* na rede. Se os *backups* estiverem na **mesma rede acessível**, são igualmente vítimas — e a câmara fica sem saída, a não ser pagar o resgate ou perder tudo.

**Solução conceptual**: pelo menos **uma cópia *air-gapped*** — armazenamento fisicamente desconectado da rede, ligado apenas durante o intervalo de cópia. Para uma câmara:

- **Tape** (cassete) — desactualizado mas funcional, custo baixo, *air-gap* natural.
- **Disco externo rotativo** — três discos, um por semana, dois em cofre.
- **Cloud com *immutability*** (Azure, AWS, etc.) — *backups* imutáveis com retenção mínima legal.
- **Repositório dedicado em rede isolada** — VLAN separada, sem rota directa, credenciais distintas.

Para o Grupo A é **expectativa**; para Grupo B é **fortemente recomendado** — e a primeira pergunta que o CNCS vai fazer numa auditoria pós-incidente.

{: .caso-pratico }
> **Caso prático 6 — Backups na mesma rede**
>
> Câmara fazia *backups* diários para uma NAS interna alojada no mesmo armário do servidor de produção. Durante um ataque de *ransomware* em Março, os dados de produção e a NAS foram cifrados em simultâneo — o atacante movimentou-se lateralmente com credenciais administrativas válidas em ambos os sistemas. O último *backup* verdadeiramente isolado era de Novembro do ano anterior, em fita armazenada num armário desorganizado, sem garantia de integridade. A equipa fazia *backups* todos os dias durante quatro meses — e perdeu na mesma quatro meses de dados.
>
> **Lição:** *backup* acessível ao atacante é apenas mais um ficheiro para cifrar.
>
> **Como deveria ter sido feito:** manter pelo menos uma cópia isolada (offline, imutável ou em rede segregada com credenciais distintas das de produção). Testar o restauro pelo menos trimestralmente, com restauro real de um sistema completo. Registar cada teste com data, sistema e responsável — sem registo, o teste não conta.

## Plano de Continuidade de Negócio (PCN) e Plano de Recuperação de Desastres (DRP)

Os dois não são a mesma coisa, e a confusão entre eles é frequente:

- **PCN** — Plano de **Continuidade de Negócio**. Resposta organizacional ao incidente: **como continua a câmara a funcionar** enquanto os sistemas estão em baixo? Quem dispara o quê? Como atendem os munícipes em modo degradado? Como comunicam com vereadores e imprensa? PCN é mais sobre **pessoas e processos** do que sobre tecnologia.
- **DRP** — Plano de **Recuperação de Desastres**. Resposta técnica: **como repõem os sistemas**? Ordem de restauro, RTO/RPO por sistema, equipas, procedimentos.

Para uma câmara de Grupo B, é razoável **um documento único** com as duas componentes claramente identificadas. Grupo A tipicamente separa os dois — PCN aprovado por executivo, DRP gerido pela informática.

**Templates**:
- [`plano-continuidade-negocio-nis2.docx`]({{ '/templates/plano-continuidade-negocio-nis2.docx' | relative_url }}) — PCN.
- [`plano-recuperacao-desastres-nis2.docx`]({{ '/templates/plano-recuperacao-desastres-nis2.docx' | relative_url }}) — DRP.
- [`politica-backups-nis2.docx`]({{ '/templates/politica-backups-nis2.docx' | relative_url }}) — política-mãe de *backups*.

## Análise de Impacto no Negócio (BIA) — opcional para Grupo A

Para definir RTO/RPO de forma fundamentada, faz-se uma **Análise de Impacto no Negócio** (Business Impact Analysis): cruzar os activos críticos (do Exercício A3 / inventário O.IAC) com os processos da câmara (atendimento, urbanismo, fiscalidade, acção social, tesouraria) e estimar o impacto financeiro/reputacional/legal de cada sistema parado durante 1h, 4h, 1 dia, 1 semana.

Template [`analise-impacto-negocio-nis2.xlsx`]({{ '/templates/analise-impacto-negocio-nis2.xlsx' | relative_url }}) — folha de cálculo a preencher por sistema.

Para Grupo B, é **boa prática** mas não obrigatório. Para Grupo A, é o **input correcto** para escrever um PCN que reflicta as prioridades reais.

## Cenários típicos a contemplar (autarquia)

O plano de continuidade tem de cobrir, no mínimo, estes três cenários — que são os que mais frequentemente afectam câmaras portuguesas:

1. **Portal do munícipe parado por 24-72h** — Plano B: aceitar requerimentos por e-mail dedicado, página estática alternativa com instruções, comunicação aos munícipes.
2. **Encriptação do servidor de ficheiros (ransomware)** — Plano B: activação do *backup* *air-gapped*, isolamento da rede afectada, comunicação interna sobre uso de dados antigos pré-incidente, notificação CNCS+CNPD.
3. **Indisponibilidade prolongada do SIG cadastral** — Plano B: certidões emitidas em formato manual com base em cópias *pdf* recentes, urbanismo em pausa funcional, comunicação aos balcões e munícipes.

Cada cenário tem **decisões pré-tomadas**: quem chama a quem, em que ordem, qual o discurso de comunicação, quem aprova as decisões. Sem decisões pré-tomadas, o dia do incidente faz-se a improvisar — exactamente o que não se quer.

## Em dupla qualificação

Para o **SMAS** qualificado como **entidade essencial**, a continuidade exige instrumentos adicionais:

- **Plano específico do sector águas** — disponível como [`plano-incidentes-setor-agua-potavel-nis2.docx`]({{ '/templates/plano-incidentes-setor-agua-potavel-nis2.docx' | relative_url }}).
- **RTO/RPO mais apertados** — interrupção do abastecimento ou da telemetria pode ter implicações de saúde pública.
- **Comunicação à ERSAR** em paralelo à comunicação ao CNCS, quando aplicável.

## Templates aplicáveis

| Template | Grupo / Etiqueta | Notas |
|---|---|---|
| [`politica-backups-nis2.docx`]({{ '/templates/politica-backups-nis2.docx' | relative_url }}) | **Adaptar — Grupo B e A** | Política-mãe de *backups*: frequência, retenção, locais, testes. |
| [`procedimento-testes-pcn-nis2.docx`]({{ '/templates/procedimento-testes-pcn-nis2.docx' | relative_url }}) | **Aplicar — Grupo B e A** | Procedimento de execução periódica de testes ao PCN. |
| [`plano-continuidade-negocio-nis2.docx`]({{ '/templates/plano-continuidade-negocio-nis2.docx' | relative_url }}) | **Adaptar — Grupo B e A** | Plano de Continuidade de Negócio (PCN). |
| [`plano-recuperacao-desastres-nis2.docx`]({{ '/templates/plano-recuperacao-desastres-nis2.docx' | relative_url }}) | **Adaptar — Grupo A** | Plano de Recuperação de Desastres (DRP). Para Grupo B pode integrar no PCN. |
| [`analise-impacto-negocio-nis2.xlsx`]({{ '/templates/analise-impacto-negocio-nis2.xlsx' | relative_url }}) | Referência — Grupo A | Análise de Impacto no Negócio (BIA). |
| [`plano-incidentes-setor-agua-potavel-nis2.docx`]({{ '/templates/plano-incidentes-setor-agua-potavel-nis2.docx' | relative_url }}) | **Para SMAS** | Plano específico para o sector água. |

## Próximo passo

[D.3 Controlo de acessos, MFA, palavras-passe →]({% link 03-outras-medidas/d3-acessos-mfa.md %})
