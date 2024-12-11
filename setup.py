from setuptools import setup, find_packages

with open("prompt_assistant/__init__.py", "r") as f:
    vervar = f.read().split("__version__ = ")[1].split("\n")[0]

setup(
    name='prompt_assistant',
    version=vervar,
    packages=find_packages(),
    install_requires=[
        'pydantic==2.10.3',
    ],
)
