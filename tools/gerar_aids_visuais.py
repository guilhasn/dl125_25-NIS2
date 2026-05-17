"""
Gera os 3 aids visuais imprimíveis do manual digital:
  1. folha-resumo-prazos-pt-vs-nis2.pdf — A4 retrato
  2. roadmap-6-meses.pdf — A4 paisagem
  3. mapa-art27-anexo-iv.pdf — A4 paisagem

Uso:
    python tools/gerar_aids_visuais.py
"""
from pathlib import Path

from reportlab.lib.colors import HexColor, white
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import (
    BaseDocTemplate, Frame, PageTemplate, Paragraph, Spacer, Table, TableStyle,
)

REPO = Path(__file__).resolve().parents[1]
DEST = REPO / "templates"

AZUL = HexColor("#1F4E78")
AZUL_CLARO = HexColor("#D9E1F2")
AZUL_MUITO_CLARO = HexColor("#EEF2F7")
LARANJA = HexColor("#C55A11")
LARANJA_CLARO = HexColor("#FCE4D6")
VERMELHO = HexColor("#C00000")
VERMELHO_CLARO = HexColor("#FDECEA")
VERDE = HexColor("#1F7A1F")
VERDE_CLARO = HexColor("#E8F5E8")
CINZA = HexColor("#595959")
CINZA_CLARO = HexColor("#F2F2F2")
PRETO = HexColor("#2C3E50")


def estilo(nome, **kw):
    base = dict(
        fontName="Helvetica", fontSize=10, leading=13, textColor=PRETO,
    )
    base.update(kw)
    return ParagraphStyle(name=nome, **base)


def banda_titulo(story, titulo, subtitulo, largura_mm, cor=AZUL):
    tbl = Table(
        [
            [Paragraph(
                f'<font color="white"><b>{titulo}</b></font>',
                estilo("t", fontSize=14, leading=18, textColor=white),
            )],
            [Paragraph(
                f'<font color="white">{subtitulo}</font>',
                estilo("st", fontSize=9, leading=12, textColor=white),
            )],
        ],
        colWidths=[largura_mm * mm],
    )
    tbl.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), cor),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
        ("TOPPADDING", (0, 0), (-1, 0), 8),
        ("BOTTOMPADDING", (0, 0), (-1, 0), 2),
        ("TOPPADDING", (0, 1), (-1, 1), 0),
        ("BOTTOMPADDING", (0, 1), (-1, 1), 8),
    ]))
    story.append(tbl)


def rodape_paragraph(story, label):
    story.append(Spacer(1, 4 * mm))
    story.append(Paragraph(
        f'<font size="7" color="#808080">{label} · '
        f'Formação NIS2 — guilhasn.github.io/dl125_25-NIS2/</font>',
        estilo("rod", fontSize=7, leading=9, textColor=CINZA, alignment=1),
    ))


# ============================================================
# 1. FOLHA-RESUMO PRAZOS PT vs NIS2 (A4 retrato)
# ============================================================

def gerar_folha_prazos():
    destino = DEST / "folha-resumo-prazos-pt-vs-nis2.pdf"
    doc = BaseDocTemplate(
        str(destino), pagesize=A4,
        leftMargin=12 * mm, rightMargin=12 * mm,
        topMargin=10 * mm, bottomMargin=10 * mm,
    )
    largura = (A4[0] - 24 * mm) / mm
    frame = Frame(
        doc.leftMargin, doc.bottomMargin,
        doc.width, doc.height, id="c", showBoundary=0,
    )
    doc.addPageTemplates([PageTemplate(id="A4", frames=[frame])])

    story = []
    banda_titulo(
        story,
        "PRAZOS DE NOTIFICAÇÃO — Regime PT vs Directiva NIS2",
        "DL 125/2025 (RJC) · arts. 40.º a 44.º · Aviso 5146/2026/2 (arts. 20.º a 22.º)",
        largura, AZUL,
    )

    story.append(Spacer(1, 4 * mm))
    story.append(Paragraph(
        "<b>⚠️ ATENÇÃO:</b> o regime PT tem 4 prazos distintos. Quem trouxer da memória "
        "os prazos «24h + 72h + 1 mês» da NIS2 pura <b>vai perder pelo menos um prazo</b>. "
        "Esta folha é para afixar no gabinete TIC ou na matriz de escalação.",
        estilo("av", fontSize=9.5, leading=13, textColor=VERMELHO),
    ))
    story.append(Spacer(1, 4 * mm))

    # Tabela principal de prazos
    cab = [
        Paragraph("<b>O QUÊ</b>", estilo("h", fontSize=9, leading=11, textColor=white)),
        Paragraph("<b>QUANDO</b>", estilo("h", fontSize=9, leading=11, textColor=white)),
        Paragraph("<b>BASE LEGAL</b>", estilo("h", fontSize=9, leading=11, textColor=white)),
        Paragraph("<b>NIS2 pura (comparar)</b>", estilo("h", fontSize=9, leading=11, textColor=white)),
    ]
    linhas = [
        cab,
        [
            Paragraph("<b>Notificação inicial</b>", estilo("c", fontSize=9, leading=11)),
            Paragraph("<b>24h após verificação</b><br/>(não detecção!)", estilo("c", fontSize=9, leading=11)),
            Paragraph("art. 42.º, n.º 1 RJC", estilo("c", fontSize=9, leading=11)),
            Paragraph("24h após<br/>conhecimento", estilo("c", fontSize=9, leading=11)),
        ],
        [
            Paragraph("Actualização (opcional)", estilo("c", fontSize=9, leading=11)),
            Paragraph("72h", estilo("c", fontSize=9, leading=11)),
            Paragraph("art. 42.º, n.º 3 RJC", estilo("c", fontSize=9, leading=11)),
            Paragraph("Obrigatória<br/>(72h)", estilo("c", fontSize=9, leading=11)),
        ],
        [
            Paragraph("<b>Fim de impacto significativo</b><br/>(específica PT)", estilo("c", fontSize=9, leading=11)),
            Paragraph("<b>24h após cessação</b>", estilo("c", fontSize=9, leading=11)),
            Paragraph("art. 43.º RJC", estilo("c", fontSize=9, leading=11)),
            Paragraph("Não existe", estilo("c", fontSize=9, leading=11)),
        ],
        [
            Paragraph("Relatório final", estilo("c", fontSize=9, leading=11)),
            Paragraph("<b>30 dias úteis</b><br/>após fim de impacto", estilo("c", fontSize=9, leading=11)),
            Paragraph("art. 44.º RJC", estilo("c", fontSize=9, leading=11)),
            Paragraph("1 mês", estilo("c", fontSize=9, leading=11)),
        ],
        [
            Paragraph("Relatório intercalar", estilo("c", fontSize=9, leading=11)),
            Paragraph("Semanal<br/>se incidente persistir", estilo("c", fontSize=9, leading=11)),
            Paragraph("art. 44.º, n.º 3 RJC", estilo("c", fontSize=9, leading=11)),
            Paragraph("—", estilo("c", fontSize=9, leading=11)),
        ],
        [
            Paragraph("<b>Resolução em ≤ 2h</b>", estilo("c", fontSize=9, leading=11)),
            Paragraph("<b>DISPENSA</b> notificação inicial", estilo("c", fontSize=9, leading=11)),
            Paragraph("art. 41.º RJC", estilo("c", fontSize=9, leading=11)),
            Paragraph("Não previsto", estilo("c", fontSize=9, leading=11)),
        ],
    ]
    tbl = Table(linhas, colWidths=[40 * mm, 50 * mm, 35 * mm, 40 * mm])
    tbl.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), AZUL),
        ("BACKGROUND", (0, 1), (-1, 1), AZUL_MUITO_CLARO),
        ("BACKGROUND", (0, 3), (-1, 3), AZUL_MUITO_CLARO),
        ("BACKGROUND", (0, 6), (-1, 6), VERDE_CLARO),
        ("GRID", (0, 0), (-1, -1), 0.5, CINZA),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]))
    story.append(tbl)
    story.append(Spacer(1, 5 * mm))

    # Quando começa o relógio
    story.append(Paragraph(
        "<b>Quando começa o relógio</b>",
        estilo("h", fontSize=11, leading=14, textColor=AZUL),
    ))
    story.append(Spacer(1, 2 * mm))
    story.append(Paragraph(
        "O relógio das <b>24h</b> conta a partir da <b>verificação</b> do incidente significativo "
        "— ou seja, o momento em que a equipa TIC confirma a natureza, escala e impacto. "
        "<b>Não</b> a partir da detecção inicial (alerta).",
        estilo("p", fontSize=9.5, leading=13),
    ))
    story.append(Paragraph(
        "<b>T0</b> = detecção (alerta, ex.: 15h32) · "
        "<b>T1</b> = verificação técnica (ex.: 15h48) · "
        "<b>T2</b> = submissão notificação inicial até 24h após T1 (até 15h48 do dia seguinte).",
        estilo("p", fontSize=9.5, leading=13),
    ))
    story.append(Spacer(1, 5 * mm))

    # Contactos de emergência
    story.append(Paragraph(
        "<b>Se a plataforma MyCiber falhar — art. 17.º Aviso</b>",
        estilo("h", fontSize=11, leading=14, textColor=LARANJA),
    ))
    story.append(Spacer(1, 2 * mm))
    contact_data = [
        [
            Paragraph("<b>Canal alternativo</b>", estilo("ch", fontSize=9, leading=11)),
            Paragraph("<b>Como</b>", estilo("ch", fontSize=9, leading=11)),
        ],
        [
            Paragraph("E-mail", estilo("c", fontSize=9, leading=11)),
            Paragraph("cncs@cncs.gov.pt", estilo("c", fontSize=9, leading=11, fontName="Courier")),
        ],
        [
            Paragraph("Telefone", estilo("c", fontSize=9, leading=11)),
            Paragraph("CERT.PT (consultar cncs.gov.pt)", estilo("c", fontSize=9, leading=11)),
        ],
        [
            Paragraph("Plataforma", estilo("c", fontSize=9, leading=11)),
            Paragraph("myciber.gov.pt", estilo("c", fontSize=9, leading=11, fontName="Courier")),
        ],
    ]
    tbl_c = Table(contact_data, colWidths=[40 * mm, 125 * mm])
    tbl_c.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), LARANJA),
        ("TEXTCOLOR", (0, 0), (-1, 0), white),
        ("GRID", (0, 0), (-1, -1), 0.5, CINZA),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]))
    story.append(tbl_c)
    story.append(Spacer(1, 5 * mm))

    # Canais paralelos
    story.append(Paragraph(
        "<b>Canais paralelos quando há dados pessoais ou crime informático</b>",
        estilo("h", fontSize=11, leading=14, textColor=AZUL),
    ))
    story.append(Spacer(1, 2 * mm))
    par_data = [
        [
            Paragraph("<b>Regime</b>", estilo("ch", fontSize=9, leading=11, textColor=white)),
            Paragraph("<b>Autoridade</b>", estilo("ch", fontSize=9, leading=11, textColor=white)),
            Paragraph("<b>Prazo</b>", estilo("ch", fontSize=9, leading=11, textColor=white)),
        ],
        [
            Paragraph("NIS2 / DL 125/2025", estilo("c", fontSize=9, leading=11)),
            Paragraph("CNCS", estilo("c", fontSize=9, leading=11)),
            Paragraph("24h após verificação", estilo("c", fontSize=9, leading=11)),
        ],
        [
            Paragraph("RGPD / Lei 58/2019", estilo("c", fontSize=9, leading=11)),
            Paragraph("CNPD", estilo("c", fontSize=9, leading=11)),
            Paragraph("72h após conhecimento", estilo("c", fontSize=9, leading=11)),
        ],
        [
            Paragraph("Lei do Cibercrime (109/2009)", estilo("c", fontSize=9, leading=11)),
            Paragraph("Ministério Público", estilo("c", fontSize=9, leading=11)),
            Paragraph("Sem prazo estrito (paralelo)", estilo("c", fontSize=9, leading=11)),
        ],
    ]
    tbl_p = Table(par_data, colWidths=[65 * mm, 50 * mm, 50 * mm])
    tbl_p.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), AZUL),
        ("GRID", (0, 0), (-1, -1), 0.5, CINZA),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]))
    story.append(tbl_p)

    rodape_paragraph(story, "Folha-resumo Prazos PT vs NIS2")
    doc.build(story)
    print(f"  [ok] {destino.name}")


# ============================================================
# 2. ROADMAP 6 MESES (A4 paisagem)
# ============================================================

def gerar_roadmap():
    destino = DEST / "roadmap-6-meses.pdf"
    doc = BaseDocTemplate(
        str(destino), pagesize=landscape(A4),
        leftMargin=10 * mm, rightMargin=10 * mm,
        topMargin=10 * mm, bottomMargin=10 * mm,
    )
    largura = (landscape(A4)[0] - 20 * mm) / mm
    frame = Frame(
        doc.leftMargin, doc.bottomMargin,
        doc.width, doc.height, id="c", showBoundary=0,
    )
    doc.addPageTemplates([PageTemplate(id="A4L", frames=[frame])])

    story = []
    banda_titulo(
        story,
        "ROADMAP DE 6 MESES — Conformidade NIS2 para autarquias (Grupo B)",
        "Para chegar ao mínimo demonstrável que invoca o art. 65.º RJC (dispensa de coimas) até Abril de 2027",
        largura, AZUL,
    )

    story.append(Spacer(1, 4 * mm))

    cab = [
        Paragraph("<b>MÊS</b>", estilo("h", fontSize=10, leading=12, textColor=white)),
        Paragraph("<b>FOCO</b>", estilo("h", fontSize=10, leading=12, textColor=white)),
        Paragraph("<b>ENTREGÁVEIS-CHAVE</b>", estilo("h", fontSize=10, leading=12, textColor=white)),
        Paragraph("<b>PEÇA QUE SAI</b>", estilo("h", fontSize=10, leading=12, textColor=white)),
    ]
    meses = [
        [
            Paragraph("<b>1</b>", estilo("c", fontSize=14, leading=17, alignment=1, textColor=AZUL)),
            Paragraph("<b>Qualificação</b>", estilo("c", fontSize=10, leading=12)),
            Paragraph(
                "☐ Auto-identificação no MyCiber<br/>"
                "☐ Despacho ponto de contacto<br/>"
                "☐ Classificação entidades operacionais<br/>"
                "☐ Lista art. 32.º (20 dias úteis)<br/>"
                "☐ Registo SMAS separado (se aplicável)",
                estilo("c", fontSize=9, leading=12),
            ),
            Paragraph("Comprovativo<br/>de registo +<br/>lista pública", estilo("c", fontSize=9, leading=12)),
        ],
        [
            Paragraph("<b>2</b>", estilo("c", fontSize=14, leading=17, alignment=1, textColor=AZUL)),
            Paragraph("<b>Políticas-base</b>", estilo("c", fontSize=10, leading=12)),
            Paragraph(
                "☐ Política segurança da informação<br/>"
                "☐ Política palavras-passe (NIST)<br/>"
                "☐ Política controlo de acessos<br/>"
                "☐ Política backups<br/>"
                "☐ Política gestão de incidentes",
                estilo("c", fontSize=9, leading=12),
            ),
            Paragraph("5 políticas<br/>aprovadas por<br/>despacho", estilo("c", fontSize=9, leading=12)),
        ],
        [
            Paragraph("<b>3</b>", estilo("c", fontSize=14, leading=17, alignment=1, textColor=AZUL)),
            Paragraph("<b>Diagnóstico</b>", estilo("c", fontSize=10, leading=12)),
            Paragraph(
                "☐ Inventário 20-40 activos críticos<br/>"
                "☐ Inventário 15-25 fornecedores<br/>"
                "☐ Matriz risco 15-25 entradas<br/>"
                "☐ Mapeamento activos × fornecedores<br/>"
                "☐ (A) Funções críticas (O.ID, O.PSI)",
                estilo("c", fontSize=9, leading=12),
            ),
            Paragraph("Inventário +<br/>matriz<br/>completos", estilo("c", fontSize=9, leading=12)),
        ],
        [
            Paragraph("<b>4</b>", estilo("c", fontSize=14, leading=17, alignment=1, textColor=AZUL)),
            Paragraph("<b>Medidas técnicas</b>", estilo("c", fontSize=10, leading=12)),
            Paragraph(
                "☐ MFA em M365 / VPN / admin<br/>"
                "☐ Backups testados (1.º teste)<br/>"
                "☐ Backup air-gapped<br/>"
                "☐ Patches em dia<br/>"
                "☐ SPF + DKIM + DMARC<br/>"
                "☐ HTTPS em sites institucionais",
                estilo("c", fontSize=9, leading=12),
            ),
            Paragraph("Configurações<br/>técnicas<br/>documentadas", estilo("c", fontSize=9, leading=12)),
        ],
        [
            Paragraph("<b>5</b>", estilo("c", fontSize=14, leading=17, alignment=1, textColor=AZUL)),
            Paragraph("<b>Resposta</b>", estilo("c", fontSize=10, leading=12)),
            Paragraph(
                "☐ Plano Continuidade Negócio (PCN)<br/>"
                "☐ Playbooks ransomware + data breach<br/>"
                "☐ Matriz de escalação afixada<br/>"
                "☐ Folha-resumo prazos afixada<br/>"
                "☐ Tabletop exercise interno",
                estilo("c", fontSize=9, leading=12),
            ),
            Paragraph("PCN +<br/>playbooks +<br/>1ª simulação", estilo("c", fontSize=9, leading=12)),
        ],
        [
            Paragraph("<b>6</b>", estilo("c", fontSize=14, leading=17, alignment=1, textColor=VERDE)),
            Paragraph("<b>Ciclo</b>", estilo("c", fontSize=10, leading=12, textColor=VERDE)),
            Paragraph(
                "☐ Auditoria interna<br/>"
                "☐ Plano de acções correctivas<br/>"
                "☐ 1.ª sessão de formação anual<br/>"
                "☐ Registo de presenças<br/>"
                "☐ <b>Acta de revisão pela gestão</b>",
                estilo("c", fontSize=9, leading=12),
            ),
            Paragraph("<b>Acta anual<br/>assinada<br/>pelo presidente</b>", estilo("c", fontSize=9, leading=12, textColor=VERDE)),
        ],
    ]
    tbl = Table([cab] + meses, colWidths=[18 * mm, 38 * mm, 130 * mm, 40 * mm])
    tbl.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), AZUL),
        ("BACKGROUND", (0, 1), (-1, 1), AZUL_MUITO_CLARO),
        ("BACKGROUND", (0, 3), (-1, 3), AZUL_MUITO_CLARO),
        ("BACKGROUND", (0, 5), (-1, 5), AZUL_MUITO_CLARO),
        ("BACKGROUND", (0, 6), (-1, 6), VERDE_CLARO),
        ("GRID", (0, 0), (-1, -1), 0.5, CINZA),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]))
    story.append(tbl)

    story.append(Spacer(1, 5 * mm))
    story.append(Paragraph(
        "<b>Após o mês 6 — ciclo anual de manutenção:</b> "
        "Anual: revisão pela gestão, plano de formação, lista art. 32.º · "
        "Semestral: revisão das matrizes, teste do PCN · "
        "Trimestral: teste de backup, revisão de contas, refresher de formação · "
        "Mensal: patches, monitorização, logs.",
        estilo("p", fontSize=9, leading=12),
    ))

    rodape_paragraph(story, "Roadmap 6 meses NIS2 — A imprimir e afixar")
    doc.build(story)
    print(f"  [ok] {destino.name}")


# ============================================================
# 3. MAPA ART. 27.º → ANEXO IV (A4 paisagem)
# ============================================================

def gerar_mapa_art27():
    destino = DEST / "mapa-art27-anexo-iv.pdf"
    doc = BaseDocTemplate(
        str(destino), pagesize=landscape(A4),
        leftMargin=10 * mm, rightMargin=10 * mm,
        topMargin=10 * mm, bottomMargin=10 * mm,
    )
    largura = (landscape(A4)[0] - 20 * mm) / mm
    frame = Frame(
        doc.leftMargin, doc.bottomMargin,
        doc.width, doc.height, id="c", showBoundary=0,
    )
    doc.addPageTemplates([PageTemplate(id="A4L", frames=[frame])])

    story = []
    banda_titulo(
        story,
        "MAPA DE CORRESPONDÊNCIA — art. 27.º RJC → Anexo IV do Aviso 5146",
        "Para autarquias: o art. 27.º NÃO se aplica directamente; o que vincula é o Anexo IV",
        largura, AZUL,
    )

    story.append(Spacer(1, 3 * mm))
    story.append(Paragraph(
        "<b>⚠️</b> O <b>art. 27.º RJC</b> aplica-se a entidades essenciais e importantes. "
        "Para autarquias (Grupo A/B), o regime concreto é o <b>art. 33.º RJC + Anexo IV do Aviso 5146</b>, "
        "organizado em <b>3 famílias</b>: <b>O</b> (Organizacionais), <b>T</b> (Técnicas), <b>H</b> (Humanas).",
        estilo("p", fontSize=9.5, leading=13),
    ))
    story.append(Spacer(1, 3 * mm))

    cab = [
        Paragraph("<b>Alínea<br/>art. 27.º</b>", estilo("h", fontSize=9, leading=11, textColor=white)),
        Paragraph("<b>Tema</b>", estilo("h", fontSize=9, leading=11, textColor=white)),
        Paragraph("<b>Anexo III<br/>(essenciais)</b>", estilo("h", fontSize=9, leading=11, textColor=white)),
        Paragraph("<b>Anexo IV — Grupo B<br/>(autarquia 75-249 trab.)</b>", estilo("h", fontSize=9, leading=11, textColor=white)),
        Paragraph("<b>Anexo IV — Grupo A<br/>(adicional, ≥250 trab.)</b>", estilo("h", fontSize=9, leading=11, textColor=white)),
    ]
    linhas = [
        cab,
        [
            Paragraph("<b>a)</b>", estilo("c", fontSize=10, leading=12, alignment=1)),
            Paragraph("Tratamento<br/>de incidentes", estilo("c", fontSize=9, leading=11)),
            Paragraph("Medidas O+T<br/>dedicadas + RC/PCP", estilo("c", fontSize=8.5, leading=10.5)),
            Paragraph("<b>O.CRI</b><br/>(ponto de contacto)", estilo("c", fontSize=8.5, leading=10.5)),
            Paragraph("+ Políticas formais<br/>de gestão eventos", estilo("c", fontSize=8.5, leading=10.5)),
        ],
        [
            Paragraph("<b>b)</b>", estilo("c", fontSize=10, leading=12, alignment=1)),
            Paragraph("Continuidade,<br/>backups, DR", estilo("c", fontSize=9, leading=11)),
            Paragraph("O.PCN + T.CS + T.RAR<br/>(matriz Anexo II)", estilo("c", fontSize=8.5, leading=10.5)),
            Paragraph("<b>T.CS</b> (cópias) +<br/><b>T.RAR</b> (registos)", estilo("c", fontSize=8.5, leading=10.5)),
            Paragraph("+ Segregação<br/>backups + air-gap", estilo("c", fontSize=8.5, leading=10.5)),
        ],
        [
            Paragraph("<b>c)</b>", estilo("c", fontSize=10, leading=12, alignment=1)),
            Paragraph("Cadeia de<br/>abastecimento", estilo("c", fontSize=9, leading=11)),
            Paragraph("Medidas dedicadas<br/>(art. 28.º RJC)", estilo("c", fontSize=8.5, leading=10.5)),
            Paragraph("<b>O.PSF</b><br/>(inventário + contactos)", estilo("c", fontSize=8.5, leading=10.5)),
            Paragraph("<b>O.PSF</b> completa<br/>(política + scorecard)", estilo("c", fontSize=8.5, leading=10.5)),
        ],
        [
            Paragraph("<b>d)</b>", estilo("c", fontSize=10, leading=12, alignment=1)),
            Paragraph("Aquisição,<br/>vulnerabilidades", estilo("c", fontSize=9, leading=11)),
            Paragraph("Medidas dedicadas<br/>+ certificação", estilo("c", fontSize=8.5, leading=10.5)),
            Paragraph("<b>T.AS</b> + <b>T.GPT</b><br/>(patches)", estilo("c", fontSize=8.5, leading=10.5)),
            Paragraph("+ <b>T.SC</b> (hardening)", estilo("c", fontSize=8.5, leading=10.5)),
        ],
        [
            Paragraph("<b>e)</b>", estilo("c", fontSize=10, leading=12, alignment=1)),
            Paragraph("Avaliação<br/>de eficácia", estilo("c", fontSize=9, leading=11)),
            Paragraph("Auditorias e SOA", estilo("c", fontSize=8.5, leading=10.5)),
            Paragraph("(sem medida<br/>específica)", estilo("c", fontSize=8.5, leading=10.5)),
            Paragraph("Indirectamente<br/>via <b>O.GMO</b>", estilo("c", fontSize=8.5, leading=10.5)),
        ],
        [
            Paragraph("<b>f)</b>", estilo("c", fontSize=10, leading=12, alignment=1)),
            Paragraph("Ciber-higiene<br/>e formação", estilo("c", fontSize=9, leading=11)),
            Paragraph("Medidas H<br/>dedicadas", estilo("c", fontSize=8.5, leading=10.5)),
            Paragraph("<b>H.PF</b> (plano) +<br/><b>H.FIC</b> (formação)", estilo("c", fontSize=8.5, leading=10.5)),
            Paragraph("+ <b>H.EC</b><br/>(phishing simulado)", estilo("c", fontSize=8.5, leading=10.5)),
        ],
        [
            Paragraph("<b>g)</b>", estilo("c", fontSize=10, leading=12, alignment=1)),
            Paragraph("Criptografia", estilo("c", fontSize=9, leading=11)),
            Paragraph("Medidas T<br/>dedicadas", estilo("c", fontSize=8.5, leading=10.5)),
            Paragraph("<b>T.PEW</b><br/>(SPF, DKIM, HTTPS)", estilo("c", fontSize=8.5, leading=10.5)),
            Paragraph("+ HSTS, MTA-STS,<br/>cabeçalhos HTTP", estilo("c", fontSize=8.5, leading=10.5)),
        ],
        [
            Paragraph("<b>h)</b>", estilo("c", fontSize=10, leading=12, alignment=1)),
            Paragraph("Seg. RH +<br/>acessos +<br/>activos", estilo("c", fontSize=9, leading=11)),
            Paragraph("Medidas O+H<br/>dedicadas", estilo("c", fontSize=8.5, leading=10.5)),
            Paragraph("<b>O.IAC</b> + <b>O.GAP</b> +<br/><b>O.GMO</b>", estilo("c", fontSize=8.5, leading=10.5)),
            Paragraph("+ <b>O.PAP</b> + <b>O.PUA</b> +<br/><b>O.PP</b> + <b>O.GEC</b> + <b>O.ID</b>", estilo("c", fontSize=8.5, leading=10.5)),
        ],
        [
            Paragraph("<b>i)</b>", estilo("c", fontSize=10, leading=12, alignment=1)),
            Paragraph("MFA +<br/>comunicações<br/>seguras", estilo("c", fontSize=9, leading=11)),
            Paragraph("Medidas T<br/>dedicadas", estilo("c", fontSize=8.5, leading=10.5)),
            Paragraph("<b>T.AM</b> + <b>T.AR</b> +<br/><b>T.PAS</b> + <b>T.MA</b>", estilo("c", fontSize=8.5, leading=10.5)),
            Paragraph("+ <b>T.GP</b> + <b>T.PAD</b>", estilo("c", fontSize=8.5, leading=10.5)),
        ],
    ]
    tbl = Table(linhas, colWidths=[18 * mm, 36 * mm, 50 * mm, 60 * mm, 62 * mm])
    tbl.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), AZUL),
        ("BACKGROUND", (0, 1), (-1, 1), AZUL_MUITO_CLARO),
        ("BACKGROUND", (0, 3), (-1, 3), AZUL_MUITO_CLARO),
        ("BACKGROUND", (0, 5), (-1, 5), AZUL_MUITO_CLARO),
        ("BACKGROUND", (0, 7), (-1, 7), AZUL_MUITO_CLARO),
        ("BACKGROUND", (0, 9), (-1, 9), AZUL_MUITO_CLARO),
        ("GRID", (0, 0), (-1, -1), 0.5, CINZA),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ]))
    story.append(tbl)

    story.append(Spacer(1, 4 * mm))
    story.append(Paragraph(
        "<b>O Grupo A acumula sempre o Grupo B</b> — para uma câmara grande, somam-se as duas colunas direita. "
        "<b>Anexo IV não tem medida explícita «análise de risco»</b> — emerge transversalmente das medidas O. "
        "<b>art. 32.º Aviso</b> (lista de activos publicamente acessíveis) é transversal a essenciais + importantes + públicas relevantes — 20 dias úteis.",
        estilo("p", fontSize=8.5, leading=11),
    ))

    rodape_paragraph(story, "Mapa art. 27.º → Anexo IV")
    doc.build(story)
    print(f"  [ok] {destino.name}")


def main():
    DEST.mkdir(parents=True, exist_ok=True)
    print(f"A gerar aids visuais em {DEST}:")
    gerar_folha_prazos()
    gerar_roadmap()
    gerar_mapa_art27()
    print("Concluído.")


if __name__ == "__main__":
    main()
