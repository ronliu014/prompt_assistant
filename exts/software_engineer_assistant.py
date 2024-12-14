from pydantic import ValidationError
from typing import Any, Dict, Optional
from core import PromptAssistant, PromptTemplateModel

# Example SoftwareEngineerAssistant for extensions
class SoftwareEngineerAssistant(PromptAssistant):
    """
    An assistant class customized specifically for Python software engineers, automatically setting roles and related fields.
    """

    def create_prompt(
        self,
        task: str,
        context: Optional[str] = None,
        additional_input: Optional[Dict[str, Any]] = None,
        additional_output: Optional[Dict[str, Any]] = None,
        additional_constraints: Optional[Dict[str, Any]] = None,
        additional_cot: Optional[Dict[str, Any]] = None
    ) -> PromptTemplateModel:
        """
        Create a prompt template for a Python software engineer, allowing the user to provide only the task and optional context and constraints.
        
        :param task: Description of the user's programming task.
        :param context: Optional background information.
        :param additional_input: Optional list of additional input params.
        :param additional_output: Optional list of additional output params.
        :param additional_constraints: Optional list of additional constraint params.
        :param additional_cot: Optional chain of thought configuration.
        :return: The created and validated prompt template.
        """
        default_role = "You are an experienced Python software engineer, proficient in writing efficient and maintainable Python code, and well-versed in various Python frameworks and libraries."
        default_context = context if context else "Please write a Python code implementation based on the provided task description."

        default_input = {
            "type": "text", 
            "data": [task],
            "examples": []
        }
        if additional_input:
            if "type" in additional_input:
                default_input["type"] = additional_input["type"]
            if "data" in additional_input:
                default_input["data"].extend(additional_input["data"])
            if "examples" in additional_input:
                default_input["examples"].extend(additional_input["examples"])

        default_output = {
            "type": "text",
            "format": "code_with_comments",
            "constraints": {"type_specific": ["Clear code comments", "Includes code explanations and usage examples"]},
            "examples": []
        }
        if additional_output:
            if "type" in additional_output:
                default_output["type"] = additional_output["type"]
            if "format" in additional_output:
                default_output["format"] = additional_output["format"]
            if "constraints" in additional_output:
                if "type_specific" in additional_output["constraints"]:
                    default_output["constraints"]["type_specific"].extend(additional_output["constraints"]["type_specific"])
            if "examples" in additional_output:
                default_output["examples"].extend(additional_output["examples"])

        default_constraints = {
            "rules": [
                "Code should adhere to object-oriented design principles",
                "Code should ensure efficient algorithm implementation",
                "Code should have good readability and maintainability"
            ],
            "time_limit": None,
            "length_limit": None  # Can be adjusted based on task requirements
        }
        if additional_constraints:
            if "rules" in additional_constraints:
                default_constraints["rules"].extend(additional_constraints["rules"])
            if "time_limit" in additional_constraints:
                default_constraints["time_limit"] = additional_constraints["time_limit"]
            if "length_limit" in additional_constraints:
                default_constraints["length_limit"] = additional_constraints["length_limit"]

        default_style = {"language": "Chinese"}

        default_cot = {
            "enable": False,
            "instructions": "",
            "format": ""
        }
        if additional_cot:
            default_cot["enable"] = True
            if "instructions" in additional_cot:
                default_cot["instructions"] = additional_cot["instructions"]
            if "format" in additional_cot:
                default_cot["format"] = additional_cot["format"]

        try:
            template = PromptTemplateModel(
                task=task,
                role=default_role,
                context=default_context,
                input=default_input,
                output=default_output,
                constraints=default_constraints,
                style=default_style,
                chain_of_thought=default_cot
            )
            self.templates.append(template)
            return template
        except ValidationError as e:
            raise ValueError(f"Error creating Python Software Engineer prompt template: {e}")