---
title: "D.3 Acessos, MFA e palavras-passe"
layout: default
parent: "D. Outras medidas do art. 27.º"
nav_order: 3
---

# D.3 Controlo de acessos, MFA e palavras-passe

{: .note }
> **Grupo A** = autarquia com ≥ 250 trabalhadores  
> **Grupo B** = autarquia com 75-249 trabalhadores  
> (art. 7.º RJC — ver [A.2 Quem está abrangido]({% link 00-enquadramento/a2-quem-esta-abrangido.md %}))

**Duração**: 15 min · **Base legal**: art. 27.º al. h), i), j) RJC + Anexo IV [<abbr title="Política de Acessos e Privilégios">**O.PAP**</abbr>]({% link recursos/anexo-iv-aviso-5146.md %}#o-pap) (Política de Acessos e Privilégios), [<abbr title="Política de Palavras-Passe">**O.PP**</abbr>]({% link recursos/anexo-iv-aviso-5146.md %}#o-pp) (Política de Palavras-Passe), [<abbr title="Autenticação Multi-fator">**T.AM**</abbr>]({% link recursos/anexo-iv-aviso-5146.md %}#t-am) (Tecnologias de Autenticação Multi-fator).

A maior parte dos incidentes graves em câmaras portuguesas começa por um **acesso comprometido**. Phishing que captura credenciais, password fraca exposta numa fuga pública, conta de prestador de serviços nunca desactivada que continua ativa anos depois da rescisão do contrato. As três medidas desta página — **controlo de acessos**, **MFA** e **palavras-passe** — são as **medidas técnicas de maior retorno por euro investido** em todo o Anexo IV.

## O que a lei diz

> «As entidades essenciais e importantes (...) adoptam medidas relativas ao controlo dos acessos, gestão dos privilégios, autenticação reforçada (...).» — art. 27.º, n.º 1, als. h), i), j) RJC (paráfrase)

> «A entidade implementa controlo de acessos baseado em privilégios mínimos, autenticação multi-fator para acessos administrativos e remotos, e gestão documentada do ciclo de vida das credenciais.» — Anexo IV, medidas **O.PAP** + **O.PP** + **T.AM** (síntese aplicável a Grupos A e B)

## MFA: obrigatório para acessos administrativos

A **autenticação multi-fator (MFA)** é o controlo individual de maior impacto. Estima-se que **bloqueie 99% dos ataques baseados em credenciais** — não pelo fator adicional ser mágico, mas porque o **custo do atacante** sobe para níveis em que ataques massivos deixam de compensar.

**Onde tem de estar ativo, sem exceção**:

| Sistema | Quem | Quando |
|---|---|---|
| **Microsoft 365** (e-mail, OneDrive, Teams) | **Todos** os utilizadores | Imediatamente |
| **VPN** corporativa | Todos os que se ligam remotamente | Imediatamente |
| **Acesso administrativo** a servidores, *firewall*, *switch* | Apenas administradores | Imediatamente |
| **Plataforma MyCiber** do CNCS | Pessoas designadas para a plataforma | Por defeito (CC/CMD já são MFA) |
| **Active Directory / identidade central** | Privilegiados (administradores de domínio) | Imediatamente |
| **Aplicações financeiras** (contabilidade, tesouraria, pagamentos) | Utilizadores com poderes de operação financeira | Imediatamente |

**Onde é fortemente recomendado mas pode haver exceções fundamentadas**:

- Aplicações antigas sem suporte para MFA → mitigar com VPN obrigatória + MFA no acesso à VPN.
- Quiosques de atendimento ao público → modelo de conta partilhada com restrições rigorosas + auditoria.

**Tecnologias**: aplicação autenticadora (Microsoft Authenticator, Google Authenticator), SMS (menos seguro mas aceitável onde nada mais funciona), token físico (FIDO2, mais seguro para Grupo A).

Templates: [`politica_controlo_acessos_pt.docx`]({{ '/templates/politica_controlo_acessos_pt.docx' | relative_url }}). _Nota: existe versão `_pt` em vez da convencional `-nis2`; é equivalente em conteúdo, com terminologia portuguesa._

## Palavras-passe — abordagem moderna (NIST)

O conselho tradicional («palavras-passe complexas com símbolos, rotação trimestral, mínimo 8 caracteres») foi **revisto pelo NIST** em 2017 e a tendência consolidou-se na Europa. A regra atual é mais simples e mais segura:

- **Comprimento mínimo**: **12 caracteres** (idealmente **15+**). Caracteres especiais opcionais.
- **Sem rotação obrigatória** (exceto após suspeita de compromisso). Rotações forçadas levam os utilizadores a padrões previsíveis (`Verao2025!`, `Verao2026!`).
- **Verificação contra listas de senhas vazadas** (HaveIBeenPwned, dicionários comuns) — bloquear senhas conhecidas.
- **Gestores de palavras-passe** institucionais incentivados (1Password Business, Bitwarden, KeePass) — eliminam o "reutilizar a mesma password em todo o lado".
- **Frase-passe** como alternativa: `quatro cavalos correm pelo prado verde` (40 caracteres, fácil de lembrar, computacionalmente inquebrável).

Templates: [`politica_palavras_passe_pt.docx`]({{ '/templates/politica_palavras_passe_pt.docx' | relative_url }}).

## Privilégio mínimo (O.PAP)

A maior parte das contas em câmaras portuguesas tem **mais permissões do que deveria**. Trabalhador da contabilidade que tem acesso ao módulo de recursos humanos «porque um dia precisou». Antigo chefe de divisão que ainda é administrador do domínio «porque ninguém revogou». Estagiária que ainda tem conta ativa três anos depois de sair.

**Regra**: cada utilizador tem **exatamente as permissões necessárias** para a função atual. Nem mais, nem menos.

**Operacionalização**:

1. **Inventário de contas** semestral mínimo — quem tem acesso a quê.
2. **Revisão por chefias** trimestral — chefes de divisão validam as permissões da sua equipa.
3. **Revogação imediata** quando função muda (não no fim do mês, no dia).
4. **Contas de prestadores externos** com **data de fim** automática, prolongável apenas com pedido formal.
5. **Contas administrativas** segregadas das contas de utilizador normal — administrador faz login normal com a sua conta de utilizador e eleva quando precisa.

## *Onboarding* e *offboarding* — onde a teoria encontra a vida real

A medida onde se ganha mais com menos esforço é a **checklist de entrada e saída de trabalhadores e prestadores**. Sem ela, contas órfãs acumulam-se. Com ela, o ciclo de vida é controlado.

**Onboarding** (entrada): criação de conta, atribuição de privilégios mínimos, MFA configurado no primeiro dia, formação inicial obrigatória (ver [D.4]({% link 03-outras-medidas/d4-formacao.md %})), termo de confidencialidade assinado, equipamentos entregues com registo.

**Offboarding** (saída ou mudança de função): revogação imediata de credenciais, devolução de equipamentos, transferência de ficheiros do utilizador para a chefia, exclusão de grupos de distribuição, **revogação de MFA no equipamento pessoal** (se aplicável).

Templates:
- [`checklist-onboarding-nis2.docx`]({{ '/templates/checklist-onboarding-nis2.docx' | relative_url }}) — **Aplicar tal-qual**.
- [`checklist-offboarding-nis2.docx`]({{ '/templates/checklist-offboarding-nis2.docx' | relative_url }}) — **Aplicar tal-qual**.
- [`termo-confidencialidade-nis2.docx`]({{ '/templates/termo-confidencialidade-nis2.docx' | relative_url }}) — assinatura obrigatória no *onboarding* para todos os trabalhadores e prestadores com acesso a sistemas.

## Em dupla qualificação

Para o **SMAS** ou empresa municipal qualificada como **entidade essencial**, o regime exige:

- **MFA obrigatório também para utilizadores normais** (não só administradores) — política reforçada.
- **Segregação rigorosa** entre rede TIC corporativa e rede OT (operações técnicas — SCADA, telemetria), com controlo de acessos próprio entre as duas.
- **Auditoria semestral** das permissões em sistemas SCADA (mais frequente do que para câmara).
- **FIDO2 (tokens físicos)** preferido a app autenticadora para administradores de SCADA.

## 💬 Check-in (2 min)

Antes de avançar para D.4, momento curto de revisão. Em quantas das suas **contas privilegiadas** (M365, VPN, administração de servidores, Active Directory, aplicações financeiras) tem **MFA ativo neste momento**?

- 🔴 **Nenhuma** — é o ponto mais frequente de incidentes em câmaras. Ação imediata para a próxima semana.
- 🟠 **1-2** — começou bem; está na altura de alargar a todas as contas privilegiadas.
- 🟡 **3 ou mais (mas não todas)** — bem; falta finalizar. Identifique as que faltam.
- 🟢 **Todas** — postura defensável neste ponto. Validar trimestralmente.

## Templates aplicáveis

| Template | Grupo / Etiqueta | Notas |
|---|---|---|
| [`politica_controlo_acessos_pt.docx`]({{ '/templates/politica_controlo_acessos_pt.docx' | relative_url }}) | **Adaptar — Grupo B e A** | Política de controlo de acessos. Versão `_pt` (equivalente à `-nis2`). |
| [`politica_palavras_passe_pt.docx`]({{ '/templates/politica_palavras_passe_pt.docx' | relative_url }}) | **Adaptar — Grupo B e A** | Política de palavras-passe, alinhada com NIST. |
| [`checklist-onboarding-nis2.docx`]({{ '/templates/checklist-onboarding-nis2.docx' | relative_url }}) | **Aplicar — Grupo B e A** | Checklist de entrada de trabalhador. |
| [`checklist-offboarding-nis2.docx`]({{ '/templates/checklist-offboarding-nis2.docx' | relative_url }}) | **Aplicar — Grupo B e A** | Checklist de saída. |
| [`termo-confidencialidade-nis2.docx`]({{ '/templates/termo-confidencialidade-nis2.docx' | relative_url }}) | **Aplicar — Grupo B e A** | Termo a assinar no *onboarding*. |
| [`politica-seguranca-rh-nis2.docx`]({{ '/templates/politica-seguranca-rh-nis2.docx' | relative_url }}) | Adaptar — Grupo A | Política mais ampla de segurança no ciclo de vida do trabalhador. |
| [`politica-trabalho-remoto-nis2.docx`]({{ '/templates/politica-trabalho-remoto-nis2.docx' | relative_url }}) | Adaptar — Grupo A | Política de teletrabalho seguro. |

## Próximo passo

[D.4 Formação e sensibilização →]({% link 03-outras-medidas/d4-formacao.md %})
