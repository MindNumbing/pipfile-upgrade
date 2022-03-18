import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pipfile-upgrade-mindnumbing",
    version="0.0.1",
    author="MindNumbing",
    author_email="its.all@mindnumbing.work",
    description="Software for upgrading pipfile to latest pypi version",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MindNumbing/pipfile-upgrade",
    project_urls={
        "Bug Tracker": "https://github.com/MindNumbing/pipfile-upgrade/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.7.0",
)
