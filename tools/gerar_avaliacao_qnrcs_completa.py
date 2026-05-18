"""
Gera o Excel de auto-avaliação de maturidade QNRCS v2 — versão COMPLETA.

Versão complementar do Excel reduzido. Cobre todos os 107 controlos do
Anexo I do Aviso 5146/2026/2, com mapeamentos heurísticos para Anexo IV.
Destina-se a câmaras maduras (Grupo A, SMAS qualificado, ou Grupo B com
maturidade alta) que queiram aprofundar para além dos 26 controlos do
Excel reduzido.

Uso:
    python tools/gerar_avaliacao_qnrcs_completa.py

Saída: templates/avaliacao-maturidade-qnrcs-completa.xlsx (não
encriptado — encriptar a seguir com aplicar_password.py).
"""
from pathlib import Path

from openpyxl import Workbook
from openpyxl.chart import RadarChart, Reference
from openpyxl.formatting.rule import CellIsRule
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.worksheet.datavalidation import DataValidation

from controlos_qnrcs_completos import CONTROLOS_COMPLETOS

# --- estilos partilhados (idênticos ao gerador reduzido) ----------------

TITULO = Font(name="Calibri", size=16, bold=True, color="FFFFFF")
CAB = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
TXT = Font(name="Calibri", size=11)
TXT_NEGRITO = Font(name="Calibri", size=11, bold=True)

AZUL = PatternFill("solid", fgColor="1F4E78")
AZUL_CLARO = PatternFill("solid", fgColor="D9E1F2")
VERDE_CLARO = PatternFill("solid", fgColor="D9EAD3")
AMARELO_CLARO = PatternFill("solid", fgColor="FFF2CC")
VERMELHO_CLARO = PatternFill("solid", fgColor="F4CCCC")

LINHA = Side(border_style="thin", color="A6A6A6")
CAIXA = Border(left=LINHA, right=LINHA, top=LINHA, bottom=LINHA)

CENTRO = Alignment(horizontal="center", vertical="center", wrap_text=True)
ESQUERDA = Alignment(horizontal="left", vertical="center", wrap_text=True)
TOPO = Alignment(horizontal="left", vertical="top", wrap_text=True)

REPO = Path(__file__).resolve().parents[1]
DEST = REPO / "templates"

NOMES_COMPLETOS = {
    "GR": "Gerir",
    "ID": "Identificar",
    "PR": "Proteger",
    "DE": "Detectar",
    "RS": "Responder",
    "RC": "Recuperar",
}

# --- mapeamento Anexo IV (heurístico, baseado nos 26 do Excel reduzido) -

# Mapeamento dos 26 controlos do Excel reduzido (cópia exacta).
# Os restantes 81 controlos recebem mapeamento heurístico por categoria.
MAPEAMENTO_26_REDUZIDO = {
    "GR.CO-3": ("Transversal", "Sim (mínimo Básico)"),
    "GR.GR-1": ("Transversal · B.2", "Sim (mínimo Básico)"),
    "GR.FR-1": ("O.CRI · C.1", "Sim (mínimo Básico)"),
    "GR.PP-1": ("Transversal", "Sim (mínimo Básico)"),
    "GR.SP-1": ("E.1 supervisão", "Sim (mínimo Básico)"),
    "GR.CA-1": ("O.PSF · D.1", "Sim (mínimo Básico)"),
    "ID.GA-1": ("O.IAC · B.3", "Sim (mínimo Básico)"),
    "ID.GA-5": ("O.IAC · B.3", "Sim (mínimo Básico)"),
    "ID.AR-1": ("B.2 análise de risco", "Sim (mínimo Básico)"),
    "ID.MC-1": ("E.2 documentação", "Sim (mínimo Básico)"),
    "PR.GA-1": ("O.GAP · D.3", "Sim (mínimo Básico)"),
    "PR.GA-3": ("T.AM · D.3", "Sim (mínimo Básico)"),
    "PR.FC-1": ("H.PF · D.4", "Sim (mínimo Básico)"),
    "PR.SD-1": ("T.PEW · D.2", "Sim (mínimo Básico)"),
    "PR.SD-5": ("T.CS · D.2", "Sim (mínimo Básico)"),
    "PR.SP-1": ("T.PAS · T.AS · D.3", "Sim (mínimo Básico)"),
    "PR.RI-1": ("T.AS · D.2", "Sim (mínimo Básico)"),
    "DE.MC-1": ("T.MA", "Sim (mínimo Básico)"),
    "DE.AE-1": ("O.GEC", "Sim (mínimo Básico)"),
    "DE.AE-3": ("C.2 prazos", "Sim (mínimo Básico)"),
    "RS.GI-1": ("O.CRI · C.1", "Sim (mínimo Básico)"),
    "RS.AI-1": ("C.6", "Sim (mínimo Básico)"),
    "RS.NC-1": ("art. 42.º · C.2/C.3", "Sim (mínimo Básico)"),
    "RS.MI-1": ("C.6", "Sim (mínimo Básico)"),
    "RC.PR-1": ("T.CS · D.2", "Sim (mínimo Básico)"),
    "RC.CO-1": ("art. 48.º · C.4", "Sim (mínimo Básico)"),
}

# Mapeamento heurístico para controlos fora dos 26.
# Por categoria, define-se o mapeamento padrão e a aplicabilidade.
MAPEAMENTO_HEURISTICO_POR_CATEGORIA = {
    # Gerir
    "GR.CO": ("Transversal", "Sim (mínimo Básico)"),
    "GR.GR": ("B.2 análise de risco", "Sim (mínimo Básico)"),
    "GR.FR": ("O.CRI · C.1", "Sim (mínimo Básico)"),
    "GR.PP": ("Transversal · C.1 plano", "Sim (mínimo Básico)"),
    "GR.SP": ("E.1 supervisão", "Sim (mínimo Básico)"),
    "GR.CA": ("O.PSF · D.1", "Sim (mínimo Básico)"),
    # Identificar
    "ID.GA": ("O.IAC · B.3", "Sim (mínimo Básico)"),
    "ID.AR": ("B.2 análise de risco", "Sim (mínimo Básico)"),
    "ID.MC": ("E.2 documentação", "Sim (mínimo Básico)"),
    # Proteger
    "PR.GA": ("O.GAP · T.AM · D.3", "Sim (mínimo Básico)"),
    "PR.FC": ("H.PF · D.4", "Sim (mínimo Básico)"),
    "PR.SD": ("T.CS · T.PEW · D.2", "Sim (mínimo Básico)"),
    "PR.SP": ("T.PAS · T.AS · D.3", "Sim (mínimo Básico)"),
    "PR.RI": ("T.AS · D.2", "Sim (mínimo Básico)"),
    # Detectar
    "DE.MC": ("T.MA", "Sim (mínimo Básico)"),
    "DE.AE": ("O.GEC · C.2", "Sim (mínimo Básico)"),
    # Responder
    "RS.GI": ("O.CRI · C.1", "Sim (mínimo Básico)"),
    "RS.AI": ("C.6", "Sim (mínimo Básico)"),
    "RS.NC": ("art. 42.º · C.2/C.3", "Sim (mínimo Básico)"),
    "RS.MI": ("C.6", "Sim (mínimo Básico)"),
    # Recuperar
    "RC.PR": ("T.CS · D.2", "Sim (mínimo Básico)"),
    "RC.CO": ("art. 48.º · C.4", "Sim (mínimo Básico)"),
}

# Controlos que são tipicamente fora do escopo Grupo B (Operational
# Technology específica, controlos avançados de Operational Technology, etc.)
# Marcados como "Anexo III · essencial" para SMAS / empresas municipais.
APENAS_ESSENCIAIS = {
    "DE.MC-3",  # monitorização da atividade dos colaboradores — invasivo, raro Grupo B
    "PR.SP-4",  # ciclo de vida de desenvolvimento seguro — só para câmaras que desenvolvem software
    "PR.RI-2",  # ambientes desenvolvimento separados — só relevante se houver desenvolvimento
    "GR.CA-9",  # integração da cadeia em programas formais — Anexo III
    "GR.CA-10",  # processos avançados de cadeia — Anexo III
}


def obter_mapeamento(codigo: str) -> tuple[str, str]:
    """Devolve (mapeamento_anexo_iv, aplicabilidade_grupo_b)."""
    if codigo in MAPEAMENTO_26_REDUZIDO:
        return MAPEAMENTO_26_REDUZIDO[codigo]
    if codigo in APENAS_ESSENCIAIS:
        categoria = ".".join(codigo.split(".")[:2])
        return ("Anexo III · nível B (essenciais)", "Opcional (Grupo A) / Anexo III (essenciais)")
    # heurística por categoria
    categoria = ".".join(codigo.split(".")[:2])
    if categoria in MAPEAMENTO_HEURISTICO_POR_CATEGORIA:
        return MAPEAMENTO_HEURISTICO_POR_CATEGORIA[categoria]
    return ("Transversal", "Sim (recomendado)")


# --- abas ----------------------------------------------------------------

def aba_instrucoes(wb: Workbook) -> None:
    ws = wb.active
    ws.title = "Instruções"

    ws.column_dimensions["A"].width = 110
    ws.row_dimensions[1].height = 30

    ws["A1"] = "Auto-avaliação QNRCS v2 — Versão completa (107 controlos)"
    ws["A1"].font = TITULO
    ws["A1"].fill = AZUL
    ws["A1"].alignment = CENTRO

    linhas = [
        ("Base legal", "Art. 23.º + Anexo I do Aviso n.º 5146/2026/2 — QNRCS v2 integral."),
        ("Para quem", "Câmaras com maturidade alta, Grupo A, ou autarquias com SMAS / empresa municipal qualificada como entidade essencial. Para câmaras Grupo B em fase inicial, recomendamos primeiro o Excel reduzido de 26 controlos (avaliacao-maturidade-qnrcs.xlsx)."),
        ("Cobertura", "Todos os 107 controlos do QNRCS v2, distribuídos pelos 6 objectivos (Gerir · Identificar · Proteger · Detectar · Responder · Recuperar) e 22 categorias."),
        ("Tempo estimado", "~6-8 horas em equipa, distribuídas por 3-4 sessões. Significativamente mais demorado que o Excel reduzido (~2h)."),
        ("Os 3 níveis cumulativos", "Básico ⊂ Substancial ⊂ Elevado. Para Grupo B: aspirar a Básico em controlos com 'Sim (mínimo Básico)' na coluna F. Para parte SMAS/essencial: aspirar a Substancial ou Elevado nos controlos com 'Anexo III · nível B (essenciais)'."),
        ("Mapeamento Anexo IV", "Cada controlo tem indicação na coluna E. 'Transversal' = aplicável a todos. 'Sim (mínimo Básico)' = obrigatório para autarquias Grupo A/B. 'Anexo III · nível B' = exigência específica para entidades essenciais (SMAS); câmara Grupo B pode marcar como 'N/A' com justificação. Os 26 controlos do Excel reduzido têm mapeamento explícito; os restantes 81 têm mapeamento heurístico por categoria."),
        ("Como preencher", "Coluna C 'Estado actual': Não / Parcial / Sim / N/A · Coluna D 'Nível atingido': Não cumpre / Básico / Substancial / Elevado · Coluna G 'Evidência existente'. Controlos 'N/A' não contam para o cálculo de maturidade."),
        ("Dashboard", "Pontuação por objectivo, gráfico radar, lista dos controlos em défice. Controlos marcados 'N/A' são excluídos do denominador."),
    ]

    linha_actual = 3
    for titulo, texto in linhas:
        ws.cell(row=linha_actual, column=1, value=titulo).font = TXT_NEGRITO
        ws.cell(row=linha_actual, column=1).fill = AZUL_CLARO
        ws.cell(row=linha_actual, column=1).alignment = ESQUERDA
        ws.cell(row=linha_actual, column=1).border = CAIXA
        ws.row_dimensions[linha_actual].height = 22

        ws.cell(row=linha_actual + 1, column=1, value=texto).font = TXT
        ws.cell(row=linha_actual + 1, column=1).alignment = TOPO
        ws.cell(row=linha_actual + 1, column=1).border = CAIXA
        ws.row_dimensions[linha_actual + 1].height = 65

        linha_actual += 2


def aba_objectivo(wb: Workbook, prefixo: str, controlos: list) -> None:
    """Cria uma aba com todos os controlos de um objectivo."""
    ws = wb.create_sheet(title=prefixo)
    nome_completo = NOMES_COMPLETOS[prefixo]

    ws.column_dimensions["A"].width = 12
    ws.column_dimensions["B"].width = 60
    ws.column_dimensions["C"].width = 14
    ws.column_dimensions["D"].width = 18
    ws.column_dimensions["E"].width = 30
    ws.column_dimensions["F"].width = 28
    ws.column_dimensions["G"].width = 40
    ws.column_dimensions["H"].width = 30

    ws.merge_cells("A1:H1")
    ws["A1"] = f"Objectivo {prefixo} — {nome_completo} ({len(controlos)} controlos)"
    ws["A1"].font = TITULO
    ws["A1"].fill = AZUL
    ws["A1"].alignment = CENTRO
    ws.row_dimensions[1].height = 28

    cabecalhos = [
        "Código",
        "Descrição do controlo",
        "Estado actual",
        "Nível atingido",
        "Mapeamento Anexo IV",
        "Aplicável Grupo B?",
        "Evidência existente",
        "Notas",
    ]
    for col, texto in enumerate(cabecalhos, start=1):
        c = ws.cell(row=2, column=col, value=texto)
        c.font = CAB
        c.fill = AZUL
        c.alignment = CENTRO
        c.border = CAIXA
    ws.row_dimensions[2].height = 35

    primeira_linha_dados = 3
    for i, (codigo, descricao) in enumerate(controlos, start=primeira_linha_dados):
        mapeamento, aplicavel = obter_mapeamento(codigo)
        ws.cell(row=i, column=1, value=codigo).font = TXT_NEGRITO
        ws.cell(row=i, column=2, value=descricao).font = TXT
        ws.cell(row=i, column=3, value="")
        ws.cell(row=i, column=4, value="")
        ws.cell(row=i, column=5, value=mapeamento).font = TXT
        ws.cell(row=i, column=6, value=aplicavel).font = TXT
        ws.cell(row=i, column=7, value="")
        ws.cell(row=i, column=8, value="")

        for col in range(1, 9):
            ws.cell(row=i, column=col).border = CAIXA
            ws.cell(row=i, column=col).alignment = TOPO if col in (2, 5, 6, 7, 8) else CENTRO

        ws.row_dimensions[i].height = 40

    ultima_linha_dados = primeira_linha_dados + len(controlos) - 1

    # Data validation — Estado (coluna C): inclui N/A
    dv_estado = DataValidation(
        type="list", formula1='"Não,Parcial,Sim,N/A"', allow_blank=True
    )
    dv_estado.add(f"C{primeira_linha_dados}:C{ultima_linha_dados}")
    ws.add_data_validation(dv_estado)

    # Data validation — Nível atingido (coluna D)
    dv_nivel = DataValidation(
        type="list",
        formula1='"Não cumpre,Básico,Substancial,Elevado"',
        allow_blank=True,
    )
    dv_nivel.add(f"D{primeira_linha_dados}:D{ultima_linha_dados}")
    ws.add_data_validation(dv_nivel)

    # Formatação condicional na coluna D
    intervalo_nivel = f"D{primeira_linha_dados}:D{ultima_linha_dados}"
    ws.conditional_formatting.add(
        intervalo_nivel,
        CellIsRule(operator="equal", formula=['"Não cumpre"'], fill=VERMELHO_CLARO),
    )
    ws.conditional_formatting.add(
        intervalo_nivel,
        CellIsRule(operator="equal", formula=['"Básico"'], fill=AMARELO_CLARO),
    )
    ws.conditional_formatting.add(
        intervalo_nivel,
        CellIsRule(operator="equal", formula=['"Substancial"'], fill=VERDE_CLARO),
    )
    ws.conditional_formatting.add(
        intervalo_nivel,
        CellIsRule(operator="equal", formula=['"Elevado"'], fill=VERDE_CLARO),
    )


def aba_dashboard(wb: Workbook) -> None:
    """Dashboard com resumo, % maturidade e gráfico radar.

    Considera Total = controlos não-N/A. Cálculo: (Sim + 0.5*Parcial) / Total.
    """
    ws = wb.create_sheet(title="Dashboard")

    ws.column_dimensions["A"].width = 22
    for letra in ("B", "C", "D", "E", "F"):
        ws.column_dimensions[letra].width = 12
    ws.column_dimensions["G"].width = 18

    ws.merge_cells("A1:G1")
    ws["A1"] = "Dashboard — Perfil de maturidade QNRCS v2 (versão completa)"
    ws["A1"].font = TITULO
    ws["A1"].fill = AZUL
    ws["A1"].alignment = CENTRO
    ws.row_dimensions[1].height = 28

    cabecalhos = ["Objectivo", "Total*", "Sim", "Parcial", "Não", "N/A", "% Maturidade"]
    for col, texto in enumerate(cabecalhos, start=1):
        c = ws.cell(row=3, column=col, value=texto)
        c.font = CAB
        c.fill = AZUL
        c.alignment = CENTRO
        c.border = CAIXA
    ws.row_dimensions[3].height = 30

    primeira_linha_resumo = 4
    for i, prefixo in enumerate(["GR", "ID", "PR", "DE", "RS", "RC"], start=primeira_linha_resumo):
        controlos = CONTROLOS_COMPLETOS[prefixo]
        n_total = len(controlos)
        primeira_linha_dados = 3
        ultima_linha_dados = primeira_linha_dados + n_total - 1
        intervalo = f"'{prefixo}'!C{primeira_linha_dados}:C{ultima_linha_dados}"

        ws.cell(row=i, column=1, value=NOMES_COMPLETOS[prefixo]).font = TXT_NEGRITO
        # Total* = n_total - N/A (controlos efectivos)
        ws.cell(row=i, column=2, value=f'={n_total}-COUNTIF({intervalo},"N/A")')
        ws.cell(row=i, column=3, value=f'=COUNTIF({intervalo},"Sim")')
        ws.cell(row=i, column=4, value=f'=COUNTIF({intervalo},"Parcial")')
        ws.cell(row=i, column=5, value=f'=COUNTIF({intervalo},"Não")')
        ws.cell(row=i, column=6, value=f'=COUNTIF({intervalo},"N/A")')
        # % maturidade: (Sim + 0.5*Parcial) / Total*; protegido contra divisão por zero
        ws.cell(row=i, column=7, value=f'=IF(B{i}=0,0,(C{i}*1+D{i}*0.5)/B{i})')
        ws.cell(row=i, column=7).number_format = "0%"

        for col in range(1, 8):
            ws.cell(row=i, column=col).border = CAIXA
            ws.cell(row=i, column=col).alignment = CENTRO
        ws.row_dimensions[i].height = 22

    ultima_linha_resumo = primeira_linha_resumo + 5

    # Linha total
    linha_total = ultima_linha_resumo + 1
    ws.cell(row=linha_total, column=1, value="Total").font = TXT_NEGRITO
    for col in (2, 3, 4, 5, 6):
        ws.cell(
            row=linha_total,
            column=col,
            value=f"=SUM({chr(64 + col)}{primeira_linha_resumo}:{chr(64 + col)}{ultima_linha_resumo})",
        )
    ws.cell(
        row=linha_total,
        column=7,
        value=f'=IF(B{linha_total}=0,0,(C{linha_total}*1+D{linha_total}*0.5)/B{linha_total})',
    )
    ws.cell(row=linha_total, column=7).number_format = "0%"
    for col in range(1, 8):
        ws.cell(row=linha_total, column=col).fill = AZUL_CLARO
        ws.cell(row=linha_total, column=col).border = CAIXA
        ws.cell(row=linha_total, column=col).alignment = CENTRO
        ws.cell(row=linha_total, column=col).font = TXT_NEGRITO

    # Nota sobre Total*
    linha_nota = linha_total + 1
    ws.merge_cells(start_row=linha_nota, start_column=1, end_row=linha_nota, end_column=7)
    ws.cell(
        row=linha_nota,
        column=1,
        value="* Total = controlos não marcados como 'N/A'. Controlos 'N/A' (não aplicáveis) são excluídos do cálculo de maturidade.",
    )
    ws.cell(row=linha_nota, column=1).font = Font(name="Calibri", size=10, italic=True, color="555555")
    ws.cell(row=linha_nota, column=1).alignment = ESQUERDA

    # Gráfico radar
    chart = RadarChart()
    chart.type = "filled"
    chart.style = 26
    chart.title = "Perfil de maturidade por objectivo (107 controlos)"

    dados = Reference(
        ws,
        min_col=7,
        min_row=3,
        max_row=ultima_linha_resumo,
        max_col=7,
    )
    categorias = Reference(
        ws,
        min_col=1,
        min_row=primeira_linha_resumo,
        max_row=ultima_linha_resumo,
    )
    chart.add_data(dados, titles_from_data=True)
    chart.set_categories(categorias)
    chart.height = 12
    chart.width = 16

    ws.add_chart(chart, f"A{linha_nota + 2}")

    # Recomendação
    linha_rec = linha_nota + 22
    ws.merge_cells(start_row=linha_rec, start_column=1, end_row=linha_rec, end_column=7)
    ws.cell(
        row=linha_rec,
        column=1,
        value=(
            "Os objectivos com pontuação mais baixa são candidatos prioritários "
            "para o roadmap E.3. Para cada objectivo em défice, ir à aba "
            "respectiva e listar os controlos marcados como 'Não' com "
            "Mapeamento Anexo IV não-vazio — esses são as entradas naturais "
            "do plano de 6 meses. Os 26 controlos do Excel reduzido são "
            "a prioridade absoluta."
        ),
    )
    ws.cell(row=linha_rec, column=1).font = TXT
    ws.cell(row=linha_rec, column=1).alignment = TOPO
    ws.cell(row=linha_rec, column=1).fill = AMARELO_CLARO
    ws.cell(row=linha_rec, column=1).border = CAIXA
    ws.row_dimensions[linha_rec].height = 75


# --- main ---------------------------------------------------------------

def main() -> None:
    DEST.mkdir(parents=True, exist_ok=True)
    wb = Workbook()
    aba_instrucoes(wb)
    for prefixo in ("GR", "ID", "PR", "DE", "RS", "RC"):
        aba_objectivo(wb, prefixo, CONTROLOS_COMPLETOS[prefixo])
    aba_dashboard(wb)

    destino = DEST / "avaliacao-maturidade-qnrcs-completa.xlsx"
    wb.save(destino)
    total = sum(len(v) for v in CONTROLOS_COMPLETOS.values())
    print(f"OK -> {destino} ({total} controlos)")


if __name__ == "__main__":
    main()
