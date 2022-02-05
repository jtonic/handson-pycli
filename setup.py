from setuptools import setup, find_packages

setup(
    name="pycli",
    version="0.9.0",
    description="Py cli project",
    author="Antonel-Ernest Pazargic",
    author_email="antonel.pazargic@gmail.com",
    url="https://github.com/jtonic/handson-pycli",
    license="MIT",
    packages=find_packages(where="src/main"),
    package_dir={"": "src/main"},
    python_requires=">=3.6, <4",
    install_requires=[
        "click==8.0.1",
        "click-completion==0.5.2",
        "pyyaml==5.3.1",
        "Jinja2==2.11.2",
        "pendulum==2.1.2",
        "numpy==1.21.4",
        "pandas==1.3.4",
        "matplotlib==3.4.3",
        "pydantic==1.8.2",
    ],
    setup_requires=["pytest-runner>=5.2"],
    extras_require=dict(
        dev=[
            "pytest==6.2.5",
            "pytest-html==3.1.1",
            "pytest-cov==3.0.0",
            "pylint==2.11.1",
            "pylint-json2html==0.3.0",
            "click-completion==0.5.2",
            "mypy==0.910",
            "pytest-mypy==0.8.1",
            "flake8==4.0.1",
            "ipykernel==6.5.0",
        ]
    ),
    package_data={"": ["*.yaml", "*.html"]},
    entry_points={  # Optional
        "console_scripts": [
            "pycli=pycli.main:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
