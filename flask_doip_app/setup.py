import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='DoIP-chaitanya',
    version='0.0.1',
    author="Chaitanya Reddy",
    author_email="chaitu.ycr@gmail.com",
    description='Python tool for DoIP(Diagnostics over IP)',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AutomotiveKS/doip_flask_app.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    package_dir={'': 'src'},
    py_modules=["doip_flask_app"],
)