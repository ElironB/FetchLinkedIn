class LinkedInToolkit(BaseToolkit, ABC):
    name: str = "LinkedIn Toolkit"
    description: str = "LinkedIn Tool kit contains all tools related to LinkedIn"

    def get_tools(self) -> List[BaseTool]:
        return [LinkedInProfileTool()]

    def get_env_keys(self) -> List[str]:
        return ["X-RapidAPI-Key"]