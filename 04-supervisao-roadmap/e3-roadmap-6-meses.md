---
title: "E.3 Roadmap 6 meses"
layout: default
parent: "E. Supervisão e roadmap"
nav_order: 3
---

# E.3 Roadmap 6 meses — *cheatsheet* operacional

{: .note }
> **Grupo A** = autarquia com ≥ 250 trabalhadores  
> **Grupo B** = autarquia com 75-249 trabalhadores  
> (art. 7.º RJC — ver [A.2 Quem está abrangido]({% link 00-enquadramento/a2-quem-esta-abrangido.md %}))

**Duração**: 5 min · **Forma**: *cheatsheet* para imprimir e afixar — uma só página, com a sequência dos primeiros 6 meses

Ao fim deste dia de formação, vocês têm uma matriz de risco em embrião, um *top 5* de ativos, um *top 5* de fornecedores e o esboço de uma notificação 24h. **Não chega**, mas é o ponto de partida certo. Este roadmap traduz o resto — o caminho mês-a-mês para chegar a uma **postura defensável** em **6 meses**. Não é o caminho para a perfeição (que demora anos); é o caminho para o **mínimo demonstrável** que se invocará perante o [*art. 65.º RJC*{:.legal}]({% link recursos/legislacao-dl-125-2025.md %}#art-65) (dispensa de coimas).

## A sequência

Cada mês tem **um objetivo principal** e **3-5 entregáveis concretos**. O mês 6 fecha o ciclo com uma revisão pela gestão que produz a primeira **acta de revisão anual**.

### Mês 1 — Qualificação e identificação

**Objetivo**: estar **registado no MyCiber** e ter **classificação correta** comunicada e aceite.

- ☐ Auto-identificação no MyCiber (logo após o registo abrir).
- ☐ Despacho de designação do **ponto de contacto** (com substituto).
- ☐ Lista das **entidades operacionais** da autarquia (câmara + SMAS + empresas + fundações) classificadas — usar saída do **Exercício A1**.
- ☐ Para entidades em dupla qualificação: registo **separado** SMAS / empresa municipal como entidade essencial (se aplicável).
- ☐ **Lista de ativos publicamente acessíveis** ([*art. 32.º do Aviso*{:.legal}]({% link recursos/legislacao-aviso-5146.md %}#art-32)) — submeter no prazo de **20 dias úteis** após qualificação.

**Templates a aplicar**: [`formulario-registo-cncs-nis2.docx`]({{ '/templates/formulario-registo-cncs-nis2.docx' | relative_url }}).

### Mês 2 — Políticas-base

**Objetivo**: ter **5 políticas escritas e aprovadas** que sustentam tudo o que se segue.

- ☐ **Política de segurança da informação** (política-mãe) — apoia-se na ISO 27001 se existir.
- ☐ **Política de palavras-passe** alinhada com NIST 2017.
- ☐ **Política de controlo de acessos** com princípio do privilégio mínimo.
- ☐ **Política de *backups*** — frequência, retenção, testes.
- ☐ **Política de gestão de incidentes** (ou plano de resposta a incidentes, mais operacional).

**Aprovação**: despacho do presidente ou deliberação do executivo. Sem aprovação formal, são apenas rascunhos.

**Templates a usar**: [`politica_controlo_acessos_pt.docx`]({{ '/templates/politica_controlo_acessos_pt.docx' | relative_url }}), [`politica_palavras_passe_pt.docx`]({{ '/templates/politica_palavras_passe_pt.docx' | relative_url }}), [`politica-backups-nis2.docx`]({{ '/templates/politica-backups-nis2.docx' | relative_url }}), [`plano-resposta-incidentes-nis2.docx`]({{ '/templates/plano-resposta-incidentes-nis2.docx' | relative_url }}).

### Mês 3 — Inventário e matriz de risco

**Objetivo**: ter o **inventário de ativos críticos completo** e a **matriz de risco** com pelo menos 15-25 entradas (não só os 3 e 5 do dia da formação).

- ☐ **Inventário de ativos críticos** alargado de 5 (Exercício A3) para 20-40 entradas.
- ☐ **Inventário de fornecedores TIC críticos** alargado de 5 (Exercício A5) para 15-25.
- ☐ **Matriz de risco** alargada de 3 (Exercício A2) para 15-25 entradas com tratamento decidido.
- ☐ **Mapeamento entre ativos críticos e fornecedores** — para cada ativo crítico, qual o fornecedor que o sustenta.
- ☐ **(A)** Identificação de **funções críticas** ([O.ID]({% link recursos/anexo-iv-aviso-5146.md %}#o-id)) e classificação de informação ([O.PSI]({% link recursos/anexo-iv-aviso-5146.md %}#o-psi)).

**Workshops internos** — duas tardes de 3h com informática, DPO e gabinete chegam para fechar este mês.

### Mês 4 — Medidas técnicas

**Objetivo**: implementar tecnicamente **as medidas T mais críticas**.

- ☐ **MFA ativo** em Microsoft 365, VPN, administração de servidores, *firewall* — para **todos** os utilizadores privilegiados; idealmente para todos os utilizadores.
- ☐ **Backups testados** — execução do procedimento de teste; primeiro teste documentado.
- ☐ **Backup *air-gapped*** ou *immutability* — uma cópia fora do alcance do ransomware.
- ☐ **Patches em dia** — atualização do parque informático para versões suportadas.
- ☐ **SPF + DKIM + DMARC** no *e-mail* institucional (mínimo).
- ☐ **HTTPS** em todos os sites institucionais com certificados válidos.

**Investimento típico**: 1-3 semanas-homem de informática interna + apoio do fornecedor de M365 + custos de hardware (~5.000-15.000 € para *air-gap* sério).

### Mês 5 — *Playbooks* e simulação

**Objetivo**: ter **planos de resposta operacionais** e **fazer uma simulação** interna.

- ☐ **Plano de Continuidade de Negócio (PCN)** finalizado, com pelo menos 3 cenários (portal parado, ransomware, indisponibilidade do SIG).
- ☐ ***Playbooks*** específicos para ransomware e *data breach*.
- ☐ **Matriz de escalação** afixada no gabinete TIC + na receção.
- ☐ **Folha-resumo dos prazos PT vs NIS2** afixada (imprimível a partir do manual digital).
- ☐ ***Tabletop exercise*** interno — 30-60 minutos com gabinete + informática + DPO, usando uma das 4 fichas de cenário do exercício A4.

**Templates a usar**: [`plano-continuidade-negocio-nis2.docx`]({{ '/templates/plano-continuidade-negocio-nis2.docx' | relative_url }}), [`matriz-escalacao-incidentes-nis2.docx`]({{ '/templates/matriz-escalacao-incidentes-nis2.docx' | relative_url }}), [`playbook-ransomware-nis2.docx`]({{ '/templates/playbook-ransomware-nis2.docx' | relative_url }}), [`playbook-data-breach-nis2.docx`]({{ '/templates/playbook-data-breach-nis2.docx' | relative_url }}).

### Mês 6 — Auditoria interna e revisão pela gestão

**Objetivo**: **fechar o ciclo** com auditoria interna (mesmo informal) e **acta de revisão pela gestão** — a peça que demonstra ciclo de melhoria ativo.

- ☐ **Auditoria interna**: percorrer a checklist de [E.2 Documentação mínima]({% link 04-supervisao-roadmap/e2-documentacao-minima.md %}) e identificar lacunas. Pode ser feita pela própria equipa de informática + DPO.
- ☐ **Plano de ações correctivas** para as lacunas identificadas — 3-6 meses para fechar.
- ☐ **1.ª sessão de formação anual** aos trabalhadores (mínimo: ciber-higiene + phishing + comunicação de incidentes).
- ☐ **Registo de presenças** arquivado.
- ☐ **Acta de revisão pela gestão** — assinada pelo presidente — formaliza o estado da postura e o plano para o ano seguinte.

**Templates a usar**: [`gap-analysis-nis2.xlsx`]({{ '/templates/gap-analysis-nis2.xlsx' | relative_url }}), [`ata-revisao-gestao-nis2.docx`]({{ '/templates/ata-revisao-gestao-nis2.docx' | relative_url }}), [`registo-presencas-formacao-nis2.xlsx`]({{ '/templates/registo-presencas-formacao-nis2.xlsx' | relative_url }}), [`plano-acoes-corretivas-nis2.xlsx`]({{ '/templates/plano-acoes-corretivas-nis2.xlsx' | relative_url }}).

## *Cheatsheet* visual — uma linha por mês

| Mês | Foco | Peça-chave |
|---|---|---|
| **1** | Qualificação | Registo no MyCiber + ponto de contacto + lista [*art. 32.º do Aviso*{:.legal}]({% link recursos/legislacao-aviso-5146.md %}#art-32) |
| **2** | Políticas-base | 5 políticas aprovadas |
| **3** | Diagnóstico | Inventário (20-40) + Matriz risco (15-25) + Fornecedores (15-25) |
| **4** | Medidas técnicas | MFA + backups testados + air-gap + SPF/DKIM/DMARC |
| **5** | Resposta | PCN + playbooks + matriz escalação + simulação |
| **6** | Ciclo | Auditoria interna + 1.ª formação + acta de revisão anual |

## Versão imprimível

📄 **[Roadmap 6 meses (PDF, A4 paisagem)]({{ '/templates/roadmap-6-meses.pdf' | relative_url }})**

Tabela em A4 paisagem com os 6 meses lado-a-lado, entregáveis-chave por mês, e a peça que sai no fim de cada um. Pronto a imprimir e afixar no gabinete TIC ou na sala da equipa de informática — referência diária do ponto de contacto NIS2.

## E depois?

Após o mês 6, o ciclo entra em **manutenção anual**:

- **Anual**: revisão pela gestão, atualização do plano de formação, atualização da lista do [*art. 32.º do Aviso*{:.legal}]({% link recursos/legislacao-aviso-5146.md %}#art-32).
- **Semestral**: revisão das matrizes (risco, ativos, fornecedores), teste do PCN.
- **Trimestral**: teste de *backup*, revisão de contas, *refresher* de formação.
- **Mensal** (informática): patches, monitorização, *logs*.
- **Ao incidente**: o ritmo é o ritmo do CNCS — não o ritmo administrativo habitual.

## Próximo passo

[E.4 Compromisso para a próxima semana →]({% link 04-supervisao-roadmap/e4-compromisso.md %})
