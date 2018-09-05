# -*- coding: utf-8 -*-
# @Time    : 2018/3/28 15:50
# @Author  : Abner.F
# @File    : __init__.py
# @Software: PyCharm


from setuptools import setup, find_packages

setup(

    name                   =    "aliyun_api",
    version                =    "1.0",
    author                 =    "Abner",
    license                =    "GPLv3, it owns dfxk",
    description            =    "only for aliyun api",
    platforms              =    "linux or windows",
    packages               =    find_packages(),
    include_package_data   =    True,
    exclude_package_data   =    {
                                  '': ['.gitignore'],
                                  "aliyun_api/logs": ['access.log']
                                },
    install_requires       =    [
                                  "requests>=2.18.4",
                                ]
)