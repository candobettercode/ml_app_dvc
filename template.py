import os

# Define the project name
project_dir = os.path.dirname(os.path.abspath(__file__))
# project_dir = os.path.join(base_dir, "basic_ml_app_dvc")

# Define the folder structure
folders = [
    "data",
    "notebooks",
    "logs",
    "src/data",
    "src/models",
    "src/utils",
    "tests",
    "outputs",
    "config"
]

# Define some common files
files = [
    ".gitignore",
    "README.md",
    "requirements.txt",
    "environment.yml",
    "Dockerfile",
    "config/config.yaml",
    "src/__init__.py",
    "src/data/__init__.py",
    "src/data/preprocess.py",
    "src/data/features.py",
    "src/models/__init__.py",
    "src/models/train_model.py",
    "src/models/evaluate_model.py",
    "src/models/save_load.py",
    "src/utils/__init__.py",
    "src/utils/helpers.py",
    "tests/__init__.py"
]

# Create the folders
for folder in folders:
    path = os.path.join(project_dir, folder)
    os.makedirs(path, exist_ok=True)

# Create empty files
for file in files:
    path = os.path.join(project_dir, file)
    if not os.path.exists(path):
        with open(path, "w") as f:
            f.write("")

print(f"Flask ML project structure for '{project_dir}' created successfully! 🚀")
