from pydantic import ValidationError
from typing import Any, Dict, Optional
from core import PromptAssistant, PromptTemplateModel

# Example PythonDeveloperAssistant for extensions
class PythonDeveloperAssistant(PromptAssistant):
    """
    An assistant class customized specifically for Python software developers, automatically setting roles and related fields.
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
        Create a prompt template for a Python developer, allowing the user to provide only the task and optional context and constraints.

        :param task: Description of the user's programming task.
        :param context: Optional background information.
        :param additional_input: Optional additional input parameters.
        :param additional_output: Optional additional output parameters.
        :param additional_constraints: Optional additional constraint rules.
        :return: The created and validated prompt template.
        """
        # Set default role description
        default_role = (
            "You are an experienced backend software engineer with deep expertise in backend architecture design, "
            "proficient in Python, Django, Flask, FastAPI, Tornado, Nginx, SQLite, MySQL, PostgreSQL, Aiohttp, and RESTful APIs."
        )

        # Set default context
        default_context = context if context else "Please write Python backend code based on the provided task description."

        # Set default input
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

        # Set default output
        default_output = {
            "type": "text",
            "format": "code_with_comments",
            "constraints": {"type_specific": [
                "Code should include clear comments",
                "Includes code explanations and usage examples"
            ]},
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

        # Set default constraints
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

        # Set default style
        default_style = {"language": "Chinese", "tone": "professional"}

        # 添加默认的 chain of thought 配置
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
            raise ValueError(f"Error creating PythonDeveloper prompt template: {e}")