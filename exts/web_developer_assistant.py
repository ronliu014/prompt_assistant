from pydantic import ValidationError
from typing import Any, Dict, Optional
from core import PromptAssistant, PromptTemplateModel

# Example WebDeveloperAssistant for extensions
class WebDeveloperAssistant(PromptAssistant):
    """
    An Assistant class tailored for Web Developers, automatically setting role and related fields.
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
        Create a prompt template for a Web Developer, allowing the user to provide the task and optional context.
        
        :param task: The user's web development task description.
        :param context: Optional background information.
        :param additional_input: Optional list of additional input params.
        :param additional_output: Optional list of additional output params.
        :param additional_constraints: Optional list of additional constraint params.
        :param additional_cot: Optional additional chain of thought configuration.
        :return: The created and validated prompt template.
        """
        default_role = (
            "You are an experienced Web Developer proficient in HTML, CSS, JavaScript, TypeScript, React, Nextjs, "
            "Node.js, and other web technologies. You write efficient, maintainable front-end code and are well-versed "
            "in responsive design and front-end optimization."
        )
        default_context = context if context else (
            "You are knowledgeable in HTML, CSS, JavaScript, TypeScript, React, Nextjs, Node.js, and other front-end technologies, "
            "capable of providing professional code implementations and technical advice based on the task description."
        )

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
            "constraints": {
                "type_specific": [
                    "Code should include detailed comments",
                    "Provide code explanations and usage examples",
                    "Follow best front-end development practices"
                ]
            },
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
                "Code should adhere to modular design principles",
                "Ensure code readability and maintainability",
                "Optimize code for performance and loading speed"
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
            raise ValueError(f"Error creating Web Developer prompt template: {e}")