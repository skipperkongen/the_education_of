from distutils.core import setup, Extension

module1 = Extension('spam',
                    sources = ['spammodule.c'])

setup (name = 'Spam',
       version = '1.0',
       description = 'This is the spam package',
       ext_modules = [module1])
