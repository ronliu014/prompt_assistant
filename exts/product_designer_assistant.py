from pydantic import ValidationError
from typing import Optional, List
from core import PromptAssistant, PromptTemplateModel

# Example ProductDesignerAssistant for extensions
class ProductDesignerAssistant(PromptAssistant):
    """
    An assistant class customized specifically for product designers, automatically setting roles and related fields.
    """

    def create_prompt(
        self,
        task: str,
        context: Optional[str] = "",
        additional_constraints: Optional[List[str]] = None
    ) -> PromptTemplateModel:
        """
        Create a prompt template for a product designer, allowing the user to provide only the task and optional context and constraints.
        
        :param task: Description of the user's design task.
        :param context: Optional background information.
        :param additional_constraints: Optional list of additional constraint rules.
        :return: The created and validated prompt template.
        """
        default_role = "You are an experienced product designer specializing in AI and mobile internet product design."
        default_context = context if context else "Please create a product design based on the provided task description."
        default_input = {"type": "text", "data": task}
        default_output = {
            "type": "text",
            "format": "paragraph",
            "constraints": {"type_specific": ["Highly professional", "Well-structured"]},
            "examples": []
        }
        constraints = {
            "rules": ["Provide detailed design proposals", "Include user needs analysis"],
            "time_limit": None,
            "length_limit": 500  # Default length limit
        }
        if additional_constraints:
            constraints["rules"].extend(additional_constraints)
        default_style = {"tone": "formal", "language": "English"}

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
            raise ValueError(f"Error creating product designer prompt template: {e}")