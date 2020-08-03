from setuptools import setup
from setuptools import find_packages


setup(
    name="resthinker",
    version="1.0.0",
    description="A chat response processor with aiml",
    license="MIT",
    author="Nathan Botelho",
    author_email="nimbotelho@gmail.com",
    url="https://enbot.github.io/chat/",
    packages=find_packages(),
    install_requires=[
        "flask>=0.12.3",
        "aiml==0.8.6"
    ],
    classifiers=[
        "Programming Language :: Python :: 2",
        "License :: GNU General Public License v3.0",
        "Operating System :: OS Independent",
    ],
    scripts=[
        "main.py",
        "server.py",
    ]
)
