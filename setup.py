from setuptools import setup

with open('requirements.txt') as fp:
    install_requires = fp.read()

setup(
    name='file_api_bundle',
    packages=['file_api_bundle'],
    version='1.0',
    description='Applauncher integration with the client of the Bmat TV/AV file api',
    author='BMAT developers',
    author_email='tv-av@bmat.com',
    url='https://github.com/bmat/file_api_bundle',
    download_url='https://github.com/bmat/file_api_bundle/archive/master.zip',
    keywords=['bmat', 'file', 'api', 'applauncher'],
    classifiers=['Topic :: Adaptive Technologies', 'Topic :: Software Development', 'Topic :: System',
                 'Topic :: Utilities'],
    install_requires=install_requires
)
