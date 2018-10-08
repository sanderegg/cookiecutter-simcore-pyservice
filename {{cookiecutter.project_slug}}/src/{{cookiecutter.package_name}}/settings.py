""" Configuration of {{ cookiecutter.package_name }}

The application can consume settings revealed at different
stages of the development workflow. This submodule gives access
to all of them.

"""
from simcore_servicelib.resources import Resources

from .__version__ import get_version_object

resources = Resources(__name__, config_folder='etc/{{ cookie_cutter.package_name }}')

## Constants: low-level tweals ...
TIMEOUT_IN_SECS = 2


## Settings revealed at build/installation time: only known after some setup or build step is completed
PACKAGE_VERSION = get_version_object()
OPENAPI_SPECS = resources.get_path(resources.RESOURCE_KEY_OPENAPI)


## Settings revealed at runtime: only known when the application starts 
#  - via the config file passed to the cli
