"""
Gera os esqueletos de todas as páginas do hub.

Uso: python tools/gerar_esqueletos.py
Corre a partir da raiz do repo.
"""
from pathlib import Path

ROOT = Path(__file__).parent.parent

# Definição da estrutura: pasta -> (título_pasta, nav_order_pasta, sub_paginas)
# sub_paginas é lista de (slug, titulo)
ESTRUTURA = {
    "00-enquadramento": (
        "A. Enquadramento legal",
        2,
        [
            ("a1-origem-diplomas", "A.1 Origem e estrutura dos diplomas"),
            ("a2-quem-esta-abrangido", "A.2 Quem está abrangido"),
            ("a3-plataforma-cncs", "A.3 Plataforma electrónica do CNCS"),
            ("a4-prazos-sancoes", "A.4 Prazos, sanções e amnistia"),
        ],
    ),
    "01-gestao-risco": (
        "B. Art. 27.º — Risco e ativos",
        3,
        [
            ("b1-art27-panorama", "B.1 Panorama do art. 27.º"),
            ("b2-analise-risco", "B.2 Análise e gestão de risco"),
            ("b3-inventario-ativos", "B.3 Inventário e classificação de ativos"),
            ("b4-sintese", "B.4 Síntese da manhã"),
        ],
    ),
    "02-notificacao-incidentes": (
        "C. Notificação de incidentes",
        4,
        [
            ("c1-plano-resposta", "C.1 Plano de resposta a incidentes"),
            ("c2-prazos-pt-vs-nis2", "C.2 Prazos PT vs NIS2"),
            ("c3-conteudo-notificacao", "C.3 Conteúdo de cada notificação"),
            ("c4-cruzamento-rgpd", "C.4 Cruzamento RGPD"),
            ("c5-demos", "C.5 Demos: simulador e plataforma CNCS"),
            ("c6-cenarios-exercicio", "C.6 Cartões de cenário do exercício A4"),
        ],
    ),
    "03-outras-medidas": (
        "D. Outras medidas do art. 27.º",
        5,
        [
            ("d1-cadeia-fornecimento", "D.1 Cadeia de fornecimento"),
            ("d2-continuidade-backups", "D.2 Continuidade e backups"),
            ("d3-acessos-mfa", "D.3 Acessos, MFA e palavras-passe"),
            ("d4-formacao", "D.4 Formação e sensibilização"),
        ],
    ),
    "04-supervisao-roadmap": (
        "E. Supervisão e roadmap",
        6,
        [
            ("e1-supervisao", "E.1 Supervisão ex post"),
            ("e2-documentacao-minima", "E.2 Documentação mínima — checklist"),
            ("e3-roadmap-6-meses", "E.3 Roadmap 6 meses"),
        ],
    ),
    "exercicios": (
        "Exercícios A1–A5",
        7,
        [
            ("a1-classificacao", "A1. Classificação da autarquia"),
            ("a2-matriz-risco", "A2. Matriz de risco"),
            ("a3-inventario", "A3. Inventário top 5 ativos"),
            ("a4-notificacao", "A4. Simulação de notificação"),
            ("a5-fornecedores", "A5. Top 5 fornecedores críticos"),
        ],
    ),
    "trilho-essencial": (
        "Trilho essencial (dupla qualificação)",
        8,
        [
            ("dupla-qualificacao", "Dupla qualificação: como identificar"),
            ("anexo-iii-vs-anexo-iv", "Anexo III vs Anexo IV"),
            ("smas-checklist", "Checklist específica SMAS"),
        ],
    ),
    "recursos": (
        "Recursos",
        9,
        [
            ("templates", "Índice de templates"),
            ("legislacao", "Legislação e referências"),
            ("glossario", "Glossário"),
            ("faq", "Perguntas frequentes"),
        ],
    ),
    "templates": (
        "Descargas (templates protegidos)",
        10,
        [],
    ),
}

INDEX_TEMPLATE = """---
title: "{titulo}"
layout: default
nav_order: {nav_order}
has_children: {has_children}
---

# {titulo}

> ⏳ Em construção — conteúdo a publicar até 8 de Junho de 2026.
"""

SUB_TEMPLATE = """---
title: "{titulo}"
layout: default
parent: "{parent}"
nav_order: {nav_order}
---

# {titulo}

> ⏳ Em construção — conteúdo a publicar até 8 de Junho de 2026.
"""


def main():
    criados = 0
    for pasta, (titulo, nav_order, sub_paginas) in ESTRUTURA.items():
        dir_path = ROOT / pasta
        dir_path.mkdir(exist_ok=True)

        # Index da pasta
        index_path = dir_path / "index.md"
        has_children = "true" if sub_paginas else "false"
        index_path.write_text(
            INDEX_TEMPLATE.format(
                titulo=titulo, nav_order=nav_order, has_children=has_children
            ),
            encoding="utf-8",
        )
        criados += 1
        print(f"  > {pasta}/index.md")

        # Sub-páginas
        for i, (slug, sub_titulo) in enumerate(sub_paginas, start=1):
            sub_path = dir_path / f"{slug}.md"
            sub_path.write_text(
                SUB_TEMPLATE.format(
                    titulo=sub_titulo, parent=titulo, nav_order=i
                ),
                encoding="utf-8",
            )
            criados += 1
            print(f"    - {pasta}/{slug}.md")

    print(f"\nTotal: {criados} ficheiros criados.")


if __name__ == "__main__":
    main()
