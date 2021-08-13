import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='easytools',
    version='0.0.1',
    author='Evgenia Tkachenko',
    author_email='evgeniatkachenko24@gmail.com',
    description='Testing installation of Package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/evgenia-tkachenko/easytools',
    project_urls = {
        "Bug Tracker": "https://github.com/evgenia-tkachenko/easytools/issues"
    },
    license='MIT',
    packages=['easytools'],
    install_requires=['requests'],
)
