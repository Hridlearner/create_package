import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="example_package", # Replace with your own username
    version="0.0.5",
    author="hrid",
    author_email="hrid.bis@outlook.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    #url="https://github.com/Hridlearner/create_package",
    url="https://github.com",
    packages=['create_package'],
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

# after changing the code eachtime (it will create the wheel file)
# python setup.py sdist bdist_wheel

#push to the github or your cloud 

# go to your local powershell and run below line (path of the repos)
#pip install git+https://github.com/Hridlearner/create_package