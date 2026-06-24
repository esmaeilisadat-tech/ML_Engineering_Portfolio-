import nbformat
from pathlib import Path
import re

workspace_dir = Path(r'C:\Users\esmae\Documents\Educx Kurs machine lerning\ML_Projekt_Workspace')

projects = {
    '01-ml-engineering-foundations': ['energy_data.csv', 'life_data.csv'],
    'anomaly-detection-outlier-analysis': ['indian_pharmaceutical_products_clean.csv'],
    'ensemble-learning-model-comparison': ['Steel_industry_data.csv'],
    'gradient-boosting-performance-tuning': ['bank.csv', 'train.csv'],
    'hyperparameter-optimization-machine-learning': ['bank.csv', 'bank-full.csv', 'train.csv', 'test.csv', 'sonar.csv', 'auto-insurance.csv', 'mobile_price_data_train.csv']
}

print("=== Missing Data Check Report ===")
for proj, files in projects.items():
    proj_dir = workspace_dir / proj
    data_dir = proj_dir / 'data'
    missing = []
    found = []
    
    for f in files:
        if (data_dir / f).exists():
            found.append(f)
        else:
            missing.append(f)
            
    print(f"\nProject: {proj}")
    print(f"  Required Data Files: {', '.join(files)}")
    print(f"  Found: {', '.join(found) if found else 'None'}")
    if missing:
        print(f"  Missing: {', '.join(missing)}")
        print(f"  Next Action: User needs to download and place these files.")
    else:
        print(f"  Missing: None")
        print(f"  Next Action: Ready for execution.")
