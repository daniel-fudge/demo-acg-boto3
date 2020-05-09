from setuptools import setup

setup(
    name='snapshot-maker',
    version='0.1',
    author='Daniel Fudge',
    author_email='daniel.fudge1977@gmail.com',
    description='A tool for managing AWS EC2 snapshots.',
    licenses='MIT',
    packages=['shotty'],
    url='https://github.com/daniel-fudge/demo-acg-boto3',
    install_requires=['click', 'boto3'],
    entry_points='''
        [console_scripts]
        shotty=shotty.shotty:click
    ''',
)
