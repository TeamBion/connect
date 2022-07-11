import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='connect',
    version='0.1.1',    
    description='An ssm connector of the aws instances',
    url='https://github.com/Teambion/connect',
    author='WoodProgrammer',
    author_email='emirozbir@teambion.com',
    packages=["connect"],
    install_requires=['boto3==1.14.15',
    'simple_term_menu'],
     entry_points ={
            'console_scripts': [
                'connect = connect.main:main'
            ]
        },
)