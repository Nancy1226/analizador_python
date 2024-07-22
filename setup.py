from setuptools import setup, find_packages

setup(
    name='AppFlask',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'Flask==3.0.3',
        'blinker==1.8.2',
        'click==8.1.7',
        'Flask-Cors==4.0.1',
        'itsdangerous==2.2.0',
        'Jinja==23.1.4',
        'MarkupSafe==2.1.5',
        'pip==24.1.2',
        'ply==3.11',
        'Werkzeug==3.0.3',
        'build==1.2.1',
    ],
)
