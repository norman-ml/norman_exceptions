from norman_exceptions.norman_exception import NormanException


class ConfigurationException(NormanException):
    http_code: int = 400
    grpc_code: int = 3
    error_type: str = "configuration"

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