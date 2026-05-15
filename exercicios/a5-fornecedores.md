---
title: "A5 — Top 5 fornecedores"
layout: default
parent: "Exercícios A1–A5"
nav_order: 5
---

# A5. Top 5 fornecedores TIC críticos

{: .note }
> **Grupo A** = autarquia com ≥ 250 trabalhadores  
> **Grupo B** = autarquia com 75-249 trabalhadores  
> (art. 7.º RJC — ver [A.2 Quem está abrangido]({% link 00-enquadramento/a2-quem-esta-abrangido.md %}))

**Duração**: 10 min · **Bloco**: D.1 · **Materiais**: [`a5-top5-fornecedores.xlsx`]({{ '/templates/a5-top5-fornecedores.xlsx' | relative_url }})

## Objectivo

Mapear os 5 fornecedores TIC mais críticos da autarquia e classificá-los por **criticidade** e **risco de cadeia de abastecimento** — base da medida [<abbr title="Política de Segurança da cadeia de Fornecimento">**O.PSF**</abbr>]({% link recursos/anexo-iv-aviso-5146.md %}#o-psf) do Anexo IV. Para autarquias, este é provavelmente o exercício mais útil de todos: uma câmara depende, na prática, de **uma mão-cheia de fornecedores** para tudo o que é digital. Saber quais são, saber o que falha primeiro se um deles cair, e ter cláusulas contratuais alinhadas, é metade do trabalho.

## Instruções (individual, 10 minutos)

1. Abra [`a5-top5-fornecedores.xlsx`]({{ '/templates/a5-top5-fornecedores.xlsx' | relative_url }}) (password da formação).
2. Apague a linha de exemplo.
3. Liste os **5 fornecedores TIC mais críticos** da câmara. Critério: aquele cuja falha ou compromisso afecta **directamente** o serviço público.
   - Suspeitos habituais em autarquias: Medidata, AIRC, Glintt, Visionware, Microsoft (M365), AMA, alojamento/cloud, ISP/operador de telecomunicações, fornecedor de segurança de rede, fornecedor de SIG, fornecedor de contabilidade.
4. Para cada fornecedor, preencha:
   - **Serviço prestado** — o que faz para a câmara, em linguagem concreta.
   - **Acesso a dados pessoais?** — sim/não/não sei. Se sim, há implicações RGPD (subcontratante de tratamento, art. 28.º RGPD).
   - **Criticidade** — Alta / Média / Baixa, em função do impacto no serviço público.
   - **Contrato formal?** — sim/não. Se não, é um risco em si — todos os fornecedores críticos deveriam ter contrato escrito.
   - **Risco identificado** — uma frase descrevendo a vulnerabilidade principal (dependência única, fim de contrato, fornecedor pequeno, etc.).
   - **Mitigação prevista** — o que está (ou deveria estar) em vigor para mitigar esse risco.

## Output esperado

5 linhas preenchidas. Padrão típico em câmara média:

- **2 fornecedores de criticidade alta** (Microsoft 365 + fornecedor da plataforma de gestão municipal — Medidata ou similar).
- **2 de criticidade média** (alojamento, fornecedor de SIG, fornecedor de contabilidade).
- **1 de criticidade baixa** mas relevante por área (segurança de rede, fornecedor de telefonia IP).

Pelo menos um deverá ter **"Contrato formal? = Não"** — verificar e remediar.

## Validação rápida (formador) — armadilhas comuns

| Armadilha | Correcção |
|---|---|
| Esquecer a **Microsoft 365** | É quase sempre o fornecedor mais crítico (e-mail, identidade, OneDrive, Teams). Tem de estar na lista. |
| Confundir **fornecedor de hardware** com **fornecedor de serviço** | O exercício é sobre serviços (software, cloud, plataformas). Hardware entra noutra dimensão. |
| Marcar **"Não sei"** em todos os campos | Se isto acontece, o exercício revelou uma **lacuna de conhecimento** — boa coisa. Anotar e investigar em câmara. |
| Marcar todos como **criticidade Alta** | Há gradação. Se tudo é "alta", a classificação perde valor — repensar com 3 níveis distintos. |
| Esquecer **fornecedor de SIG cadastral** | Crítico para urbanismo, fiscalidade, ordenamento. Frequentemente um único fornecedor, sem alternativa. |

## Como continuar este trabalho na câmara

1. **Inventário completo** dos fornecedores TIC — alargar de 5 para todos (típicamente 15-25 em câmara média) usando o template [`inventario-fornecedores-nis2.xlsx`]({{ '/templates/inventario-fornecedores-nis2.xlsx' | relative_url }}).
2. **Revisão dos contratos críticos** — para cada fornecedor de criticidade alta, verificar se o contrato tem:
   - Cláusulas de segurança alinhadas com o Anexo IV — usar [`clausulas-seguranca-fornecedores-nis2.docx`]({{ '/templates/clausulas-seguranca-fornecedores-nis2.docx' | relative_url }}).
   - Obrigação de notificação de incidentes em prazo curto (24-72h).
   - Direito de auditoria.
   - SLA com penalizações por indisponibilidade.
3. **Due diligence** dos fornecedores antes de contratar (e renovar) — usar [`questionario-due-diligence-fornecedor-nis2.docx`]({{ '/templates/questionario-due-diligence-fornecedor-nis2.docx' | relative_url }}).
4. **Scorecard anual** para fornecedores críticos (Grupo A) — [`scorecard-fornecedor-nis2.xlsx`]({{ '/templates/scorecard-fornecedor-nis2.xlsx' | relative_url }}).
5. **Plano de saída** — para cada fornecedor sem alternativa imediata, ter pelo menos uma alternativa identificada e custos estimados.

## Articulação com RGPD

Se um fornecedor **acede a dados pessoais** dos vossos munícipes, é **subcontratante de tratamento** (art. 28.º RGPD) e precisa de:

- **Contrato escrito** com cláusulas obrigatórias do art. 28.º, n.º 3.
- **Obrigação de notificação** em caso de violação (RGPD art. 33.º).
- **Possibilidade de auditoria** pela câmara como responsável pelo tratamento.

A coluna "Acesso a dados pessoais?" deste exercício é uma **primeira triagem** — todos os que respondam "Sim" devem ter contrato RGPD em ordem.

## Templates relacionados

- [`inventario-fornecedores-nis2.xlsx`]({{ '/templates/inventario-fornecedores-nis2.xlsx' | relative_url }}) — versão completa.
- [`clausulas-seguranca-fornecedores-nis2.docx`]({{ '/templates/clausulas-seguranca-fornecedores-nis2.docx' | relative_url }}) — cláusulas para inserir em cadernos de encargos.
- [`scorecard-fornecedor-nis2.xlsx`]({{ '/templates/scorecard-fornecedor-nis2.xlsx' | relative_url }}) — avaliação periódica (Grupo A).
- [`questionario-due-diligence-fornecedor-nis2.docx`]({{ '/templates/questionario-due-diligence-fornecedor-nis2.docx' | relative_url }}) — questionário pré-contratual.
- [`politica-cadeia-fornecimento-nis2.docx`]({{ '/templates/politica-cadeia-fornecimento-nis2.docx' | relative_url }}) — política formal (Grupo A).
