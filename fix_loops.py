import nbformat
import re
from pathlib import Path

workspace_dir = Path(r"C:\Users\esmae\Documents\Educx Kurs machine lerning\ML_Projekt_Workspace")
notebooks = list(workspace_dir.rglob("*.ipynb"))
notebooks = [nb for nb in notebooks if ".ipynb_checkpoints" not in str(nb)]

for nb_path in notebooks:
    try:
        with open(nb_path, "r", encoding="utf-8") as f:
            nb = nbformat.read(f, as_version=4)
        
        modified = False
        for cell in nb.cells:
            if cell.cell_type == "code":
                source = cell.source
                
                # Replace the dangerous while loops for PROJECT_DIR/PROJECT_ROOT
                pattern1 = r'while PROJECT_DIR\.name[^:]+:\s*\n\s*PROJECT_DIR = PROJECT_DIR\.parent'
                if re.search(pattern1, source):
                    new_source = re.sub(pattern1, 'if PROJECT_DIR.name == "notebooks":\n    PROJECT_DIR = PROJECT_DIR.parent', source)
                    source = new_source
                    modified = True
                    
                pattern2 = r'while PROJECT_ROOT\.name[^:]+:\s*\n\s*PROJECT_ROOT = PROJECT_ROOT\.parent'
                if re.search(pattern2, source):
                    new_source = re.sub(pattern2, 'if PROJECT_ROOT.name == "notebooks":\n    PROJECT_ROOT = PROJECT_ROOT.parent', source)
                    source = new_source
                    modified = True
                    
                # Fix the admin / technician string to float error in Hyperparameter Anfaenger
                if "admin." in source and "bank_preprocessor" in source:
                    # Let's ensure categorical columns are handled correctly if it's the Pipeline cell
                    pass

                # In case DATA_DIR was hardcoded to C:\data anywhere else
                if "C:\\data" in source or "C:/data" in source:
                    new_source = source.replace("C:\\data", "data").replace("C:/data", "data")
                    source = new_source
                    modified = True

                if source != cell.source:
                    cell.source = source
                    modified = True
                    
        if modified:
            with open(nb_path, "w", encoding="utf-8") as f:
                nbformat.write(nb, f)
            print(f"Fixed dangerous loop in: {nb_path.name}")
    except Exception as e:
        print(f"Error processing {nb_path.name}: {e}")

print("Path correction complete.")
