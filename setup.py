from setuptools import setup, find_packages

setup(
    name='JpGeocode',
    version='0.3.1',
    description='Search coordinates from municipalities in Japan',
    url='https://github.com/0x0u/JpGeocode',
    author='m0zu',
    author_email='m0zurillex@gmail.com',
    license='MIT',
    keywords='Python3 japan geocoding',
    packages=find_packages(),
    package_data={'JpGeocode':['data/jp_geocode.json']},
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=['Programming Language :: Python :: 3.6']
)


