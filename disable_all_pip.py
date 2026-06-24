import nbformat
import re
from pathlib import Path

workspace_dir = Path(r'C:\Users\esmae\Documents\Educx Kurs machine lerning\ML_Projekt_Workspace')
notebooks = list(workspace_dir.rglob('*.ipynb'))
for nb_path in notebooks:
    if '.ipynb_checkpoints' in str(nb_path): continue
    try:
        with open(nb_path, 'r', encoding='utf-8') as f:
            nb = nbformat.read(f, as_version=4)
        modified = False
        for cell in nb.cells:
            if cell.cell_type == 'code':
                new_source = []
                for line in cell.source.split('\n'):
                    if 'pip install' in line:
                        new_source.append('# ' + line)
                        modified = True
                    else:
                        new_source.append(line)
                new_str = '\n'.join(new_source)
                if cell.source != new_str:
                    cell.source = new_str
                    modified = True
        if modified:
            with open(nb_path, 'w', encoding='utf-8') as f:
                nbformat.write(nb, f)
            print(f'Disabled pip in {nb_path.name}')
    except Exception as e:
        print(f'Error: {e}')
