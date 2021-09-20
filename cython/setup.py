from setuptools import setup
from Cython.Build import cythonize


setup(
    name='main',
    ext_modules=cythonize("main.pyx", annotate=True),
    zip_safe=False,
)
