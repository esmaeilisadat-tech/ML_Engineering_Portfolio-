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
                old_source = cell.source
                s = old_source.replace('\"01_anfaenger\"', '\"Anfaenger\"')
                s = s.replace('\"02_fortgeschrittene\"', '\"Fortgeschrittene\"')
                s = s.replace('\"03_experten\"', '\"Experte\"')
                s = s.replace('\"01_beginner\"', '\"Anfaenger\"')
                s = s.replace('\"02_intermediate\"', '\"Fortgeschrittene\"')
                s = s.replace('\"03_expert\"', '\"Experte\"')
                
                if s != old_source:
                    cell.source = s
                    modified = True
                    
            if cell.cell_type == 'markdown':
                old_source = cell.source
                s = old_source.replace('01_anfaenger', 'Anfaenger')
                s = s.replace('02_fortgeschrittene', 'Fortgeschrittene')
                s = s.replace('03_experten', 'Experte')
                s = s.replace('01_beginner', 'Anfaenger')
                s = s.replace('02_intermediate', 'Fortgeschrittene')
                s = s.replace('03_expert', 'Experte')
                s = s.replace('outputs/', 'output/')
                if s != old_source:
                    cell.source = s
                    modified = True
                    
        if modified:
            with open(nb_path, 'w', encoding='utf-8') as f:
                nbformat.write(nb, f)
            print(f'Fixed hardcoded paths in {nb_path.name}')
    except Exception as e:
        print(f'Error processing {nb_path.name}: {e}')
