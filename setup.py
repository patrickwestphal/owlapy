try:
    from setuptools import setup
except ImportError:
    from distutils import setup

config = {
    'description': 'An OWL API port to Python',
    'author': 'Patrick Westphal',
    'url': 'https://github.com/patrickwestphal/owlapy',
    'download_url': 'https://github.com/patrickwestphal/owlapy',
    'author_email': 'patrick.westphal@informatik.uni-leipzig.de',
    'version': '0.0.1',
    'tests_require': [
        'nose==1.3.4',
        'coverage>=4.0a5',
    ],
    'install_requires': [
        'enum34==1.0.4',
        'rdflib==4.2.0'
    ],
    'packages': ['owlapy.model'],
    'name': 'owlapy'
}

setup(**config)
