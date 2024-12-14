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

    # Test Case 5: Creating a Python Programming Task with COT Enabled
    # Scenario 5: User provides task description and enables COT
    prompt5 = assistant.create_prompt(
        task="Write a Python program to implement the binary search algorithm.",
        context="This algorithm will be used for fast searching in large datasets, requiring optimized code to enhance search efficiency.",
        chain_of_thought={
            "enable": True,
            "instructions": "Please detail the design rationale and each step of the logic.",
            "format": "Step-by-step explanation, each step with brief description."
        }
    )

    print("\n\nTest Case 5: Creating a Python Programming Task with COT Enabled:\n")
    print("\nCreated Prompt5 Template:")
    print(prompt5)
    print("\nPrompt5 json output:")
    print(assistant.to_json(prompt5))
    print("\nPrompt5 compact json output:")
    print(assistant.to_compact_json(prompt5))

    # Test Case 6: Creating a Python Programming Task with Additional Constraints and COT
    # Scenario 6: User provides task description, additional constraints, and enables COT
    prompt6 = assistant.create_prompt(
        task="Write a Python program to implement the binary search algorithm.",
        additional_constraints=["Code must support custom comparison functions", "Should handle empty lists and single-element lists"],
        chain_of_thought={
            "enable": True,
            "instructions": "Provide a detailed reasoning process for each design decision.",
            "format": "Logical reasoning steps with explanations."
        }
    )

    print("\n\nTest Case 6: Creating a Python Programming Task with Additional Constraints and COT:\n")
    print("\nCreated Prompt6 Template:")
    print(prompt6)
    print("\nPrompt6 json output:")
    print(prompt6.to_json())
    print("\nPrompt6 compact json output:")
    print(prompt6.to_compact_json())

    # Test Case 7: Creating a Python Programming Task with Context, Additional Constraints, and COT
    # Scenario 7: User provides task description, context, additional constraints, and enables COT
    prompt7 = assistant.create_prompt(
        task="Write a Python program to implement the binary search algorithm.",
        context="This algorithm will be used for fast searching in large datasets, requiring optimized code to enhance search efficiency.",
        additional_constraints=["Code must support custom comparison functions", "Should handle empty lists and single-element lists"],
        chain_of_thought={
            "enable": True,
            "instructions": "Please provide a comprehensive reasoning process for the implementation steps.",
            "format": "Detailed step-by-step reasoning with explanations."
        }
    )

    print("\nTest Case 7: Creating a Python Programming Task with Context, Additional Constraints, and COT:\n")
    print("\nCreated Prompt7 Template:")
    print(prompt7)
    print("\nPrompt7 json output:")
    print(assistant.to_json(prompt7))
    print("\nPrompt7 compact json output:")
    print(assistant.to_compact_json(prompt7))