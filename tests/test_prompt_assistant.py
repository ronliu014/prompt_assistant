from prompt_assistant import PromptAssistant
from prompt_assistant import CustomAssistant

# Example usage
if __name__ == "__main__":
    # Create an instance of PromptAssistant
    assistant = PromptAssistant()

    # Create a structured prompt template
    prompt = assistant.create_prompt(
        task="Generate a product description",
        context="E-commerce website description",
        input={"type": "text", "data": "Lightweight laptop with touchscreen."},
        output={
            "type": "text",
            "format": "paragraph",
            "examples": ["This lightweight laptop features a touchscreen, perfect for students and professionals."]
        },
        constraints={"rules": ["Focus on positive aspects", "Limit to 100 words"]},
        style={"tone": "professional", "language": "English"}
    )

    # Print the created prompt
    print("Created Prompt Template:")
    print(prompt)

    # Export templates to a file
    assistant.export_to_file("templates.json")

    # Clear and re-import templates
    assistant.clear_templates()
    assistant.import_from_file("templates.json")

    # List imported templates
    print("\nImported Templates:")
    print(assistant.list_templates())

    # Example of custom assistant usage
    custom_assistant = CustomAssistant()
    custom_assistant.create_prompt(
        task="Write a Python function",
        input={"type": "code"},
        output={"type": "code", "format": "Python"}
    )
    print("\nFiltered Templates by Task ('Python'):")
    print(custom_assistant.filter_templates_by_task("Python"))
