from setuptools import find_packages, setup

setup(
    name='django-gulp',
    author='Beau Gunderson',
    author_email='beau@beaugunderson.com',

    url='https://github.com/beaugunderson/django-gulp',

    description='Run your gulp tasks with runserver and collectstatic',
    long_description_markdown_filename='README.md',

    keywords=['django', 'gulp'],

    version='4.0.0',

    license='MIT',

    packages=find_packages(),

    install_requires=[
        'ansicolors>=1.1.8,<2.0',
        'env-tools>=2.2.0,<3.0',
        'futures>=3.1.1,<4.0',
        'psutil>=5.2.2,<6.0',
    ],

    setup_requires=[
        'setuptools-markdown'
    ],

    classifiers=[
        'Environment :: Web Environment',

        'Framework :: Django',

        'Development Status :: 5 - Production/Stable',

        'Intended Audience :: Developers',

        'License :: OSI Approved :: MIT License',

        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: MacOS :: MacOS X',

        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries',
        'Topic :: Utilities',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ])
