import setuptools 

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "Cocci-Chicken-Disease"
AUTHOR_USER_NAME = "Renaldo Arapi"
SRC_REPO = "cnnClassifier_chicken_disease"
AUTHOR_EMAIL = "renaldo.arapi@live.it"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="An end-to-end deep learning package for automated classification of chicken diseases using CNNs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    package_dir={
        "": "src"
    },
    packages=setuptools.find_packages(where="src")
)