from setuptools import setup, find_packages,SetuptoolsDeprecationWarning

from typing import List
HYPHEN_E = '-e .'

def get_requires(file_path: str) -> List[str]:
    """Read the requirements from a file and return as a list."""
    with open(file_path, 'r') as file:
        requirements = file.readlines()
        if HYPHEN_E in requirements:
            requirements.remove(HYPHEN_E)
    return [req.strip() for req in requirements if req.strip() and not req.startswith('#')]

setup(
    name="ML_PROJECT",
    version="0.1.0",
    author="Vivek Kumar adile",
    author_email="vivekadile700@gmail.com",
    packages=find_packages(),
    install_requires=[get_requires('requirements.txt')],
)