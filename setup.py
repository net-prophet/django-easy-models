from setuptools import setup, find_packages
import version

VERSION = version.get_version()

f = open('README.md', 'r')
LONG_DESCRIPTION = f.read()
f.close()


setup(
    name='django-easy-models',
    version=VERSION,
    description='Common model utilties and starter templates for frequent tasks',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author='Leeward Bound',
    author_email='lee@net-prophet.tech',
    url='https://code.netprophet.tech/netp/django-easy-models',
    license='unlicensed',
    packages=find_packages(exclude=['ez_setup', 'tests*']),
    include_package_data=True,
    install_requires = [
        'django',
    ],
)
