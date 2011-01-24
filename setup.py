from setuptools import setup, find_packages

setup(
    name = 'djff',
    version = '0.1',
    author = 'Johannes Dollinger',
    author_email = 'emulbreh@googlemail.com',
    description = "A django app to highlighting diffs",
    url = 'http://github.com/emulbreh/djff/',
    packages = find_packages(),
    package_data = {'djff': ['templates/djff/*.html', 'static/*.css'],},
    install_requires = [],
    classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Topic :: Utilities',
        'Topic :: Text Processing :: Filters',
        'Environment :: Web Environment',
        'Framework :: Django',
    ],
)