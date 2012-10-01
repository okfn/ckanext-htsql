from setuptools import setup, find_packages

version = '0.1'

setup(
    name='ckanext-htsql',
    version=version,
    description="Enables HTSQL queries in the new datastore.",
    long_description="""\
    """,
    classifiers=[],  # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='ckan, datastore, htsql',
    author='Dominik Moritz',
    author_email='',
    url='',
    license='',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['ckanext', 'ckanext.htsql'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # -*- Extra requirements: -*-
    ],
    entry_points=\
    """
    [ckan.plugins]
    htsql=ckanext.htsql.plugin:DatastoreHTSQLPlugin
    """,
)
