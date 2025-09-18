from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="ccom",
    version="0.2.0",
    author="debashishroy00",
    author_email="debashishroy00@example.com",
    description="CCOM v0.2 - Claude Code Orchestrator and Memory system with management features",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/debashishroy00/ccom",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.7",
    install_requires=[],
    entry_points={
        "console_scripts": [
            "ccom=cco.cli:main",
        ],
    },
    include_package_data=True,
    package_data={
        "cco": ["templates/*"],
    },
)