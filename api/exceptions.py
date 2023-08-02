from rest_framework.exceptions import APIException
from rest_framework import status


class NoFileError(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "No file to upload or invalid key - must be 'deals'"


class WrongFileFormatError(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = 'Not a csv file.'
