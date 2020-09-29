from typing import Optional


class CredentialsConfig:
    """
    Global configuration class that stores AWS credentials.
    """
    __TESTING_AWS_PROFILE: Optional[str] = None
    __TESTING_AWS_ACCESS_KEY_ID: Optional[str] = None
    __TESTING_AWS_SECRET_ACCESS_KEY: Optional[str] = None
    __TESTING_AWS_REGION: Optional[str] = None

    """
    AWS profile.
    """

    @staticmethod
    def set_testing_aws_profile(profile: str) -> None:
        if CredentialsConfig.__TESTING_AWS_ACCESS_KEY_ID or CredentialsConfig.__TESTING_AWS_SECRET_ACCESS_KEY:
            raise ValueError('Access keys already set. You can specify either access keys or a profile.')

        CredentialsConfig.__TESTING_AWS_PROFILE = profile

    @staticmethod
    def get_testing_aws_profile() -> Optional[str]:
        return CredentialsConfig.__TESTING_AWS_PROFILE

    """
    AWS region.
    """

    @staticmethod
    def set_testing_aws_region(region: str) -> None:
        CredentialsConfig.__TESTING_AWS_REGION = region

    @staticmethod
    def get_testing_aws_region() -> Optional[str]:
        return CredentialsConfig.__TESTING_AWS_REGION

    """
    AWS key.
    """

    @staticmethod
    def set_testing_aws_access_key_id(key_id: str) -> None:
        if CredentialsConfig.__TESTING_AWS_PROFILE:
            raise ValueError('Profile already set. You can specify either access keys or a profile.')

        CredentialsConfig.__TESTING_AWS_ACCESS_KEY_ID = key_id

    @staticmethod
    def get_testing_aws_access_key_id() -> Optional[str]:
        return CredentialsConfig.__TESTING_AWS_ACCESS_KEY_ID

    """
    AWS secret key.
    """

    @staticmethod
    def set_testing_aws_secret_access_key(secret_key: str) -> None:
        if CredentialsConfig.__TESTING_AWS_PROFILE:
            raise ValueError('Profile already set. You can specify either access keys or a profile.')

        CredentialsConfig.__TESTING_AWS_SECRET_ACCESS_KEY = secret_key

    @staticmethod
    def get_testing_aws_secret_access_key() -> Optional[str]:
        return CredentialsConfig.__TESTING_AWS_SECRET_ACCESS_KEY
