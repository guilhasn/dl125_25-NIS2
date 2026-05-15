---
title: "Anexo IV — medidas O/T/H"
layout: default
parent: "Recursos"
nav_order: 2
search_exclude: false
---

# Anexo IV do Aviso 5146/2026/2 — Medidas O / T / H

> ⚠️ **Preliminar.** A **consulta pública** do Aviso 5146/2026/2 **terminou em 22 de Abril de 2026**. O CNCS está agora na **fase de análise dos contributos e redacção da versão final**, que será publicada no Diário da República em data ainda não anunciada. Os códigos e nomes apresentados aqui reflectem o **projecto** posto a consulta — podem sofrer alterações terminológicas na versão final. Esta página será actualizada quando o diploma for publicado em definitivo.

O Anexo IV organiza as medidas obrigatórias em **três famílias**, identificadas pela primeira letra do código:

- **O — Organizacionais** — políticas, processos, decisões de gestão. Não são tecnologia; são *como a câmara se organiza* para enfrentar a ciberseguranca.
- **T — Técnicas** — controlos tecnológicos concretos. Configurações, *software*, *hardware* específicos.
- **H — Humanas** — formação, sensibilização, exercícios. Pessoas.

Cada código tem o formato **`X.YY`** ou **`X.YYY`**. Sempre que um destes códigos aparece num bloco do hub, **passa o cursor por cima** para ver o nome rápido ou **clica** para vir a esta página com a definição completa.

## Como ler a tabela de aplicabilidade

| Símbolo | Significado |
|---|---|
| **B** | Aplica-se ao Grupo B (autarquias 75-249 trabalhadores) |
| **A** | Aplica-se ao Grupo A (autarquias ≥ 250 trabalhadores) — **cumulativo** com o Grupo B |
| **A·B** | Aplica-se a ambos (Grupo A e B) |
| **SMAS** | Aplica-se também (com maior intensidade) a entidades essenciais — Anexo III |

---

## O — Medidas Organizacionais

### `O.CRI` — Comunicação e Resposta a Incidentes {#o-cri}

**Aplicabilidade**: A·B · **Base**: art. 27.º al. a) RJC

Designação de **ponto de contacto** para comunicação com o CNCS e estrutura mínima de resposta a incidentes. Para Grupo B, basta o ponto de contacto; Grupo A adiciona políticas formais. Para entidades essenciais (SMAS), aplicam-se os papéis formais de **RC** (Responsável de Ciberseguranca — art. 31.º) e **PCP** (Ponto de Contacto Permanente — art. 32.º).

Ver: [C.1 Plano de resposta a incidentes]({% link 02-notificacao-incidentes/c1-plano-resposta.md %}).

### `O.PCN` — Plano de Continuidade de Negócio {#o-pcn}

**Aplicabilidade**: A·B · **Base**: art. 27.º al. b) RJC + Anexo III

Plano que descreve como a câmara continua a funcionar perante indisponibilidade de sistemas críticos — quem dispara o quê, atendimento em modo degradado, comunicação a vereadores e imprensa. Distinto do plano de **recuperação de desastres** (DRP), que é técnico.

Ver: [D.2 Continuidade e backups]({% link 03-outras-medidas/d2-continuidade-backups.md %}).

### `O.PSF` — Política de Segurança da cadeia de Fornecimento {#o-psf}

**Aplicabilidade**: A·B · **Base**: art. 27.º al. c) + art. 28.º RJC

Para Grupo B: inventário de fornecedores TIC críticos + identificação de pontos de contacto + comunicação contratual de incidentes. Para Grupo A: política completa com critérios de aceitação, scorecards e auditoria.

Ver: [D.1 Cadeia de fornecimento]({% link 03-outras-medidas/d1-cadeia-fornecimento.md %}).

### `O.GAP` — Gestão de Acessos e Privilégios {#o-gap}

**Aplicabilidade**: B · **Base**: art. 27.º al. h) RJC

Procedimentos mínimos de gestão de contas e privilégios. Para Grupo A é expandido em medidas mais específicas (`O.PAP`, `O.PUA`, `O.PP`).

### `O.GMO` — Gestão de Mudanças nas Operações {#o-gmo}

**Aplicabilidade**: B · **Base**: art. 27.º al. e) + h) RJC

Controlo de alterações em configurações, sistemas e equipamentos. Inclui o registo das mudanças e a aprovação prévia.

### `O.GEC` — Gestão de Eventos de Ciberseguranca {#o-gec}

**Aplicabilidade**: A · **Base**: art. 27.º al. h) RJC

Procedimento estruturado de recolha, triagem e análise de eventos de segurança. Liga-se directamente ao `T.MA` (monitorização técnica).

### `O.IAC` — Inventariação de Activos Críticos {#o-iac}

**Aplicabilidade**: A·B · **Base**: art. 27.º al. h) RJC

Inventário dos sistemas, equipamentos e aplicações sem os quais a câmara deixa de prestar serviço público. Para Grupo B, foca em activos críticos (tipicamente 20-40); para Grupo A, inventário completo.

Ver: [B.3 Inventário e classificação de activos]({% link 01-gestao-risco/b3-inventario-ativos.md %}) · [Exercício A3]({% link exercicios/a3-inventario.md %}).

### `O.ID` — Identificação de funções e activos críticos {#o-id}

**Aplicabilidade**: A · **Base**: art. 27.º al. h) RJC

Cruza o inventário com as **funções/actividades críticas** da câmara — matriz funções × activos com dependências. Base da BIA e do plano de continuidade.

Ver: [B.3 Inventário e classificação de activos]({% link 01-gestao-risco/b3-inventario-ativos.md %}).

### `O.PSI` — Política de Classificação da Informação {#o-psi}

**Aplicabilidade**: A · **Base**: art. 27.º al. h) RJC

Define níveis de sensibilidade dos dados (público / interno / confidencial / restrito). Cada activo que armazena dados é classificado pelo nível mais elevado dos dados que contém.

### `O.PAP` — Política de Acessos e Privilégios {#o-pap}

**Aplicabilidade**: A · **Base**: art. 27.º al. h) RJC

Política formal de **privilégio mínimo**, ciclo de vida das contas, revisões periódicas. Para Grupo B existe sob a forma agregada `O.GAP`.

Ver: [D.3 Acessos, MFA e palavras-passe]({% link 03-outras-medidas/d3-acessos-mfa.md %}).

### `O.PUA` — Política de Utilização Aceitável {#o-pua}

**Aplicabilidade**: A · **Base**: art. 27.º al. h) RJC

Política sobre o uso aceitável dos meios informáticos da câmara — equipamentos, e-mail, Internet, *cloud*, dispositivos pessoais (BYOD).

### `O.PP` — Política de Palavras-Passe {#o-pp}

**Aplicabilidade**: A · **Base**: art. 27.º al. h) + i) RJC

Política formal de palavras-passe, alinhada com a abordagem moderna do NIST (comprimento ≥ 12, sem rotação obrigatória, verificação contra senhas comprometidas, gestores institucionais).

Ver: [D.3 Acessos, MFA e palavras-passe]({% link 03-outras-medidas/d3-acessos-mfa.md %}).

---

## T — Medidas Técnicas

### `T.AM` — Autenticação Multi-factor {#t-am}

**Aplicabilidade**: A·B · **Base**: art. 27.º al. i) RJC

MFA obrigatório para acessos administrativos e remotos. Em Grupo B, foco em aplicações críticas; em Grupo A, alargado a todas as contas privilegiadas.

Ver: [D.3 Acessos, MFA e palavras-passe]({% link 03-outras-medidas/d3-acessos-mfa.md %}).

### `T.AR` — Acesso Remoto seguro {#t-ar}

**Aplicabilidade**: B · **Base**: art. 27.º al. i) RJC

VPN com MFA, cifragem de canal, terminação numa zona controlada. Sem acessos directos administrativos pela Internet.

### `T.AS` — Actualizações de Segurança {#t-as}

**Aplicabilidade**: A·B · **Base**: art. 27.º al. d) RJC

Aplicação regular de patches críticos. Inventário de sistemas com idade de patch acompanhada.

### `T.CS` — Cópias de Segurança {#t-cs}

**Aplicabilidade**: A·B · **Base**: art. 27.º al. b) RJC

Cópias de segurança regulares, **testadas**, com pelo menos uma cópia *offline* / *air-gapped* para protecção contra ransomware. Frequência mínima recomendada: trimestral para Grupo B, mensal para Grupo A.

Ver: [D.2 Continuidade e backups]({% link 03-outras-medidas/d2-continuidade-backups.md %}).

### `T.GP` — Gestão de Palavras-passe técnica {#t-gp}

**Aplicabilidade**: A · **Base**: art. 27.º al. i) RJC

Mecanismos técnicos para forçar a política de palavras-passe definida em `O.PP`: complexidade, comprimento, validação contra listas de senhas comprometidas, gestores corporativos.

### `T.GPT` — Gestão de Patches {#t-gpt}

**Aplicabilidade**: A·B · **Base**: art. 27.º al. d) RJC

Processo de identificação, teste e instalação de actualizações de segurança em servidores, aplicações e equipamentos. Distinto de `T.AS` (aplicação rotineira); este é o **processo** documentado.

### `T.MA` — Monitorização e Alertas {#t-ma}

**Aplicabilidade**: B · **Base**: art. 27.º al. i) RJC

Sistema básico de monitorização de eventos de segurança e alertas para anomalias.

### `T.PAD` — Privilégios Administrativos Diferenciados {#t-pad}

**Aplicabilidade**: A · **Base**: art. 27.º al. i) RJC

Contas administrativas **segregadas** das contas de utilizador normal. O administrador faz *login* normal com a sua conta de utilizador e **eleva** quando precisa.

### `T.PAS` — Protecção de Acessos a Sistemas {#t-pas}

**Aplicabilidade**: B · **Base**: art. 27.º al. h) + i) RJC

Conjunto de controlos de acesso aos sistemas: autenticação, autorização, registo de acessos.

### `T.PEW` — Protecção de Correio Electrónico e Web {#t-pew}

**Aplicabilidade**: A·B · **Base**: art. 27.º al. g) RJC

Para Grupo B: SPF, DKIM, DMARC no e-mail; HTTPS nos sites institucionais. Para Grupo A: HSTS, cabeçalhos de segurança HTTP, MTA-STS, TLS-RPT.

### `T.RAR` — Registo e Auditoria de Registos {#t-rar}

**Aplicabilidade**: A·B · **Base**: art. 27.º al. b) + i) RJC

*Logs* de eventos de segurança preservados, com retenção mínima e protecção contra alteração. Para Grupo A, recolha centralizada (SIEM) e correlação.

### `T.SC` — Segurança das Comunicações {#t-sc}

**Aplicabilidade**: A · **Base**: art. 27.º al. d) RJC

*Hardening* de canais de comunicação, segmentação de rede, cifragem em trânsito de comunicações sensíveis. Inclui DMZ, VLANs por sensibilidade, *firewall* aplicacional.

---

## H — Medidas Humanas

### `H.PF` — Plano de Formação e Sensibilização {#h-pf}

**Aplicabilidade**: A·B · **Base**: art. 27.º al. g) + f) RJC

Plano anual de formação por perfil (administrativos, dirigentes, técnicos, autarcas), com registo de presenças e avaliação. Mínimo anual, com *refreshers* curtos trimestrais ou semestrais.

Ver: [D.4 Formação e sensibilização]({% link 03-outras-medidas/d4-formacao.md %}).

### `H.FIC` — Formação Inicial e Contínua {#h-fic}

**Aplicabilidade**: A·B · **Base**: art. 27.º al. f) RJC

Componente da formação para todos os trabalhadores no acto de **entrada** (*onboarding*) e em momentos de **actualização** ao longo do ciclo de vida do trabalhador.

Ver: [D.3 Acessos, MFA e palavras-passe]({% link 03-outras-medidas/d3-acessos-mfa.md %}) (secção *onboarding*).

### `H.EC` — Exercícios Controlados {#h-ec}

**Aplicabilidade**: A · **Base**: art. 27.º al. f) RJC

Campanhas internas de **phishing simulado** periódicas, com medição da taxa de cliques e *follow-up* educativo não-punitivo. Para Grupo B é boa prática; para Grupo A é exigência.

Ver: [D.4 Formação e sensibilização]({% link 03-outras-medidas/d4-formacao.md %}).

---

## Convenção tipográfica no hub

Para tornar a leitura mais fluida, no resto do hub:

- A **primeira ocorrência** de cada código numa página é **clicável** e tem **tooltip** (passe o cursor para ver o nome rápido). Exemplo: [<abbr title="Política de Acessos e Privilégios">**O.PAP**</abbr>]({% link recursos/anexo-iv-aviso-5146.md %}#o-pap).
- As **ocorrências seguintes** ficam em **bold** sem link — para evitar poluição visual. Use o botão *back* do *browser* para regressar à página de onde veio.

## Glossário de siglas auxiliares

| Sigla | Significado |
|---|---|
| **RJC** | Regime Jurídico da Ciberseguranca (anexo ao DL 125/2025) |
| **Aviso 5146** | Aviso n.º 5146/2026/2 — regulamento de execução do RJC |
| **CNCS** | Centro Nacional de Ciberseguranca |
| **CNPD** | Comissão Nacional de Protecção de Dados |
| **RC** | Responsável de Ciberseguranca (art. 31.º RJC, apenas essenciais e importantes) |
| **PCP** | Ponto de Contacto Permanente (art. 32.º RJC, apenas essenciais e importantes) |
| **BIA** | *Business Impact Analysis* — Análise de Impacto no Negócio |
| **PCN** | Plano de Continuidade de Negócio |
| **DRP** | *Disaster Recovery Plan* — Plano de Recuperação de Desastres |
| **MFA** | *Multi-Factor Authentication* — Autenticação Multi-factor |
| **SCADA** | *Supervisory Control and Data Acquisition* — sistemas de controlo industrial |
| **SMAS** | Serviços Municipalizados de Água e Saneamento |
| **OT** | *Operational Technology* — tecnologia operacional, distinta da TI corporativa |
