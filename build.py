#   -*- coding: utf-8 -*-
from pybuilder.core import use_plugin, init, Author

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.flake8")
use_plugin("python.coverage")
use_plugin("python.distutils")
use_plugin('python.install_dependencies')

name = "ifiapp"
authors = [Author('IFI', 'ifi@uio.no')]
license = 'MIT'
summary = 'Hello world application.'
url = 'https://github.com/dervism/ifiapp_python'
version = '0.0.1'

default_task = ["clean", 'install_dependencies', 'analyze', 'publish']

@init
def set_properties(project):
    project.set_property('dir_source_unittest_python', 'src/unittest/python/ifiapp')
    project.set_property('dir_source_main_python','src/main/python')
    project.build_depends_on("mockito")
    project.build_depends_on("flake8")
