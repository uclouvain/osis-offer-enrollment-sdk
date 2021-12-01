"""
    Offer Enrollment Service

    A set of API endpoints that allow you to get information about offer enrollment  # noqa: E501

    The version of the OpenAPI document: 1.2
    Generated by: https://openapi-generator.tech
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "osis-offer-enrollment-sdk"
VERSION = "1.2"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
  "urllib3 >= 1.25.3",
  "python-dateutil",
]

setup(
    name=NAME,
    version=VERSION,
    description="Offer Enrollment Service",
    author="OpenAPI Generator community",
    author_email="team@openapitools.org",
    url="",
    keywords=["OpenAPI", "OpenAPI-Generator", "Offer Enrollment Service"],
    python_requires=">=3.5",
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description="""\
    A set of API endpoints that allow you to get information about offer enrollment  # noqa: E501
    """
)
