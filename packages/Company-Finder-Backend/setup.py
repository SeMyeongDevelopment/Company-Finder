from setuptools import setup, find_packages


setup(
    name='manager',
    version='0.0.1',
    description='Company Finder Backend',
    py_modules='manager',
    author='KimVuu',
    author_email='kimvuulib@gmail.com',
    url='https://github.com/SeMyeongDevelopment/Company-Finder',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Django',
        'djangorestframework',
    ]
)