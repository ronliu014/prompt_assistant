from pydantic import ValidationError
from typing import Any, Dict, Optional, List
from core import PromptAssistant, PromptTemplateModel

# Example SoftwareArchitectAssistant for extensions
class SoftwareArchitectAssistant(PromptAssistant):
    """
    An assistant class customized specifically for Software Architects, automatically setting roles and related fields.
    """

    def create_prompt(
        self,
        task: str,
        context: Optional[str] = None,
        additional_input: Optional[List[str]] = None,
        additional_output: Optional[List[str]] = None,
        additional_constraints: Optional[List[str]] = None
    ) -> PromptTemplateModel:
        """
        Create a prompt template for a Software Architect, allowing the user to provide only the task and optional context and constraints.
        
        :param task: Description of the user's software architecture task.
        :param context: Optional background information.
        :param additional_constraints: Optional list of additional constraint rules.
        :return: The created and validated prompt template.
        """
        default_role = "You are an experienced Software Architect with expertise in designing scalable, maintainable, and robust software systems."
        default_context = context if context else "Please design a software architecture based on the provided task description."
        default_input = {"type": "text", "data": [task]}
        if additional_input:
            default_input["data"].extend(additional_input)
        default_output = {
            "type": "text",
            "format": "architecture_plan_with_diagrams",
            "constraints": {"type_specific": ["Clear architecture diagrams", "Detailed explanations", "Inclusion of UML descriptions"]},
            "examples": []
        }
        if additional_output:
            default_input["examples"].extend(additional_output)
        default_constraints = {
            "rules": [
                "Adhere to industry-standard architectural patterns",
                "Ensure scalability and maintainability",
                "Incorporate security best practices"
            ],
            "time_limit": None,
            "length_limit": None  # Can be adjusted based on task requirements
        }
        if additional_constraints:
            default_constraints["rules"].extend(additional_constraints)
        default_style = {"language": "Chinese"}

        try:
            template = PromptTemplateModel(
                task=task,
                role=default_role,
                context=default_context,
                input=default_input,
                output=default_output,
                constraints=default_constraints,
                style=default_style
            )
            self.templates.append(template)
            return template
        except ValidationError as e:
            raise ValueError(f"Error creating Software Architect prompt template: {e}")