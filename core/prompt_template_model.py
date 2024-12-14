from pydantic import BaseModel, Field
from typing import Optional, Any, Dict

# Pydantic data model for prompt template
class PromptTemplateModel(BaseModel):
    """
    A data model for structured prompt templates.
    """
    task: str
    role: Optional[str] = Field(
        default="", 
        description="Optional the role expected to be played by AI assistants."
    )
    context: Optional[str] = Field(
        default="", 
        description="Optional context or background information"
    )
    input: Dict[str, Any] = Field(
        default={"type": "text", "data": [], "examples": []},
        description="Input details including type, data, and examples"
    )
    output: Dict[str, Any] = Field(
        default={"type": "text", "format": "text", "constraints": {"type_specific": []}, "examples": []},
        description="Output details including type, format, and examples"
    )
    constraints: Dict[str, Any] = Field(
        default={"rules": [], "time_limit": None, "length_limit": None},
        description="Constraints like rules, time limit, and length limit"
    )
    style: Dict[str, Any] = Field(
        default={"tone": "neutral", "language": "English"},
        description="Style preferences such as tone and language"
    )
    chain_of_thought: Optional[Dict[str, Any]] = Field(
        default={"enable": False, "instructions": "", "format": ""},
        description="""
        Optional Chain-of-Thought (COT) configuration.
        - enable: Whether to enable COT (boolean).
        - instructions: Specific instructions for the reasoning process (optional).
        - format: Desired format for the reasoning output (optional).
        """
    )

    def to_json(self) -> str:
        """
        Returns a pretty-printed JSON string of the model's data.
        
        :return: A JSON string with indentation for readability.
        """
        return self.model_dump_json(indent=4, exclude_unset=True)
    
    def to_compact_json(self) -> str:
        """
        Returns a compact JSON string of the model's data.
        
        :return: A JSON string without extra whitespace.
        """
        return self.model_dump_json(exclude_unset=True)
    
    def dump_prompt(self) -> str:
        """
        Returns a formatted string containing the JSON representation of the prompt.

        :return: A formatted string with the prompt's JSON data.
        """
        return f"""
=======================Prompt json output===============================

{self.to_json()}

===================Prompt compact json output===========================

{self.to_compact_json()}

========================================================================
"""
    
    def to_markdown(self) -> str:
        """
        Converts the prompt template to a well-formatted markdown string.
        
        :return: A markdown formatted string representation of the prompt template.
        """
        def format_dict(d: Dict[str, Any], level: int = 2) -> str:
            """Helper function to format dictionary content into markdown"""
            md = ""
            for key, value in d.items():
                if isinstance(value, dict):
                    md += f"{'#' * level} {key.title()}\n\n"
                    md += format_dict(value, level + 1)
                elif isinstance(value, list):
                    if value:  # Only add if list is not empty
                        md += f"{'#' * level} {key.title()}\n\n"
                        for item in value:
                            md += f"- {item}\n"
                        md += "\n"
                elif value not in [None, "", False]:  # Only add if value is meaningful
                    md += f"{'#' * level} {key.title()}\n\n{value}\n\n"
            return md

        markdown = "# Prompt Template\n\n"
        
        # Handle task
        markdown += f"## Task\n\n{self.task}\n\n"
        
        # Handle role if present
        if self.role:
            markdown += f"## Role\n\n{self.role}\n\n"
        
        # Handle context if present
        if self.context:
            markdown += f"## Context\n\n{self.context}\n\n"
        
        # Handle input
        markdown += "## Input\n\n"
        if self.input["type"]:
            markdown += f"**Type:** {self.input['type']}\n\n"
        if self.input["data"]:
            markdown += "### Data\n\n"
            for item in self.input["data"]:
                markdown += f"- {item}\n"
            markdown += "\n"
        if self.input["examples"]:
            markdown += "### Examples\n\n"
            for item in self.input["examples"]:
                markdown += f"- {item}\n"
            markdown += "\n"
        
        # Handle output
        markdown += "## Output\n\n"
        if self.output["type"]:
            markdown += f"**Type:** {self.output['type']}\n"
        if self.output["format"]:
            markdown += f"**Format:** {self.output['format']}\n\n"
        if self.output["constraints"]["type_specific"]:
            markdown += "### Constraints\n\n"
            for constraint in self.output["constraints"]["type_specific"]:
                markdown += f"- {constraint}\n"
            markdown += "\n"
        if self.output["examples"]:
            markdown += "### Examples\n\n"
            for example in self.output["examples"]:
                markdown += f"- {example}\n"
            markdown += "\n"
        
        # Handle constraints
        if any(self.constraints.values()):
            markdown += "## Constraints\n\n"
            if self.constraints["rules"]:
                markdown += "### Rules\n\n"
                for rule in self.constraints["rules"]:
                    markdown += f"- {rule}\n"
                markdown += "\n"
            if self.constraints["time_limit"]:
                markdown += f"**Time Limit:** {self.constraints['time_limit']}\n\n"
            if self.constraints["length_limit"]:
                markdown += f"**Length Limit:** {self.constraints['length_limit']}\n\n"
        
        # Handle style
        markdown += "## Style\n\n"
        markdown += f"**Tone:** {self.style['tone']}\n"
        markdown += f"**Language:** {self.style['language']}\n\n"
        
        # Handle chain of thought if enabled
        if self.chain_of_thought["enable"]:
            markdown += "## Chain of Thought\n\n"
            if self.chain_of_thought["instructions"]:
                markdown += f"### Instructions\n\n{self.chain_of_thought['instructions']}\n\n"
            if self.chain_of_thought["format"]:
                markdown += f"### Format\n\n{self.chain_of_thought['format']}\n\n"
        
        return markdown
