from pydantic import ValidationError
from typing import Any, Dict, Optional
from core import PromptAssistant, PromptTemplateModel

# Example ProductDesignerAssistant for extensions
class ProductDesignerAssistant(PromptAssistant):
    """
    An assistant class customized specifically for product designers, automatically setting roles and related fields.
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
        Create a prompt template for a product designer, allowing the user to provide only the task and optional context and constraints.
        
        :param task: Description of the user's design task.
        :param context: Optional background information.
        :param additional_input: Optional list of additional input params.
        :param additional_output: Optional list of additional output params.
        :param additional_constraints: Optional list of additional constraint params.
        :param additional_cot: Optional chain of thought configuration.
        :return: The created and validated prompt template.
        """
        default_role = "You are an experienced product designer specializing in AI and mobile internet product design."
        default_context = context if context else "Please create a product design based on the provided task description."

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
            "format": "markdown",
            "constraints": {"type_specific": ["Highly professional", "Well-structured"]},
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
            "rules": ["Provide detailed design proposals", "Include user needs analysis"],
            "time_limit": None,  # Default time limit
            "length_limit": None  # Default length limit
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
            "instructions": "",
            "format": "",
            "workflow":[]
        }
        if additional_cot:
            if "instructions" in additional_cot:
                default_cot["instructions"] = additional_cot["instructions"]
            if "format" in additional_cot:
                default_cot["format"] = additional_cot["format"]
            if "workflow" in additional_cot:
                default_cot["workflow"] = additional_cot["workflow"]
        else:
            default_cot = None

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
            raise ValueError(f"Error creating product designer prompt template: {e}")