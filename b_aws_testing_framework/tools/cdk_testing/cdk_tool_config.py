from typing import Optional


class CdkToolConfig:
    """
    Configuration class for aws cdk tool.
    """

    def __init__(
            self,
            cdk_app_path: str,
            destroy_before_preparing: bool = True,
            project_root_path: Optional[str] = None
    ) -> None:
        """
        Constructor.

        :param cdk_app_path: Path to an AWS CDK folder where the CDK app is.
        :param destroy_before_preparing: A flag indicating whether the infrastructure manager should attempt
        to clean (destroy) the infrastructure before creating one. This is useful in cases there are some
        resource leftovers from a previous run.
        :param project_root_path: An absolute path to the root of your whole project. This variable is used
        to add to python path. If you face any import errors - it might be a good idea to set this variable.
        """
        self.__cdk_app_path = cdk_app_path
        self.__destroy_before_preparing = destroy_before_preparing
        self.__project_root_path = project_root_path

    @property
    def cdk_app_path(self):
        return self.__cdk_app_path

    @property
    def destroy_before_preparing(self):
        return self.__destroy_before_preparing

    @property
    def project_root_path(self):
        return self.__project_root_path
