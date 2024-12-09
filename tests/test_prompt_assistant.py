from prompt_assistant import PromptAssistant

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

    # Print the prompt output
    print("Prompt info:")
    print(prompt.model_dump_json(indent=4))

    # Export templates to a file
    assistant.export_to_file("templates.json")

    # Clear and re-import templates
    assistant.clear_templates()
    assistant.import_from_file("templates.json")

    # List imported templates
    print("\nImported Templates:")
    print(assistant.list_templates())

    # Example of filter templates by task
    assistant_1 = PromptAssistant()
    assistant_1.create_prompt(
        task="Write a Python function",
        input={"type": "code"},
        output={"type": "code", "format": "Python"}
    )
    print("\nFiltered Templates by Task ('Python'):")
    print(assistant_1.filter_templates_by_task("Python"))