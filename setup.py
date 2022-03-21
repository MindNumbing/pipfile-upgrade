import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pipfile_upgrade",
    version="0.1.0",
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
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "pipfile_upgrade"},
    packages=setuptools.find_packages(where="pipfile_upgrade"),
    python_requires=">=3.7.0",
)
