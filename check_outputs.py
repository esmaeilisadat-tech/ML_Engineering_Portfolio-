from pathlib import Path

workspace_dir = Path(r'C:\Users\esmae\Documents\Educx Kurs machine lerning\ML_Projekt_Workspace')

for project_dir in workspace_dir.iterdir():
    if project_dir.is_dir() and not project_dir.name.startswith('.') and project_dir.name not in ['__pycache__', 'outputs', 'venv']:
        print(f"\n--- Project: {project_dir.name} ---")
        
        # Check outputs folder
        old_outputs = project_dir / 'outputs'
        if old_outputs.exists():
            print(f"  [WARNING] Old 'outputs' folder exists!")
        
        output_dir = project_dir / 'output'
        if not output_dir.exists():
            print(f"  [ERROR] 'output' folder missing!")
        else:
            subdirs = [d.name for d in output_dir.iterdir() if d.is_dir()]
            print(f"  Output subdirs: {subdirs}")
            files = [f.name for f in output_dir.iterdir() if f.is_file()]
            if files:
                print(f"  [WARNING] Files in root output dir: {len(files)}")
            
            for sd in ['Anfaenger', 'Fortgeschrittene', 'Experte']:
                if sd not in subdirs:
                    print(f"  [INFO] Missing subdir '{sd}'")
