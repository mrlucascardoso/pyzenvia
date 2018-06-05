from distutils.core import setup
setup(
    name='PyZenvia',
    packages=['pyzenvia'], # this must be the same as the name above
    version='0.4',
    description='package for send sms by Zenvia API',
    author='Lucas Cardoso',
    author_email='mr.lucascardoso@gmail.com',
    url='https://github.com/mrlucascardoso/pyzenvia',
    keywords=['sms', 'zenvia'], # arbitrary keywords
    classifiers=[],
    install_requires=[
        'python-decouple',
        'requests',
    ]
)
