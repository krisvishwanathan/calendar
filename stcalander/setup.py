from setuptools import find_packages, setup

setup(
    name='stcalander',
    version='1.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "django>=4.0",
        "python-dotenv==1.0.0",
        "whitenoise==6.5.0",
        "gunicorn==21.2.0",
        "django-debug-toolbar==4.2.0",
        "psycopg2",
        "wheel==0.43.0",
    ],
    license='MIT',
    description='A calendar app meant to be reused as a module.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/krisvishwanathan/calendar.git',  # Replaced with calendar GitHub URL
    author='iCloudNow',
    author_email='kris@icloudnow.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 3.0',
        'Framework :: Django :: 3.1',
        'Framework :: Django :: 3.2',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
