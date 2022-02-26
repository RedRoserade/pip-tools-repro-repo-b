from setuptools import setup, find_packages

setup(
    name="repo_b",
    version="0.0.1",
    # install_requires=["pymongo", "repo_c"],
    install_requires=["pymongo"],
    packages=find_packages("."),
)
