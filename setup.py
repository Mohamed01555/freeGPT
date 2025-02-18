from setuptools import setup, find_packages

with open("README.md", encoding="utf-8") as f:
    README = f.read()
setup(
    name="freeGPT",
    version="1.2.8",
    description="freeGPT provides free access to text and image generation models.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/Mohamed01555/freeGPT",
    author="Ruu3f",
    license="GPLv3",
    keywords=[
        "natural-language-processing",
        "artificial-intelligence",
        "machine-learning",
        "deep-learning",
        "gpt4free",
        "gpt4all",
        "freegpt",
        "chatgpt",
        "python",
        "llama",
        "llm",
        "nlp",
        "gpt",
        "ai",
    ],
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
    packages=find_packages(exclude=[".github"]),
    install_requires=[
        "requests",
        "aiohttp",
    ],
    project_urls={
        "Source": "https://github.com/Mohamed01555/freeGPT",
    },
)
