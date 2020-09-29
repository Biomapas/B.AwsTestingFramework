class CdkToolConfig:
    """
    Configuration class for aws cdk tool.
    """
    def __init__(self, cdk_app_path: str):
        self.__cdk_app_path = cdk_app_path

    @property
    def cdk_app_path(self):
        return self.__cdk_app_path
