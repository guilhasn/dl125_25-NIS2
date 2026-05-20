---
title: "A3 — Inventário top 5"
layout: default
parent: "Worksheets dos exercícios"
nav_order: 3
---

# A3. Top 5 ativos críticos

**Duração**: 10 min · **Bloco**: B.3 · **Materiais**: [`a3-inventario-top5.xlsx`]({{ '/templates/a3-inventario-top5.xlsx' | relative_url }})

## Objetivo

Construir o **núcleo** do inventário de ativos críticos exigido pela medida [<abbr title="Inventariação de Ativos Críticos">**O.IAC**</abbr>]({% link recursos/anexo-iv-aviso-5146.md %}#o-iac) do Anexo IV (Grupo B e A). Cinco linhas — não cinquenta — é o mínimo viável para começar. A versão completa exige 20-40 ativos numa câmara média e constrói-se em workshop dedicado, depois.

Este exercício também serve para **identificar candidatos à lista do art. 32.º** (ativos publicamente acessíveis) — coluna específica no worksheet.

## Instruções (individual, 10 minutos)

1. Abra [`a3-inventario-top5.xlsx`]({{ '/templates/a3-inventario-top5.xlsx' | relative_url }}) (password da formação).
2. Apague a linha de exemplo.
3. Identifique os **5 ativos críticos** da sua autarquia: sistemas, aplicações, equipamentos sem os quais a câmara deixa de cumprir a sua missão de serviço público.
   - Exemplos típicos: Portal do Munícipe, Balcão Único on-line, sistema de contabilidade, GED, SIG cadastral, e-mail institucional, controlador de domínio, servidor de ficheiros, sistemas SCADA do SMAS.
   - **Não confunda com "tudo o que tem importância"**. Crítico = compromete serviço público obrigatório se cair.
4. Para cada ativo, indique:
   - **Tipo** (Servidor / Aplicação web / Base de dados / Equipamento de rede / Serviço cloud / Equipamento OT/SCADA).
   - **Serviço público** que suporta — descrição concreta ("emissão de certidões on-line", "pagamento de água").
   - **Responsável funcional interno** — pessoa da câmara que responde por esse ativo (não o fornecedor!).
   - **Fornecedor** principal (Medidata, AIRC, Glintt, Microsoft, AMA, etc.).
   - **Dependência principal** — outro ativo de que este depende (base de dados, autenticação, servidor de aplicação).
   - **Acessível pela Internet?** (Sim/Não). Se Sim, é candidato à **lista do art. 32.º**.

## Output esperado

5 linhas preenchidas. Idealmente, pelo menos **2 marcados como "Acessível pela Internet"** — esses passam para a lista do art. 32.º, com prazo de 20 dias úteis após qualificação.

## Validação rápida

Padrões frequentes a corrigir:

- "Servidor de e-mail" → na maioria das câmaras é **Microsoft 365**, um **serviço cloud**, não servidor próprio. Reclassificar.
- "Portal do Munícipe" sem identificar a base de dados associada → falha de dependência. A dependência **é o ponto de falha real**.
- Responsável funcional preenchido com o nome do **fornecedor** → erro. O responsável é interno; o fornecedor está na coluna a seguir.
- Esquecer **controlador de domínio / Active Directory** → é o ativo mais central de qualquer câmara que use Windows; a sua queda paralisa tudo.

## Como continuar este trabalho na câmara

1. **Alargar para 20-40 ativos** num workshop de 2-3 horas com a equipa de informática.
2. **Cruzar com a matriz de risco** (Exercício A2) — cada ativo crítico deve ter pelo menos um risco identificado.
3. **Validar dependências** percorrendo cada linha e perguntando "se isto cair, o que mais cai?".
4. **Extrair a lista do art. 32.º**: filtrar pelos "Acessíveis pela Internet" e completar com IP, FQDN, modelo/versão, fabricante. Submeter ao CNCS no prazo legal.
5. **Atribuir data de revisão** a cada ativo (anual mínimo).

## Templates relacionados

- [`inventario-ativos-tic-nis2.xlsx`]({{ '/templates/inventario-ativos-tic-nis2.xlsx' | relative_url }}) — versão completa, com colunas adicionais (modelo, versão, fim de vida útil).
- [`registo-ativos-nis2.xlsx`]({{ '/templates/registo-ativos-nis2.xlsx' | relative_url }}) — variante mais detalhada para Grupo A.
- [`politica-gestao-ativos-nis2.docx`]({{ '/templates/politica-gestao-ativos-nis2.docx' | relative_url }}) — política formal (Grupo A).

## Ver também

- [B.3 Inventário e classificação de ativos]({% link 01-gestao-risco/b3-inventario-ativos.md %}) — base teórica, com tratamento detalhado da lista do art. 32.º.
