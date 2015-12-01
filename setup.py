from setuptools import setup, find_packages

execfile('nuke/version.py')

setup(
    name='nuke',
    version=__version__,
    url='http://github.com/IGBC/Nuke/',
    license='GNU General Public License v3.0',
    author='Ashley Brown',
    author_email='ashleytwb@gamil.com',
    description='Light Weight Application for Securely Erasing Disks',
    entry_points={'console_scripts': ['nuke = nuke.nuke']},
    packages=['nuke'],
    include_package_data=True,
    #This only works on linux
    platforms=['linux'],
    zip_safe=False,
    install_requires=[],
    package_data={}
)