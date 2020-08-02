# import setuptools


# with open("README.md", "r") as fh:
#     long_description = fh.read()

# setuptools.setup(
#     name="example-pkg-YOUR-USERNAME-HERE", # Replace with your own username
#     version="0.0.1",
#     author="Example Author",
#     author_email="author@example.com",
#     description="A small example package",
#     long_description=long_description,
#     long_description_content_type="text/markdown",
#     url="https://github.com/pypa/sampleproject",
#     packages=setuptools.find_packages(),
#     classifiers=[
#         "Programming Language :: Python :: 3",
#         "License :: OSI Approved :: MIT License",
#         "Operating System :: OS Independent",
#     ],
#     python_requires='>=3.6',
# )

# from setuptools import setup

# setup(
#    name='foo',
#    version='1.0',
#    description='A useful module',
#    author='Man Foo',
#    author_email='foomail@foo.com',
#    packages=['foo'],  #same as name
#    install_requires=['bar', 'greek'], #external packages as dependencies
# )

# from setuptools import setup

# setup(
#    name='foo',
#    version='1.0',
#    description='A useful module',
#    author='Man Foo',
#    author_email='foomail@foo.com',
#    packages=['foo'],  #same as name
#    install_requires=['bar', 'greek'], #external packages as dependencies
#    scripts=[
#             'scripts/cool',
#             'scripts/skype',
#            ]
# )

# from setuptools import setup

# with open("README", 'r') as f:
#     long_description = f.read()

# setup(
#    name='foo',
#    version='1.0',
#    description='A useful module',
#    license="MIT",
#    long_description=long_description,
#    author='Man Foo',
#    author_email='foomail@foo.com',
#    url="http://www.foopackage.com/",
#    packages=['foo'],  #same as name
#    install_requires=['bar', 'greek'], #external packages as dependencies
#    scripts=[
#             'scripts/cool',
#             'scripts/skype',
#            ]
# )