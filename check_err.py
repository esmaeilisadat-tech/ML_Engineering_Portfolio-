import nbformat
from pathlib import Path

nb_path = Path(r'C:\Users\esmae\Documents\Educx Kurs machine lerning\ML_Projekt_Workspace\03-imbalanced-learning-techniques\notebooks\Experte.ipynb')
with open(nb_path, 'r', encoding='utf-8') as f:
    nb = nbformat.read(f, as_version=4)

for i, cell in enumerate(nb.cells):
    if cell.cell_type == 'code':
        for output in cell.outputs:
            if output.output_type == 'error':
                print(f"--- Error in Cell {i} ---")
                print('\n'.join(output.traceback))
