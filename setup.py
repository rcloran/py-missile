"""py-missile, a library for controlling USB missile launchers"""
from setuptools import setup

setup(
    name="py-missile",
    description="Library for controlling USB missile launchers",
    version="0.1",
    author="Russell Cloran",
    url="http://github.com/rcloran/py-missile",
    install_requires=[
        "PyUSB>=1.0a3",
    ],
    py_modules=["missile"],
)
