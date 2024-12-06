from typing import List, Dict, Any
from .prompt_assistant import PromptAssistant

# Example CustomAssistant for extensions
class CustomAssistant(PromptAssistant):
    """
    A customizable assistant that extends PromptAssistant.
    """

    def filter_templates_by_task(self, keyword: str) -> List[Dict[str, Any]]:
        """
        Filter templates based on a keyword in the task.

        :param keyword: The keyword to filter by.
        :return: A list of templates that match the keyword.
        """
        return [
            template.dict() for template in self.templates
            if keyword.lower() in template.task.lower()
        ]
