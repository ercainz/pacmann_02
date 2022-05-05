import setuptools

with open("readme.md","r") as fh:
    long_description = fh.read()
    
setuptools.setup(
    name = "car-price-prediction",
    version = "0.0.1",
    author = "eric.arinoto",
    author_email = "ercainz@gmail.com",
    description = "Advance data manipulation: Tugas 4",
    long_description = "lAdvance data manipulation: Tugas 4, Nomor 10",
    long_description_content_type = "text/markdown",
    url = "https://github.com/ercainz/pacmann_02",
    packages = setuptools.find_packages(),
    classifiers = ["Programming Language :: Python :: 3"],
    install_requires = [
        "numpy",
        "pandas==1.1.4",
        "scikit-learn==0.24.2",
        "matplotlib",
        "seaborn==0.11.0"
        ],
    python_requires = ">=3.7"
)