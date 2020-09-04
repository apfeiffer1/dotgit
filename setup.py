import setuptools
from glob import glob
import dotgit.info as info

with open('README.md', 'r') as readme:
    long_description = readme.read()

setuptools.setup(
        name = 'dotgit',
        version = info.__version__,
        author = info.__author__,
        author_email = info.__author_email__,
        description = 'A comprehensive solution to managing your dotfiles',
        long_description = long_description,
        long_description_content_type = 'text/markdown',
        url = info.__url__,
        license = info.__license__,
        packages = ['dotgit', 'dotgit.plugins'],
        entry_points = {
            'console_scripts': ['dotgit=dotgit.__main__:main']
            },
        scripts = ['old/dotgit.sh'],
        data_files = [('completion', glob('pkg/completion/*'))],
        package_data = {'': ['LICENSE']},
        include_package_data = True,
        classifiers = [
            'Development Status :: 2 - Pre-Alpha',
            'Programming Language :: Python :: 3',
            'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
            'Operating System :: POSIX',
            'Operating System :: MacOS',
            ],
        python_requires = '>=3.6',
        )
