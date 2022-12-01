# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from osis_offer_enrollment_sdk.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from osis_offer_enrollment_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from osis_offer_enrollment_sdk.model.enrollment import Enrollment
from osis_offer_enrollment_sdk.model.enrollment_list import EnrollmentList
from osis_offer_enrollment_sdk.model.enrollment_list_all_of import EnrollmentListAllOf
from osis_offer_enrollment_sdk.model.error import Error
from osis_offer_enrollment_sdk.model.inscription import Inscription
from osis_offer_enrollment_sdk.model.mes_inscriptions import MesInscriptions
from osis_offer_enrollment_sdk.model.paging import Paging
