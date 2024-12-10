from exts import LanguageExpertAssistant

# Example usage
if __name__ == "__main__":
    # Create an instance of LanguageExpertAssistant
    assistant = LanguageExpertAssistant()

    # Test Case 1: Creating a Basic Language Analysis Task
    # Scenario 1: User provides only the task description
    prompt1 = assistant.create_prompt(
        task="Analyze the sentiment of customer reviews for our new product."
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
        task="Summarize the key topics discussed in the provided multilingual articles.",
        context="The articles are in Chinese, English, French, German, Japanese, and Korean, focusing on recent technological advancements."
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
        task="Extract key entities and their relationships from the provided technical documents.",
        additional_constraints=["Ensure extraction accuracy above 90%", "Include contextual explanations for each entity relationship"]
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
        task="Perform sentiment analysis and topic modeling on social media posts about our recent marketing campaign.",
        context="The posts are in English, Chinese, and Japanese, collected from various platforms during the last two weeks.",
        additional_constraints=["Provide trend analysis over time", "Identify key influencers in the discussions"]
    )
    
    print("\nTest Case 4: User Provides Task Description, Background Information, and Additional Constraints:\n")
    print("\nCreated Prompt4 Template:")
    print(prompt4)
    print("\nprompt4 json output:")
    print(prompt4.to_json())
    print("\nprompt4 compact json output:")
    print(prompt4.to_compact_json())