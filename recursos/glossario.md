---
title: "Glossário"
layout: default
parent: "Recursos"
nav_order: 4
---

# Glossário

Termos técnicos, acrónimos e siglas utilizados ao longo do hub, ordenados alfabeticamente. Para os códigos de medidas do Anexo IV (O.IAC, T.AM, H.PF, etc.), consulte [Anexo IV — medidas O/T/H]({% link recursos/anexo-iv-aviso-5146.md %}).

## A

**AIRC** — Associação de Informática da Região Centro. Fornecedor frequente de software de gestão municipal em câmaras portuguesas (contabilidade, recursos humanos, gestão documental).

**AMA** — Agência para a Modernização Administrativa. Entidade pública que opera serviços partilhados como o Balcão Único, a Chave Móvel Digital e a Plataforma de Interoperabilidade.

**ANC** — Autoridade Nacional de Cibersegurança. Função atribuída ao CNCS.

**Anexo III** — Anexo do Aviso 5146/2026/2 com as medidas para entidades essenciais e importantes (com níveis Básico/Substancial/Elevado). Ver [Anexo III vs Anexo IV]({% link roteiro-essencial/anexo-iii-vs-anexo-iv.md %}).

**Anexo IV** — Anexo do Aviso 5146/2026/2 com as medidas para entidades públicas relevantes (Grupos A e B) — directamente aplicável às autarquias. Ver [Anexo IV — medidas O/T/H]({% link recursos/anexo-iv-aviso-5146.md %}).

**Auto-identificação** — Procedimento pelo qual cada entidade se classifica formalmente na plataforma MyCiber (*art. 8.º RJC*{:.legal}). Prazo: 60 dias após disponibilização da funcionalidade.

**Aviso 5146/2026/2** — Aviso do CNCS que aprova o regulamento de execução do RJC. Em fase de redacção da versão final após consulta pública. Ver [legislação completa]({% link recursos/legislacao-aviso-5146.md %}).

## B

***Air-gap*** — Cópia de segurança fisicamente desconectada da rede. Protecção essencial contra ransomware (que procura e encripta *backups* online).

***Backup*** — Cópia de segurança de dados. No NIS2, **não basta existir** — tem de ser **testado** regularmente.

**BIA** (*Business Impact Analysis*) — Análise de Impacto no Negócio. Cruza activos críticos com processos da entidade para estimar o impacto de cada sistema parado durante 1h, 4h, 1 dia, 1 semana.

**Bloco A/B/C/D/E** — Estrutura do dia da formação. A: Enquadramento legal. B: Análise de risco. C: Notificação de incidentes. D: Outras medidas. E: Supervisão e roadmap.

## C

**CASC** — Conselho de Acompanhamento para a Segurança do Ciberespaço.

**CC** — Cartão de Cidadão. Um dos dois meios de autenticação no MyCiber (o outro é a Chave Móvel Digital).

**CERT.PT** — *Computer Emergency Response Team* português, integrado no CNCS. Equipa operacional de resposta a incidentes.

***Cheatsheet*** — Folha-resumo de bolso. Neste hub, refere-se sobretudo à folha-resumo de prazos PT vs NIS2 e ao roadmap de 6 meses.

**CMD** — Chave Móvel Digital. Meio de autenticação electrónica via app no telemóvel, alternativo ao Cartão de Cidadão.

**CNCS** — Centro Nacional de Cibersegurança. Autoridade nacional para a aplicação do RJC.

**CNPD** — Comissão Nacional de Protecção de Dados. Autoridade nacional do RGPD. Recebe as notificações de violação de dados pessoais (72h).

**CSSC** — Conselho Superior de Segurança do Ciberespaço.

## D

**DDoS** (*Distributed Denial of Service*) — Ataque de negação de serviço distribuído. Tráfego anómalo massivo destinado a tornar serviços inacessíveis. Cenário 3 do exercício A4.

**DKIM** (*DomainKeys Identified Mail*) — Mecanismo de autenticação de e-mail por assinatura digital do domínio. Recomendado como mínimo para autarquias.

**DL 125/2025** — Decreto-Lei n.º 125/2025, de 4 de Dezembro. Transpõe a Directiva NIS2 para Portugal. Em vigor desde 3 de Abril de 2026. Ver [legislação completa]({% link recursos/legislacao-dl-125-2025.md %}).

**DMARC** (*Domain-based Message Authentication, Reporting and Conformance*) — Mecanismo de validação de e-mail que reforça SPF e DKIM. Recomendado como mínimo.

**DPO** (*Data Protection Officer*) — Encarregado de Protecção de Dados, obrigatório no RGPD para entidades públicas. Articula com o ponto de contacto NIS2 na decisão de notificação cruzada CNCS+CNPD.

**DRE** — Diário da República Electrónico. Fonte oficial de publicação dos diplomas.

**DRP** (*Disaster Recovery Plan*) — Plano de Recuperação de Desastres. Componente técnico do plano de continuidade, foca-se em **como repõem os sistemas**.

**Dupla qualificação** — Situação em que a mesma autarquia tem entidades que qualificam em categorias diferentes (câmara como pública relevante + SMAS como essencial). Ver [Roteiro essencial]({% link roteiro-essencial/index.md %}).

## E

**ENISA** — *European Union Agency for Cybersecurity*. Agência europeia de referência, publica directrizes e guias.

**Entidade essencial** — Categoria mais exigente do RJC (art. 6.º). Aplica-se a operadores de sectores do Anexo I (energia, água, transportes, etc.) acima dos limiares de média empresa.

**Entidade importante** — Categoria intermédia do RJC. Aplica-se a operadores de sectores do Anexo II (resíduos, indústria, etc.) acima dos limiares.

**Entidade pública relevante** — Categoria das autarquias (*art. 7.º RJC*{:.legal}). Subdivide-se em **Grupo A** (≥ 250 trabalhadores) e **Grupo B** (75-249).

**ERSAR** — Entidade Reguladora dos Serviços de Águas e Resíduos. Articula-se com o CNCS em incidentes que afectem a parte SMAS de uma autarquia.

**Exfiltração** — Saída não autorizada de dados de um sistema. Frequente em ataques de ransomware modernos (*double extortion*).

**Exposição** — Conjunto de activos directamente acessíveis pela Internet. Em NIS2 PT, regulado pelo *art. 32.º do Aviso*{:.legal} (lista a comunicar ao CNCS).

## F

**Ficha de cenário** — Folha A5 com descrição de incidente, distribuída por sorteio aos formandos no Exercício A4. As 4 fichas (ransomware, fornecedor, DDoS, phishing) estão em [exercicios/a4-notificacao]({% link exercicios/a4-notificacao.md %}).

**FIDO2** — Norma de autenticação multi-factor com tokens físicos (chaves USB ou NFC). Recomendada para acesso administrativo, especialmente em sistemas OT.

**Fim de impacto significativo** — Notificação específica do regime português (*art. 43.º RJC*{:.legal}). Submete-se 24h após cessação do impacto significativo do incidente.

## G

***Gestor de palavras-passe*** — *Software* que armazena, gera e preenche palavras-passe únicas por serviço. Eliminação do reutilizar a mesma password.

**GED** — Gestão Electrónica de Documentos. Aplicação central em câmaras portuguesas, frequentemente fornecida por Medidata, AIRC ou Glintt.

**GNS** — Gabinete Nacional de Segurança. Autoridade responsável pela segurança da informação classificada.

**Grupo A** — Subcategoria de entidade pública relevante para autarquias com **≥ 250 trabalhadores** (*art. 7.º RJC*{:.legal}). Aplica-se acumulativamente ao Grupo B + medidas adicionais.

**Grupo B** — Subcategoria para autarquias com **75 a 249 trabalhadores**. Medidas mínimas do Anexo IV.

## H

**HSTS** (*HTTP Strict Transport Security*) — Cabeçalho HTTP que força navegadores a usar HTTPS. Recomendado para Grupo A.

## I

**ID único da notificação** — Referência atribuída pelo MyCiber a cada notificação inicial submetida. Todas as notificações subsequentes relacionadas usam o mesmo ID (*art. 22.º do Aviso*{:.legal}).

**Incidente significativo** — Critério do *art. 40.º, n.º 3 RJC*{:.legal}: incidente que cause perturbação operacional grave **ou** afecte terceiros provocando prejuízos materiais ou imateriais consideráveis. Limiar de notificação obrigatória.

**Inventário de activos** — Lista dos sistemas, equipamentos e aplicações da entidade. Para Grupo B: foca-se nos **críticos** (medida [O.IAC]({% link recursos/anexo-iv-aviso-5146.md %}#o-iac)). Para Grupo A: alargado a todos.

**ISO/IEC 27001** — Norma internacional de sistema de gestão de segurança da informação. Não obrigatória mas serve como ponto de chegada metodológico — quem está certificado cumpre a maior parte do Anexo IV.

**ISO/IEC 27005** — Norma internacional de gestão de riscos de segurança da informação. Base teórica para a análise de risco. Ver [B.2]({% link 01-gestao-risco/b2-analise-risco.md %}).

## J

**JOUE** — Jornal Oficial da União Europeia. Onde foi publicada a Directiva NIS2 (2022/2555).

## L

**LCC** (Lei do Cibercrime) — Lei n.º 109/2009. Tipifica os crimes informáticos. Articulada com o RJC via art. 8.º-A introduzido pelo DL 125/2025.

**Lei 46/2018** — Regime jurídico anterior ao DL 125/2025. **Revogada** (art. 9.º do articulado preambular do DL).

**Lei 58/2019** — Execução nacional do RGPD em Portugal.

**Lei 109/2009** — Ver LCC.

## M

**MFA** (*Multi-Factor Authentication*) — Autenticação Multi-factor. Combinação de pelo menos dois elementos: o que se sabe (palavra-passe), o que se tem (telemóvel, token) e o que se é (biometria). Medida [T.AM]({% link recursos/anexo-iv-aviso-5146.md %}#t-am).

**Medidata** — Fornecedor frequente de software de gestão municipal (contabilidade, RH, GED, portal do munícipe).

**Município** — Sinónimo de autarquia local de primeiro nível. A entidade jurídica é a "Câmara Municipal de XPTO".

**MyCiber** — Plataforma electrónica do CNCS em [myciber.gov.pt](https://myciber.gov.pt/){:target="_blank"}. Canal único e oficial. Ver [A.3]({% link 00-enquadramento/a3-plataforma-cncs.md %}).

## N

**Negligência** — Modalidade subjectiva da infracção. *art. 64.º RJC*{:.legal}: reduz a metade os limites das coimas.

**NIS2** — Directiva (UE) 2022/2555 sobre segurança das redes e da informação, 2.ª geração. Transposta para Portugal pelo DL 125/2025.

**NIST CSF** — *NIST Cybersecurity Framework*. Framework americano de referência. A versão 2.0 (2024) é a base do QNRCS português.

**Notificação inicial** — Notificação obrigatória nas 24h após verificação de um incidente significativo (*art. 42.º RJC*{:.legal}).

## O

***Offboarding*** — Processo de saída de um trabalhador da entidade. Inclui revogação de credenciais, devolução de equipamento, transferência de ficheiros à chefia.

***Onboarding*** — Processo de entrada de um trabalhador na entidade. Inclui criação de conta, atribuição de privilégios mínimos, configuração de MFA, formação inicial obrigatória, assinatura do termo de confidencialidade.

**OT** (*Operational Technology*) — Tecnologia operacional. Distinta da TIC corporativa. Inclui sistemas SCADA, telemetria, automatismos industriais. Crítico em SMAS e empresas municipais de transportes.

## P

**PCN** — Plano de Continuidade de Negócio. Componente organizacional do plano de continuidade, foca-se em **como continua a câmara a funcionar** com sistemas em baixo.

**PCP** — Ponto de Contacto Permanente. Designação formal obrigatória para entidades essenciais e importantes (*art. 32.º RJC*{:.legal}). Disponibilidade 24/7 para comunicações urgentes.

**Phishing** — Engenharia social via e-mail (ou outros canais) para obter credenciais ou induzir acções fraudulentas. Cenário 4 do Exercício A4.

***Playbook*** — Documento operacional com sequência de passos para responder a um tipo específico de incidente (ransomware, *data breach*, phishing dirigido).

**Ponto de contacto** — Pessoa designada pela entidade pública relevante para comunicação com o CNCS. Não confundir com PCP (que é apenas para essenciais/importantes).

**Privilégio mínimo** — Princípio segundo o qual cada utilizador tem **exactamente as permissões necessárias** para a sua função, nem mais nem menos. Medida [O.PAP]({% link recursos/anexo-iv-aviso-5146.md %}#o-pap).

## Q

**QNRCS** — Quadro Nacional de Referência para a Ciberseguranca. Aprovado pelo Anexo I do Aviso 5146/2026/2. Alinhado com NIST CSF 2.0 e ISO 27001:2022.

## R

**Ransomware** — Software malicioso que encripta dados e exige resgate. Cenário 1 do Exercício A4.

**RC** — Responsável de Cibersegurança. Designação formal obrigatória para entidades essenciais e importantes (*art. 31.º RJC*{:.legal}). Pessoa singular com formação e independência funcional.

**RGPD** — Regulamento Geral de Protecção de Dados (UE 2016/679). Articula-se com o NIS2 na notificação de incidentes que envolvam dados pessoais (ver [C.4]({% link 02-notificacao-incidentes/c4-cruzamento-rgpd.md %})).

**RJC** — Regime Jurídico da Ciberseguranca. Aprovado em anexo ao DL 125/2025. Ver [legislação completa]({% link recursos/legislacao-dl-125-2025.md %}).

**Roteiro essencial** — Conjunto de páginas do hub dedicado à dupla qualificação. Ver [Roteiro essencial]({% link roteiro-essencial/index.md %}).

**RPO** (*Recovery Point Objective*) — Quanta perda de dados é aceitável após um incidente. Em horas. Define a frequência mínima de *backup*.

**RTO** (*Recovery Time Objective*) — Quanto tempo é aceitável estar sem o serviço após um incidente. Em horas. Define o esforço de recuperação.

## S

**SCADA** (*Supervisory Control and Data Acquisition*) — Sistemas de controlo industrial. Relevante para SMAS (gestão de bombagem, telemetria de redes de água), transportes públicos, sistemas de iluminação.

**SIEM** (*Security Information and Event Management*) — Plataforma de recolha centralizada de *logs* e correlação. Exigida em Grupo A e essenciais Substancial+.

**Simulador (MyCiber)** — Ferramenta indicativa no MyCiber para testar a categoria aplicável a uma entidade. Não vinculativa.

**SMAS** — Serviços Municipalizados de Água e Saneamento. Entidade satélite da câmara, frequentemente qualificada como **entidade essencial** (sector Anexo I).

**SOA** (*Statement of Applicability*) — Declaração de aplicabilidade. Documento típico ISO 27001 que lista quais controlos são aplicáveis à entidade.

**SPF** (*Sender Policy Framework*) — Mecanismo DNS que declara quais servidores estão autorizados a enviar e-mail em nome de um domínio. Recomendado como mínimo para autarquias.

**Supervisão *ex ante*** — Regime de supervisão das entidades essenciais e importantes (*art. 53.º RJC*{:.legal}). Inspecções programadas, relatórios anuais.

**Supervisão *ex post*** — Regime de supervisão das entidades públicas relevantes (autarquias) (*art. 55.º RJC*{:.legal}). Apenas perante motivo (incidente, denúncia, amostragem).

## T

**Tabletop exercise** — Exercício de simulação em mesa, sem activação técnica real. Tipicamente 30-60 min com gabinete + informática + DPO sobre um cenário hipotético.

**TIC** — Tecnologias de Informação e Comunicação. Distinta de OT (tecnologia operacional).

## V

**Verificação** — Momento em que a equipa TIC **confirma** a natureza e o impacto de um incidente. Distinto da detecção (alerta inicial). Inicia o relógio dos 24h NIS2.

## Referências cruzadas

- [Anexo IV — medidas O/T/H]({% link recursos/anexo-iv-aviso-5146.md %}) — definições detalhadas das 27 medidas.
- [Legislação]({% link recursos/legislacao.md %}) — diplomas centrais e conexos.
- [FAQ]({% link recursos/faq.md %}) — 30 perguntas frequentes.
- [Índice de templates]({% link recursos/templates.md %}) — 76 templates por bloco.
