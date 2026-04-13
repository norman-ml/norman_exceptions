from norman_exceptions.norman_exception import NormanException


class RateLimitException(NormanException):
    http_code: int = 429
    grpc_code: int = 8
    error_type: str = "rate_limit"

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