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
    print("\nPrompt1 markdown output:")
    print(prompt1.to_markdown())

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
    print("\nPrompt2 markdown output:")
    print(prompt2.to_markdown())

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
    print("\nPrompt3 markdown output:")
    print(prompt3.to_markdown())

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
    print("\nPrompt4 markdown output:")
    print(prompt4.to_markdown())

    # Test Case 5: Testing Chain of Thought Output
    prompt5 = assistant.create_prompt(
        task="Design a microservices architecture for an e-commerce platform",
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
    print("\nPrompt5 markdown output:")
    print(prompt5.to_markdown())

    # Test Case 6: Testing Chain of Thought Output with Additional Constraints
    prompt6 = assistant.create_prompt(
        task="Design a microservices architecture for an e-commerce platform",
        additional_cot={
            "instructions": "Explain your thought process step by step", 
            "format": "chain_of_thought_with_code",
            "workflow": [
                {
                    "step": 1,
                    "description": "Requirement Analysis and Service Division",
                    "instructions": "List all core functionalities and define a microservice for each. Ensure low coupling and high cohesion between services."
                },
                {
                    "step": 2,
                    "description": "Service Design and Technology Selection",
                    "instructions": "Design a detailed technical architecture for each microservice, including choosing appropriate technology stacks, databases, and message queues. Consider scalability, fault tolerance, and performance needs."
                },
                {
                    "step": 3,
                    "description": "Service Interaction and API Design",
                    "instructions": "Define interaction methods between microservices and design clear API interfaces. Ensure efficient communication through RESTful API, gRPC, or event-driven approaches."
                },
                {
                    "step": 4,
                    "description": "Deployment Strategy and Monitoring",
                    "instructions": "Develop a deployment strategy for microservices, including containerization, orchestration, and service discovery. Set up monitoring and logging mechanisms to track service status and performance in real-time."
                }
            ]
        },
        additional_constraints={"rules": ["Ensure fault tolerance and scalability"],
                                "length_limit": "500 words max"}
    )   

    print("\nTest Case 6: Testing Chain of Thought Output with Additional Constraints:\n")
    print("\nCreated Prompt6 Template:")
    print(prompt6)
    print("\n\nPrompt6 json output:")
    print(prompt6.to_json())
    print("\n\nPrompt6 compact json output:")
    print(prompt6.to_compact_json())
    print("\n\nPrompt6 markdown output:")
    print(prompt6.to_markdown())
    print("\n\nPrompt6 summary:")
    print(prompt6.to_summary())

    # Test Case 7: Testing Chain of Thought Output with Additional Constraints and Style
    prompt7 = assistant.create_prompt(
        task="Design a microservices architecture for an e-commerce platform",
        additional_cot={
            "instructions": "Explain your thought process step by step", 
            "format": "chain_of_thought_with_code"
            },
        additional_constraints={"rules": ["Ensure fault tolerance and scalability"], "length_limit": "500 words max"}
    )   

    print("\nTest Case 7: Testing Chain of Thought Output with Additional Constraints and Style:\n")
    print("\nCreated Prompt7 Template:")
    print(prompt7)
    print("\nPrompt7 json output:")
    print(prompt7.to_json())
    print("\nPrompt7 compact json output:")
    print(prompt7.to_compact_json())
    print("\nPrompt7 markdown output:")
    print(prompt7.to_markdown())