from pydantic import BaseModel, Field
from typing import Optional, Any, Dict
import json

# Pydantic data model for prompt template
class PromptTemplateModel(BaseModel):
    """
    A data model for structured prompt templates.
    """
    task: str
    role: Optional[str] = Field(
        default="",
        description="Optional the role expected to be played by AI assistants.",
    )
    context: Optional[str] = Field(
        default="",
        description="Optional context or background information",
    )
    input: Dict[str, Any] = Field(
        default={
            "type": "text", 
            "data": [], 
            "examples": []
        },
        description="Input details including type, data, and examples",
    )
    output: Dict[str, Any] = Field(
        default={
            "type": "text",
            "format": "text",
            "constraints": {"type_specific": []},
            "examples": [],
        },
        description="Output details including type, format, and examples",
    )
    constraints: Dict[str, Any] = Field(
        default={
            "rules": [], 
            "time_limit": None, 
            "length_limit": None
        },
        description="Constraints like rules, time limit, and length limit",
    )
    style: Dict[str, Any] = Field(
        default={
            "tone": "neutral", 
            "language": "English"
        },
        description="Style preferences such as tone and language",
    )
    chain_of_thought: Optional[Dict[str, Any]] = Field(
        default={
            "instructions": "", 
            "format": "", 
            "workflow": []
        },
        description="""
        Optional Chain-of-Thought (COT) configuration.
        - instructions: Specific instructions for the reasoning process (optional).
        - format: Desired format for the reasoning output (optional).
        - workflow: Optional structured workflow for the reasoning process (optional).
        """,
    )

    def _remove_empty_fields(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Helper function to recursively remove empty fields (e.g., None, empty dicts, or empty lists) from a dictionary.

        :param data: The dictionary to process.
        :return: A new dictionary with empty fields removed.
        """
        if isinstance(data, dict):
            return {
                key: self._remove_empty_fields(value)
                for key, value in data.items()
                if value not in (None, [], {}, "")  # Remove None, empty lists, empty dicts, or empty strings
            }
        elif isinstance(data, list):
            return [
                self._remove_empty_fields(item) 
                for item in data 
                if item not in (None, [], {}, "")  # Remove None, empty lists, empty dicts, or empty strings
            ]
        else:
            return data

    def to_json(self) -> str:
        """
        Returns a pretty-printed JSON string of the model's data, excluding empty fields.

        :return: A JSON string with indentation for readability.
        """
        # Get the model's data as a dictionary
        raw_data = self.model_dump()  # Get all fields

        # Remove empty fields recursively
        cleaned_data = self._remove_empty_fields(raw_data)

        # Convert the cleaned data to a JSON string with indentation
        return json.dumps(cleaned_data, indent=4)
    
    def to_compact_json(self) -> str:
        """
        Returns a compact JSON string of the model's data, excluding empty fields.
        Fields are tightly packed with no extra whitespace.

        :return: A compact JSON string.
        """
        # Get the model's data as a dictionary
        raw_data = self.model_dump()

        # Remove empty fields recursively
        cleaned_data = self._remove_empty_fields(raw_data)

        # Convert the cleaned data to a compact JSON string (no extra spaces or newlines)
        return json.dumps(cleaned_data, separators=(",", ":"))

    def to_markdown(self) -> str:
        """
        Dynamically generates a Markdown-formatted string of the model's data,
        displaying all top-level fields as headers and their content as nested lists.

        :return: A Markdown-formatted string.
        """
        # Get the model's data as a dictionary
        raw_data = self.model_dump()

        # Remove empty fields recursively
        cleaned_data = self._remove_empty_fields(raw_data)

        # Helper function to format nested dictionaries and lists as Markdown
        def format_markdown(data, indent=""):
            """
            Recursively format dictionaries and lists into Markdown syntax.

            :param data: The data to format (could be a dict, list, or scalar).
            :param indent: The current level of indentation (string, e.g., "  ").
            :return: A list of Markdown-formatted strings.
            """
            md_lines = []

            if isinstance(data, dict):
                for key, value in data.items():
                    # Use a bullet point for dictionary keys
                    md_lines.append(f"{indent}- **{key}**:")
                    md_lines.extend(format_markdown(value, indent + "  "))
            elif isinstance(data, list):
                for item in data:
                    if isinstance(item, dict):
                        # Use a bullet point for nested dictionaries
                        md_lines.append(f"{indent}-")
                        md_lines.extend(format_markdown(item, indent + "  "))
                    else:
                        # Use a bullet point for scalar items in a list
                        md_lines.append(f"{indent}- {item}")
            else:
                # For scalar values, output directly as a list item
                md_lines.append(f"{indent}- {data}")

            return md_lines

        # Convert the cleaned data into Markdown
        markdown_lines = []
        for field, value in cleaned_data.items():
            # Add a Markdown heading for each field
            markdown_lines.append(f"# {field}")
            # Format the field's data as nested Markdown
            markdown_lines.extend(format_markdown(value))

        # Join all lines into a single Markdown string
        return "\n".join(markdown_lines)
    
    def to_summary(self) -> str:
        """
        Returns a summary of all outputs in a structured format.
        Includes pretty-printed JSON, Markdown, and compact JSON outputs.

        :return: A string with the summarized output.
        """
        return (
            "=======================Prompt json output===============================\n\n"
            f"{self.to_json()}\n\n"
            "======================Prompt markdown output============================\n\n"
            f"{self.to_markdown()}\n\n"
            "===================Prompt compact json output===========================\n\n"
            f"{self.to_compact_json()}\n\n"
            "========================================================================"
        )