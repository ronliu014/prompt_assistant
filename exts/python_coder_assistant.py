from pydantic import ValidationError
from typing import Optional, Dict, Any
from core import PromptAssistant, PromptTemplateModel

# Example PyCoderAssistant for extensions
class PyCoderAssistant(PromptAssistant):
    """
    A specialized assistant for Python software coder, inheriting from PromptAssistant.
    """
    
    def __init__(self):
        """
        Initialize PyCoderAssistant with internal constants.
        """
        super().__init__()
        self.ROLE = "You are an experienced Python software development expert, familiar with various Python frameworks and best practices."

    def create_prompt(
        self,
        task: str,
        context: Optional[str] = None,
        input_data: Optional[Dict[str, Any]] = None,
        output: Optional[Dict[str, Any]] = None,
        constraints: Optional[Dict[str, Any]] = None,
        style: Optional[Dict[str, Any]] = None
    ) -> PromptTemplateModel:
        """
        Create a Python software expert prompt template and validate it using Pydantic.

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
                task=task if task else "Write a Python function to solve the following problem:",
                role=self.ROLE,  # Set the internal role field
                context=context if context else "Implement a Quick Sort algorithm that takes a list of integers and returns the sorted list.",
                input=input_data if input_data else {"type": "text", "data": [""]},
                output=output if output else {
                    "type": "code", 
                    "format": "python", 
                    "constraints": {
                        "type_specific": [
                            "Output only the code and don't output anything other than the code"
                        ]
                    },
                    "examples": [
                        "def quick_sort(arr):\n    if len(arr) <= 1:\n        return arr\n    pivot = arr[len(arr) // 2]\n    left = [x for x in arr if x < pivot]\n    middle = [x for x in arr if x == pivot]\n    right = [x for x in arr if x > pivot]\n    return quick_sort(left) + middle + quick_sort(right)"
                    ]
                },
                constraints=constraints if constraints else {
                    "rules": [
                        "Follow PEP 8 coding standards", 
                        "Time complexity should be O(n log n)"
                    ], 
                    "time_limit": None, 
                    "length_limit": None
                },
                style=style if style else {"tone": "professional", "language": "Chinese"}
            )
            self.templates.append(template)
            return template
        except ValidationError as e:
            raise ValueError(f"Error creating prompt: {e}")