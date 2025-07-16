# setup.py
#!/usr/bin/env python3

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="gretl-jobs-analyzer",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="Analyze GRETL Jenkins jobs and generate documentation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/your-org/gretl-jobs-analyzer-python",
    py_modules=["gretl_analyzer"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Documentation",
        "Topic :: System :: Systems Administration",
    ],
    python_requires=">=3.7",
    install_requires=[
        # No external dependencies - uses only Python stdlib
    ],
    extras_require={
        "dev": [
            "coverage>=5.0",
            "black>=21.0",
            "flake8>=3.8",
            "mypy>=0.800",
        ],
    },
    entry_points={
        "console_scripts": [
            "gretl-analyzer=gretl_analyzer:main",
        ],
    },
    keywords="gretl jenkins documentation cron jobs analysis markdown",
    project_urls={
        "Bug Reports": "https://github.com/your-org/gretl-jobs-analyzer-python/issues",
        "Source": "https://github.com/your-org/gretl-jobs-analyzer-python",
        "Documentation": "https://github.com/your-org/gretl-jobs-analyzer-python#readme",
    },
)
