---
title: "B.3 Inventário e classificação de ativos"
layout: default
parent: "B. Art. 27.º — Risco e ativos"
nav_order: 3
---

# B.3 Inventário e classificação de ativos

{: .note }
> **Grupo A** = autarquia com ≥ 250 trabalhadores  
> **Grupo B** = autarquia com 75-249 trabalhadores  
> (art. 7.º RJC — ver [A.2 Quem está abrangido]({% link 00-enquadramento/a2-quem-esta-abrangido.md %}))

O inventário de ativos é o **primeiro entregável tangível** que uma autarquia produz no caminho de conformidade — e o mais difícil de evitar. Sem inventário não há matriz de risco (vimos em [B.2]({% link 01-gestao-risco/b2-analise-risco.md %})), não há gestão de fornecedores, não há plano de continuidade, não há classificação de informação. E, peculiaridade portuguesa: existe ainda um inventário paralelo — a **lista de ativos publicamente acessíveis** — que tem prazo apertado (20 dias úteis após qualificação) e é **transversal** a essenciais, importantes e públicas relevantes. Esta página percorre as três peças: o inventário interno do Grupo B, o inventário ampliado do Grupo A, e a lista pública do art. 32.º do Aviso.

## O que a lei diz

> «A entidade deve inventariar os seus ativos críticos para a execução da sua atividade principal, deve ainda identificar as dependências entre os ativos críticos. A entidade deve atualizar o inventário de ativos críticos regularmente.» — Anexo IV, **medida O.IAC** (Inventariação dos ativos críticos), Grupo B

> «A entidade deve inventariar todos os seus ativos e identificar as dependências entre os mesmos. A entidade deve atualizar o inventário regularmente.» — Anexo IV, **medida O.IAC**, Grupo A (versão ampliada)

> «A entidade deve identificar as funções ou atividades críticas e as dependências existentes das TIC.» — Anexo IV, **medida O.ID** (Identificação de funções ou atividades críticas), Grupo A

> «(...) as entidades essenciais, importantes e públicas relevantes, devem elaborar, manter atualizado e comunicar à autoridade de cibersegurança competente uma lista de todos os ativos essenciais para a prestação dos respetivos serviços, com base no seu inventário de ativos, que estejam diretamente acessíveis publicamente através da Internet.» — art. 32.º, n.º 1 do Aviso 5146/2026/2

Três normas, três entregáveis distintos — mas com uma fonte de dados comum: o inventário interno.

## Grupo B — inventário simplificado

Para uma autarquia de Grupo B, a medida O.IAC exige **dois elementos**:

1. **Lista dos ativos críticos** para a execução da atividade principal — ou seja, dos sistemas sem os quais a câmara deixa de cumprir a sua missão de serviço público.
2. **Identificação das dependências** entre esses ativos críticos — por exemplo, "o portal do munícipe depende do servidor web X, que depende da base de dados Y, alojada no datacenter Z, que depende de electricidade da rede + UPS".

Atenção à palavra-chave **críticos**. O Anexo IV Grupo B **não exige** inventário exaustivo de todo o parque informático (a câmara não tem de listar cada uma das suas 200 estações de trabalho). Exige a lista dos ativos cuja indisponibilidade compromete o serviço — tipicamente **20 a 40 itens** numa câmara média.

Categorias-padrão a percorrer:

- **Servidores** (físicos e virtuais): controlador de domínio, servidor de ficheiros, servidor de e-mail, servidor de base de dados, servidor web.
- **Aplicações de gestão municipal**: software de contabilidade, GED, portal do munícipe, balcão único, SIG cadastral, software de obras, software de licenciamento.
- **Infraestrutura de rede**: firewall principal, switch core, ponto de acesso à Internet, VPN.
- **Serviços externos**: alojamento web/cloud, fornecedor de e-mail (se Microsoft 365 ou Google Workspace), DNS gerido, certificados.
- **Equipamentos especiais**: servidores SCADA se aplicável (raro em câmaras puras; típico em SMAS), terminais de cobrança, equipamentos de vigilância vídeo integrados em rede.

Para cada ativo crítico, registar minimamente: nome/identificador, tipo, responsável funcional na câmara, fornecedor (se externo), serviço/processo que suporta, dependências de outros ativos. O template [`inventario-ativos-tic-nis2.xlsx`]({{ '/templates/inventario-ativos-tic-nis2.xlsx' | relative_url }}) traz estas colunas pré-formatadas.

## Grupo A — inventário completo + classificação

Para autarquias do Grupo A, a obrigação amplia-se em três dimensões:

### Inventário **completo**

A medida O.IAC para Grupo A pede inventário **de todos os ativos** (não só dos críticos) **com identificação dos responsáveis e descrição**. Em câmaras grandes, isto pode significar várias centenas de itens. Estratégia recomendada: **inventário hierárquico** — categorias amplas (estações de trabalho, impressoras, telefones IP) registadas como grupo com contagem, mais inventário individual fino para servidores, aplicações e equipamentos especiais.

### Identificação de funções e ativos críticos (O.ID)

Esta é uma medida adicional do Grupo A que estabelece um pivot importante: o inventário tem de ser cruzado com as **funções ou atividades críticas** da câmara. Cada função (ex.: "atendimento ao munícipe no balcão único", "emissão de certidões on-line", "tesouraria", "contratação pública") é mapeada aos ativos que a suportam. Resultado: matriz funções × ativos com dependências marcadas. Esta matriz é depois a entrada da análise de impacto no negócio (BIA) e do plano de continuidade.

### Classificação por sensibilidade

A medida O.PSI/classificação (Grupo A) — **Processo de Classificação da Informação** — exige que a entidade defina **critérios e níveis de sensibilidade** para os dados organizacionais. Tipicamente quatro níveis: público, interno, confidencial, restrito. Cada ativo que armazena dados é classificado pelo nível mais elevado da informação que contém. Isto orienta depois as medidas de cifragem, controlo de acessos, retenção e destruição.

O template [`politica-classificacao-dados-nis2.docx`]({{ '/templates/politica-classificacao-dados-nis2.docx' | relative_url }}) traz a estrutura típica de níveis e regras; o template [`politica-gestao-ativos-nis2.docx`]({{ '/templates/politica-gestao-ativos-nis2.docx' | relative_url }}) consagra a política mais ampla de gestão do ciclo de vida dos ativos.

## A lista de ativos publicamente acessíveis (art. 32.º do Aviso) — uma obrigação separada

Esta é a peculiaridade portuguesa que costuma passar despercebida e tem o **prazo mais curto** de todo o regime.

### A quem se aplica

**A todos** os qualificados — entidades essenciais, importantes **E públicas relevantes**. Para uma autarquia, esta é a **única obrigação verdadeiramente transversal** do regime de inventário: não há regime aliviado por se ser Grupo B. Cumpre-se exatamente nos mesmos termos.

### O que tem de constar (art. 32.º, n.º 2 do Aviso)

Para cada ativo da entidade que esteja **diretamente acessível pela Internet**:

- a) Serviço suportado.
- b) Nome do equipamento / nome do software.
- c) Modelo / versão.
- d) Endereço IP (se aplicável).
- e) Fully Qualified Domain Names (FQDNs), se aplicável.
- f) Fabricante.
- g) Dependências entre ativos, quando existentes.

Tipicamente, para uma autarquia, esta lista terá entre **5 e 20 itens**: portal institucional, portal do munícipe, e-mail externo (MX records), webmail, VPN, balcão único on-line, portais de transparência, sistemas SCADA com IP público (se aplicável).

### Prazos

- **Versão inicial**: **20 dias úteis** a contar da notificação de qualificação pelo CNCS (art. 32.º, n.º 4, al. a) do Aviso). Este prazo é um dos mais apertados do regime — começa a contar **imediatamente** após qualificação, sem período de adaptação.
- **Versão atualizada**: **anualmente**, em conjunto com o relatório anual (art. 32.º, n.º 4, al. b)).
- **Actualizações pontuais**: sempre que haja alteração relevante (mudança de IP, exposição de novo serviço, descontinuação).

### Formato

> «O CNCS publica uma instrução técnica de apoio à identificação dos ativos essenciais para a prestação dos respetivos serviços (...).» — art. 32.º, n.º 5 do Aviso

À data desta formação (Junho de 2026), a **instrução técnica do CNCS ainda não foi publicada**. Isto é uma lacuna ativa: o que se sabe é o conteúdo material (alíneas a–g acima), mas o formato preciso (ficheiro CSV, formulário eletrónico, JSON estruturado) aguarda definição. Acompanhar a publicação na plataforma eletrónica nos primeiros dias após qualificação.

## Passos práticos — em que ordem fazer

Recomendamos a sequência abaixo, executada em paralelo entre câmara e SMAS (se existir dupla qualificação):

### Passo 1 — Levantamento de servidores, estações, redes e aplicações críticas

Quem faz: serviço de informática da câmara, com apoio dos fornecedores chave. Workshop de 2–3 horas, lista bruta. Output: ficheiro Excel com 50–100 entradas.

### Passo 2 — Identificar dependências (quem presta o quê)

Para cada ativo, qual o **fornecedor** responsável (Medidata, AIRC, Glintt, Visionware, Microsoft, fornecedor local de hosting, etc.). Esta etapa cria o cruzamento com o futuro [inventário de fornecedores]({% link 03-outras-medidas/d1-cadeia-fornecimento.md %}) (Bloco D).

### Passo 3 — Classificar criticidade

Para cada ativo, decidir se é **crítico** (entra no inventário O.IAC) ou apenas existente (relevante só para Grupo A). Critério: a indisponibilidade compromete um serviço público obrigatório, gera prejuízo material ou reputacional significativo, ou tem dependências a jusante de outros ativos críticos.

### Passo 4 — Marcar os publicamente acessíveis

Para cada ativo, marcar se está **diretamente acessível pela Internet** (resposta a IP público ou via FQDN público). Os marcados são os candidatos à lista do art. 32.º — extrair para ficheiro separado.

### Passo 5 — Atribuir responsáveis funcionais e datas de revisão

Cada ativo crítico tem **um nome** associado (responsável funcional na câmara — chefe de divisão informática, secretário, etc.), data de última revisão, próxima revisão programada. Sem responsável, o inventário envelhece rapidamente.

## Em dupla qualificação

Para SMAS qualificado como **entidade essencial**, aplicam-se as medidas equivalentes do *Anexo III*{:.legal} (não Anexo IV), com nível Básico/Substancial/Elevado conforme atribuído pelo CNCS. O inventário é mais exigente — exige tipicamente identificação de todos os componentes SCADA, sensores de telemetria, sistemas de bombagem, etc. O template [`checklist-setor-agua-potavel-nis2.docx`]({{ '/templates/checklist-setor-agua-potavel-nis2.docx' | relative_url }}) cobre estas especificidades. A lista do art. 32.º cumpre-se nos mesmos termos da câmara, mas separadamente para a entidade SMAS.

## Templates aplicáveis

| Template | Grupo / Etiqueta | Notas |
|---|---|---|
| [`inventario-ativos-tic-nis2.xlsx`]({{ '/templates/inventario-ativos-tic-nis2.xlsx' | relative_url }}) | **Aplicar tal-qual** | Folha Excel com colunas ativo / tipo / responsável / fornecedor / criticidade / publicamente acessível / dependências. Cobre Grupo B; estender para Grupo A. |
| [`registo-ativos-nis2.xlsx`]({{ '/templates/registo-ativos-nis2.xlsx' | relative_url }}) | Referência | Variante mais detalhada do inventário, com colunas adicionais (modelo, versão, data de aquisição, fim de vida útil). Útil para Grupo A. |
| [`politica-classificacao-dados-nis2.docx`]({{ '/templates/politica-classificacao-dados-nis2.docx' | relative_url }}) | **Adaptar para Grupo A** | Política que define os 4 níveis de sensibilidade. Obrigatória para Grupo A (medida O.PSI/classificação). |
| [`politica-gestao-ativos-nis2.docx`]({{ '/templates/politica-gestao-ativos-nis2.docx' | relative_url }}) | **Adaptar para Grupo A** | Política mais ampla — ciclo de vida dos ativos, papéis e responsabilidades, ferramentas. Obrigatória para Grupo A. |
| Lista de ativos publicamente acessíveis (art. 32.º) | A criar | Lacuna ativa — formato pendente de instrução técnica do CNCS. Produção interna do manual digital até 8 Junho com modelo provisório. |

Todos os templates disponíveis para *download* na página de [recursos]({% link recursos/templates.md %}) a partir de 8 de Junho.

## Exercício associado

[Exercício A3 — Top 5 ativos críticos]({% link exercicios/a3-inventario.md %}) (10 min, individual) — cada formando lista os 5 ativos críticos da sua autarquia, com responsável e dependência principal. Output: cinco linhas preenchidas no [`inventario-ativos-tic-nis2.xlsx`]({{ '/templates/inventario-ativos-tic-nis2.xlsx' | relative_url }}). Combinado com o Exercício A2 (matriz de risco) e com o Exercício A5 (fornecedores, no Bloco D), constitui o **núcleo do diagnóstico inicial** que fica convosco no fim da formação.

## Próximo passo

[B.4 Síntese do bloco →]({% link 01-gestao-risco/b4-sintese.md %})
