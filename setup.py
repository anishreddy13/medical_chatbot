from setuptools import find_packages, setup

setup(
    name='Generative AI Project',  # Added a comma here
    version='0.0.0',               # Added a comma here
    author='anish reddy',          # Added a comma here
    author_email='anishreddy1373@gmail.com',  # Added a comma here
    packages=find_packages(),      # Added a comma here
    install_requires=[]            # No comma needed here since it's the last argument
)