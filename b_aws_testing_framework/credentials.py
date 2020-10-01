import os
from dataclasses import dataclass
from typing import Optional, Dict

import boto3
from boto3 import Session


@dataclass
class Credentials:
    aws_access_key_id: Optional[str] = os.environ.get('AWS_ACCESS_KEY_ID')
    aws_secret_access_key: Optional[str] = os.environ.get('AWS_SECRET_ACCESS_KEY')
    profile_name: Optional[str] = os.environ.get('AWS_PROFILE')
    region_name: Optional[str] = os.environ.get('AWS_DEFAULT_REGION')

    @property
    def boto_session(self) -> Session:
        return boto3.session.Session(
            aws_access_key_id=self.aws_access_key_id,
            aws_secret_access_key=self.aws_secret_access_key,
            profile_name=self.profile_name,
            region_name=self.region_name
        )

    @property
    def environ(self) -> Optional[Dict[str, str]]:
        return {key: value for key, value in {
            'AWS_ACCESS_KEY_ID': self.aws_access_key_id,
            'AWS_SECRET_ACCESS_KEY': self.aws_secret_access_key,
            'AWS_PROFILE': self.profile_name,
            'AWS_DEFAULT_REGION': self.region_name
        }.items() if value} or None
