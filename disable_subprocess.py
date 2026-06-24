import nbformat
from pathlib import Path

nb_path = Path(r'C:\Users\esmae\Documents\Educx Kurs machine lerning\ML_Projekt_Workspace\decision-trees-predictive-modeling\notebooks\Experte.ipynb')
with open(nb_path, 'r', encoding='utf-8') as f:
    nb = nbformat.read(f, as_version=4)

for cell in nb.cells:
    if cell.cell_type == 'code' and 'subprocess.check_call' in cell.source and '\"shap\"' in cell.source:
        cell.source = '# subprocess check_call pip install shap disabled'

with open(nb_path, 'w', encoding='utf-8') as f:
    nbformat.write(nb, f)
print('Disabled subprocess pip install in Experte.ipynb')
