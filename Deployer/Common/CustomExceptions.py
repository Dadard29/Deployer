from http import HTTPStatus


class ServiceStartException(Exception):
    def __init__(self, return_code, msg="Failed to start the service", status_code=HTTPStatus.INTERNAL_SERVER_ERROR):
        self.return_code = return_code
        self.msg = msg
        self.status_code = status_code


class RepositoryException(Exception):
    def __init__(self, return_code, repository, msg="Failed to fetch the repository", status_code=HTTPStatus.INTERNAL_SERVER_ERROR):
        self.msg = "{}: {}".format(msg, repository)
        self.return_code = return_code
        self.status_code = status_code


class DalException(Exception):
    def __init__(self, msg, status_code=HTTPStatus.INTERNAL_SERVER_ERROR):
        self.msg = msg
        self.status_code = int(status_code)


class BusinessException(Exception):

    def __init__(self, msg, status_code=HTTPStatus.INTERNAL_SERVER_ERROR):
        self.msg = msg
        self.status_code = int(status_code)
