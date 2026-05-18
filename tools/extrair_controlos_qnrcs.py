"""
Extrai todos os controlos do QNRCS v2 a partir do texto integral do
Anexo I do Aviso 5146/2026/2 e produz um ficheiro Python com a lista
estruturada (código, descrição) para alimentar o gerador completo.

Uso:
    python tools/extrair_controlos_qnrcs.py <input_txt> <output_py>

Exemplo:
    python tools/extrair_controlos_qnrcs.py C:/Users/nuno/AppData/Local/Temp/aviso5146.txt tools/controlos_qnrcs_completos.py
"""
import re
import sys
from pathlib import Path

PREFIXOS = ("GR", "ID", "PR", "DE", "RS", "RC")

# Regex: início de linha com `XX.YY-N — texto` ou `XX.YY - N — texto`.
# Aceita variações com espaços extra.
PADRAO = re.compile(
    r"^(?P<codigo>(?:GR|ID|PR|DE|RS|RC)\.[A-Z]{2}\s*-\s*\d+)\s+—\s+(?P<descricao>.+?)$",
    re.MULTILINE,
)


def normalizar_codigo(codigo: str) -> str:
    """Remove espaços internos: 'ID.GA - 4' -> 'ID.GA-4'."""
    return re.sub(r"\s*-\s*", "-", codigo).strip()


def extrair(texto: str) -> dict:
    """Devolve dict {objectivo: [(codigo, descricao), ...]} ordenado."""
    vistos = set()
    por_objectivo: dict[str, list] = {p: [] for p in PREFIXOS}

    for m in PADRAO.finditer(texto):
        codigo = normalizar_codigo(m.group("codigo"))
        descricao = m.group("descricao").strip()
        # filtrar entradas das tabelas de medidas (que repetem códigos)
        if codigo in vistos:
            continue
        # ignorar entradas muito curtas (provavelmente fragmentos)
        if len(descricao) < 15:
            continue
        # se a descrição termina com word-break "com-" ou similar, juntar
        # a linha seguinte do texto original para completar
        if descricao.endswith("-"):
            inicio_seguinte = m.end()
            resto_texto = texto[inicio_seguinte:inicio_seguinte + 500]
            # a linha seguinte é tudo até ao próximo \n
            proxima_linha = resto_texto.split("\n", 2)[1] if "\n" in resto_texto else ""
            proxima_linha = proxima_linha.strip()
            # ignorar se a linha seguinte parecer cabeçalho de página
            if proxima_linha and not re.match(r"^\d+/\d+", proxima_linha) and not proxima_linha.startswith("==="):
                descricao = descricao.rstrip("-") + proxima_linha
        vistos.add(codigo)

        objectivo = codigo.split(".")[0]
        if objectivo in por_objectivo:
            por_objectivo[objectivo].append((codigo, descricao))

    return por_objectivo


def ordenar_codigo(codigo: str):
    """Chave de ordenação: (prefixo, categoria, número)."""
    match = re.match(r"^([A-Z]{2})\.([A-Z]{2})-(\d+)$", codigo)
    if not match:
        return (codigo, 0, 0)
    return (match.group(1), match.group(2), int(match.group(3)))


def gerar_python(por_objectivo: dict) -> str:
    nomes_obj = {
        "GR": "Gerir",
        "ID": "Identificar",
        "PR": "Proteger",
        "DE": "Detectar",
        "RS": "Responder",
        "RC": "Recuperar",
    }
    linhas = [
        '"""Lista completa dos controlos do QNRCS v2 (Anexo I do Aviso 5146/2026/2).',
        "",
        "Gerado automaticamente por extrair_controlos_qnrcs.py.",
        "Não editar manualmente — para regenerar, correr o script novamente.",
        '"""',
        "",
        "CONTROLOS_COMPLETOS = {",
    ]
    total = 0
    for prefixo in PREFIXOS:
        controlos = sorted(por_objectivo[prefixo], key=lambda x: ordenar_codigo(x[0]))
        total += len(controlos)
        linhas.append(f'    "{prefixo}": [  # {nomes_obj[prefixo]} — {len(controlos)} controlos')
        for codigo, descricao in controlos:
            descricao_clean = descricao.replace('"', "'").rstrip(".")
            linhas.append(f'        ("{codigo}", "{descricao_clean}"),')
        linhas.append("    ],")
    linhas.append("}")
    linhas.append("")
    linhas.append(f"# Total: {total} controlos")
    return "\n".join(linhas)


def main() -> None:
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(1)

    input_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2])

    if not input_path.is_file():
        print(f"ERRO: input nao existe: {input_path}")
        sys.exit(1)

    texto = input_path.read_text(encoding="utf-8")
    por_objectivo = extrair(texto)

    total = sum(len(v) for v in por_objectivo.values())
    print(f"Extraidos {total} controlos:")
    for prefixo in PREFIXOS:
        print(f"  {prefixo}: {len(por_objectivo[prefixo])}")

    saida = gerar_python(por_objectivo)
    output_path.write_text(saida, encoding="utf-8")
    print(f"OK -> {output_path}")


if __name__ == "__main__":
    main()
