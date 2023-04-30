from setuptools import setup, find_packages

setup(name="census-income",
      version= "0.01",
      author="Prabhu",
      author_email="basavaprabhu.uk@gmail.com",
      packages=find_packages(),
      install_requires= ["pandas","numpy","flask"]
     )