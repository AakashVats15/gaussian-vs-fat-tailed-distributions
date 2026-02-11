import os

folders = [
    "gaussian-vs-fat-tailed-distributions",
    "gaussian-vs-fat-tailed-distributions/notebooks",
    "gaussian-vs-fat-tailed-distributions/src",
    "gaussian-vs-fat-tailed-distributions/images"
]

files = [
    "gaussian-vs-fat-tailed-distributions/README.md",
    "gaussian-vs-fat-tailed-distributions/requirements.txt",
    "gaussian-vs-fat-tailed-distributions/LICENSE",
    "gaussian-vs-fat-tailed-distributions/notebooks/gaussian_vs_fat_tailed.ipynb",
    "gaussian-vs-fat-tailed-distributions/src/distributions.py",
    "gaussian-vs-fat-tailed-distributions/src/simulation.py",
    "gaussian-vs-fat-tailed-distributions/src/plots.py",
    "gaussian-vs-fat-tailed-distributions/images/pdf_comparison.png",
    "gaussian-vs-fat-tailed-distributions/images/tail_zoom.png",
    "gaussian-vs-fat-tailed-distributions/images/random_samples.png"
]

for folder in folders:
    os.makedirs(folder, exist_ok=True)

for file in files:
    open(file, "a").close()

print("Folder structure created successfully.")
