import nbformat
from pathlib import Path

nb_path = Path(r'C:\Users\esmae\Documents\Educx Kurs machine lerning\ML_Projekt_Workspace\03-imbalanced-learning-techniques\notebooks\Experte.ipynb')
with open(nb_path, 'r', encoding='utf-8') as f:
    nb = nbformat.read(f, as_version=4)

for i, cell in enumerate(nb.cells):
    if cell.cell_type == 'code':
        if 'OUTPUT_DIR' in cell.source:
            print(f"--- Cell {i} ---")
            print(cell.source)
