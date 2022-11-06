import setuptools

import auth_cord

with open("README.md", "r") as f:
    LONG_DESCRIPTION = f.read()

with open("requirements.txt", "r") as f:
    REQUIREMENTS = f.read().splitlines()

setuptools.setup(
    name="auth_cord",
    author="cibere",
    author_email="cibere.dev@gmail.com",
    url="https://github.com/cibere/auth_cord.py",
    project_urls={
        "Code": "https://github.com/cibere/auth_cord",
        "Issue tracker": "https://github.com/cibere/auth_cord/issues",
        "Discord/Support Server": "https://discord.gg/2MRrJvP42N",
    },
    version=auth_cord.__version__,
    python_requires=">=3.8",
    install_requires=REQUIREMENTS,
    packages=["auth_cord"],
    description=auth_cord.__description__,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    license="MIT",
)
