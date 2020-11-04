import logging
import time
from typing import Optional

from botocore.exceptions import ClientError

from b_aws_testing_framework.credentials import Credentials

logger = logging.getLogger(__name__)


class StackWaiter:
    """
    Waiter class that waits for a cloud formation stack to stabilize.
    """

    def __init__(self, stack_name: str):
        self.__stack_name = stack_name
        self.__client = Credentials().boto_session.client('cloudformation')

    def wait(self, current_iteration: int = 0, max_iterations: int = 100, sleep_time: int = 5) -> None:
        """
        Waits for a given stack to stabilize. E.g. waits when CREATE_IN_PROGRESS turns into CREATE_COMPLETE.

        :param current_iteration: This is a recursive function. This parameter indicates current iteration.
        :param max_iterations: Specifies maximum amount of iterations allowed.
        :param sleep_time: Specifies how long to sleep between iterations.

        :return: No return.
        """
        if current_iteration == max_iterations:
            raise RecursionError()

        stack_status = self.__get_stack_status() or ''
        logger.info(f'Stack status: {stack_status}.')

        if '_IN_PROGRESS' in stack_status:
            time.sleep(sleep_time)
            self.wait(current_iteration + 1, max_iterations, sleep_time)

    def __get_stack_status(self) -> Optional[str]:
        """
        Gets given stack status e.g. CREATE_IN_PROGRESS.

        :return: Stack status.
        """
        try:
            stack = self.__client.describe_stacks(StackName=self.__stack_name)['Stacks'][0]
            return stack['StackStatus']
        except ClientError as ex:
            # Retrieve code and message from an error.
            code = ex.response['Error']['Code']
            message = ex.response['Error']['Message']

            # If stack does not exist, its fine, just return None.
            if code == 'ValidationError' and 'does not exist' in message.lower():
                return

            # Otherwise throw an exception.
            raise
