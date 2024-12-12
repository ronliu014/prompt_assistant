from pydantic import ValidationError
from typing import Optional, List
from core import PromptAssistant, PromptTemplateModel

# Example LanguageExpertAssistant for extensions
class LanguageExpertAssistant(PromptAssistant):
    """
    An assistant class customized specifically for Language Analysis Experts, automatically setting roles and related fields.
    """

    def create_prompt(
        self,
        task: str,
        context: Optional[str] = "",
        additional_input: Optional[List[str]] = None,
        additional_output: Optional[List[str]] = None,
        additional_constraints: Optional[List[str]] = None
    ) -> PromptTemplateModel:
        """
        Create a prompt template for a Language Analysis Expert, allowing the user to provide only the task and optional context and constraints.
        
        :param task: Description of the user's language analysis task.
        :param context: Optional background information.
        :param additional_constraints: Optional list of additional constraint rules.
        :return: The created and validated prompt template.
        """
        default_role = "You are an experienced Language Analysis Expert proficient in analyzing and processing text in major global languages including Chinese, English, French, German, Japanese, and Korean."
        default_context = context if context else "Please perform a language analysis based on the provided task description."
        default_input = {"type": "text", "data": [task]}
        if additional_input:
            default_input["data"].extend(additional_input)
        default_output = {
            "type": "text",
            "format": "analysis_report",
            "constraints": {"type_specific": ["Comprehensive summaries", "Accurate sentiment analysis", "Detailed information extraction"]},
            "examples": []
        }
        if additional_output:
            default_input["examples"].extend(additional_output)
        default_constraints = {
            "rules": [
                "Ensure accuracy and relevance in all analyses",
                "Adhere to specified analysis methodologies",
                "Provide clear and concise explanations"
            ],
            "time_limit": None,
            "length_limit": None  # Can be adjusted based on task requirements
        }
        if additional_constraints:
            default_constraints["rules"].extend(additional_constraints)
        default_style = {"tone": "formal", "language": "English"}

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
            raise ValueError(f"Error creating Language Analysis Expert prompt template: {e}")