---
title: "C.7 Resoluções modelo (A4)"
layout: default
parent: "C. Notificação de incidentes"
nav_order: 7
nav_exclude: true
---

# C.7 Resoluções modelo do exercício A4

{: .warning }
> **Aviso — consultar APÓS o exercício.** Esta página contém as resoluções modelo das 4 fichas de cenário. Se ainda não fez o exercício, **pare aqui** e abra primeiro [C.6 Fichas de cenário]({% link 02-notificacao-incidentes/c6-cenarios-exercicio.md %}). As resoluções não são respostas únicas — são pontos de comparação. Há decisões intermédias defensáveis. O propósito é validar o **raciocínio**, não copiar o resultado.

Para cada ficha apresentam-se: **decisão de notificação + cronograma + canais + notificação 24h preenchida + comunicação externa + ponto sensível**. As notificações usam o template [`notificacao-24h-nis2.docx`]({{ '/templates/notificacao-24h-nis2.docx' | relative_url }}).

## Ficha 1 — Ransomware

**Deteção 15:32 · Verificação 15:48 · ~40.000 ficheiros · Indícios de exfiltração**

### Decisão de notificação

**Sim, notificar** ao CNCS em **24h após verificação (T1 = 15:48 → T2 ≤ 15:48 do dia seguinte)**. Atinge o limiar de «significativo» do art. 40.º, n.º 3 do RJC por **três parâmetros cumuláveis**: (1) perturbação operacional grave (registo civil e aprovisionamento são serviços públicos essenciais paralisados), (2) potencial perda de dados pessoais de munícipes (indícios fortes de exfiltração), (3) ataque deliberado e malicioso. Não há ambiguidade — é o cenário-tipo de notificação obrigatória.

### Cronograma decisivo

| Tempo | Ação |
|---|---|
| T0 = 15:32 | Deteção (alerta da equipa TIC) |
| T1 = 15:48 | **Verificação** — relógio NIS2 (24h) e RGPD (72h) iniciam |
| T1 + 1h | Activação do plano de resposta: isolar servidores, notificar DPO e gabinete, contactar fornecedor de M365 e backup, abrir registo cronológico |
| T1 + 6h | Confirmação de impacto e início do rascunho da notificação 24h |
| T1 + 24h (≤ 15:48 dia +1) | **Submissão da notificação inicial CNCS** no MyCiber |
| T1 + 72h | **Submissão da notificação RGPD à CNPD** |
| T0 + 24h (idealmente antes) | Participação ao **Ministério Público** (Lei 109/2009 — crime informático) |

### Canais accionados (matriz)

| Canal | Sim/Não | Base legal | Prazo |
|---|---|---|---|
| **CNCS** (NIS2) | ✅ Sim | art. 40.º, n.º 3 + art. 42.º RJC | 24h após verificação |
| **CNPD** (RGPD) | ✅ Sim | art. 33.º RGPD + Lei 58/2019 | 72h após conhecimento |
| **Ministério Público** | ✅ Sim | Lei 109/2009 (acesso ilegítimo, sabotagem informática) | Sem prazo legal estrito — recomenda-se em paralelo à notificação CNCS |
| **Comunicação a munícipes** (art. 48.º) | ⚠️ Quando confirmado o âmbito | art. 48.º RJC + art. 34.º RGPD se risco elevado | Sem prazo fixo; tipicamente 24-72h após confirmação |

### Notificação 24h modelo (campos do art. 42.º, n.º 2)

```
1. IDENTIFICAÇÃO DA ENTIDADE
   Nome: Município de [Vossa Câmara]
   NIF: [Vosso NIF]
   Categoria NIS2: Entidade pública relevante — Grupo B
   Ponto de contacto: [Nome do responsável], [e-mail], [telemóvel 24/7]

2. HORA DE VERIFICAÇÃO DO INCIDENTE
   15:48 do dia [data]
   (T0 = 15:32 deteção; T1 = 15:48 verificação técnica pela equipa TIC)

3. DESCRIÇÃO SUMÁRIA
   Ataque de ransomware contra três servidores internos da Câmara, incluindo
   o servidor que aloja a aplicação de registo civil e a aplicação de
   aprovisionamento. Bloqueio observável dos ficheiros com mensagem de
   pedido de resgate em criptomoeda. Aproximadamente 40.000 ficheiros
   afetados em volumes partilhados. Indícios fortes de exfiltração prévia
   de pastas contendo dados pessoais de munícipes.

4. ESTIMATIVA DE IMPACTO
   - Serviços afetados: registo civil (atendimento on-line e presencial),
     aprovisionamento, partilha de ficheiros internos.
   - Duração estimada: indeterminada à data — investigação em curso, com
     activação do plano de recuperação a partir de backups offline.
   - Munícipes potencialmente afetados: pendente de análise forense da
     exfiltração; estimativa preliminar até [N] titulares (processos de
     [áreas]).
   - Dimensão dos dados: indícios de exfiltração de [tipos de dados,
     ex.: dados de identificação civil, processos de ação social].

5. OUTRAS INFORMAÇÕES RELEVANTES
   - Suspeita fundada de crime informático — será efectuada participação ao
     Ministério Público nos termos da Lei 109/2009.
   - Será efectuada notificação paralela à CNPD nos termos do art. 33.º RGPD
     no prazo das 72h.
   - Cópias de segurança offline disponíveis (validação técnica em curso).
   - Sistemas afetados isolados da rede.
```

### Comunicação externa

- **Internamente**: presidente + vereadores + gabinete de comunicação informados em T1 + 30 min. Decisão sobre comunicação pública: **adiar** até confirmação do âmbito de exfiltração (provavelmente T0 + 24-48h).
- **Vereador exige resposta sobre imprensa em 30 min**: **prematuro**. Resposta-padrão: «Estamos a estabilizar a situação, vamos comunicar publicamente assim que tivermos factos confirmados, previsivelmente dentro de 24h.»
- **Comunicado público** (T0 + 24-48h): factos confirmados, medidas em curso, recurso para munícipes (linha telefónica, canal alternativo), prazos. Coordenado com gabinete de comunicação. Modelo: [`notificacao-incidente-destinatarios-nis2.docx`]({{ '/templates/notificacao-incidente-destinatarios-nis2.docx' | relative_url }}).

### Ponto sensível

A pressão do Vereador para comunicar à imprensa em 30 minutos. **Não ceder**. Comunicação prematura sem factos confirmados (1) cria pânico desproporcionado, (2) dá vantagem aos atacantes (que podem ainda estar dentro), (3) compromete a investigação criminal. A decisão de quando comunicar é técnica e jurídica, não política. Documentar internamente a recomendação e a decisão final por escrito.

---

## Ficha 2 — Fornecedor de GED comprometido

**Comunicado do fornecedor 09:15 · ~5.000 processos · Dados pessoais confirmados · Sem confirmação de exfiltração**

### Decisão de notificação

**Sim, notificar** ao CNCS em **24h após verificação (T1 = 09:15 da receção do comunicado → T2 ≤ 09:15 do dia seguinte)**. O art. 42.º, n.º 1 do RJC exige notificação quando «possa vir a existir um incidente significativo» — não obriga a aguardar confirmação. Atinge o limiar por **dois parâmetros**: (1) potencial violação de dados pessoais de munícipes em volume relevante (5.000 processos sensíveis), (2) impossibilidade de excluir impacto operacional até confirmação do fornecedor.

### Cronograma decisivo

| Tempo | Ação |
|---|---|
| T0 = 09:15 | Receção do comunicado do fornecedor |
| T0 = T1 | **Verificação** acontece simultaneamente — a entidade não tem visibilidade própria, depende do fornecedor; o relógio começa **agora** |
| T1 + 1h | Activação interna: DPO + jurídico + chefia TIC. Activação da **cláusula contratual** com o fornecedor (informação detalhada em 24-48h, evidência preservada, plano de mitigação) |
| T1 + 6h | Comunicação ao fornecedor exigindo: lista exata dos vossos dados afetados, vector de compromisso, IoCs, plano de remediação. **Em formal**, não verbal |
| T1 + 24h | **Submissão da notificação inicial CNCS** mesmo sem confirmação completa do fornecedor — usar campos com «pendente de investigação do fornecedor» |
| T1 + 72h | Notificação RGPD à CNPD (em paralelo) — mesmo princípio: notificar com informação parcial e atualizar |
| T1 + 30 dias | Relatório final, em articulação com o fornecedor |

### Canais accionados (matriz)

| Canal | Sim/Não | Justificação |
|---|---|---|
| **CNCS** (NIS2) | ✅ Sim | A entidade pública relevante é a **vossa câmara** — não o fornecedor. Vocês têm de notificar. |
| **CNPD** (RGPD) | ✅ Sim | Vocês são o responsável pelo tratamento, o fornecedor é subcontratante. A notificação cabe ao responsável. |
| **MP / Lei 109/2009** | ⚠️ Provável | Ato doloso provável (acesso não autorizado a servidores). Participação ao MP — geralmente o fornecedor já o fez, mas é prudente confirmar e referenciar |
| **Comunicação a munícipes** (art. 48.º) | ⏳ Aguardar | Sem confirmação de exfiltração, prematuro. Decidir após resposta detalhada do fornecedor (T1 + 24-72h) |

### Notificação 24h modelo (resumo)

```
2. HORA DE VERIFICAÇÃO
   09:15 do dia [data] — momento da receção do comunicado do fornecedor
   (não momento em que o fornecedor detectou).

3. DESCRIÇÃO SUMÁRIA
   Comunicado recebido do fornecedor da aplicação de Gestão Documental
   ([nome do fornecedor]) informando da deteção de acessos não autorizados
   a servidores partilhados na semana de [datas]. O fornecedor não confirma,
   à data, se dados da Câmara foram acedidos. A Câmara mantém ~5.000
   processos com dados pessoais de munícipes na referida plataforma.

4. ESTIMATIVA DE IMPACTO
   - Confirmação de exfiltração: pendente. Estimativa máxima ~5.000
     titulares com dados em [áreas: urbanismo, ação social, etc.].
   - Serviços afetados pela aplicação: gestão documental interna. Sem
     impacto direto no atendimento.

5. OUTRAS INFORMAÇÕES RELEVANTES
   - Cláusulas contratuais de notificação activadas; investigação coordenada
     com o fornecedor.
   - Notificação à CNPD em paralelo (no prazo das 72h).
   - Atualização será submetida ao CNCS quando o fornecedor confirmar o
     âmbito (estimativa: T+48-72h).
```

### Ponto sensível

A **distinção entre causa próxima e responsabilidade legal**. O incidente é do fornecedor — mas a entidade legalmente responsável perante o CNCS e a CNPD é a câmara. **Não esperar pelo fornecedor** para notificar; notificar com informação parcial e atualizar. O contrato com o fornecedor deve já prever esta cooperação; se não prevê, **isto é a lição mais importante** deste cenário: rever as cláusulas contratuais de todos os fornecedores TIC críticos. Ver [D.1 — Cadeia de fornecimento]({% link 03-outras-medidas/d1-cadeia-fornecimento.md %}).

---

## Ficha 3 — DDoS contra o Portal do Munícipe

**Deteção 09:30 · Verificação 09:45 · 90 minutos sem serviço · IPs estrangeiros · Prazos legais a expirar**

### Decisão de notificação

**Sim, notificar** ao CNCS — mas com **timing cuidado**. Aos 90 minutos não atinge ainda claramente o limiar de «significativo» (não há violação de dados; não há paragem catastrófica). **Monitorizar 30-60 min adicionais**: se persistir aos 2-4h **e** afetar prazos legais materiais para munícipes, atinge claramente o limiar. Critério prático: 4 horas de indisponibilidade contínua é o marco operacional informal.

### Cronograma decisivo

| Tempo | Ação |
|---|---|
| T0 = 09:30 | Deteção do tráfego anómalo |
| T1 = 09:45 | **Verificação** de DDoS volumétrico em curso — relógio inicia condicional |
| T1 + 30 min | Activação plano de continuidade: comunicação a munícipes pela página alternativa + redes sociais, canal de e-mail dedicado para requerimentos urgentes |
| T1 + 2h | Re-avaliação: se persistir, **notificação CNCS torna-se claramente obrigatória** |
| T1 + 4h | Se ainda em curso, submeter **notificação inicial** — o impacto cumulado claramente significativo |
| T1 + ?? | Submeter **notificação de fim de impacto significativo** (art. 43.º) 24h após cessação |

### Canais accionados (matriz)

| Canal | Sim/Não | Justificação |
|---|---|---|
| **CNCS** (NIS2) | ✅ Sim, condicional ao tempo | Se persistir > 4h ou afetar prazos legais materiais |
| **CNPD** (RGPD) | ❌ Provavelmente não | DDoS é negação de serviço, não acesso a dados. **Exceção**: se houver indícios de DDoS como diversão para ataque paralelo a dados — escalar |
| **MP** | ⚠️ Possível | Se houver pedido de resgate ou motivação criminal identificada |
| **Comunicação a munícipes** | ✅ **Sim, na 1.ª hora** | Não é art. 48.º (ainda) — é boa prática de transparência. Página alternativa + redes sociais + e-mail dedicado para requerimentos urgentes |

### Notificação 24h modelo (se atingir o limiar)

```
2. HORA DE VERIFICAÇÃO
   09:45 — confirmação técnica do ataque DDoS

3. DESCRIÇÃO SUMÁRIA
   Ataque de negação de serviço distribuído (DDoS volumétrico) contra o
   Portal do Munícipe e os formulários digitais da Câmara. Tráfego anormal
   originário de múltiplos IPs estrangeiros, mitigação activada pelo
   fornecedor (WAF + scrubbing). Duração total: [N] horas, com
   recuperação parcial entre [horas]. Sem indícios de acesso a dados ou
   violação de confidencialidade.

4. ESTIMATIVA DE IMPACTO
   - Serviços afetados: Portal do Munícipe, formulários on-line de
     [tipos].
   - Munícipes afetados: estimados [N] tentativas de acesso falhadas;
     prazos legais para [N] requerimentos administrativos potencialmente
     comprometidos — comunicação proativa efectuada.
   - Sem comprometimento de dados pessoais conhecido.

5. OUTRAS INFORMAÇÕES RELEVANTES
   - Plano de continuidade activado: canal alternativo (e-mail dedicado)
     para requerimentos urgentes.
   - Mitigação técnica do fornecedor [nome] em curso.
   - Não houve pedido de resgate; vector aparentemente volumétrico, sem
     componente de extorsão identificada.
```

### Comunicação a munícipes (não é art. 48.º, é boa prática)

- **T1 + 30 min**: aviso na rede social institucional + página alternativa estática (se existir) com mensagem-tipo: «Portal temporariamente indisponível por questão técnica. Requerimentos urgentes: [e-mail dedicado]. Atendimento presencial inalterado. Actualizaremos esta página quando o serviço regressar.»
- **T1 + 4h**: atualização se ainda em curso.
- **Após fim**: comunicado de fim, sem detalhes técnicos do ataque.

### Ponto sensível

A **decisão temporal** sobre o limiar. Notificar com 30 minutos é precipitado e gera ruído ao CNCS. Não notificar com 6 horas é arriscado. A regra prática: **monitorizar ativamente, notificar quando o impacto cumulado ultrapassar 4 horas ou quando se materializar prejuízo concreto a munícipes** (prazo legal perdido). Documentar a decisão e o raciocínio.

---

## Ficha 4 — Phishing com fraude ao Vereador

**Deteção 13:42 · Verificação 13:55 · 200 e-mails fraudulentos · Bancos suspenderam · MFA inactivo**

### Decisão de notificação

**Sim, notificar** ao CNCS em **24h após verificação (T1 = 13:55 → T2 ≤ 13:55 do dia seguinte)**. Atinge o limiar por **três parâmetros**: (1) compromisso da identidade institucional de um titular de cargo electivo, (2) tentativa de fraude com dimensão financeira (transferências para 200 destinos), (3) acesso não autorizado à caixa de e-mail (contém dados pessoais de munícipes em correspondência). Sem ambiguidade.

### Cronograma decisivo

| Tempo | Ação |
|---|---|
| T0 = 13:42 | Alerta automático do Microsoft 365 (deteção comportamental) |
| T1 = 13:55 | **Verificação** — confirmação de envios não autorizados |
| T1 + 5 min | Bloqueio imediato da conta + revogação de tokens + reset forçado de credenciais |
| T1 + 30 min | Activação MFA obrigatório para todos os Vereadores e cargos de chefia (não estava ativo!) |
| T1 + 1h | Comunicação aos 200 fornecedores destinatários do *spear-phishing* — informar da fraude, alertar para potenciais e-mails subsequentes |
| T1 + 6h | Análise forense da caixa — o que esteve acessível ao atacante durante [N] horas? |
| T1 + 24h | **Submissão notificação CNCS** |
| T1 + 72h | **Submissão notificação CNPD** (caixa contém dados pessoais de munícipes) |
| T0 + 24h | Participação ao **MP** — falsificação informática (Lei 109/2009) |

### Canais accionados (matriz)

| Canal | Sim/Não | Justificação |
|---|---|---|
| **CNCS** (NIS2) | ✅ Sim | Limiar claramente ultrapassado |
| **CNPD** (RGPD) | ✅ Sim | A caixa de e-mail do Vereador contém correspondência com dados de munícipes — violação de confidencialidade |
| **MP / Lei 109/2009** | ✅ Sim | Falsificação informática + tentativa de fraude — crimes públicos |
| **Comunicação a destinatários afetados** | ✅ Sim — aos 200 fornecedores | Não é estritamente o art. 48.º (não são todos munícipes), mas comunicação devida e urgente para prevenir consumação da fraude |
| **Bancos** | ✅ Sim — confirmação formal | Confirmar a paragem das transferências, registar IDs das tentativas para inquérito criminal |

### Notificação 24h modelo (resumo)

```
2. HORA DE VERIFICAÇÃO
   13:55 do dia [data] — confirmação técnica de envios não autorizados a
   partir da caixa de e-mail de um titular de cargo electivo

3. DESCRIÇÃO SUMÁRIA
   Compromisso da caixa de e-mail institucional de um Vereador
   ([cargo, sem nome se possível por segurança da investigação]) com envio
   de 200 e-mails fraudulentos a fornecedores municipais, contendo pedidos
   de transferência bancária com falsificação de assinatura eletrónica.
   Dois fornecedores tentaram efectuar as transferências; ambos os bancos
   suspenderam as operações em tempo. Vector inicial provável: phishing
   dirigido ao Vereador, sem MFA ativo na sua conta à data do incidente.

4. ESTIMATIVA DE IMPACTO
   - Impacto financeiro materializado: nulo (bancos suspenderam).
   - Impacto financeiro evitado: ~[valor] em transferências tentadas.
   - Dados acedidos: caixa de e-mail completa do Vereador (período N de
     correspondência institucional, contendo correspondência com munícipes).
   - Reputacional: elevado — gestão pública alvo, comunicação interna
     ainda em curso.

5. OUTRAS INFORMAÇÕES RELEVANTES
   - MFA não estava ativo na conta afetada à data do incidente; activação
     forçada para todas as contas privilegiadas como medida correctiva
     imediata.
   - Análise forense em curso para apurar o âmbito de exposição.
   - Comunicação efectuada aos 200 destinatários.
   - Participação ao Ministério Público em curso (Lei 109/2009).
   - Notificação à CNPD em paralelo no prazo das 72h.
```

### Ponto sensível

O **fator humano + organizacional**. A conta tinha privilégios de Vereador, **sem MFA** — falha estrutural identificada no incidente. A ação correctiva imediata (activar MFA para todas as contas privilegiadas) deve ficar **documentada na notificação** como medida pós-incidente — demonstra postura ativa, fundamenta argumentação para dispensa de coimas (art. 65.º), e fecha a vulnerabilidade explorada. Atenção também ao **discurso interno**: o Vereador pode resistir («mas eu não cliquei em nada»). Não é matéria de culpabilização individual — é de política institucional. Activar MFA para todos, incluindo o próprio executivo.

---

## Tabela-síntese das 4 fichas

| Ficha | Limiar significativo? | CNCS | CNPD | MP | Comunicação 48.º | Decisão temporal crítica |
|---|---|---|---|---|---|---|
| **1 Ransomware** | ✅ Inequívoco | 24h | 72h | Sim | Quando confirmado | Não comunicar prematuramente à imprensa |
| **2 Fornecedor** | ✅ Por precaução | 24h (com incompletude) | 72h | Geralmente fornecedor | Aguardar confirmação | Não esperar pelo fornecedor para notificar |
| **3 DDoS** | ⚠️ Condicional | Se > 4h | ❌ Geralmente não | Se motivação criminal | Boa prática imediata | Monitorizar antes de notificar |
| **4 Phishing** | ✅ Inequívoco | 24h | 72h | Sim | Aos 200 fornecedores | Activar MFA já + não culpar Vereador |

## O que estes 4 cenários ensinam ao plano de resposta

1. **A hora de verificação não é a hora de deteção** — define-se com timestamps registados, não memória.
2. **Notificar com informação parcial é melhor que esperar pela completa** — art. 42.º permite, e o atraso é mais grave.
3. **CNCS, CNPD e MP são canais paralelos** — não substitutos. Triângulo.
4. **A pressão política para comunicar à imprensa é gerida pelo gabinete, não pelo técnico** — não responder em 30 minutos.
5. **As medidas correctivas pós-incidente fazem parte da notificação** — demonstram postura ativa, são argumento de dispensa de coimas.
6. **Cada incidente revela uma falha estrutural** — MFA, contrato com fornecedor, plano de continuidade, formação. O *post-mortem* (template [`template-post-incident-review-nis2.docx`]({{ '/templates/template-post-incident-review-nis2.docx' | relative_url }})) é onde se aprende.

## Próximo passo

[← Voltar a C.6 Fichas de cenário]({% link 02-notificacao-incidentes/c6-cenarios-exercicio.md %}) · [Bloco D — Outras medidas →]({% link 03-outras-medidas/index.md %})
