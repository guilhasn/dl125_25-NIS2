---
title: "B.4 Síntese do bloco"
layout: default
parent: "B. Art. 27.º — Risco e ativos"
nav_order: 4
---

# B.4 Síntese do bloco

{: .note }
> **Grupo A** = autarquia com ≥ 250 trabalhadores  
> **Grupo B** = autarquia com 75-249 trabalhadores  
> (art. 7.º RJC — ver [A.2 Quem está abrangido]({% link 00-enquadramento/a2-quem-esta-abrangido.md %}))

Dez minutos a fixar o que ficou nos Blocos A e B, e a antecipar os Blocos C, D e E.

## O que vimos até aqui

No **Bloco A** percorremos o enquadramento legal: a vossa qualificação (Grupo A ou B, mais a eventual dupla qualificação se operam SMAS ou empresa municipal em sector Anexo I/II), a plataforma eletrónica do CNCS (MyCiber) como porta de entrada das obrigações, os prazos críticos a partir da disponibilização da plataforma, e a leitura cuidadosa do regime sancionatório — incluindo a clarificação de que a "amnistia" do art. 65.º **não é automática** e exige plano de adaptação documentado.

No **Bloco B** abrimos o art. 27.º do RJC e demonstrámos a sua **não-aplicabilidade direta** às autarquias: para vocês, o regime é o art. 33.º + Anexo IV do Aviso, organizado em medidas O / T / H. Em seguida fixámos os dois pilares da gestão de risco — a **matriz probabilidade × impacto** com cinco categorias de ameaça e cinco passos metodológicos, e o **inventário de ativos críticos** com o seu prazo paralelo da lista pública (art. 32.º Aviso) que vincula transversalmente todas as entidades qualificadas, com versão inicial em 20 dias úteis.

Saíram daqui dois exercícios começados: a matriz de risco com 3 linhas e o inventário com top 5 ativos críticos. **Levem esses ficheiros**.

## O que vem a seguir

Os blocos seguintes:

- **Bloco C — Notificação de incidentes** (90 min): o tema mais crítico do dia. Os prazos do esquema português (24h+24h+30 dias úteis) e como evitar a confusão com os prazos da diretiva NIS2 pura. Termina com simulação de notificação 24h sobre cenário escrito (Exercício A4).
- **Bloco D — Outras medidas + documentação** (60 min): cadeia de fornecimento (e o vosso fornecedor crítico real, Exercício A5), continuidade e *backups*, controlo de acesso, ciber-higiene e formação. É o resto do art. 27.º.
- **Bloco E — Supervisão, sanções e roadmap** (15 min): como o CNCS supervisiona uma pública relevante (*ex post*, art. 55.º) e qual o plano dos próximos 6-12 meses para a vossa autarquia.

## Três coisas a fixar antes de avançar

1. **Qual o vosso grupo** — Grupo A, Grupo B ou fora; e se há dupla qualificação a tratar em paralelo. Se ainda têm dúvida, é a hora de a colocarem no chat ou de pedirem a palavra.
2. **Onde encontrar a matriz de risco** no manual digital e a metodologia recomendada. Vão precisar dos ficheiros para continuar o trabalho na semana seguinte.
3. **Que ativos vão classificar**. O Exercício A3 listou 5; a versão final terá 20-40 numa câmara média. Comecem agora a mapa mental dos que faltam.

## Preparar o exercício A5 (cadeia de fornecimento)

No Bloco D vamos trabalhar **cadeia de fornecimento**. Quem tiver à mão dados sobre os **fornecedores TIC críticos** — quem presta o software de gestão municipal, quem aloja o portal, quem fornece o e-mail, quem gere a rede — chegará melhor preparado para o Exercício A5. Não é pré-requisito; é facilitador.

## Revisão do Bloco B — 8 perguntas

**1.** O *art. 27.º RJC* aplica-se diretamente à minha câmara (Grupo B)?

<details markdown="block">
<summary><strong>Ver resposta</strong></summary>

**Não.** O *art. 27.º RJC* aplica-se a **entidades essenciais e importantes**. Para autarquias (entidade pública relevante, Grupo A/B), aplica-se o *art. 33.º RJC* + **Anexo IV do Aviso**. As medidas concretas estão no Anexo IV organizadas em O / T / H. Ver [B.1 Panorama do art. 27.º]({% link 01-gestao-risco/b1-art27-panorama.md %}).
</details>

**2.** Risco com **probabilidade 3** e **impacto 5** — em que nível fica (baixo / médio / alto)?

<details markdown="block">
<summary><strong>Ver resposta</strong></summary>

**Alto** (P × I = 15). Escala: 1-6 baixo · 8-12 médio · 15-25 alto. Riscos de nível alto exigem **tratamento prioritário** e — para Grupo A — **acta de aceitação formal do risco residual** assinada pelo presidente. Ver [B.2 Análise e gestão de risco]({% link 01-gestao-risco/b2-analise-risco.md %}).
</details>

**3.** Quantos ativos críticos típicos numa câmara média de Grupo B?

<details markdown="block">
<summary><strong>Ver resposta</strong></summary>

**20-40 ativos críticos.** Não é o parque informático inteiro (500-2.000 itens), mas sim os sistemas, aplicações e equipamentos **sem os quais a câmara deixa de prestar serviço público**. Para Grupo A, o inventário é alargado a **todos** os ativos. Ver [B.3 Inventário e classificação de ativos]({% link 01-gestao-risco/b3-inventario-ativos.md %}).
</details>

**4.** A lista de ativos publicamente acessíveis do *art. 32.º Aviso* aplica-se só a entidades essenciais?

<details markdown="block">
<summary><strong>Ver resposta</strong></summary>

**Não.** É a **única obrigação verdadeiramente transversal** — aplica-se a **essenciais, importantes E públicas relevantes** (autarquias incluídas). Prazo: **20 dias úteis** após qualificação pelo CNCS. Conteúdo: lista de IPs/FQDNs públicos, com serviço suportado, modelo, fabricante, dependências.
</details>

**5.** As três famílias de medidas do Anexo IV são:

<details markdown="block">
<summary><strong>Ver resposta</strong></summary>

**O** (Organizacionais) — políticas, processos, decisões de gestão. <br/>
**T** (Técnicas) — controlos tecnológicos: configurações, *software*, *hardware*. <br/>
**H** (Humanas) — formação, sensibilização, exercícios. <br/>
Cada código tem formato `X.YY` (ex.: `O.IAC`, `T.AM`, `H.PF`). Ver [Anexo IV — medidas O/T/H]({% link recursos/anexo-iv-aviso-5146.md %}).
</details>

**6.** Verdadeiro ou falso: "O Anexo IV não enumera explicitamente uma medida 'análise de risco' para autarquias do Grupo B".

<details markdown="block">
<summary><strong>Ver resposta</strong></summary>

**Verdadeiro.** A medida **O.IAC** (inventário de ativos críticos) e **O.ID** (Grupo A, identificação de funções críticas) pressupõem análise de risco — mas o termo "análise de risco" não aparece explicitamente como medida própria para Grupo B. **Recomendação prática**: tratar como se fosse exigida, pois é metodologicamente impossível cumprir as restantes medidas sem ela. Ver [B.2]({% link 01-gestao-risco/b2-analise-risco.md %}).
</details>

**7.** Para uma autarquia do **Grupo A**, que peças adicionais de análise de risco são exigidas (face ao Grupo B)?

<details markdown="block">
<summary><strong>Ver resposta</strong></summary>

Três peças adicionais (*art. 30.º, n.º 3 do Aviso*):

1. **Metodologia documentada** da análise (política escrita aprovada).
2. **Identificação de funções críticas** ([O.ID]({% link recursos/anexo-iv-aviso-5146.md %}#o-id)) — matriz funções × ativos.
3. **Acta de aceitação formal do risco residual** assinada pelo dirigente máximo.
</details>

**8.** O que é mais correto: a matriz de risco é "para auditoria interna" ou "para tomar decisões"?

<details markdown="block">
<summary><strong>Ver resposta</strong></summary>

**Para tomar decisões.** A matriz é o instrumento que **organiza todas as outras escolhas** — qual fornecedor mais crítico, que sistema merece *backup* duplicado, onde aplicar MFA primeiro. Auditoria interna usa-a como evidência, mas o seu uso primário é **operacional**. Sem matriz, as decisões posteriores ficam arbitrárias.
</details>

## Próximo passo

[Bloco C — Notificação de incidentes →]({% link 02-notificacao-incidentes/index.md %})
