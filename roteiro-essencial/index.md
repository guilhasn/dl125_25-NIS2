---
title: "Roteiro essencial (dupla qualificação)"
layout: default
nav_order: 8
has_children: true
---

# Roteiro essencial — dupla qualificação

{: .note }
> **Grupo A** = autarquia com ≥ 250 trabalhadores  
> **Grupo B** = autarquia com 75-249 trabalhadores  
> (art. 7.º RJC — ver [A.2 Quem está abrangido]({% link 00-enquadramento/a2-quem-esta-abrangido.md %}))

Este roteiro paralelo dirige-se às autarquias que operam serviços de **sectores listados no Anexo I ou II** do DL 125/2025 — tipicamente **água potável e águas residuais** (via SMAS) ou **resíduos** (via empresa municipal). Estas entidades qualificam-se em **duas categorias simultaneamente** com **obrigações cumuláveis** — daí o nome "dupla qualificação".

O conteúdo principal do manual digital (Blocos A a E) é desenhado para a **parte câmara** (entidade pública relevante, Grupo A ou B). Este roteiro acrescenta o que muda quando há uma **parte essencial** ao lado.

## Quem precisa de seguir este roteiro?

Verifique se a sua entidade tem **qualquer uma destas características**:

- ☐ A câmara opera **abastecimento de água potável** ou **águas residuais** (via SMAS, EM ou diretamente).
- ☐ A câmara opera **gestão de resíduos** via empresa municipal (Anexo II).
- ☐ A câmara opera **transportes urbanos** via empresa municipal.
- ☐ A câmara tem empresa municipal de **infraestruturas TIC** prestando serviços a outras entidades.
- ☐ A câmara tem **outra entidade do Anexo I** com dimensão acima dos limiares de média empresa.

Se respondeu **sim** a qualquer ponto, este roteiro aplica-se. Se respondeu **não a todos**, segue só o conteúdo principal do manual digital.

## Sub-páginas

1. [Dupla qualificação: como identificar]({% link roteiro-essencial/dupla-qualificacao.md %}) — quais entidades operacionais podem ser essenciais; como qualificar cada uma; consequências operacionais (dois registos no MyCiber, dois pontos de contacto, dois regimes paralelos).
2. [Anexo III vs Anexo IV]({% link roteiro-essencial/anexo-iii-vs-anexo-iv.md %}) — tabela comparativa das medidas O/T/H nos dois regimes. O que **acumula** quando há dupla qualificação.
3. [Checklist específica SMAS]({% link roteiro-essencial/smas-checklist.md %}) — peças específicas para SMAS qualificado como essencial: RC/PCP designados, segregação rede TIC vs OT, plano sectorial águas, ERSAR, telemetria SCADA.

## A peça-chave: dois conjuntos de obrigações

Resumo gráfico:

```
Município de XPTO (entidade jurídica única)
├── Câmara em sentido próprio (180 trabalhadores)
│   ├── Categoria: Pública relevante Grupo B
│   ├── Regime: art. 33.º RJC + Anexo IV do Aviso
│   ├── Registo no MyCiber: 1 (em nome da câmara)
│   └── Ponto de contacto: 1
└── SMAS de Águas (80 trabalhadores)
    ├── Categoria: Entidade essencial (sector água potável)
    ├── Regime: arts. 26.º-32.º RJC + Anexo III do Aviso (nível B/S/E)
    ├── Registo no MyCiber: 1 (em nome do SMAS — separado da câmara)
    └── RC + PCP designados formalmente (arts. 31.º e 32.º RJC)
```

As duas qualificações geram **dois processos administrativos paralelos** na plataforma do CNCS, com obrigações distintas. Notificação de incidentes faz-se **por entidade afetada**: se o incidente atinge só o SMAS, notifica-se em nome do SMAS; se atinge só a câmara, idem; se atinge as duas, notificam-se **duas vezes**.

## Calendário de leitura

Sugestão: ler este roteiro **depois** do conteúdo principal do manual digital. Os princípios das medidas (O/T/H, ciclo de notificação, plano de continuidade) são os mesmos; muda a **intensidade** e a **formalização**.

| Leu antes... | Aprofunde aqui... |
|---|---|
| [A.2 Quem está abrangido]({% link 00-enquadramento/a2-quem-esta-abrangido.md %}) | [Dupla qualificação: como identificar]({% link roteiro-essencial/dupla-qualificacao.md %}) |
| [B.1 Panorama art. 27.º]({% link 01-gestao-risco/b1-art27-panorama.md %}) | [Anexo III vs Anexo IV]({% link roteiro-essencial/anexo-iii-vs-anexo-iv.md %}) |
| Bloco D completo | [Checklist específica SMAS]({% link roteiro-essencial/smas-checklist.md %}) |
