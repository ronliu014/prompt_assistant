from exts import PythonDeveloperAssistant

# Example usage
if __name__ == "__main__":
    # Create an instance of PythonDeveloperAssistant
    assistant = PythonDeveloperAssistant()

    # Test Case 1: User provides only the task description
    # Scenario 1: The user supplies only the python development task description without any additional context.
    prompt1 = assistant.create_prompt(
        task="Write a Python program to implement the binary search algorithm."
    )

    print("\n\nTest Case 1: Providing Only Task Description:\n")
    print("\nCreated Prompt1 Template:")
    print(prompt1)
    print("\nPrompt1 json output:")
    print(prompt1.to_json())
    print("\nPrompt1 compact json output:")
    print(prompt1.to_compact_json())

    # Test Case 2: User Provides Task Description and Background Information
    # Scenario 2: The user provides a web development task along with specific background information.
    prompt2 = assistant.create_prompt(
        task="Write a Python program to implement the binary search algorithm.",
        context="This algorithm will be used for fast searching in large datasets, requiring optimized code to enhance search efficiency.",
        chain_of_thought=True
    )

    print("\n\nTest Case 2: User Provides Task Description and Background Information:\n")
    print("\nCreated Prompt2 Template:")
    print(prompt2)
    print("\nPrompt2 json output:")
    print(prompt2.to_json())
    print("\nPrompt2 compact json output:")
    print(prompt2.to_compact_json())

    # Test Case 3: Providing Task Description Without Context
    # Scenario 3: Similar to Test Case 1, the user provides only the task description to verify default context application.
    prompt3 = assistant.create_prompt(
        task="Write a Python program to implement the binary search algorithm.",
        additional_constraints={"rules":[
            "Code must support custom comparison functions",
            "Should handle empty lists and single-element lists"
        ]}
    )

    print("\n\nTest Case 3: User Provides Task Description and Additional Constraints:\n")
    print("\nCreated Prompt3 Template:")
    print(prompt3)
    print("\nPrompt3 json output:")
    print(prompt3.to_json())
    print("\nPrompt3 compact json output:")
    print(prompt3.to_compact_json())

    # Test Case 4: User Provides Task Description, Background Information, and Additional Constraints
    # Scenario 4: The user supplies a detailed task description along with comprehensive background information to test the Assistant's handling of complex contexts.
    prompt4 = assistant.create_prompt(
        task="Write a Python program to implement the binary search algorithm.",
        context="This algorithm will be used for fast searching in large datasets, requiring optimized code to enhance search efficiency.",
        additional_constraints={"rules":[
            "Code must support custom comparison functions",
            "Should handle empty lists and single-element lists"
        ]}
    )
    
    print("\nTest Case 4: User Provides Task Description, Background Information, and Additional Constraints:\n")
    print("\nCreated Prompt4 Template:")
    print(prompt4)
    print("\nprompt4 json output:")
    print(prompt4.to_json())
    print("\nprompt4 compact json output:")
    print(prompt4.to_compact_json())

    # Test Case 5: Testing Chain of Thought Output
    prompt5 = assistant.create_prompt(
        task="Implement a custom sorting algorithm for a specific use case.",
        context="The sorting algorithm needs to handle partially sorted data efficiently.",
        additional_cot={"enable": True, "instructions": "Explain your thought process step by step", "format": "chain_of_thought_with_code"},
        additional_constraints={"rules": [
            "Must handle edge cases gracefully",
            "Should provide performance analysis"
        ]}
    )

    print("\nTest Case 5: Testing Chain of Thought Output:\n")
    print("\nCreated Prompt5 Template:")
    print(prompt5)
    print("\nPrompt5 json output:")
    print(prompt5.to_json())
    print("\nPrompt5 compact json output:")
    print(prompt5.to_compact_json())

