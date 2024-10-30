from setuptools import setup, find_packages 
 
setup( 
    name='sample-python-web', 
    version='0.1', 
    packages=find_packages(), 
    install_requires=[ 
        'flask', 
        'flask-swagger-ui',
    ], 
    entry_points={ 
        'console_scripts': [ 
            'sample-python-web=src.app:main' 
        ] 
    }, 
) 
