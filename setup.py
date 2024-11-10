from setuptools import setup, find_packages

setup(
    name="math_quiz",
    version="0.1",
    author="Your Name",
    author_email="your.email@example.com",
    description="A math quiz package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Jeshwanthg/dsss_homework_2",
    packages=find_packages(),
    install_requires=open("requirements.txt").read().splitlines(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
