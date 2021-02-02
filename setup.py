import humor_langs
from setuptools import setup


with open("README.md", "r", encoding="UTF-8") as f:
    long_desc = f.read()


setup(
    name='humor_langs',
    description='Translate your string to humorous text!',
    long_description=long_desc,
    long_description_content_type="text/markdown",
    version=humor_langs.__version__,
    packages=['humor_langs'],
    author='Makiyu',
    author_email='dankerdanker11@gmail.com',
    url='https://github.com/Makiyu-py/humor_langs',
    license='MIT',
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Programming Language :: Python :: 3",
    ],
    keywords="Humor owo translate"  # I couldn't think of something I swear
)
