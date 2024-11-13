from setuptools import find_packages, setup


setup(
    name='tasks-cli',
    version='0.1.4',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'tasks-cli=src.__init__:Main.main'
        ]
    }
)
