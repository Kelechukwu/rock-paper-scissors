from rest_framework.exceptions import APIException

class Conflict(APIException):
    status_code = 409
    default_detail = "Conflict with the request data."
    default_code = "conflict"

