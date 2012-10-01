from setuptools import setup, find_packages

version = '0.1.1'

setup(
    name='ckanext-htsql',
    version=version,
    description="Enables HTSQL queries in the new datastore in CKAN.",
    long_description="""\
    The new datastore offers a way to store data directly in CKAN.
    This plugin adds an API enpoint 'datastore_search_htsql' that allows htsql
    on the datastore. Because of restrictions with the sql endpoint, not all htsql queries
    are possible.
    """,
    classifiers=[],  # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='ckan, datastore, htsql',
    author='Dominik Moritz',
    author_email='',
    url='',
    license='AGPL',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['ckanext', 'ckanext.htsql'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'htsql'
    ],
    entry_points=\
    """
    [ckan.plugins]
    htsql=ckanext.htsql.plugin:DatastoreHTSQLPlugin
    """,
)
