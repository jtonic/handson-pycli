from setuptools import setup, find_packages
setup(
    name='pycli',
    version='0.1.2',
    description='Py cli project',
    author='Antonel-Ernest Pazargic',
    author_email='antonel.pazargic@gmail.com',
    url='https://github.com/jtonic/handson-pycli',
    license='MIT',
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
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
