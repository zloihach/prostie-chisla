from setuptools import setup, Extension

prime_lib_module = Extension(
    'prime_lib',
    sources=['./server/prime_lib.c']
)

setup(
    name='prime_lib',
    version='1.0',
    description='C extension module for prime number operations',
    ext_modules=[prime_lib_module],
)
