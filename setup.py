from setuptools import setup, find_packages

setup(
        name='sweep',
        py_modules='sweep.py',
        packages=find_packages(),
        entry_points={
            'console_scripts': [
                'sweep = sweep:run'
            ],
        },
)
