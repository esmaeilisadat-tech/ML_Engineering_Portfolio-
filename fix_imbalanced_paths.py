import nbformat
from pathlib import Path

nb_path = Path(r'C:\Users\esmae\Documents\Educx Kurs machine lerning\ML_Projekt_Workspace\03-imbalanced-learning-techniques\notebooks\Experte.ipynb')
with open(nb_path, 'r', encoding='utf-8') as f:
    nb = nbformat.read(f, as_version=4)

modified = False
for cell in nb.cells:
    if cell.cell_type == 'code':
        if 'OUTPUT_DIR = BASE_DIR / "output"' in cell.source:
            cell.source = cell.source.replace(
                'OUTPUT_DIR = BASE_DIR / "output"',
                'OUTPUT_DIR = BASE_DIR / "output" / "Experte"'
            )
            modified = True
            
if modified:
    with open(nb_path, 'w', encoding='utf-8') as f:
        nbformat.write(nb, f)
    print("Modified Experte.ipynb to use output/Experte")
