from exts import WebDeveloperAssistant

# Example usage
if __name__ == "__main__":
    # Create an instance of WebDeveloperAssistant
    assistant = WebDeveloperAssistant()

    # Test Case 1: Providing Only Task Description
    # Scenario 1: The user supplies only the web development task description without any additional context.
    prompt1 = assistant.create_prompt(
        task="Create a responsive navigation bar with dropdown menus and a search feature."
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
        task="Implement an image carousel component with animation effects.",
        context="The carousel will be used on the homepage of an e-commerce website and must support automatic cycling and manual navigation."
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
        task="Develop a real-time data visualization dashboard."
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
        task="Design a multi-language user login interface with OAuth integration.",
        context=(
            "This login interface will be used for an international social platform, supporting English, Chinese, and Spanish languages, "
            "and integrating Google and Facebook OAuth authentication."
        )
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
        task="Create a responsive grid layout system with CSS Grid.",
        context="The grid system should be flexible and support both fixed and fluid layouts.",
        additional_cot={
            "instructions": "Explain your thought process step by step", 
            "format": "chain_of_thought_with_code"
            }
    )

    print("\nTest Case 5: Testing Chain of Thought Output:\n")
    print("\nCreated Prompt5 Template:")
    print(prompt5)
    print("\nPrompt5 json output:")
    print(prompt5.to_json())
    print("\nPrompt5 compact json output:")
    print(prompt5.to_compact_json())

    # Test Case 6: Testing Chain of Thought Output with Additional Constraints
    prompt6 = assistant.create_prompt(
        task="Create a responsive grid layout system with CSS Grid.",
        context="The grid system should be flexible and support both fixed and fluid layouts.",
        additional_cot={
            "instructions": "Explain your thought process step by step",
            "format": "chain_of_thought_with_code"
        },
        additional_constraints={"rules": [
            "Must support different screen sizes",
            "Should include fallback for older browsers"
        ]}
    )

    print("\nTest Case 6: Testing Chain of Thought Output with Additional Constraints:\n")
    print("\nCreated Prompt6 Template:")
    print(prompt6)
    print("\nPrompt6 json output:")
    print(prompt6.to_json())
    print("\nPrompt6 compact json output:")
    print(prompt6.to_compact_json())
