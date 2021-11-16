import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cache-simulator-jnbrq",
    version="0.0.1",
    author="Canberk Sönmez",
    author_email="canberk.sonmez.409@gmail.com",
    description="Package for simulating simple cache structures.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jnbrq/cache_simulator",
    project_urls={
        "Bug Tracker": "https://github.com/jnbrq/cache_simulator/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    include_package_data=True,
    python_requires=">=3.6",
    package_data={  },
    install_requires=[ ],
    license="MIT"
)
