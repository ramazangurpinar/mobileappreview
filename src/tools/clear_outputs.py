import os
import nbformat
from nbconvert.preprocessors import ClearOutputPreprocessor

def clear_notebook_outputs(path):
    print(f"Clearing outputs in: {path}")
    with open(path, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)

    ClearOutputPreprocessor().preprocess(nb, {})

    with open(path, 'w', encoding='utf-8') as f:
        nbformat.write(nb, f)

if __name__ == "__main__":
    NOTEBOOKS_DIR = "notebooks"

    for filename in os.listdir(NOTEBOOKS_DIR):
        if filename.endswith(".ipynb"):
            full_path = os.path.join(NOTEBOOKS_DIR, filename)
            clear_notebook_outputs(full_path)
            print(f"Cleared outputs for {filename}")