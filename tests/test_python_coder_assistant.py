from exts import PyCoderAssistant

# Example usage
if __name__ == "__main__":
    # Create an instance of PyCoderAssistant
    assistant = PyCoderAssistant()

    # Test Case 1: Create a Prompt to Generate a Python Function
    # Create a prompt template for generating a quick sort algorithm
    prompt1 = assistant.create_prompt(
        task="Generate a Python function for the Quick Sort algorithm",
        input_data={"type": "text", "data": "Implement a Quick Sort algorithm that takes a list of integers and returns the sorted list."},
        output={
            "type": "code",
            "format": "Python",
            "constraints": {
                "type_specific": [
                    "Output only the code and don't output anything other than the code"
                ]
            },
            "examples": [
                "def sum(a, b):\n        return a + b"
            ]
        },
        constraints={"rules": ["Follow PEP 8 coding standards", "Time complexity should be O(n log n)"]},
        style={"language": "Chinese"}
    )

    print("\n\nTest Case 1: Create a Prompt to Generate a Python Function:\n")
    print("\nCreated Prompt1 Template:")
    print(prompt1)
    print("\nPrompt1 json output:")
    print(prompt1.to_json())
    print("\nPrompt1 compact json output:")
    print(prompt1.to_compact_json())

    # Test Case 2: Create a Prompt to Debug Python Code
    # Create a prompt template for debugging Python code
    prompt2 = assistant.create_prompt(
        task="Debug the following Python code and provide a solution",
        input_data={"type": "code", "data": "def add(a, b):\n    return a + b"},
        constraints={"rules": ["Provide detailed error analysis", "Ensure the code runs correctly"]},
        style={"language": "English"}
    )

    print("\n\nTest Case 2: Create a Prompt to Debug Python Code:\n")
    print("\nCreated Prompt2 Template:")
    print(prompt2)
    print("\nPrompt2 json output:")
    print(prompt2.to_json())
    print("\nPrompt2 compact json output:")
    print(prompt2.to_compact_json())

    # Test Case 3: Create a Prompt to Optimize Python Algorithm Performance
    # Create a prompt template for optimizing Python algorithm performance
    prompt3 = assistant.create_prompt(
        task="Optimize the following Python algorithm for better performance",
        input_data={
            "type": "text",
            "data": "The current algorithm runs slowly when handling large datasets. How can it be optimized?"
        },
        output={
            "type": "text",
            "format": "paragraph",
            "examples": ["Consider using more efficient data structures such as dictionaries or sets to avoid unnecessary loops."]
        },
        constraints={"length_limit": "Within 200 words"},
        style={"language": "Chinese"}
    )

    print("\n\nTest Case 3: Create a Prompt to Optimize Python Algorithm Performance:\n")
    print("\nCreated Prompt3 Template:")
    print(prompt3)
    print("\nPrompt3 json output:")
    print(prompt3.to_json())
    print("\nPrompt3 compact json output:")
    print(prompt3.to_compact_json())