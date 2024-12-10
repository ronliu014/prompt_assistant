from exts import SoftwareEngineerAssistant

# Example usage
if __name__ == "__main__":
    # Create an instance of SoftwareEngineerAssistant
    assistant = SoftwareEngineerAssistant()

    # Test Case 1: Creating a Basic Python Programming Task
    # Scenario 1: User provides only the task description
    prompt1 = assistant.create_prompt(
        task="Write a Python program to implement the binary search algorithm."
    )

    print("\n\nTest Case 1: Creating a Basic Python Programming Task:\n")
    print("\nCreated Prompt1 Template:")
    print(prompt1)
    print("\nPrompt1 json output:")
    print(prompt1.to_json())
    print("\nPrompt1 compact json output:")
    print(prompt1.to_compact_json())

    # Test Case 2: User Provides Task Description and Background Information
    # Scenario 2: User provides task description and context
    prompt2 = assistant.create_prompt(
        task="Write a Python program to implement the binary search algorithm.",
        context="This algorithm will be used for fast searching in large datasets, requiring optimized code to enhance search efficiency."
    )

    print("\n\nTest Case 2: User Provides Task Description and Background Information:\n")
    print("\nCreated Prompt2 Template:")
    print(prompt2)
    print("\nPrompt2 json output:")
    print(prompt2.to_json())
    print("\nPrompt2 compact json output:")
    print(prompt2.to_compact_json())

    # Test Case 3: User Provides Task Description and Additional Constraints
    # Scenario 3: User provides task description and additional constraints
    prompt3 = assistant.create_prompt(
        task="Write a Python program to implement the binary search algorithm.",
        additional_constraints=["Code must support custom comparison functions", "Should handle empty lists and single-element lists"]
    )

    print("\n\nTest Case 3: User Provides Task Description and Additional Constraints:\n")
    print("\nCreated Prompt3 Template:")
    print(prompt3)
    print("\nPrompt3 json output:")
    print(prompt3.to_json())
    print("\nPrompt3 compact json output:")
    print(prompt3.to_compact_json())

    # Test Case 4: User Provides Task Description, Background Information, and Additional Constraints
    # Scenario 4: User provides task description, context, and additional constraints
    prompt4 = assistant.create_prompt(
        task="Write a Python program to implement the binary search algorithm.",
        context="This algorithm will be used for fast searching in large datasets, requiring optimized code to enhance search efficiency.",
        additional_constraints=["Code must support custom comparison functions", "Should handle empty lists and single-element lists"]
    )
    
    print("\nTest Case 4: User Provides Task Description, Background Information, and Additional Constraints:\n")
    print("\nCreated Prompt4 Template:")
    print(prompt4)
    print("\nprompt4 json output:")
    print(prompt4.to_json())
    print("\nprompt4 compact json output:")
    print(prompt4.to_compact_json())