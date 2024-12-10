from exts import PyArchitectAssistant

# Example usage
if __name__ == "__main__":
    # Create an instance of PyCoderAssistant
    assistant = PyArchitectAssistant()

    # Test Case 1: Create a Prompt for Designing a Microservices Architecture
    # The user wants the assistant to design a Python-based microservices architecture for an e-commerce platform, 
    # including service decomposition, communication methods, and database selection
    prompt1 = assistant.create_prompt(
        task="Design a microservices architecture for an e-commerce platform",
        input_data={
            "type": "text",
            "data": "Design a scalable and maintainable microservices architecture for an online e-commerce platform handling high traffic and large volumes of transactions."
        },
        output={
            "type": "text",
            "format": "paragraph",
            "examples": [
                "The microservices architecture consists of separate services for user management, product catalog, order processing, and payment. Communication is handled via RESTful APIs and message queues using RabbitMQ. Databases are distributed, with MongoDB for product data and PostgreSQL for transactional data."
            ]
        },
        constraints={"rules": ["Ensure fault tolerance and scalability"], "length_limit": "500 words max"},
        style={"language": "English"}
    )

    print("\n\nTest Case 1: Create a Prompt for Designing a Microservices Architecture:\n")
    print("\nCreated Prompt Template:")
    print(prompt1)
    print("\nPrompt1 json output:")
    print(prompt1.to_json())
    print("\nPrompt1 compact json output:")
    print(prompt1.to_compact_json())

    # Test Case 2: Create a Prompt for Designing a High-Availability System
    # The user wants the assistant to design a high-availability Python system that ensures quick recovery in case of failures.
    prompt2 = assistant.create_prompt(
        task="Design a high-availability system for real-time data processing",
        input_data={"type": "text", "data": "Design a Python-based system that processes real-time data streams with minimal downtime and quick recovery in case of failures."},
        output={
            "type": "text",
            "format": "paragraph",
            "examples": [
                "Implement a redundant infrastructure using load balancers and multiple application servers. Utilize Kubernetes for orchestration and automatic failover. Employ Redis for in-memory data caching and Apache Kafka for reliable message streaming."
            ]
        },
        constraints={"rules": ["Implement redundancy and failover mechanisms"], "time_limit": "24 hours"},  # Time_limit here might not be typical, but included for illustration
        style={"language": "English"}
    )

    print("\n\nTest Case 2: Create a Prompt for Designing a High-Availability System:\n")
    print("\nCreated Prompt2 Template:")
    print(prompt2)
    print("\nPrompt2 json output:")
    print(prompt2.to_json())
    print("\nPrompt2 compact json output:")
    print(prompt2.to_compact_json())

    # Test Case 3: Create a Prompt for Designing a Distributed Database System
    # The user wants the assistant to design a distributed database system that ensures data consistency and high performance.
    prompt3 = assistant.create_prompt(
        task="Design a distributed database system for a social media application",
        input_data={
            "type": "text",
            "data": "Design a distributed database system for a social media application that ensures data consistency, scalability, and high performance."
        },
        output={
            "type": "text",
            "format": "paragraph",
            "examples": [
                "Use a combination of Cassandra for handling large volumes of write operations and Elasticsearch for efficient read queries. Implement a consistency model with eventual consistency for user posts and strong consistency for user profiles. Utilize replication and sharding to achieve scalability."
            ]
        },
        constraints={"rules": ["Ensure data replication and sharding"], "length_limit": "400 words max"},
        style={"language": "English"}
    )

    print("\n\nTest Case 3: Create a Prompt for Designing a Distributed Database System:\n")
    print("\nCreated Prompt3 Template:")
    print(prompt3)
    print("\nPrompt3 json output:")
    print(prompt3.to_json())
    print("\nPrompt3 compact json output:")
    print(prompt3.to_compact_json())