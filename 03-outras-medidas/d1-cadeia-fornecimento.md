---
title: "D.1 Cadeia de fornecimento"
layout: default
parent: "D. Outras medidas do art. 27.º"
nav_order: 1
---

# D.1 Cadeia de fornecimento

**Duração**: 20 min · **Base legal**: art. 27.º al. c) RJC + art. 28.º RJC + Anexo IV **O.PSF** (Política de Segurança da cadeia de Fornecimento).

Esta é a medida que mais directamente toca a realidade quotidiana de qualquer câmara portuguesa: uma autarquia média **não opera os seus próprios sistemas**. Opera-os através de **fornecedores** — Medidata, AIRC, Glintt, Visionware, AMA, Microsoft, ISP, alojamento, fornecedor de segurança de rede. Quando um deles é comprometido, o problema é vosso. Quando um deles altera silenciosamente uma cláusula contratual, o risco vem para o vosso colo. O Anexo IV exige que a câmara **conheça**, **classifique** e **monitorize** esta dependência — não que a elimine (seria irrealista), mas que a torne **gerível**.

## O que a lei diz

> «As entidades essenciais e importantes (...) gerem os riscos de ciberseguranca que se colocam na cadeia de abastecimento, incluindo dos aspetos relacionados com a segurança dos fornecedores diretos.» — art. 28.º, n.º 1 RJC (paráfrase)

> «As entidades públicas relevantes asseguram a segurança das relações com os fornecedores, exigindo-lhes o cumprimento de requisitos de segurança proporcionais ao risco.» — Anexo IV, medida **O.PSF** (paráfrase aplicável a Grupos A e B)

O art. 28.º dirige-se literalmente a entidades essenciais e importantes, mas a sua **lógica é transversal**: para uma autarquia, o regime equivalente está na medida O.PSF do Anexo IV, em duas intensidades distintas para Grupo A e Grupo B.

## A realidade autárquica

Uma câmara média portuguesa depende, na prática, de **uma mão-cheia de fornecedores TIC** para tudo o que é digital:

- **Software de gestão municipal**: tipicamente **Medidata** (contabilidade, recursos humanos, gestão documental) ou **AIRC** ou **Glintt** ou **Sciencephere**. Frequentemente **fornecedor único** sem alternativa funcional a curto prazo.
- **Portal do munícipe + balcão único**: o mesmo fornecedor da gestão municipal, ou um especializado (Visionware, **AMA**).
- **Microsoft 365**: e-mail, identidade, OneDrive, Teams — base operacional indispensável.
- **SIG cadastral**: ESRI, QGIS+Geomedia, ou fornecedor especializado.
- **Alojamento / cloud**: pode ser interno (datacenter da câmara) ou externo (Azure, AWS, OVH, fornecedor local).
- **ISP / operador**: NOS, MEO, Vodafone — conexão à Internet.
- **Segurança de rede**: firewall, antivírus, MDR/SOC se aplicável.

A maior parte destes fornecedores está numa **posição de poder negocial elevado** face à câmara — não há substituibilidade fácil, há *lock-in* de dados, e os contratos são frequentemente padronizados sem possibilidade de adaptação significativa.

## Para o Grupo B — inventário e contactos

Para uma autarquia de Grupo B, a medida O.PSF concretiza-se em **dois entregáveis mínimos**:

1. **Inventário de fornecedores TIC críticos** com:
   - Identificação do fornecedor (nome, NIF, contactos).
   - Serviço prestado.
   - Criticidade para a entidade.
   - Acesso a dados pessoais (sim/não) — interface com RGPD.
   - Contrato em vigor (referência, validade).
   - **Ponto de contacto** designado pelo fornecedor para **comunicação de incidentes** (esta é a obrigação operacional mais importante).

2. **Comunicação de incidentes** — exigência contratual de que o fornecedor notifique a câmara em **prazo curto** (24-72h) qualquer incidente que possa afectar a sua entidade. Sem esta exigência contratual, o cumprimento do prazo de 24h do art. 42.º RJC pelo fornecedor é fortuito — e o relógio NIS2 começa quando vocês souberem, o que pode ser tarde demais.

Saída do **[Exercício A5]({% link exercicios/a5-fornecedores.md %})**: top 5 desta lista, classificada por criticidade. Em câmara, alargar para todos os fornecedores TIC.

## Para o Grupo A — instrumentos adicionais

Grupos A acrescentam três peças:

- **Scorecard de avaliação periódica** de cada fornecedor crítico (anual mínimo): cumprimento contratual, incidentes notificados, evolução do risco. Template [`scorecard-fornecedor-nis2.xlsx`]({{ '/templates/scorecard-fornecedor-nis2.xlsx' | relative_url }}).
- **Cláusulas contratuais de ciberseguranca** alinhadas com o Anexo IV — para inserção em novos cadernos de encargos ou adendas voluntárias a contratos em vigor. Template [`clausulas-seguranca-fornecedores-nis2.docx`]({{ '/templates/clausulas-seguranca-fornecedores-nis2.docx' | relative_url }}).
- **Due diligence pré-contratual** — questionário a enviar ao fornecedor antes de adjudicar um novo contrato. Template [`questionario-due-diligence-fornecedor-nis2.docx`]({{ '/templates/questionario-due-diligence-fornecedor-nis2.docx' | relative_url }}).
- **Política formal** de gestão da cadeia de fornecimento aprovada por despacho do presidente. Template [`politica-cadeia-fornecimento-nis2.docx`]({{ '/templates/politica-cadeia-fornecimento-nis2.docx' | relative_url }}).

## Sidebar — dupla qualificação

Para o **SMAS** ou empresa municipal qualificada como **entidade essencial**, o **art. 28.º RJC aplica-se directamente** — não a versão atenuada do Anexo IV. Implicação: gestão activa de risco da cadeia, não apenas inventário. Para fornecedores SCADA do SMAS (telemetria de redes de água, sistemas de bombagem), a obrigação é particularmente rigorosa e pode envolver auditoria pelos serviços, certificação obrigatória do fornecedor, e ligações contínuas de monitorização.

## Articulação com RGPD

Sempre que um fornecedor **acede a dados pessoais** de munícipes, é **subcontratante de tratamento** (art. 28.º RGPD) e exige:

- **Contrato escrito** com cláusulas obrigatórias do art. 28.º, n.º 3 RGPD.
- **Obrigação de notificação** em caso de violação (art. 33.º RGPD).
- **Possibilidade de auditoria** pela câmara como responsável pelo tratamento.

A coluna "Acesso a dados pessoais?" do inventário é a primeira triagem; todos os "Sim" devem ter contrato RGPD em ordem **independentemente** do NIS2.

## Templates aplicáveis

| Template | Grupo / Etiqueta | Notas |
|---|---|---|
| [`inventario-fornecedores-nis2.xlsx`]({{ '/templates/inventario-fornecedores-nis2.xlsx' | relative_url }}) | **Aplicar — Grupo B e A** | Inventário operacional dos fornecedores TIC. Saída do Exercício A5 alargada. |
| [`clausulas-seguranca-fornecedores-nis2.docx`]({{ '/templates/clausulas-seguranca-fornecedores-nis2.docx' | relative_url }}) | **Adaptar — Grupo B e A** | Cláusulas-tipo de ciberseguranca para inserir em cadernos de encargos. |
| [`questionario-due-diligence-fornecedor-nis2.docx`]({{ '/templates/questionario-due-diligence-fornecedor-nis2.docx' | relative_url }}) | Referência — Grupo A | Questionário pré-contratual. |
| [`scorecard-fornecedor-nis2.xlsx`]({{ '/templates/scorecard-fornecedor-nis2.xlsx' | relative_url }}) | Grupo A | Scorecard de avaliação periódica. |
| [`politica-cadeia-fornecimento-nis2.docx`]({{ '/templates/politica-cadeia-fornecimento-nis2.docx' | relative_url }}) | **Adaptar — Grupo A** | Política formal. Boa prática para Grupo B mesmo sem ser obrigatória. |

## Exercício associado

[Exercício A5 — Top 5 fornecedores TIC]({% link exercicios/a5-fornecedores.md %}) (10 min, individual) — listar os 5 fornecedores mais críticos da vossa autarquia, classificar por criticidade e identificar risco principal.

## Próximo passo

[D.2 Continuidade, backups e recuperação →]({% link 03-outras-medidas/d2-continuidade-backups.md %})
