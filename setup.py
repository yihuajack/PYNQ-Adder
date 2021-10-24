from setuptools import setup, find_packages
from pynq.utils import build_py
import pynq_adder

setup(
   name = "pynq_adder",
   version = pynq_adder.__version__,
   url = 'https://github.com/yihuajack/PYNQ-Adder',
   license = 'All rights reserved.',
   author = "Yihua Liu",
   author_email = "yihuajack@live.cn",
   packages = find_packages(),
   inlcude_package_data=True,
   install_requires=[
       'pynq'
   ],
   setup_requires=[
       'pynq'
   ],
   entry_points={
       'pynq.notebooks': [
           'pynq-adder = pynq_adder.notebooks'
       ]
   },
   cmdclass={'build_py': build_py},
   description = "HLS Adder"
)