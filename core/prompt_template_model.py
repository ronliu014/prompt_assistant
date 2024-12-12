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
        default={"type": "text", "data": []},
        description="Input details including type and data"
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