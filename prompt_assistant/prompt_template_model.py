from pydantic import BaseModel, Field, Optional, Any, Dict

# Pydantic data model for prompt template
class PromptTemplateModel(BaseModel):
    """
    A data model for structured prompt templates.
    """
    task: str
    context: Optional[str] = Field(default="", description="Optional context or background information")
    input: Dict[str, Any] = Field(
        default={"type": "text", "data": ""},
        description="Input details including type and data"
    )
    output: Dict[str, Any] = Field(
        default={"type": "text", "format": "text", "examples": []},
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
