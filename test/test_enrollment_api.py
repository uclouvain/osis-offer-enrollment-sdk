"""
    Offer Enrollment Service

    A set of API endpoints that allow you to get information about offer enrollment  # noqa: E501

    The version of the OpenAPI document: 1.4
    Generated by: https://openapi-generator.tech
"""


import unittest

import osis_offer_enrollment_sdk
from osis_offer_enrollment_sdk.api.enrollment_api import EnrollmentApi  # noqa: E501


class TestEnrollmentApi(unittest.TestCase):
    """EnrollmentApi unit test stubs"""

    def setUp(self):
        self.api = EnrollmentApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_enrollments_list(self):
        """Test case for enrollments_list

        """
        pass

    def test_mes_inscriptions_get(self):
        """Test case for mes_inscriptions_get

        """
        pass

    def test_my_enrollments_list(self):
        """Test case for my_enrollments_list

        """
        pass


if __name__ == '__main__':
    unittest.main()
