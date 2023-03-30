from setuptools import setup, find_packages

setup(name = "census income",
      version = "0.0.1",
      author='vinay',
      author_email='vinayreddykappeta@gmail.com',
      packages=find_packages(),
      install_requies = ["pandas","numpy","flask","seaborn","matplotlib"]
      )


