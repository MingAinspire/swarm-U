import nbformat as nbf
import os

def create_notebook_dir():
    """Create directory for notebooks if it doesn't exist"""
    if not os.path.exists('notebooks'):
        os.makedirs('notebooks')

def create_module1_lesson1():
    """Create Introduction to Autonomous Agents notebook"""
    nb = nbf.v4.new_notebook()
    
    # Title and Overview
    nb.cells.append(nbf.v4.new_markdown_cell("""
    # Module 1.1: Introduction to Autonomous Agents
    
    ## Learning Objectives
    By the end of this lesson, you will:
    - Understand the architecture of autonomous agents
    - Learn about key components of enterprise agents
    - Get familiar with the Swarms agent ecosystem
    
    ## Prerequisites
    - Python 3.10+
    - OpenAI/Anthropic API key
    - Basic Python knowledge
    """))
    
    # Setup Section
    nb.cells.append(nbf.v4.new_markdown_cell("""
    ## Environment Setup
    First, let's set up our development environment and required packages.
    """))
    
    nb.cells.append(nbf.v4.new_code_cell("""
    !pip install -U swarms python-dotenv

    import os
    from dotenv import load_dotenv
    
    # Load environment variables
    load_dotenv()
    
    # Set workspace directory
    os.environ["WORKSPACE_DIR"] = "agent_workspace"
    
    print("Environment setup complete!")
    """))
    
    # Agent Architecture Section
    nb.cells.append(nbf.v4.new_markdown_cell("""
    ## Understanding Agent Architecture
    
    Autonomous agents in Swarms are composed of several key components:
    1. Language Model (LLM)
    2. Memory Systems
    3. Tool Integration
    4. Planning & Execution Logic
    
    Let's explore a basic agent structure:
    """))
    
    nb.cells.append(nbf.v4.new_code_cell("""
    from swarms import Agent
    from swarms.models import OpenAIChat
    
    # Initialize the LLM
    llm = OpenAIChat()
    
    # Create a basic agent
    agent = Agent(
        llm=llm,
        agent_name="enterprise-agent-01",
        max_loops=1,
        system_prompt="You are an enterprise assistant helping with business tasks."
    )
    
    # Examine agent components
    print(f"Agent Name: {agent.agent_name}")
    print(f"Max Loops: {agent.max_loops}")
    print(f"System Prompt: {agent.system_prompt}")
    """))
    
    # Enterprise Components Section
    nb.cells.append(nbf.v4.new_markdown_cell("""
    ## Key Components of Enterprise Agents
    
    Enterprise agents require additional capabilities beyond basic agents:
    1. Long-term Memory
    2. Tool Integration
    3. Error Handling
    4. Monitoring
    """))
    
    nb.cells.append(nbf.v4.new_code_cell("""
    # Creating an enterprise-ready agent
    enterprise_agent = Agent(
        llm=llm,
        agent_name="enterprise-agent-02",
        max_loops=3,
        system_prompt="You are an enterprise assistant helping with business tasks.",
        verbose=True,
        return_history=True,
        self_healing_enabled=True,
        autosave=True
    )
    
    # Demonstrate enterprise features
    print("Enterprise Agent Configuration:")
    print(f"Self-healing enabled: {enterprise_agent.self_healing_enabled}")
    print(f"Autosave enabled: {enterprise_agent.autosave}")
    print(f"History tracking: {enterprise_agent.return_history}")
    """))
    
    return nb

def create_module1_lesson2():
    """Create Agent Fundamentals notebook"""
    nb = nbf.v4.new_notebook()
    
    # Title and Overview
    nb.cells.append(nbf.v4.new_markdown_cell("""
    # Module 1.2: Agent Fundamentals
    
    ## Learning Objectives
    By the end of this lesson, you will:
    - Learn how to initialize and configure agents
    - Understand system prompts and templates
    - Master basic memory management
    
    ## Prerequisites
    - Completion of Module 1.1
    - Working Swarms installation
    """))
    
    # Agent Initialization Section
    nb.cells.append(nbf.v4.new_markdown_cell("""
    ## Agent Initialization and Configuration
    
    Let's explore different ways to initialize and configure agents:
    """))
    
    nb.cells.append(nbf.v4.new_code_cell("""
    from swarms import Agent
    from swarms.models import OpenAIChat
    
    # Initialize LLM
    llm = OpenAIChat()
    
    # Basic configuration
    basic_agent = Agent(
        llm=llm,
        agent_name="config-demo-agent",
        max_loops=2
    )
    
    # Advanced configuration
    advanced_agent = Agent(
        llm=llm,
        agent_name="advanced-config-agent",
        max_loops=3,
        system_prompt="You are an advanced enterprise assistant.",
        temperature=0.7,
        context_length=4096,
        dynamic_temperature_enabled=True,
        interactive=True
    )
    
    print("Agent Configurations:")
    print(f"Basic Agent Max Loops: {basic_agent.max_loops}")
    print(f"Advanced Agent Temperature: {advanced_agent.temperature}")
    """))
    
    # System Prompts Section
    nb.cells.append(nbf.v4.new_markdown_cell("""
    ## System Prompts and Templates
    
    System prompts define the agent's behavior and capabilities.
    Let's explore different prompt strategies:
    """))
    
    nb.cells.append(nbf.v4.new_code_cell("""
    # Different system prompt examples
    customer_service_prompt = '''You are an enterprise customer service assistant.
    Your role is to:
    1. Address customer inquiries professionally
    2. Follow company guidelines
    3. Escalate complex issues appropriately'''
    
    data_analyst_prompt = '''You are an enterprise data analysis assistant.
    Your role is to:
    1. Analyze data patterns
    2. Generate insights
    3. Create reports'''
    
    # Create agents with different prompts
    cs_agent = Agent(
        llm=llm,
        agent_name="customer-service",
        system_prompt=customer_service_prompt
    )
    
    analyst_agent = Agent(
        llm=llm,
        agent_name="data-analyst",
        system_prompt=data_analyst_prompt
    )
    
    # Test the agents
    cs_response = cs_agent.run("How do I handle a customer complaint?")
    analyst_response = analyst_agent.run("What patterns should I look for in sales data?")
    
    print("Customer Service Response:", cs_response)
    print("\nData Analyst Response:", analyst_response)
    """))
    
    # Memory Management Section
    nb.cells.append(nbf.v4.new_markdown_cell("""
    ## Memory Management Basics
    
    Understanding how to manage agent memory is crucial for enterprise applications:
    """))
    
    nb.cells.append(nbf.v4.new_code_cell("""
    # Create an agent with memory management
    memory_agent = Agent(
        llm=llm,
        agent_name="memory-demo",
        max_loops=3,
        context_length=4096,
        memory_chunk_size=2000
    )
    
    # Demonstrate memory operations
    memory_agent.add_message_to_memory("Important customer information: Customer ID 12345")
    memory_agent.add_message_to_memory("Previous interaction: Product inquiry about Enterprise Suite")
    
    # Check memory content
    print("Current Memory Content:")
    print(memory_agent.short_memory.return_history_as_string())
    
    # Check token usage
    tokens_used = memory_agent.check_available_tokens()
    print(f"\nTokens Used: {tokens_used}")
    print(f"Available Tokens: {memory_agent.context_length - tokens_used}")
    """))
    
    return nb

def create_module1_lesson3():
    """Create Practical Exercise notebook"""
    nb = nbf.v4.new_notebook()
    
    # Title and Overview
    nb.cells.append(nbf.v4.new_markdown_cell("""
    # Module 1.3: Practical Exercise
    
    ## Learning Objectives
    By the end of this practical exercise, you will:
    - Set up a fully functional enterprise agent
    - Configure the agent for specific business tasks
    - Run and test the agent in different scenarios
    
    ## Prerequisites
    - Completion of Modules 1.1 and 1.2
    - Working Swarms installation
    """))
    
    # Setup Section
    nb.cells.append(nbf.v4.new_markdown_cell("""
    ## Exercise 1: Setting Up Your First Enterprise Agent
    
    Let's create a comprehensive enterprise agent that can handle multiple business tasks:
    """))
    
    nb.cells.append(nbf.v4.new_code_cell("""
    from swarms import Agent
    from swarms.models import OpenAIChat
    
    # Initialize the LLM
    llm = OpenAIChat()
    
    # Create an enterprise agent with comprehensive configuration
    enterprise_agent = Agent(
        llm=llm,
        agent_name="enterprise-assistant",
        max_loops=5,
        system_prompt='''You are an enterprise assistant capable of:
        1. Analyzing business data
        2. Generating reports
        3. Answering customer inquiries
        4. Providing product recommendations
        Always maintain professional communication and follow best practices.''',
        temperature=0.7,
        context_length=4096,
        dynamic_temperature_enabled=True,
        self_healing_enabled=True,
        autosave=True,
        verbose=True,
        return_history=True
    )
    """))
    
    # Configuration Exercise
    nb.cells.append(nbf.v4.new_markdown_cell("""
    ## Exercise 2: Basic Agent Configuration
    
    Let's test different configurations and see how they affect agent behavior:
    """))
    
    nb.cells.append(nbf.v4.new_code_cell("""
    # Test different temperature settings
    def test_temperature_impact():
        results = []
        
        for temp in [0.1, 0.5, 0.9]:
            agent = Agent(
                llm=llm,
                agent_name=f"temp-test-{temp}",
                temperature=temp,
                max_loops=1
            )
            
            response = agent.run("Suggest a marketing strategy for a new product.")
            results.append({
                "temperature": temp,
                "response": response
            })
        
        return results
    
    # Run temperature test
    temperature_results = test_temperature_impact()
    
    for result in temperature_results:
        print(f"\nTemperature: {result['temperature']}")
        print(f"Response: {result['response']}")
    """))
    
    # Practical Tasks
    nb.cells.append(nbf.v4.new_markdown_cell("""
    ## Exercise 3: Running Simple Tasks
    
    Let's put our agent to work with some real-world business scenarios:
    """))
    
    nb.cells.append(nbf.v4.new_code_cell("""
    # Define some business tasks
    tasks = [
        "Analyze the customer feedback: 'Your product is great but the interface needs improvement'",
        "Create a brief report on market trends in the tech industry",
        "Generate a response to a customer inquiry about pricing"
    ]
    
    # Process tasks
    for task in tasks:
        print(f"\nProcessing Task: {task}")
        response = enterprise_agent.run(task)
        print(f"Response: {response}")
        
    # Check agent performance
    print("\nAgent Performance Metrics:")
    print(f"Total Tokens Used: {enterprise_agent.check_available_tokens()}")
    print(f"Remaining Context Length: {enterprise_agent.context_length - enterprise_agent.check_available_tokens()}")
    """))
    
    # Final Challenge
    nb.cells.append(nbf.v4.new_markdown_cell("""
    ## Final Challenge
    
    Now it's your turn! Create an agent for a specific business use case:
    1. Choose a specific business domain (e.g., HR, Sales, Customer Support)
    2. Configure the agent appropriately
    3. Test it with relevant tasks
    """))
    
    nb.cells.append(nbf.v4.new_code_cell("""
    # Your solution here
    # Example structure:
    specialized_agent = Agent(
        llm=llm,
        agent_name="your-specialized-agent",
        system_prompt="Your custom prompt here",
        # Add your configuration
    )
    
    # Test your agent
    test_tasks = [
        # Add your test tasks
    ]
    
    # Run tests
    # Add your test code
    """))
    
    return nb

def save_notebooks():
    """Save all notebooks to files"""
    create_notebook_dir()
    
    notebooks = {
        'module1_lesson1.ipynb': create_module1_lesson1(),
        'module1_lesson2.ipynb': create_module1_lesson2(),
        'module1_lesson3.ipynb': create_module1_lesson3()
    }
    
    for filename, nb in notebooks.items():
        with open(os.path.join('notebooks', filename), 'w') as f:
            nbf.write(nb, f)
        print(f"Created {filename}")

if __name__ == "__main__":
    save_notebooks()
    print("All notebooks generated successfully!")