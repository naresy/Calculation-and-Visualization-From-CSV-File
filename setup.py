from setuptools import setup, find_packages

setup(
    name="FormulaMonk_assessment",
    version="0.1.0",
    author="Naresh Upadhyay",
    author_email="info.naresh74@gmail.com",
    description="A package for analyzing apple time series data",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/naresy/Formula_Monk_Assessment.git",
    license="MIT",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "pandas",
        "plotly"
    ],
)
