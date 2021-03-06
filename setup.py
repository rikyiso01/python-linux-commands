from setuptools import setup,find_packages
from distutils_commands import command,publish_github,publish_pypi,clean,pytest,wheel,source,get_cmdclass
from os.path import join

@command('publish')
def publish(changelog:str):
    test()
    source()
    wheel()
    publish_github(changelog)
    publish_pypi()
    clean()

@command('test')
def test():
    pytest(join('tests','tests.py'))

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
    name='linux-commands',
    version='0.3',
    description='Reimplementation of the subprocess module',
    license="GPL-3",
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Riccardo Isola',
    author_email='riky.isola@gmail.com',
    url="https://github.com/RikyIsola/python-linux-commands",
    packages=find_packages(),
    cmdclass=get_cmdclass(),
    classifiers=['Development Status :: 4 - Beta',
                 'Intended Audience :: Developers',
                 'Topic :: Software Development :: Libraries',
                 'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
                 'Programming Language :: Python :: 3.7',
                 'Programming Language :: Python :: 3.8',
                 'Programming Language :: Python :: 3.9'],
    keywords='shell sh subprocess',
    python_requires='>=3.7',
    project_urls={'Tracker':'https://github.com/RikyIsola/python-linux-commands/issues'},
    setup_requires=['distutils-commands[wheel]>=1.5.1','distutils-commands[pytest]>=1.5.1',
                    'distutils-commands[pypi]>=1.5.1','pytest'],
)
