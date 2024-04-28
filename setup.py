import os
from glob import glob
from setuptools import find_packages, setup

ROOT_PATH = os.path.abspath(os.path.dirname(__file__))
NAME = 'LMS'
VERSION = '0.1'

# 의존 패키지 정리
def get_requirements(env):
    with open("requirements-{}.txt".format(env)) as fp:
        return [x.strip() for x in fp.read().split("\n") if not x.startswith("#")]

install_requires = get_requirements("base")
dev_requires = get_requirements("dev")

# 
with open(os.path.join(ROOT_PATH, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name=NAME,
    version=VERSION,
    author="JooSsi",
    long_description=long_description,
    long_description_content_type="text/markdown",
    package_dir={'':'src'},
    packages=find_packages(where='src'),
    python_requires='>=3.9',
    # zip_safe=False,
    install_requires=install_requires,
    extras_require={"dev": dev_requires},
)