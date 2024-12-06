from setuptools import setup, find_packages

setup(
    name='prompt_assistant',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'pydantic==2.10.3',
    ],
)
