
from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT='-e .'

__version__="0.0.1"
PKG_NAME = "TestHist"
REPO_NAME = "mlops-hist_test_repo"
AUTHOR_USER_NAME = "itzaijaz"
AUTHOR_EMAIL = "a@a.com"
pkg_desc = "Python package for displayiong test Histogram"
url = f"github.com/{AUTHOR_USER_NAME}/{REPO_NAME}"
project_urls = {
    "Bug Tracker" : f"github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"
}
package_dir={"":"src"}

with open("README.md", 'r', encoding='utf-8') as f:
    long_description=f.read()


setup(
    name=PKG_NAME,
    version='0.0.1',
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description=pkg_desc,
    long_description=long_description,
    long_description_content="text/markdown",
    url=url,
    project_urls=project_urls,
    package_dir=package_dir,
    packages=find_packages(where="src"),
)