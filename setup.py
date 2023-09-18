from setuptools import setup

APP = ['webp.py']
DATA_FILES = []
OPTIONS = {'argv_emulation': True, 'includes': ['pdf2image', 'PIL',
                                                'tkinterdnd2', 'tkinter', 'os', 'sys']}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
