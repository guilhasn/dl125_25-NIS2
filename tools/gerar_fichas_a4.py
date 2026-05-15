"""
Gera as 4 fichas PDF (formato A5) do Exercício A4 — simulação de notificação 24h.

Cada ficha é um PDF independente, pensado para impressão em papel A5 e distribuição
em sala (uma ficha por par). Tipografia legível em condições de leitura rápida.

Uso:
    python tools/gerar_fichas_a4.py
"""
from pathlib import Path

from reportlab.lib.colors import HexColor, white
from reportlab.lib.pagesizes import A5
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import (
    BaseDocTemplate, Frame, PageTemplate, Paragraph, Spacer, Table, TableStyle,
)

REPO = Path(__file__).resolve().parents[1]
DEST = REPO / "templates"

AZUL = HexColor("#1F4E78")
AZUL_CLARO = HexColor("#D9E1F2")
LARANJA = HexColor("#C55A11")
LARANJA_CLARO = HexColor("#FCE4D6")
CINZA = HexColor("#595959")
CINZA_CLARO = HexColor("#F2F2F2")


def estilo(nome, **kw):
    base = dict(
        fontName="Helvetica",
        fontSize=10.5,
        leading=14,
        textColor=CINZA,
    )
    base.update(kw)
    return ParagraphStyle(name=nome, **base)


def construir_ficha(numero: int, titulo: str, hora: str, narrativa: str,
                    factos: list[tuple[str, str]], destino: Path):
    doc = BaseDocTemplate(
        str(destino), pagesize=A5,
        leftMargin=12 * mm, rightMargin=12 * mm,
        topMargin=10 * mm, bottomMargin=10 * mm,
    )
    frame = Frame(
        doc.leftMargin, doc.bottomMargin,
        doc.width, doc.height, id="conteudo",
        showBoundary=0,
    )
    doc.addPageTemplates([PageTemplate(id="A5", frames=[frame])])

    story = []

    # Cabeçalho — banda azul com número
    cab_data = [[Paragraph(
        f'<font color="white"><b>CENÁRIO Nº {numero}</b></font>',
        estilo("cab_n", fontSize=10, leading=12, textColor=white),
    ), Paragraph(
        f'<font color="white"><b>Exercício A4 · {hora}</b></font>',
        estilo("cab_h", fontSize=10, leading=12, textColor=white,
               alignment=2),
    )]]
    tbl = Table(cab_data, colWidths=[60 * mm, 64 * mm])
    tbl.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), AZUL),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]))
    story.append(tbl)

    # Título do incidente
    story.append(Spacer(1, 5 * mm))
    story.append(Paragraph(
        f"<b>{titulo}</b>",
        estilo("titulo", fontSize=16, leading=20, textColor=AZUL),
    ))

    # Narrativa
    story.append(Spacer(1, 4 * mm))
    story.append(Paragraph(narrativa, estilo("narrativa", fontSize=10.5, leading=15)))

    # Factos numa tabela
    story.append(Spacer(1, 5 * mm))
    factos_data = [
        [Paragraph(f"<b>{k}</b>", estilo("fk", fontSize=9, leading=12)),
         Paragraph(v, estilo("fv", fontSize=9, leading=12))]
        for k, v in factos
    ]
    tbl_factos = Table(factos_data, colWidths=[36 * mm, 88 * mm])
    tbl_factos.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), CINZA_CLARO),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("LINEBELOW", (0, 0), (-1, -2), 0.5, HexColor("#BFBFBF")),
    ]))
    story.append(tbl_factos)

    # Tarefa
    story.append(Spacer(1, 5 * mm))
    tarefa_html = (
        "<b>TAREFA</b><br/><br/>"
        "Preencham a <b>notificação inicial 24h</b> (art. 42.º RJC) "
        "com base nestes factos. Decidam: quando começa a contar o prazo, "
        "qual o conteúdo mínimo, quem assina, e se há que articular com a CNPD "
        "(RGPD) ou Ministério Público (Lei do Cibercrime).<br/><br/>"
        "<b>Tempo: 15 minutos. Output:</b> "
        "<font color=\"#1F4E78\"><b>notificacao-24h-nis2.docx</b></font> "
        "preenchida + nota lateral com as decisões-chave."
    )
    tbl_tarefa = Table(
        [[Paragraph(tarefa_html, estilo("tarefa", fontSize=10, leading=14))]],
        colWidths=[124 * mm],
    )
    tbl_tarefa.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), LARANJA_CLARO),
        ("BOX", (0, 0), (-1, -1), 1, LARANJA),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
    ]))
    story.append(tbl_tarefa)

    # Rodapé
    story.append(Spacer(1, 4 * mm))
    story.append(Paragraph(
        '<font size="7">'
        'Formação NIS2 — A ciberseguranca nas autarquias locais · '
        'guilhasn.github.io/dl125_25-NIS2/'
        '</font>',
        estilo("rodape", fontSize=7, leading=9, textColor=HexColor("#808080"),
               alignment=1),
    ))

    doc.build(story)
    print(f"  [ok] {destino.name}")


CENARIOS = [
    {
        "numero": 1,
        "titulo": "Ransomware no servidor de ficheiros",
        "hora": "Hoje, 15:32",
        "narrativa": (
            "O técnico de informática reporta que <b>três servidores</b> "
            "— incluindo os que alojam o <b>registo civil</b> e o "
            "<b>aprovisionamento</b> — apresentam ecrã de bloqueio com pedido "
            "de resgate em criptomoeda. Cópias de segurança são offline mas "
            "ainda não foram testadas este trimestre. O Vereador da "
            "Modernização exige saber em <b>30 minutos</b> se devem comunicar "
            "à imprensa local."
        ),
        "factos": [
            ("Detecção", "15:32 — alerta da equipa TIC"),
            ("Verificação", "15:48 — confirmada encriptação"),
            ("Sistemas", "Registo civil, aprovisionamento, ficheiros"),
            ("Ficheiros afectados", "~40.000"),
            ("Exfiltração", "Indícios fortes — pastas com dados de munícipes acedidas"),
            ("Backups", "Offline, sem teste recente"),
            ("Pressão externa", "Vereador, imprensa local, eleição em 6 meses"),
        ],
        "ficheiro": "a4-ficha-cenario-1-ransomware.pdf",
    },
    {
        "numero": 2,
        "titulo": "Fornecedor de GED comprometido",
        "hora": "Hoje, 09:15",
        "narrativa": (
            "O fornecedor da vossa aplicação de <b>Gestão Documental</b> "
            "envia comunicado a todos os clientes: foram detectados acessos "
            "não autorizados a servidores partilhados na semana passada. "
            "<b>Não confirma</b> se dados dos vossos munícipes foram acedidos. "
            "A empresa diz estar a investigar e que mais informação chegará "
            "em 48-72h. Vocês têm 5.000 processos sensíveis nessa plataforma."
        ),
        "factos": [
            ("Detecção", "09:15 — comunicado do fornecedor"),
            ("Verificação", "Ainda em curso — depende do fornecedor"),
            ("Sistema afectado", "GED — gestão documental SaaS"),
            ("Volume", "~5.000 processos sensíveis"),
            ("Dados pessoais", "Confirmado — pedidos de acção social, urbanismo"),
            ("Contrato", "Cláusula de notificação prevê 24h — fornecedor cumpriu"),
            ("Acção do fornecedor", "Investigação interna, sem confirmação ainda"),
        ],
        "ficheiro": "a4-ficha-cenario-2-fornecedor.pdf",
    },
    {
        "numero": 3,
        "titulo": "DDoS contra o Portal do Munícipe",
        "hora": "Hoje, 11:00",
        "narrativa": (
            "O <b>Portal do Munícipe</b> e os formulários digitais estão "
            "<b>inacessíveis há 90 minutos</b>. O fornecedor confirma tráfego "
            "anormal a partir de IPs estrangeiros — DDoS volumétrico em curso. "
            "Munícipes não conseguem submeter requerimentos com <b>prazo a "
            "expirar hoje</b> (urbanismo, atendimento social). O Vereador da "
            "Modernização Administrativa pergunta: «quando volta?»."
        ),
        "factos": [
            ("Detecção", "09:30 — monitorização do fornecedor"),
            ("Verificação", "09:45 — confirmação técnica de DDoS"),
            ("Sistemas", "Portal do Munícipe, formulários on-line"),
            ("Duração actual", "90 minutos e a contar"),
            ("Origem", "IPs estrangeiros, vector volumétrico"),
            ("Mitigação", "Fornecedor activou WAF + scrubbing em curso"),
            ("Pressão externa", "Prazos legais a expirar, Vereador, RTP local"),
        ],
        "ficheiro": "a4-ficha-cenario-3-ddos.pdf",
    },
    {
        "numero": 4,
        "titulo": "Phishing à caixa de e-mail do Vereador",
        "hora": "Hoje, 14:00",
        "narrativa": (
            "Detectado movimento anómalo na caixa de <b>e-mail de um "
            "Vereador</b>: 200 e-mails enviados em 30 minutos com pedidos "
            "de transferência bancária para fornecedores municipais, "
            "falsificando assinatura do executivo. Dois fornecedores tentaram "
            "efectuar transferências — os bancos suspenderam. O Vereador "
            "afirma não ter clicado em nada suspeito. MFA não estava activo "
            "na sua conta."
        ),
        "factos": [
            ("Detecção", "13:42 — alerta automático do Microsoft 365"),
            ("Verificação", "13:55 — confirmação de envios não autorizados"),
            ("Conta afectada", "E-mail do Vereador (sem MFA activo)"),
            ("Acções do atacante", "200 e-mails com pedidos de transferência"),
            ("Vítimas tentadas", "2 fornecedores, bancos suspenderam"),
            ("Dados acedidos", "Caixa de e-mail completa do Vereador"),
            ("Vector provável", "Phishing dirigido — falta de MFA"),
        ],
        "ficheiro": "a4-ficha-cenario-4-phishing.pdf",
    },
]


def main():
    DEST.mkdir(parents=True, exist_ok=True)
    print(f"A gerar fichas A5 em {DEST}:")
    for c in CENARIOS:
        construir_ficha(
            c["numero"], c["titulo"], c["hora"],
            c["narrativa"], c["factos"],
            DEST / c["ficheiro"],
        )
    print("Concluído.")


if __name__ == "__main__":
    main()
