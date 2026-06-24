import nbformat
from pathlib import Path

nb_path = Path(r'C:\Users\esmae\Documents\Educx Kurs machine lerning\ML_Projekt_Workspace\03-imbalanced-learning-techniques\notebooks\Experte.ipynb')
with open(nb_path, 'r', encoding='utf-8') as f:
    nb = nbformat.read(f, as_version=4)

modified = False
for cell in nb.cells:
    if cell.cell_type == 'code':
        if 'if BASE_DIR.name == "exercise":' in cell.source:
            cell.source = cell.source.replace('if BASE_DIR.name == "exercise":', 'if BASE_DIR.name in ["exercise", "notebooks"]:')
            modified = True
        if 'OUTPUT_DIR.mkdir(exist_ok=True)' in cell.source:
            cell.source = cell.source.replace('OUTPUT_DIR.mkdir(exist_ok=True)', 'OUTPUT_DIR.mkdir(parents=True, exist_ok=True)')
            modified = True

if modified:
    with open(nb_path, 'w', encoding='utf-8') as f:
        nbformat.write(nb, f)
    print("Fixed BASE_DIR logic and mkdir(parents=True) in Experte.ipynb")
