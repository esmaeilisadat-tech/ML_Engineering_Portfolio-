import nbformat
from pathlib import Path

workspace_dir = Path(r'C:\Users\esmae\Documents\Educx Kurs machine lerning\ML_Projekt_Workspace')

projects = [
    '01-ml-engineering-foundations',
    '02-advanced-data-preprocessing',
    'autoencoder-feature-extraction',
    'automl-pipeline-optimization',
    'computer-vision-cnn-cats-dogs',
    'dimensionality-reduction-pca-wine',
    'reinforcement-learning-cartpole',
    'ensemble-learning-model-comparison',
    'gradient-boosting-performance-tuning',
    'hyperparameter-optimization-machine-learning'
]

def fix_notebook(nb_path):
    try:
        with open(nb_path, 'r', encoding='utf-8') as f:
            nb = nbformat.read(f, as_version=4)
            
        modified = False
        for cell in nb.cells:
            if cell.cell_type == 'code':
                # Fix BASE_DIR.name
                if 'if BASE_DIR.name == "exercise":' in cell.source:
                    cell.source = cell.source.replace('if BASE_DIR.name == "exercise":', 'if BASE_DIR.name in ["exercise", "notebooks"]:')
                    modified = True
                
                # Fix OUTPUT_DIR.mkdir
                if 'OUTPUT_DIR.mkdir(exist_ok=True)' in cell.source:
                    cell.source = cell.source.replace('OUTPUT_DIR.mkdir(exist_ok=True)', 'OUTPUT_DIR.mkdir(parents=True, exist_ok=True)')
                    modified = True
                    
                if 'SUBMISSION_DIR.mkdir(exist_ok=True)' in cell.source:
                    cell.source = cell.source.replace('SUBMISSION_DIR.mkdir(exist_ok=True)', 'SUBMISSION_DIR.mkdir(parents=True, exist_ok=True)')
                    modified = True
                    
                if 'TABLE_DIR.mkdir(exist_ok=True)' in cell.source:
                    cell.source = cell.source.replace('TABLE_DIR.mkdir(exist_ok=True)', 'TABLE_DIR.mkdir(parents=True, exist_ok=True)')
                    modified = True
                    
                if 'OUT_TABLES.mkdir(exist_ok=True)' in cell.source:
                    cell.source = cell.source.replace('OUT_TABLES.mkdir(exist_ok=True)', 'OUT_TABLES.mkdir(parents=True, exist_ok=True)')
                    modified = True

        if modified:
            with open(nb_path, 'w', encoding='utf-8') as f:
                nbformat.write(nb, f)
            return True
    except Exception as e:
        print(f"Error reading {nb_path}: {e}")
    return False

total_fixed = 0
for proj in projects:
    proj_dir = workspace_dir / proj
    if not proj_dir.exists(): continue
    for nb_path in proj_dir.rglob('*.ipynb'):
        if '.ipynb_checkpoints' in str(nb_path): continue
        if fix_notebook(nb_path):
            total_fixed += 1
            print(f"Fixed: {nb_path.relative_to(workspace_dir)}")

print(f"\nTotal notebooks fixed: {total_fixed}")
