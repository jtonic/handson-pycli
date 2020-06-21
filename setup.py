from setuptools import setup, find_packages
setup(
    name='pycli',
    version='0.1.1',
    description='Py cli project',
    author='Antonel-Ernest Pazargic',
    author_email='antonel.pazargic@gmail.com',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    python_requires='>=3.6, <4',
    install_requires=['click', 'pyyaml'],
    setup_requires=['pytest-runner'],
    extras_require=dict(tests=['pytest']),
    package_data={
        '': ['*.yaml']
    },
    entry_points={  # Optional
      'console_scripts': [
        'pycli=pycli:main',
      ],
    }
)
