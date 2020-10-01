from abc import ABC, abstractmethod

from b_aws_testing_framework.credentials import Credentials


class BaseTestingManager(ABC):
    """
    Abstract class for testing managers.
    """
    def __init__(self, credentials: Credentials) -> None:
        """
        Constructor.
        """
        self.credentials = credentials

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
