from datetime import datetime, timezone
from typing import Optional


class NormanException(Exception):
    _norman_exception = True

    def __init__(
        self,
        http_code: int,
        grpc_code: int,
        error_type: str,
        message: str,
        cause: str,
        suggestions: list[str]
    ):
        super().__init__(message)
        self.timestamp = datetime.now(timezone.utc)
        self.http_code = http_code
        self.grpc_code = grpc_code
        self.error_type = error_type
        self.message = message
        self.cause = cause
        self.suggestions = suggestions

    def to_dict(self):
        return {
            "timestamp": self.timestamp.isoformat(),
            "http_code": self.http_code,
            "grpc_code": self.grpc_code,
            "error_type": self.error_type,
            "message": self.message,
            "cause": self.cause,
            "suggestions": self.suggestions
        }

    @staticmethod
    def cast(e: Exception, message: Optional[str] = None):
        try:
            if isinstance(e, NormanException):
                return e

            exception_dict = False
            if e.args is not None and len(e.args) > 0:
                exception_dict = e.args[0]

            if isinstance(exception_dict, dict):
                exception = NormanException(
                    http_code=exception_dict["http_code"],
                    grpc_code=exception_dict["grpc_code"],
                    error_type=exception_dict["error_type"],
                    message=exception_dict["message"],
                    cause=exception_dict["cause"],
                    suggestions=exception_dict["suggestions"]
                )
                return exception

            cause = str(e)
            if message is None:
                message = "Norman encountered an error"

            exception = NormanException(
                http_code=500,
                grpc_code=13,
                error_type="Server",
                message=message,
                cause=cause,
                suggestions=[
                    "Try again in a few moments",
                    "Contact support if the problem persists",
                    "Check the service status page"
                ]
            )
            return exception
        except Exception as e:
            cause = str(e)
            exception = NormanException(
                http_code=500,
                grpc_code=13,
                error_type="Configuration",
                message="Failed to create an exception due to malformed configuration",
                cause=cause,
                suggestions=[
                    "Check that your configuration is correct.",
                    "Verify that your configuration has no missing fields."
                ]
            )
            return exception
