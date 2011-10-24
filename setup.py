import os.path
from setuptools import setup, find_packages

version = '0.1'

setup(
    name = 'collective.portletclass',
    version = version,
    description = 'Add custom CSS classes to Plone portlet wrappers for flexible theming.',
    long_description = open("README.txt").read() + "\n\n" +
                     open("CHANGES.txt").read(),
    classifiers = [
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Zope2",
        'Intended Audience :: Developers',
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        ],
    keywords = 'plone',
    author = 'Laurence Rowe',
    author_email = 'lrowe@shuttlethread.com',
    url='https://github.com/shuttlethread/collective.portletclass',
    license = 'GPL version 2',
    packages = find_packages('src'),
    package_dir = {'': 'src'},
    namespace_packages = ['collective'],
    include_package_data = True,
    platforms = 'Any',
    zip_safe = False,
    install_requires = [
        'collective.monkeypatcher',
        'plone.app.portlets',
        'plone.browserlayer',
        'setuptools',
        'z3c.jbot',
        'zope.event',
        'zope.formlib',
        'zope.i18nmessageid',
        'zope.interface',
        'zope.lifecycleevent',
        'zope.schema',
        ],
    extras_require = {
        'test': [
            'plone.app.testing',
            ],
        },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
    )
