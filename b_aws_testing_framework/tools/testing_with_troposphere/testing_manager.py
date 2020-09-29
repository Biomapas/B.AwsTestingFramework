import logging

from biomapas_aws_test.base_testing_manager import BaseTestingManager

logger = logging.getLogger(__name__)


class TestingManager(BaseTestingManager):
    """
    Troposphere testing manager.
    """
    def prepare_infrastructure(self) -> None:
        raise NotImplementedError()

    def destroy_infrastructure(self) -> None:
        raise NotImplementedError()
