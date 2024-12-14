from exts import SoftwareArchitectAssistant

# Example usage
if __name__ == "__main__":
    # Create an instance of SoftwareArchitectAssistant
    assistant = SoftwareArchitectAssistant()

    # Test Case 1: Creating a Basic Software Architecture Task
    # Scenario 1: User provides only the task description
    prompt1 = assistant.create_prompt(
        task="Design a software architecture for a scalable e-commerce platform."
    )

    print("\n\nTest Case 1: Creating a Basic Software Architecture Task:\n")
    print("\nCreated Prompt1 Template:")
    print(prompt1)
    print("\nPrompt1 json output:")
    print(prompt1.to_json())
    print("\nPrompt1 compact json output:")
    print(prompt1.to_compact_json())

    # Test Case 2: User Provides Task Description and Background Information
    # Scenario 2: User provides task description and context
    prompt2 = assistant.create_prompt(
        task="Design a software architecture for a scalable e-commerce platform.",
        context="The platform should support high traffic volumes during peak sales seasons and integrate with multiple payment gateways."
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
        task="Design a software architecture for a scalable e-commerce platform.",
        additional_constraints=["Must include microservices architecture", "Ensure compliance with GDPR regulations"]
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
        task="Design a software architecture for a scalable e-commerce platform.",
        context="The platform should support high traffic volumes during peak sales seasons and integrate with multiple payment gateways.",
        additional_constraints=["Must include microservices architecture", "Ensure compliance with GDPR regulations"]
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
        task="Design a microservices architecture for an e-commerce platform",
        additional_cot={"enable": True, "instructions": "Explain your thought process step by step", "format": "chain_of_thought_with_code"}
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
        task="Design a microservices architecture for an e-commerce platform",
        additional_cot={"enable": True, "instructions": "Explain your thought process step by step", "format": "chain_of_thought_with_code"},
        additional_constraints={"rules": ["Ensure fault tolerance and scalability"], "length_limit": "500 words max"}
    )   

    print("\nTest Case 6: Testing Chain of Thought Output with Additional Constraints:\n")
    print("\nCreated Prompt6 Template:")
    print(prompt6)
    print("\nPrompt6 json output:")
    print(prompt6.to_json())
    print("\nPrompt6 compact json output:")
    print(prompt6.to_compact_json())

    # Test Case 7: Testing Chain of Thought Output with Additional Constraints and Style
    prompt7 = assistant.create_prompt(
        task="Design a microservices architecture for an e-commerce platform",
        additional_cot={"enable": True, "instructions": "Explain your thought process step by step", "format": "chain_of_thought_with_code"},
        additional_constraints={"rules": ["Ensure fault tolerance and scalability"], "length_limit": "500 words max"},
        style={"language": "English"}
    )   

    print("\nTest Case 7: Testing Chain of Thought Output with Additional Constraints and Style:\n")
    print("\nCreated Prompt7 Template:")
    print(prompt7)
    print("\nPrompt7 json output:")
    print(prompt7.to_json())
    print("\nPrompt7 compact json output:")
    print(prompt7.to_compact_json())
