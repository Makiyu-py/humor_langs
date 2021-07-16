import humor_langs
from setuptools import setup


with open("README.md", "r", encoding="UTF-8") as f:
    long_desc = f.read()


setup(
    name="humor_langs",
    description="Translate your string to humorous text!",
    long_description=long_desc,
    long_description_content_type="text/markdown",
    version=humor_langs.__version__,
    python_requires='>=3.6.0',
    packages=["humor_langs"],
    author="Makiyu",
    author_email="73825066+Makiyu-py@users.noreply.github.com",
    url="https://github.com/Makiyu-py/humor_langs",
    license="MIT",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Games/Entertainment",
    ],
    keywords="Humor owo translate copypasta emojis",
)
