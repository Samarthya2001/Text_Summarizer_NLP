import setuptools

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

__version__ = '0.0.0'

REPO_NAME = 'Text_Summarizer_NLP'
AUTHOR_USER_NAME = 'Samarthya2001'
SRC_REPO = 'Text Summarizer'
AUTHOR_EMAIL = 'sammygoyal2002@gmail.com'

setuptools.setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description='Text Summarizer Application package for NLP',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url=f'https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}',
    project_urls = {
        "Bug Tracker" : f'https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues'
    },
    package_dir = {'': 'src'},
    packages=setuptools.find_packages(where='src')
)