import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "previsor"

list_of_files = [
    # GitHub Actions
    ".github/workflows/.gitkeep",
    ".github/workflows/scraping.yml",
    ".github/workflows/training.yml",
    
    # Source - Core
    f"src/{project_name}/__init__.py",
    
    # Source - Components
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/components/data_validation.py",
    f"src/{project_name}/components/data_transformation.py",
    f"src/{project_name}/components/model_trainer.py",
    f"src/{project_name}/components/model_evaluation.py",
    
    # Source - Web Scraping
    f"src/{project_name}/scraping/__init__.py",
    f"src/{project_name}/scraping/base_scraper.py",
    f"src/{project_name}/scraping/chavesnamao_scraper.py",
    f"src/{project_name}/scraping/infoimoveis_scraper.py",
    f"src/{project_name}/scraping/utils.py",
    
    # Source - Utils
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/utils/logger.py",
    
    # Source - Config
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    
    # Source - Pipeline
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/pipeline/stage_01_data_ingestion.py",
    f"src/{project_name}/pipeline/stage_02_data_validation.py",
    f"src/{project_name}/pipeline/stage_03_data_transformation.py",
    f"src/{project_name}/pipeline/stage_04_model_trainer.py",
    f"src/{project_name}/pipeline/stage_05_model_evaluation.py",
    f"src/{project_name}/pipeline/predict.py",
    
    # Source - Entity
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    
    # Source - Constants
    f"src/{project_name}/constants/__init__.py",
    
    # Config files
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    
    # Data directories
    "data/raw/.gitkeep",
    "data/processed/.gitkeep",
    "data/external/.gitkeep",
    
    # Models directory
    "models/.gitkeep",
    
    # Artifacts directory
    "artifacts/.gitkeep",
    
    # Logs directory
    "logs/.gitkeep",
    
    # Research notebooks
    "research/01_data_collection.ipynb",
    "research/02_eda.ipynb",
    "research/03_feature_engineering.ipynb",
    "research/04_model_experiments.ipynb",
    
    # Streamlit app
    "app.py",
    
    # Tests
    "tests/__init__.py",
    "tests/test_scraping.py",
    "tests/test_components.py",
    "tests/test_pipeline.py",
    
    # Root files
    "main.py",
    "setup.py",
    "Dockerfile",
    ".env.example",
    ".dvcignore",
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory {filedir} for the file: {filename}")
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} is already exists")