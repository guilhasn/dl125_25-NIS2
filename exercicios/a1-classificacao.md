---
title: "A1 — Classificação"
layout: default
parent: "Worksheets dos exercícios"
nav_order: 1
---

# A1. Classificação da autarquia

{: .note }
> **Grupo A** = autarquia com ≥ 250 trabalhadores  
> **Grupo B** = autarquia com 75-249 trabalhadores  
> (art. 7.º RJC — ver [A.2 Quem está abrangido]({% link 00-enquadramento/a2-quem-esta-abrangido.md %}))

**Duração**: 10 min · **Bloco**: A.2 · **Materiais**: [`a1-classificacao-autarquia.xlsx`]({{ '/templates/a1-classificacao-autarquia.xlsx' | relative_url }})

## Objectivo

Identificar **todas as entidades operacionais** que dependem da câmara e classificar cada uma face ao DL 125/2025. O resultado é a **base material da auto-identificação** que cada autarquia terá de fazer no [MyCiber]({% link 00-enquadramento/a3-plataforma-cncs.md %}).

Não é exercício teórico. O conteúdo que produzirem aqui é o que **levam de volta** para a câmara e usam, sem alterações de fundo, no acto formal de registo quando a funcionalidade estiver aberta.

## Instruções (individual, 10 minutos)

1. Abra o ficheiro [`a1-classificacao-autarquia.xlsx`]({{ '/templates/a1-classificacao-autarquia.xlsx' | relative_url }}) (password da formação).
2. Apague a linha de exemplo.
3. Liste **todas** as entidades operacionais da sua autarquia, uma por linha:
   - Câmara em sentido próprio.
   - SMAS (se existir).
   - Empresa(s) municipal(ais).
   - Fundação(ões) municipais.
   - Agências regionais com participação.
4. Para cada entidade, preencha:
   - Tipo (Câmara / SMAS / Empresa municipal / Fundação / Agência).
   - **Número actual de trabalhadores** no quadro de pessoal.
   - Sector de actividade — em especial, verificar se opera serviço listado no Anexo I (energia, transportes, banca, infraestruturas digitais, água potável, águas residuais, etc.) ou Anexo II.
5. Aplique o critério do [*art. 7.º RJC*{:.legal}]({% link recursos/legislacao-dl-125-2025.md %}#art-7):
   - **≥ 250 trabalhadores** → Grupo A (entidade pública relevante).
   - **75 a 249** → Grupo B (entidade pública relevante).
   - **< 75** → fora do regime obrigatório.
   - Se opera serviços do Anexo I/II e excede limiar de média empresa → **entidade essencial / importante**, independentemente do número de trabalhadores da entidade-mãe.

## Output esperado

Folha Excel com 1–4 linhas preenchidas (média típica: câmara + SMAS = 2 linhas; câmaras maiores podem ter 4+). Cada linha tem **uma qualificação clara**: Grupo A, Grupo B, fora do regime, essencial, ou importante.

Se houver linhas marcadas como **"Em dúvida"**, traga-as à discussão em plenária e verifique adicionalmente com o resultado do [Simulador do MyCiber]({% link 00-enquadramento/a3-plataforma-cncs.md %}#o-simulador--primeira-funcionalidade-já-disponível).

## Validação rápida (formador)

- Câmaras médias (típicamente entre 75 e 249) → Grupo B.
- Câmaras grandes (Porto, Lisboa, Coimbra, Cascais, Sintra, Loures, Braga…) → Grupo A.
- SMAS que opera água potável + águas residuais → quase certo **entidade essencial** (mesmo com poucos trabalhadores).
- Junta de freguesia ou câmara muito pequena (< 75 trab.) → fora do regime obrigatório, **mas** continua a ser boa prática implementar o essencial.

## Como continuar este trabalho na câmara

1. Confirmar o **número exacto de trabalhadores** com o Mapa de Pessoal a 31 de Dezembro do ano anterior.
2. Documentar internamente a classificação proposta com **acto formal** assinado pelo presidente.
3. Quando o MyCiber abrir o registo formal, submeter esta classificação como auto-identificação.
4. Para entidades em dupla qualificação (câmara + SMAS), submeter **dois registos separados**.

## Templates relacionados

- [`formulario-registo-cncs-nis2.docx`]({{ '/templates/formulario-registo-cncs-nis2.docx' | relative_url }}) — versão imprimível do formulário de auto-identificação que se passa depois para o MyCiber.

## Ver também

- [A.2 Quem está abrangido]({% link 00-enquadramento/a2-quem-esta-abrangido.md %}) — base teórica.
- [Roteiro essencial — Dupla qualificação]({% link roteiro-essencial/dupla-qualificacao.md %}) — para SMAS / empresas municipais em sectores Anexo I/II.
- [FAQ §1 — Quem está abrangido]({% link recursos/faq.md %}#1-quem-está-abrangido) — casos práticos.
