"""Setup up for Code Fellows class-assigned kata."""

from setuptools import setup

setup(
    name="code-katas",
    description="class-assigned code challenges",
    version=0.1,
    author="Rick Valenzuela",
    author_email="rick@rickv.com",
    license="MIT",
    package_dir={'': 'src'},
    py_modules=[''],
    install_requires=['ipython'],
    extras_require={
        "test": ['tox', 'pytest', 'pytest-watch', 'pytest-cov']
    },
    entry_points={},
)
