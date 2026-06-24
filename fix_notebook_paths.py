import nbformat
import re
from pathlib import Path

workspace_dir = Path(r'C:\Users\esmae\Documents\Educx Kurs machine lerning\ML_Projekt_Workspace')
notebooks = list(workspace_dir.rglob('*.ipynb'))
notebooks = [nb for nb in notebooks if '.ipynb_checkpoints' not in str(nb)]

for nb_path in notebooks:
    try:
        with open(nb_path, 'r', encoding='utf-8') as f:
            nb = nbformat.read(f, as_version=4)
        
        modified = False
        for cell in nb.cells:
            if cell.cell_type == 'code':
                source = cell.source
                
                # Fix output directory name
                if '\"outputs\"' in source:
                    source = source.replace('\"outputs\"', '\"output\"')
                    modified = True
                if '\'outputs\'' in source:
                    source = source.replace('\'outputs\'', '\"output\"')
                    modified = True
                    
                # Fix OUTPUT_SUBDIR values
                old_source = source
                source = re.sub(r'OUTPUT_SUBDIR\s*=\s*[\"\'\']01_anfaenger[\"\'\']', 'OUTPUT_SUBDIR = "Anfaenger"', source)
                source = re.sub(r'OUTPUT_SUBDIR\s*=\s*[\"\'\']02_fortgeschrittene[\"\'\']', 'OUTPUT_SUBDIR = "Fortgeschrittene"', source)
                source = re.sub(r'OUTPUT_SUBDIR\s*=\s*[\"\'\']03_experten[\"\'\']', 'OUTPUT_SUBDIR = "Experte"', source)
                source = re.sub(r'OUTPUT_SUBDIR\s*=\s*[\"\'\']01_beginner[\"\'\']', 'OUTPUT_SUBDIR = "Anfaenger"', source)
                source = re.sub(r'OUTPUT_SUBDIR\s*=\s*[\"\'\']02_intermediate[\"\'\']', 'OUTPUT_SUBDIR = "Fortgeschrittene"', source)
                source = re.sub(r'OUTPUT_SUBDIR\s*=\s*[\"\'\']03_expert[\"\'\']', 'OUTPUT_SUBDIR = "Experte"', source)
                
                # Some notebooks might have hardcoded outputs paths
                source = source.replace('OUTPUT_DIR = PROJECT_DIR / "outputs"', 'OUTPUT_DIR = PROJECT_DIR / "output"')
                source = source.replace('OUT_DIR = PROJECT_DIR / "outputs"', 'OUT_DIR = PROJECT_DIR / "output"')
                
                if source != old_source:
                    modified = True
                
                if source != cell.source:
                    cell.source = source
                    
        if modified:
            with open(nb_path, 'w', encoding='utf-8') as f:
                nbformat.write(nb, f)
            print(f'Fixed output paths in: {nb_path}')
    except Exception as e:
        print(f'Error processing {nb_path.name}: {e}')

print('Notebook paths fixed successfully.')
