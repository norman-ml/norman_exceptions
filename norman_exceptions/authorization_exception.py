from norman_exceptions.norman_exception import NormanException


class AuthorizationException(NormanException):
    http_code: int = 403
    grpc_code: int = 7
    error_type: str = "authorization"

    def __init__(
            self,
            message: str,
            cause: str,
            suggestions: list[str]
    ):

        super().__init__(
            http_code=self.http_code,
            grpc_code=self.grpc_code,
            error_type=self.error_type,
            message=message,
            cause=cause,
            suggestions=suggestions
        )