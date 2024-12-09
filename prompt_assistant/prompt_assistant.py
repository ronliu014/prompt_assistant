from pydantic import ValidationError
from typing import List, Dict, Any
from .prompt_template_model import PromptTemplateModel
import json

class PromptAssistant:
    """
    A library for creating, managing, and exporting/importing structured prompt templates.
    """

    def __init__(self):
        """
        Initialize the assistant with an empty template list.
        """
        self.templates: List[PromptTemplateModel] = []

    def create_prompt(self, task: str, **kwargs) -> PromptTemplateModel:
        """
        Create a new prompt template and validate it using Pydantic.

        :param task: The task for the prompt.
        :param kwargs: Additional parameters for the prompt template.
        :return: The created and validated prompt template.
        """
        try:
            template = PromptTemplateModel(task=task, **kwargs)
            self.templates.append(template)
            return template
        except ValidationError as e:
            raise ValueError(f"Error creating prompt: {e}")

    def list_templates(self) -> List[Dict[str, Any]]:
        """
        List all stored templates as dictionaries.

        :return: A list of all templates.
        """
        return [template.model_dump() for template in self.templates]

    def clear_templates(self):
        """
        Clear all stored templates.
        """
        self.templates = []

    def add_custom_rule(self, template: PromptTemplateModel, rule: str):
        """
        Add a custom rule to a specific template.

        :param template: The target template.
        :param rule: The rule to be added.
        """
        if isinstance(template, PromptTemplateModel):
            template.constraints["rules"].append(rule)
        else:
            raise TypeError("Invalid template. Must be an instance of PromptTemplateModel.")

    def export_to_file(self, file_path: str):
        """
        Export all templates to a JSON file.

        :param file_path: The path to the output JSON file.
        """
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(self.list_templates(), f, indent=4)

    def import_from_file(self, file_path: str):
        """
        Import templates from a JSON file.

        :param file_path: The path to the input JSON file.
        """
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            for item in data:
                try:
                    template = PromptTemplateModel(**item)
                    self.templates.append(template)
                except ValidationError as e:
                    print(f"Error importing template: {e}")

    def __repr__(self):
        return f"PromptAssistant(templates={len(self.templates)})"
