from pathlib import Path

workspace_dir = Path(r'C:\Users\esmae\Documents\Educx Kurs machine lerning\ML_Projekt_Workspace')

for project_dir in workspace_dir.iterdir():
    if project_dir.is_dir() and not project_dir.name.startswith('.') and project_dir.name not in ['__pycache__', 'outputs', 'venv']:
        output_dir = project_dir / 'output'
        if output_dir.exists():
            items = list(output_dir.rglob('*'))
            files = [str(f.relative_to(output_dir)) for f in items if f.is_file() and f.name != '.gitkeep']
            if files:
                print(f"Files in {project_dir.name}/output: {files}")
