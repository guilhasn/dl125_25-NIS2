"""
Gera os 4 worksheets Excel dos exercícios A1, A2, A3 e A5.

Uso:
    python tools/gerar_worksheets_exercicios.py

Saída: 4 ficheiros .xlsx em templates/ (não encriptados — a encriptação
faz-se a seguir com aplicar_password.py).
"""
from pathlib import Path

from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation

# --- estilos partilhados ------------------------------------------------

TITULO = Font(name="Calibri", size=16, bold=True, color="FFFFFF")
SUBTITULO = Font(name="Calibri", size=11, italic=True, color="555555")
CAB = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
TXT = Font(name="Calibri", size=11)
EXEMPLO = Font(name="Calibri", size=11, italic=True, color="808080")

AZUL = PatternFill("solid", fgColor="1F4E78")
AZUL_CLARO = PatternFill("solid", fgColor="D9E1F2")
CINZA = PatternFill("solid", fgColor="F2F2F2")

LINHA = Side(border_style="thin", color="A6A6A6")
CAIXA = Border(left=LINHA, right=LINHA, top=LINHA, bottom=LINHA)

CENTRO = Alignment(horizontal="center", vertical="center", wrap_text=True)
ESQUERDA = Alignment(horizontal="left", vertical="center", wrap_text=True)
TOPO = Alignment(horizontal="left", vertical="top", wrap_text=True)

REPO = Path(__file__).resolve().parents[1]
DEST = REPO / "templates"


def faixa_titulo(ws, titulo: str, subtitulo: str, n_cols: int):
    """Aplica banda visual no topo: linhas 1 (título) + 2 (subtítulo)."""
    ws.merge_cells(start_row=1, start_column=1, end_row=1, end_column=n_cols)
    c = ws.cell(row=1, column=1, value=titulo)
    c.font = TITULO
    c.fill = AZUL
    c.alignment = ESQUERDA
    ws.row_dimensions[1].height = 32

    ws.merge_cells(start_row=2, start_column=1, end_row=2, end_column=n_cols)
    c = ws.cell(row=2, column=1, value=subtitulo)
    c.font = SUBTITULO
    c.alignment = ESQUERDA
    ws.row_dimensions[2].height = 22


def cabecalho(ws, linha: int, valores: list[str]):
    for i, val in enumerate(valores, start=1):
        c = ws.cell(row=linha, column=i, value=val)
        c.font = CAB
        c.fill = AZUL
        c.alignment = CENTRO
        c.border = CAIXA
    ws.row_dimensions[linha].height = 28


def linha_dados(ws, linha: int, valores: list, exemplo: bool = False):
    for i, val in enumerate(valores, start=1):
        c = ws.cell(row=linha, column=i, value=val)
        c.font = EXEMPLO if exemplo else TXT
        c.alignment = TOPO
        c.border = CAIXA
        if exemplo:
            c.fill = CINZA
    ws.row_dimensions[linha].height = 30 if exemplo else 36


def larguras(ws, valores: list[float]):
    for i, w in enumerate(valores, start=1):
        ws.column_dimensions[get_column_letter(i)].width = w


def caixa_instrucoes(ws, linha_inicio: int, n_cols: int, texto: str, altura: int = 90):
    ws.merge_cells(
        start_row=linha_inicio, start_column=1,
        end_row=linha_inicio, end_column=n_cols,
    )
    c = ws.cell(row=linha_inicio, column=1, value=texto)
    c.font = TXT
    c.fill = AZUL_CLARO
    c.alignment = Alignment(horizontal="left", vertical="top", wrap_text=True)
    c.border = CAIXA
    ws.row_dimensions[linha_inicio].height = altura


# --- A1 — Classificação --------------------------------------------------

def gerar_a1():
    wb = Workbook()
    ws = wb.active
    ws.title = "A1 — Classificação"

    cols = ["Entidade operacional", "Tipo", "Nº trabalhadores",
            "Sector (Anexo I/II?)", "Qualificação proposta", "Notas"]
    larguras(ws, [26, 18, 14, 26, 26, 30])

    faixa_titulo(
        ws,
        "Exercício A1 — Classificação da autarquia",
        "10 min · resultado a usar como base da auto-identificação no MyCiber",
        len(cols),
    )

    caixa_instrucoes(
        ws, 3, len(cols),
        "INSTRUÇÕES (em pares, 10 min)\n"
        "1. Listem TODAS as entidades operacionais que dependem da câmara: "
        "câmara em sentido próprio, SMAS, empresa(s) municipal(ais), fundação(ões), "
        "agências regionais com participação. Uma linha por entidade.\n"
        "2. Para cada, preencham número actual de trabalhadores e sector de actividade.\n"
        "3. Apliquem o critério do art. 7.º RJC + Anexos I/II do DL 125/2025:\n"
        "   • ≥ 250 trab. → Grupo A (pública relevante)  • 75-249 → Grupo B  • < 75 → fora do regime\n"
        "   • Se opera serviços do Anexo I (água, resíduos, energia, …) e excede limiar de média empresa → entidade ESSENCIAL.\n"
        "4. A linha 7 traz um exemplo a apagar antes de começarem.",
        altura=140,
    )

    cabecalho(ws, 5, cols)

    # exemplo (linha 6)
    linha_dados(
        ws, 6,
        ["[exemplo] Câmara Municipal de Vale Verde", "Câmara",
         "180", "Administração Local (sem Anexo I/II)",
         "Grupo B — entidade pública relevante",
         "Limiar 75-249. Confirmar com mapa de pessoal a 31 Dez."],
        exemplo=True,
    )

    # linhas em branco (6 entradas para preencher)
    for i in range(7, 13):
        linha_dados(ws, i, ["", "", "", "", "", ""])

    # validação de dados — coluna E (Qualificação)
    qualificacoes = ('"Grupo A — pública relevante,Grupo B — pública relevante,'
                     'Fora do regime,Entidade essencial,Entidade importante,Em dúvida"')
    dv = DataValidation(type="list", formula1=qualificacoes, allow_blank=True)
    dv.add("E6:E12")
    ws.add_data_validation(dv)

    # validação de tipo
    tipos = '"Câmara,SMAS,Empresa municipal,Fundação,Agência,Outro"'
    dv2 = DataValidation(type="list", formula1=tipos, allow_blank=True)
    dv2.add("B6:B12")
    ws.add_data_validation(dv2)

    ws.print_options.horizontalCentered = True
    ws.page_setup.orientation = ws.ORIENTATION_LANDSCAPE
    ws.page_setup.fitToWidth = 1
    ws.page_setup.fitToHeight = 1
    ws.sheet_properties.pageSetUpPr.fitToPage = True

    out = DEST / "a1-classificacao-autarquia.xlsx"
    wb.save(out)
    print(f"  [ok] {out.name}")


# --- A2 — Matriz de risco -----------------------------------------------

def gerar_a2():
    wb = Workbook()
    ws = wb.active
    ws.title = "A2 — Matriz de risco"

    cols = ["#", "Risco identificado", "Activo afectado",
            "Probabilidade (1-5)", "Impacto (1-5)", "Nível (P×I)",
            "Tratamento", "Acção concreta"]
    larguras(ws, [4, 30, 22, 14, 12, 12, 16, 30])

    faixa_titulo(
        ws,
        "Exercício A2 — Matriz de risco da entidade",
        "15 min · 3 riscos identificados, classificados e com tratamento decidido",
        len(cols),
    )

    caixa_instrucoes(
        ws, 3, len(cols),
        "INSTRUÇÕES (em pares, 15 min)\n"
        "1. Identifiquem 3 riscos da vossa autarquia. Não inventem — pensem em coisas que vos preocupam realmente "
        "(ransomware, indisponibilidade do portal, dependência de fornecedor único, …).\n"
        "2. Para cada, indiquem qual ACTIVO é mais afectado (ver Exercício A3 a seguir).\n"
        "3. Classifiquem probabilidade (1=raro, 5=quase certo) e impacto (1=irrelevante, 5=paralisação).\n"
        "4. Nível P×I é calculado automaticamente. Risco 1-6 = baixo, 8-12 = médio, 15-25 = alto.\n"
        "5. Decidam tratamento (Mitigar / Transferir / Aceitar / Evitar) e descrevam a acção concreta.\n"
        "6. A linha 7 traz exemplo a apagar.",
        altura=160,
    )

    cabecalho(ws, 5, cols)

    # exemplo
    linha_dados(
        ws, 6,
        [1, "[exemplo] Ransomware encripta servidor de ficheiros",
         "Servidor de ficheiros + cópias online",
         3, 5, "=D6*E6", "Mitigar",
         "Backups offline testados trimestralmente + MFA nos acessos administrativos"],
        exemplo=True,
    )

    # 3 linhas em branco
    for i, n in enumerate([1, 2, 3]):
        r = 7 + i
        linha_dados(ws, r, [n, "", "", "", "", f"=D{r}*E{r}", "", ""])

    # validações
    dv_pi = DataValidation(type="list", formula1='"1,2,3,4,5"', allow_blank=True)
    dv_pi.add("D6:E9")
    ws.add_data_validation(dv_pi)

    dv_tr = DataValidation(
        type="list", formula1='"Mitigar,Transferir,Aceitar,Evitar"',
        allow_blank=True,
    )
    dv_tr.add("G6:G9")
    ws.add_data_validation(dv_tr)

    ws.print_options.horizontalCentered = True
    ws.page_setup.orientation = ws.ORIENTATION_LANDSCAPE
    ws.sheet_properties.pageSetUpPr.fitToPage = True

    out = DEST / "a2-matriz-risco-simplificada.xlsx"
    wb.save(out)
    print(f"  [ok] {out.name}")


# --- A3 — Inventário top 5 ----------------------------------------------

def gerar_a3():
    wb = Workbook()
    ws = wb.active
    ws.title = "A3 — Inventário top 5"

    cols = ["#", "Activo crítico", "Tipo", "Serviço público que suporta",
            "Responsável funcional", "Fornecedor",
            "Dependência principal", "Acessível pela Internet?"]
    larguras(ws, [4, 26, 16, 26, 22, 18, 24, 16])

    faixa_titulo(
        ws,
        "Exercício A3 — Top 5 activos críticos",
        "10 min · base do inventário O.IAC + ponto de partida da lista do art. 32.º",
        len(cols),
    )

    caixa_instrucoes(
        ws, 3, len(cols),
        "INSTRUÇÕES (em pares, 10 min)\n"
        "1. Listem os 5 activos cuja indisponibilidade compromete serviço público obrigatório da câmara. "
        "Exemplos: portal do munícipe, balcão único, contabilidade, GED, e-mail institucional, "
        "controlador de domínio, sistema de bombagem (SMAS), SIG cadastral.\n"
        "2. Para cada, identifiquem responsável funcional INTERNO (não fornecedor) e fornecedor externo.\n"
        "3. Marquem se está directamente acessível pela Internet — esses entram na lista do art. 32.º.\n"
        "4. A linha 7 traz exemplo a apagar.",
        altura=140,
    )

    cabecalho(ws, 5, cols)

    # exemplo
    linha_dados(
        ws, 6,
        [1, "[exemplo] Portal do Munícipe", "Aplicação web",
         "Pedidos on-line de licenciamento e certidões",
         "Chefe de Divisão de Modernização",
         "Medidata",
         "Servidor de base de dados + autenticação CC/CMD",
         "Sim"],
        exemplo=True,
    )

    # 5 linhas em branco
    for i, n in enumerate([1, 2, 3, 4, 5]):
        linha_dados(ws, 7 + i, [n, "", "", "", "", "", "", ""])

    # validações
    tipo_vals = ('"Servidor,Aplicação web,Base de dados,Equipamento de rede,'
                 'Serviço cloud,Equipamento OT/SCADA,Outro"')
    dv1 = DataValidation(type="list", formula1=tipo_vals, allow_blank=True)
    dv1.add("C6:C11")
    ws.add_data_validation(dv1)

    dv2 = DataValidation(type="list", formula1='"Sim,Não"', allow_blank=True)
    dv2.add("H6:H11")
    ws.add_data_validation(dv2)

    ws.print_options.horizontalCentered = True
    ws.page_setup.orientation = ws.ORIENTATION_LANDSCAPE
    ws.sheet_properties.pageSetUpPr.fitToPage = True

    out = DEST / "a3-inventario-top5.xlsx"
    wb.save(out)
    print(f"  [ok] {out.name}")


# --- A5 — Top 5 fornecedores --------------------------------------------

def gerar_a5():
    wb = Workbook()
    ws = wb.active
    ws.title = "A5 — Top 5 fornecedores"

    cols = ["#", "Fornecedor", "Serviço prestado",
            "Acesso a dados pessoais?", "Criticidade",
            "Contrato formal?", "Risco identificado", "Mitigação prevista"]
    larguras(ws, [4, 22, 28, 16, 14, 14, 28, 24])

    faixa_titulo(
        ws,
        "Exercício A5 — Top 5 fornecedores TIC",
        "10 min · base do inventário de fornecedores + risco de cadeia de abastecimento",
        len(cols),
    )

    caixa_instrucoes(
        ws, 3, len(cols),
        "INSTRUÇÕES (em pares, 10 min)\n"
        "1. Listem os 5 fornecedores TIC mais críticos da câmara — aqueles cuja falha ou compromisso "
        "afecta directamente o vosso serviço público. Tipicamente: Medidata, AIRC, Glintt, Microsoft, "
        "alojamento, ISP, segurança de rede, GED, SIG, contabilidade.\n"
        "2. Para cada, indiquem se tratam dados pessoais de munícipes (cuidado com RGPD).\n"
        "3. Classifiquem a criticidade (Alta/Média/Baixa) e confirmem se há contrato formal em vigor.\n"
        "4. Identifiquem o principal risco e a mitigação já prevista (se houver).\n"
        "5. A linha 7 traz exemplo a apagar.",
        altura=160,
    )

    cabecalho(ws, 5, cols)

    # exemplo
    linha_dados(
        ws, 6,
        [1, "[exemplo] Medidata",
         "Gestão documental + portal do munícipe",
         "Sim", "Alta", "Sim",
         "Dependência única — sem alternativa funcional a curto prazo",
         "Plano de contingência + cláusulas SLA reforçadas no próximo concurso"],
        exemplo=True,
    )

    for i, n in enumerate([1, 2, 3, 4, 5]):
        linha_dados(ws, 7 + i, [n, "", "", "", "", "", "", ""])

    dv_sim = DataValidation(type="list", formula1='"Sim,Não,Não sei"', allow_blank=True)
    dv_sim.add("D6:D11")
    dv_sim.add("F6:F11")
    ws.add_data_validation(dv_sim)

    dv_crit = DataValidation(type="list", formula1='"Alta,Média,Baixa"', allow_blank=True)
    dv_crit.add("E6:E11")
    ws.add_data_validation(dv_crit)

    ws.print_options.horizontalCentered = True
    ws.page_setup.orientation = ws.ORIENTATION_LANDSCAPE
    ws.sheet_properties.pageSetUpPr.fitToPage = True

    out = DEST / "a5-top5-fornecedores.xlsx"
    wb.save(out)
    print(f"  [ok] {out.name}")


def main():
    DEST.mkdir(parents=True, exist_ok=True)
    print(f"A gerar worksheets em {DEST}:")
    gerar_a1()
    gerar_a2()
    gerar_a3()
    gerar_a5()
    print("Concluído.")


if __name__ == "__main__":
    main()
