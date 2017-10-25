from distutils.core import setup

setup(
    name = 'git-webhook',
    packages = [
        'app'
    ],
    version = '0.1',
    install_requires=[
            'Flask',
            'gunicorn'
        ]
)