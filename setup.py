from setuptools import setup,find_packages
from distutils_commands import command,publish_github,publish_pypi,clean,pytest,wheel,source
from os.path import join

@command
def publish():
    test()
    source()
    wheel()
    publish_github()
    publish_pypi()
    clean()

@command
def test():
    pytest(join('tests','tests.py'))

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
    name='linux-commands',
    version='0.1',
    description='Reimplementation of the subprocess module',
    license="GPL-3",
    long_description=long_description,
    author='Riccardo Isola',
    author_email='riky.isola@gmail.com',
    url="https://github.com/RikyIsola/python-linux-commands",
    packages=find_packages(),
    cmdclass={'publish':publish,'test':test,'clean':clean},
    classifiers=['Development Status :: 4 - Beta',
                 'Intended Audience :: Developers',
                 'Topic :: Software Development :: Libraries',
                 'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
                 'Programming Language :: Python :: 3.9'],
    keywords='shell sh subprocess',
    python_requires='>=3.9',
    project_urls={'Tracker':'https://github.com/RikyIsola/python-linux-commands/issues'}
)
