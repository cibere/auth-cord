import setuptools

import discord_oauth

with open("README.md", "r") as f:
    LONG_DESCRIPTION = f.read()

with open("requirements.txt", "r") as f:
    REQUIREMENTS = f.read().splitlines()

setuptools.setup(
    name="discord-oauth",
    author="cibere",
    author_email="cibere.dev@gmail.com",
    url="https://github.com/cibere/cibere-dev.py",
    project_urls={
        "Code": "https://github.com/cibere/discord-oauth",
        "Issue tracker": "https://github.com/cibere/discord-oauth/issues",
        "Discord/Support Server": "https://discord.gg/2MRrJvP42N",
    },
    version=discord_oauth.__version__,
    python_requires=">=3.8",
    install_requires=REQUIREMENTS,
    packages=["discord_oauth"],
    description=discord_oauth.__description__,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    license="MIT",
)
