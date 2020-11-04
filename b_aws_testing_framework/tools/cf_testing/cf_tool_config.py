class CfToolConfig:
    """
    Configuration class for cloud formation tool.
    """

    def __init__(self, cf_template_path: str):
        self.__cf_template_path = cf_template_path

    @property
    def cf_template_path(self):
        return self.__cf_template_path
