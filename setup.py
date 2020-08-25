from setuptools import setup, find_packages
setup(
    name='pycli',
    version='0.1.3',
    description='Py cli project',
    author='Antonel-Ernest Pazargic',
    author_email='antonel.pazargic@gmail.com',
    url='https://github.com/jtonic/handson-pycli',
    license='MIT',
    packages=find_packages(where='src/main'),
    package_dir={'': 'src/main'},
    python_requires='>=3.6, <4',
    install_requires=[
        'click>=7.1.2', 'pyyaml>=5.3.1', 'dataclasses==0.6',
        'Jinja2>=2.11.2'
    ],
    setup_requires=['pytest-runner>=5.2'],
    extras_require=dict(
        dev=[
            'pytest>=6.0.0', "pytest-html>=2.1.1", "pytest-cov>=2.10.1",
            'pylint>=2.6.0', 'pylint-json2html>=0.2.0', 'click-completion==0.5.2'
            ]
    ),
    package_data={
        '': ['*.yaml', '*.html']
    },
    entry_points={  # Optional
      'console_scripts': [
        'pycli=pycli:main',
      ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
