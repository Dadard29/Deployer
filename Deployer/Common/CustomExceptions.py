from http import HTTPStatus


class ServiceStartException(Exception):
    def __init__(self, return_code, msg="Failed to start the service", status_code=HTTPStatus.INTERNAL_SERVER_ERROR):
        self.return_code = return_code
        self.msg = msg
        self.status_code = status_code


class BuildException(Exception):
    def __init__(self, build_number, msg="Build failed", status_code=HTTPStatus.INTERNAL_SERVER_ERROR):
        self.msg = msg
        self.build_number = build_number
        self.status_code = status_code


class DalException(Exception):
    def __init__(self, msg, status_code=HTTPStatus.INTERNAL_SERVER_ERROR):
        self.msg = msg
        self.status_code = int(status_code)


class BusinessException(Exception):

    def __init__(self, msg, status_code=HTTPStatus.INTERNAL_SERVER_ERROR):
        self.msg = msg
        self.status_code = int(status_code)
