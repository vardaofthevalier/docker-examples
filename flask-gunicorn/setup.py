from distutils.core import setup

setup(
    name = 'flask-gunicorn-app',
    packages = [
        'app'
    ],
    version = '0.1',
    install_requires=[
            'Flask',
            'gunicorn'
        ]
)


