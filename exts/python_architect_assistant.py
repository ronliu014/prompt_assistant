from pydantic import ValidationError
from typing import Optional, Dict, Any
from core import PromptAssistant, PromptTemplateModel

# Example PyArchitectAssistant for extensions
class PyArchitectAssistant(PromptAssistant):
    """
    A specialized assistant for Python software architects, inheriting from PromptAssistant.
    """
    
    def __init__(self):
        """
        Initialize PyArchitectAssistant with internal constants.
        """
        super().__init__()
        self.ROLE = "You are an experienced Python software architect, proficient in designing efficient and scalable software architectures, and familiar with various architectural patterns and best practices."

    def create_prompt(
        self,
        task: str,
        context: Optional[str] = "",
        input_data: Optional[Dict[str, Any]] = None,
        output: Optional[Dict[str, Any]] = None,
        constraints: Optional[Dict[str, Any]] = None,
        style: Optional[Dict[str, Any]] = None
    ) -> PromptTemplateModel:
        """
        Create a Python software architect prompt template and validate it using Pydantic.

        :param task: The task description provided by the user.
        :param context: Optional background information or context.
        :param input_data: Details of the input, including type and data.
        :param output: Details of the output, including type, format, and examples.
        :param constraints: Constraints such as rules, time limits, and length limits.
        :param style: Style preferences such as tone and language.
        :return: The created and validated prompt template.
        """
        try:
            template = PromptTemplateModel(
                task=task if task else "Design a scalable software architecture for the following problem:",
                role=self.ROLE,  # Set internal role field
                context=context if context else "Develop a microservices-based architecture for a large-scale e-commerce platform.",
                input=input_data if input_data else {"type": "text", "data": ""},
                output=output if output else {"type": "text", "format": "text", "constraints": {}, "examples": []},
                constraints=constraints if constraints else {"rules": ["Ensure architectural scalability and maintainability"], "time_limit": None, "length_limit": None},
                style=style if style else {"tone": "professional", "language": "English"}
            )
            self.templates.append(template)
            return template
        except ValidationError as e:
            raise ValueError(f"Error creating prompt: {e}")