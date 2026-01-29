from setuptools import setup, find_packages
from typing import List

HYPHEN_E = "-e ."

def get_requires(file_path: str) -> List[str]:
    with open(file_path) as file:
        requirements = []
        for line in file:
            line = line.strip()
            if line and line != HYPHEN_E and not line.startswith("#"):
                requirements.append(line)
        return requirements


setup(
    name="ML_PROJECT",
    version="0.1.0",
    author="Vivek Kumar Adile",
    author_email="vivekadile700@gmail.com",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=get_requires("requirements.txt"),
)
