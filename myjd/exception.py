"""Exceptions of the MyJDownloader API."""

from .const import (
    EXCEPTION_API_COMMAND_NOT_FOUND,
    EXCEPTION_API_INTERFACE_NOT_FOUND,
    EXCEPTION_AUTH_FAILED,
    EXCEPTION_BAD_PARAMETERS,
    EXCEPTION_BAD_REQUEST,
    EXCEPTION_CHALLENGE_FAILED,
    EXCEPTION_EMAIL_FORBIDDEN,
    EXCEPTION_EMAIL_INVALID,
    EXCEPTION_ERROR_EMAIL_NOT_CONFIRMED,
    EXCEPTION_FAILED,
    EXCEPTION_FILE_NOT_FOUND,
    EXCEPTION_INTERNAL_SERVER_ERROR,
    EXCEPTION_MAINTENANCE,
    EXCEPTION_METHOD_FORBIDDEN,
    EXCEPTION_OFFLINE,
    EXCEPTION_OUTDATED,
    EXCEPTION_OVERLOAD,
    EXCEPTION_SESSION,
    EXCEPTION_STORAGE_ALREADY_EXISTS,
    EXCEPTION_STORAGE_INVALID_KEY,
    EXCEPTION_STORAGE_INVALID_STORAGEID,
    EXCEPTION_STORAGE_KEY_NOT_FOUND,
    EXCEPTION_STORAGE_LIMIT_REACHED,
    EXCEPTION_STORAGE_NOT_FOUND,
    EXCEPTION_TOKEN_INVALID,
    EXCEPTION_TOO_MANY_REQUESTS,
    EXCEPTION_UNKNOWN,
)


class MYJDException(BaseException):
    """Base MyJDownloader Exception."""


class MYJDConnectionException(MYJDException):
    """Connection Exception."""


class MYJDDeviceNotFoundException(MYJDException):
    """Device not found Exception."""


class MYJDDecodeException(MYJDException):
    """Decode Exception."""


class MYJDApiException(MYJDException):
    """Base MyJDownloader API Exception."""

    @classmethod
    def get_exception(
        cls,
        exception_source,
        exception_type=EXCEPTION_UNKNOWN,
        *args,
        **kwargs,
    ):
        """Get exception object from MyJDownloader exception type."""
        return EXCEPTION_CLASSES.get(exception_type.upper(), MYJDUnknownException)(
            exception_source,
            *args,
            **kwargs,
        )

    def __init__(self, exception_source, *args, **kwargs):
        """Initialize MyJDownloader API exception."""
        self.source = exception_source.upper()
        super().__init__(*args, **kwargs)


class MYJDApiCommandNotFoundException(MYJDApiException):
    """MyJDownloader command not found API Exception."""


class MYJDApiInterfaceNotFoundException(MYJDApiException):
    """MyJDownloader interface not found API Exception."""


class MYJDAuthFailedException(MYJDApiException):
    """MyJDownloader auth failed API Exception."""


class MYJDBadParametersException(MYJDApiException):
    """MyJDownloader bad parameters API Exception."""


class MYJDBadRequestException(MYJDApiException):
    """MyJDownloader bad request API Exception."""


class MYJDChallengeFailedException(MYJDApiException):
    """MyJDownloader challenge failed API Exception."""


class MYJDEmailForbiddenException(MYJDApiException):
    """MyJDownloader email forbidden API Exception."""


class MYJDEmailInvalidException(MYJDApiException):
    """MyJDownloader email invalid API Exception."""


class MYJDErrorEmailNotConfirmedException(MYJDApiException):
    """MyJDownloader email not confirmed API Exception."""


class MYJDFailedException(MYJDApiException):
    """MyJDownloader failed API Exception."""


class MYJDFileNotFoundException(MYJDApiException):
    """MyJDownloader file not found API Exception."""


class MYJDInternalServerErrorException(MYJDApiException):
    """MyJDownloader internal server error API Exception."""


class MYJDMaintenanceException(MYJDApiException):
    """MyJDownloader maintenance API Exception."""


class MYJDMethodForbiddenException(MYJDApiException):
    """MyJDownloader method forbidden API Exception."""


class MYJDOfflineException(MYJDApiException):
    """MyJDownloader offline API Exception."""


class MYJDOutdatedException(MYJDApiException):
    """MyJDownloader outdated API Exception."""


class MYJDOverloadException(MYJDApiException):
    """MyJDownloader overload API Exception."""


class MYJDSessionException(MYJDApiException):
    """MyJDownloader session API Exception."""


class MYJDStorageAlreadyExistsException(MYJDApiException):
    """MyJDownloader storage already exists API Exception."""


class MYJDStorageInvalidKeyException(MYJDApiException):
    """MyJDownloader storage invalid key API Exception."""


class MYJDStorageInvalidStorageIdException(MYJDApiException):
    """MyJDownloader storage invalid storage id API Exception."""


class MYJDStorageKeyNotFoundException(MYJDApiException):
    """MyJDownloader storage key not found API Exception."""


class MYJDStorageLimitReachedException(MYJDApiException):
    """MyJDownloader storage limit reached API Exception."""


class MYJDStorageNotFoundException(MYJDApiException):
    """MyJDownloader storage not found API Exception."""


class MYJDTokenInvalidException(MYJDApiException):
    """MyJDownloader token invalid API Exception."""


class MYJDTooManyRequestsException(MYJDApiException):
    """MyJDownloader too many request API Exception."""


class MYJDUnknownException(MYJDApiException):
    """MyJDownloader unknown API Exception."""


EXCEPTION_CLASSES = {
    EXCEPTION_API_COMMAND_NOT_FOUND: MYJDApiCommandNotFoundException,
    EXCEPTION_API_INTERFACE_NOT_FOUND: MYJDApiInterfaceNotFoundException,
    EXCEPTION_AUTH_FAILED: MYJDAuthFailedException,
    EXCEPTION_BAD_PARAMETERS: MYJDBadParametersException,
    EXCEPTION_BAD_REQUEST: MYJDBadRequestException,
    EXCEPTION_CHALLENGE_FAILED: MYJDChallengeFailedException,
    EXCEPTION_EMAIL_FORBIDDEN: MYJDEmailForbiddenException,
    EXCEPTION_EMAIL_INVALID: MYJDEmailInvalidException,
    EXCEPTION_ERROR_EMAIL_NOT_CONFIRMED: MYJDErrorEmailNotConfirmedException,
    EXCEPTION_FAILED: MYJDFailedException,
    EXCEPTION_FILE_NOT_FOUND: MYJDFileNotFoundException,
    EXCEPTION_INTERNAL_SERVER_ERROR: MYJDInternalServerErrorException,
    EXCEPTION_MAINTENANCE: MYJDMaintenanceException,
    EXCEPTION_METHOD_FORBIDDEN: MYJDMethodForbiddenException,
    EXCEPTION_OFFLINE: MYJDOfflineException,
    EXCEPTION_OUTDATED: MYJDOutdatedException,
    EXCEPTION_OVERLOAD: MYJDOverloadException,
    EXCEPTION_SESSION: MYJDSessionException,
    EXCEPTION_STORAGE_ALREADY_EXISTS: MYJDStorageAlreadyExistsException,
    EXCEPTION_STORAGE_INVALID_KEY: MYJDStorageInvalidKeyException,
    EXCEPTION_STORAGE_INVALID_STORAGEID: MYJDStorageInvalidStorageIdException,
    EXCEPTION_STORAGE_KEY_NOT_FOUND: MYJDStorageKeyNotFoundException,
    EXCEPTION_STORAGE_LIMIT_REACHED: MYJDStorageLimitReachedException,
    EXCEPTION_STORAGE_NOT_FOUND: MYJDStorageNotFoundException,
    EXCEPTION_TOKEN_INVALID: MYJDTokenInvalidException,
    EXCEPTION_TOO_MANY_REQUESTS: MYJDTooManyRequestsException,
    EXCEPTION_UNKNOWN: MYJDUnknownException,
}
