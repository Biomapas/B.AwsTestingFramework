import os
from typing import Optional, Dict

import boto3
from boto3 import Session


class Credentials:
    """
    Credentials dataclass for storing AWS credentials.
    """

    def __init__(
            self,
            aws_access_key_id: Optional[str] = os.environ.get('AWS_ACCESS_KEY_ID'),
            aws_secret_access_key: Optional[str] = os.environ.get('AWS_SECRET_ACCESS_KEY'),
            profile_name: Optional[str] = os.environ.get('AWS_PROFILE'),
            region_name: Optional[str] = os.environ.get('AWS_DEFAULT_REGION'),
    ) -> None:
        self.aws_access_key_id = aws_access_key_id
        self.aws_secret_access_key = aws_secret_access_key
        self.profile_name = profile_name
        self.region_name = region_name

    @property
    def boto_session(self) -> Session:
        """
        Property for boto session.

        :return: Boto session instance.
        """
        return boto3.session.Session(
            aws_access_key_id=self.aws_access_key_id,
            aws_secret_access_key=self.aws_secret_access_key,
            profile_name=self.profile_name,
            region_name=self.region_name
        )

    @property
    def environ(self) -> Optional[Dict[str, str]]:
        """
        Property for serialized credentials to dict.

        :return: Credentials in a form of a dict.
        """
        return {key: value for key, value in {
            'AWS_ACCESS_KEY_ID': self.aws_access_key_id,
            'AWS_SECRET_ACCESS_KEY': self.aws_secret_access_key,
            'AWS_PROFILE': self.profile_name,
            'AWS_DEFAULT_REGION': self.region_name
        }.items() if value} or None
