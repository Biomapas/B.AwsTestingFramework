class CdkToolConfig:
    """
    Configuration class for aws cdk tool.
    """

    def __init__(
            self,
            cdk_app_path: str,
            destroy_before_preparing: bool = True
    ) -> None:
        """
        Constructor.

        :param cdk_app_path: Path to an AWS CDK folder where the CDK app is.
        :param destroy_before_preparing: A flag indicating whether the infrastructure manager should attempt
        to clean (destroy) the infrastructure before creating one. This is useful in cases there are some
        resource leftovers from a previous run.
        """
        self.__cdk_app_path = cdk_app_path
        self.__destroy_before_preparing = destroy_before_preparing

    @property
    def cdk_app_path(self):
        return self.__cdk_app_path

    @property
    def destroy_before_preparing(self):
        return self.__destroy_before_preparing
