from setuptools import setup

setup(
    name='libpardus',
    version='0.0.1',    
    description='Pardus Library for Pardus Applications and Utilities',
    url='https://github.com/pardus/libpardus',
    author='Osman Coskun',
    author_email='osman.coskun@pardus.org.tr',
    license='GPLv3',
    packages=['libpardus','libpardus.Ptk'],
    package_dir={'libpardus':'libpardus'},
    install_requires=[],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: X11 Applications :: GTK',
        'Environment :: X11 Applications :: Gnome',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: Turkish',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.11',
        'Topic :: Desktop Environment :: Gnome'    
    ],
)