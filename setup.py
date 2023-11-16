from setuptools import setup

version_file = 'caxutils/version.py'


def get_version():
    with open(version_file, 'r') as f:
        exec(compile(f.read(), version_file, 'exec'))
    return locals()['__version__']


def get_readme():
    with open('README.md', encoding='utf-8') as f:
        content = f.read()
    return content


if __name__ == '__main__':
    setup(
        name='usfutils',
        version=get_version(),
        author='AoXuan Chen',
        author_email='cax1165@163.com',
        url='https://github.com/chenaoxuan/CaxUtils.git',
        license='Apache License 2.0',
        description='Open Source Universal Tool Library for Python Project',
        long_description=get_readme(),
        long_description_content_type='text/markdown',
        keywords='python,pytorch,utils',
        classifiers=[
            'Development Status :: 4 - Beta',
            'Operating System :: OS Independent',
            'License :: OSI Approved :: Apache Software License',
            'Programming Language :: Python :: 3',
        ]
    )
