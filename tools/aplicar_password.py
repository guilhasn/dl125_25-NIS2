"""
Protege todos os templates da formação com password de abertura.

Uso:
    python aplicar_password.py <pasta_origem> <pasta_destino>

Exemplo:
    python tools/aplicar_password.py "C:/Users/nuno/Dropbox/Formação/#Formação/2026/DL 125_25 (NIS2)/Templates" "C:/Users/nuno/Dropbox/Formação/#Formação/2026/DL 125_25 (NIS2)/Templates_protegidos"

Encripta DOCX/XLSX/PPTX via msoffcrypto-tool (formato OOXML).
Outros tipos de ficheiro são apenas copiados.
"""
import sys
import shutil
from pathlib import Path

from msoffcrypto.format.ooxml import OOXMLFile

PASSWORD = "NIS2_DL125_$%2026"
EXTENSOES_SUPORTADAS = {".docx", ".xlsx", ".pptx"}


def proteger_ficheiro(origem: Path, destino: Path) -> str:
    """Encripta um ficheiro Office. Retorna 'encriptado' | 'copiado' | 'erro'."""
    destino.parent.mkdir(parents=True, exist_ok=True)

    if origem.suffix.lower() not in EXTENSOES_SUPORTADAS:
        shutil.copy2(origem, destino)
        return "copiado"

    with open(origem, "rb") as f_in:
        office = OOXMLFile(f_in)
        with open(destino, "wb") as f_out:
            office.encrypt(PASSWORD, f_out)
    return "encriptado"


def main():
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(1)

    origem = Path(sys.argv[1])
    destino = Path(sys.argv[2])

    if not origem.is_dir():
        print(f"ERRO: pasta de origem nao existe: {origem}")
        sys.exit(1)

    destino.mkdir(parents=True, exist_ok=True)

    encriptados = 0
    copiados = 0
    erros = []

    for ficheiro in origem.rglob("*"):
        if ficheiro.is_dir():
            continue
        rel = ficheiro.relative_to(origem)
        destino_ficheiro = destino / rel
        try:
            resultado = proteger_ficheiro(ficheiro, destino_ficheiro)
            if resultado == "encriptado":
                encriptados += 1
                print(f"  [enc] {rel}")
            else:
                copiados += 1
                print(f"  [cpy] {rel}")
        except Exception as e:
            erros.append((str(rel), str(e)))
            print(f"  [ERR] {rel}: {e}")

    print(f"\nResumo: {encriptados} encriptados, {copiados} copiados, {len(erros)} erros.")
    if erros:
        print("\nErros:")
        for r, e in erros:
            print(f"  - {r}: {e}")
        sys.exit(2)


if __name__ == "__main__":
    main()
