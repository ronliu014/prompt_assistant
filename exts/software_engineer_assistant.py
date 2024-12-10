from pydantic import ValidationError
from typing import Optional, List
from core import PromptAssistant, PromptTemplateModel

# Example SoftwareEngineerAssistant for extensions
class SoftwareEngineerAssistant(PromptAssistant):
    """
    An assistant class customized specifically for Python software engineers, automatically setting roles and related fields.
    """

    def create_prompt(
        self,
        task: str,
        context: Optional[str] = "",
        additional_constraints: Optional[List[str]] = None
    ) -> PromptTemplateModel:
        """
        Create a prompt template for a Python software engineer, allowing the user to provide only the task and optional context and constraints.
        
        :param task: Description of the user's programming task.
        :param context: Optional background information.
        :param additional_constraints: Optional list of additional constraint rules.
        :return: The created and validated prompt template.
        """
        default_role = "You are an experienced Python software engineer, proficient in writing efficient and maintainable Python code, and well-versed in various Python frameworks and libraries."
        default_context = context if context else "Please write a Python code implementation based on the provided task description."
        default_input = {"type": "text", "data": task}
        default_output = {
            "type": "text",
            "format": "code_with_comments",
            "constraints": {"type_specific": ["Clear code comments", "Includes code explanations and usage examples"]},
            "examples": []
        }
        constraints = {
            "rules": [
                "Code should adhere to object-oriented design principles",
                "Code should ensure efficient algorithm implementation",
                "Code should have good readability and maintainability"
            ],
            "time_limit": None,
            "length_limit": None  # Can be adjusted based on task requirements
        }
        if additional_constraints:
            constraints["rules"].extend(additional_constraints)
        default_style = {"tone": "technical", "language": "English"}

        try:
            template = PromptTemplateModel(
                task=task,
                role=default_role,
                context=default_context,
                input=default_input,
                output=default_output,
                constraints=constraints,
                style=default_style
            )
            self.templates.append(template)
            return template
        except ValidationError as e:
            raise ValueError(f"Error creating Python Software Engineer prompt template: {e}")