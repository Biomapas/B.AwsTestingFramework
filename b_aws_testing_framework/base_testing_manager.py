import random
import string
import tempfile
import os.path
import os
from abc import ABC, abstractmethod
from typing import Optional

from b_aws_testing_framework.credentials import Credentials


class BaseTestingManager(ABC):
    """
    Abstract class for testing managers.
    """
    __GLOBAL_PREFIX_PATH: str = f'{tempfile.gettempdir()}/B_AWS_TESTING_FRAMEWORK_GLOBAL_PREFIX.txt'

    def __init__(self, credentials: Credentials) -> None:
        """
        Constructor.
        """
        self.__credentials = credentials

    @property
    def credentials(self) -> Credentials:
        """
        Property for credentials attribute.

        :return: Credentials.
        """
        return self.__credentials

    @staticmethod
    def set_global_prefix(prefix: Optional[str] = None, override: bool = True) -> None:
        """
        Sets a global prefix to be used to name resources.

        :param prefix: An optional prefix. If the value is not given, a random string is generated.
        :param override: Specify whether the prefix should be overridden if its already set.

        :return: No return.
        """
        if (override is False) and (BaseTestingManager.is_global_prefix_set() is True):
            return

        prefix = prefix or ''.join(random.choice(
            string.ascii_lowercase + string.ascii_uppercase,
        ) for _ in range(5))

        with open(BaseTestingManager.__GLOBAL_PREFIX_PATH, 'w') as file:
            file.write(prefix)

    @staticmethod
    def get_global_prefix() -> str:
        """
        Gets a global prefix that is used to name resources.

        :return: Global prefix.
        """
        if not BaseTestingManager.is_global_prefix_set():
            raise ValueError('Global prefix is not set!')

        with open(BaseTestingManager.__GLOBAL_PREFIX_PATH) as file:
            prefix = str(file.read())

        if not prefix:
            raise ValueError('Prefix is empty!')

        return prefix

    @staticmethod
    def delete_global_prefix() -> None:
        """
        Deletes a global prefix.

        :return: No return.
        """
        try:
            os.remove(BaseTestingManager.__GLOBAL_PREFIX_PATH)
        except FileNotFoundError:
            pass

    @staticmethod
    def is_global_prefix_set() -> bool:
        """
        Checks whether global prefix is set.

        :return: True if is set, false otherwise.
        """
        return os.path.isfile(BaseTestingManager.__GLOBAL_PREFIX_PATH)

    @abstractmethod
    def prepare_infrastructure(self) -> None:
        """
        Function to create and prepare infrastructure for testing.

        :return: No return.
        """
        pass

    @abstractmethod
    def destroy_infrastructure(self) -> None:
        """
        Function to destroy the infrastructure.

        :return: No return.
        """
        pass
