"""
    Offer Enrollment Service

    A set of API endpoints that allow you to get information about offer enrollment  # noqa: E501

    The version of the OpenAPI document: 1.4
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import osis_offer_enrollment_sdk
from osis_offer_enrollment_sdk.model.enrollment import Enrollment
from osis_offer_enrollment_sdk.model.enrollment_list_all_of import EnrollmentListAllOf
from osis_offer_enrollment_sdk.model.paging import Paging
globals()['Enrollment'] = Enrollment
globals()['EnrollmentListAllOf'] = EnrollmentListAllOf
globals()['Paging'] = Paging
from osis_offer_enrollment_sdk.model.enrollment_list import EnrollmentList


class TestEnrollmentList(unittest.TestCase):
    """EnrollmentList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testEnrollmentList(self):
        """Test EnrollmentList"""
        # FIXME: construct object with mandatory attributes with example values
        # model = EnrollmentList()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
