import nbformat
from pathlib import Path
import re

workspace_dir = Path(r'C:\Users\esmae\Documents\Educx Kurs machine lerning\ML_Projekt_Workspace')

projects = [
    '01-ml-engineering-foundations',
    '02-advanced-data-preprocessing',
    'anomaly-detection-outlier-analysis',
    'autoencoder-feature-extraction',
    'automl-pipeline-optimization',
    'computer-vision-cnn-cats-dogs',
    'dimensionality-reduction-pca-wine',
    'ensemble-learning-model-comparison',
    'gradient-boosting-performance-tuning',
    'hyperparameter-optimization-machine-learning',
    'reinforcement-learning-cartpole'
]

for proj in projects:
    proj_dir = workspace_dir / proj
    if not proj_dir.exists(): continue
    
    print(f"\n--- {proj} ---")
    notebooks = list(proj_dir.rglob('*.ipynb'))
    datasets = set()
    internal = set()
    
    for nb_path in notebooks:
        if '.ipynb_checkpoints' in str(nb_path): continue
        try:
            with open(nb_path, 'r', encoding='utf-8') as f:
                nb = nbformat.read(f, as_version=4)
            for cell in nb.cells:
                if cell.cell_type == 'code':
                    source = cell.source
                    # find external files
                    matches = re.findall(r"read_csv\([^\)]*(?:\'|\")([^\'\"]+\.csv)(?:\'|\")", source)
                    for m in matches: datasets.add(m)
                    matches = re.findall(r"read_excel\([^\)]*(?:\'|\")([^\'\"]+\.xlsx)(?:\'|\")", source)
                    for m in matches: datasets.add(m)
                    matches = re.findall(r"DATA_DIR / (?:\'|\")([^\'\"]+\.csv)(?:\'|\")", source)
                    for m in matches: datasets.add(m)
                    
                    # find internal datasets
                    if 'make_classification' in source: internal.add('make_classification')
                    if 'make_regression' in source: internal.add('make_regression')
                    if 'make_blobs' in source: internal.add('make_blobs')
                    if 'make_moons' in source: internal.add('make_moons')
                    if 'load_wine' in source: internal.add('load_wine')
                    if 'load_iris' in source: internal.add('load_iris')
                    if 'load_breast_cancer' in source: internal.add('load_breast_cancer')
                    if 'load_diabetes' in source: internal.add('load_diabetes')
                    if 'fetch_california_housing' in source: internal.add('fetch_california_housing')
                    if 'keras.datasets' in source: internal.add('keras.datasets')
                    if 'gym.make' in source: internal.add('gymnasium / cartpole')
                    if 'wget' in source or 'urlretrieve' in source: internal.add('downloads from web automatically')
                    if 'pd.DataFrame({' in source: internal.add('hardcoded dataframe')
        except Exception as e:
            pass
    if datasets:
        print("  Needs external files:", datasets)
    if internal:
        print("  Uses internal generators/datasets:", internal)
    if not datasets and not internal:
        print("  Could not automatically detect data source. Need manual check.")
