import nbformat
from pathlib import Path

nb_path = Path(r'C:\Users\esmae\Documents\Educx Kurs machine lerning\ML_Projekt_Workspace\03-imbalanced-learning-techniques\notebooks\Experte.ipynb')
with open(nb_path, 'r', encoding='utf-8') as f:
    nb = nbformat.read(f, as_version=4)

print(nb.cells[1].outputs if hasattr(nb.cells[1], 'outputs') else 'No output')
