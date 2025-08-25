from setuptools import setup, find_packages
import os

with open(os.path.join(os.path.dirname(__file__), "..", "README.md"), "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='EED',
    version='0.1.0',
    packages=find_packages(),
    description='A Python package for calculating the Expression Edit Distance (EED) for LaTeX expressions.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='PhyBench', # Should be updated in README.md
    author_email='phybench@example.com', # Should be updated in README.md
    url='https://github.com/phybench/phybench-eed',  # Add a URL to your project
    license='MIT',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'sympy',
        'numpy',
        'latex2sympy2-extended',
        'timeout-decorator',
    ],
)