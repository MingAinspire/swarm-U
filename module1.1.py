import nbformat as nbf

nb = nbf.v4.new_notebook()

# Title and Overview
nb.cells.append(nbf.v4.new_markdown_cell("""# 1.2 Agent Fundamentals

## Overview
This module covers the essential fundamentals of working with agents in the Swarms framework, including initialization, configuration, system prompts, and memory management.

## Learning Objectives
- Master agent initialization and configuration options
- Understand and create effective system prompts
- Learn memory management fundamentals
- Practice creating specialized agents
"""))

# Setup
nb.cells.append(nbf.v4.new_markdown_cell("""## Setup and Environment Configuration

First, let's set up our development environment and import required libraries."""))

nb.cells.append(nbf.v4.new_code_cell("""import os
from swarms import Agent
from swarms.prompts.prompt import Prompt
from swarm_models import OpenAIChat, Anthropic
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Example with Groq
groq_api_key = os.getenv("GROQ_API_KEY")
groq_model = OpenAIChat(
    openai_api_base="https://api.groq.com/openai/v1",
    openai_api_key=groq_api_key,
    model_name="llama-3.1-70b-versatile",
    temperature=0.1,
)

# Example with Anthropic
anthropic_model = Anthropic(
    model_name="claude-3-5-sonnet-20240620",
    temperature=0.1,
)"""))

# Agent Initialization
nb.cells.append(nbf.v4.new_markdown_cell("""## 1. Agent Initialization and Configuration

Agents in Swarms can be initialized with various configurations to suit different use cases. Let's explore the key configuration options:

### Key Configuration Parameters:
- `llm`: Language model instance
- `agent_name`: Unique identifier for the agent
- `system_prompt`: Initial instructions/personality
- `max_loops`: Maximum conversation turns
- `memory_system`: Type of memory management
- `tools`: Available functions/capabilities
- `temperature`: Response randomness (0-1)"""))

nb.cells.append(nbf.v4.new_code_cell("""# Basic agent initialization
basic_agent = Agent(
    llm=anthropic_model,
    agent_name="basic-enterprise-agent",
    system_prompt="You are a helpful enterprise assistant.",
    max_loops=1
)

# Advanced agent configuration
advanced_agent = Agent(
    llm=anthropic_model,
    agent_name="advanced-enterprise-agent",
    system_prompt="You are an advanced enterprise assistant with specific capabilities.",
    max_loops=3,
    temperature=0.7,
    context_length=4096,
    dynamic_loops=True,
    interactive=True,
    verbose=True
)"""))

# System Prompts
nb.cells.append(nbf.v4.new_markdown_cell("""## 2. System Prompts and Templates

System prompts are crucial for defining agent behavior and capabilities. The Swarms framework provides a Prompt class for creating structured, production-grade prompts."""))

nb.cells.append(nbf.v4.new_code_cell("""# Create a prompt template using the Prompt class
enterprise_prompt = Prompt(
    name="enterprise-assistant-prompt",
    description="A specialized prompt for enterprise tasks",
    content='''
    You are an enterprise-grade assistant specialized in business operations.
    
    # Instructions
    - Analyze business requirements thoroughly
    - Provide structured, actionable responses
    - Maintain professional communication
    - Follow company policies and guidelines
    
    # Examples
    1. When asked about process improvement:
       - Analyze current workflow
       - Identify bottlenecks
       - Suggest optimizations
       - Provide implementation steps
    
    2. When handling data analysis:
       - Verify data quality
       - Apply appropriate methods
       - Present clear insights
       - Recommend actions
    
    # Constraints
    - Maintain data confidentiality
    - Follow compliance requirements
    - Stay within authorized access
    - Document all actions
    '''
)

# Create an agent with the specialized prompt
enterprise_agent = Agent(
    llm=anthropic_model,
    agent_name="specialized-enterprise-agent",
    system_prompt=enterprise_prompt.get_prompt(),
    max_loops=2
)"""))

# Prompt Generator
nb.cells.append(nbf.v4.new_markdown_cell("""### Using the Prompt Generator

The Swarms framework includes a prompt generator system for creating reliable, production-grade prompts."""))

nb.cells.append(nbf.v4.new_code_cell("""# Initialize the prompt generator
prompt_generator = Prompt(
    name="custom-prompt-generator",
    description="Generate specialized prompts for business cases",
    content='''
    Your task is to generate effective prompts for business scenarios.
    
    ## Guidelines
    1. Understand the specific business need
    2. Include clear instructions and examples
    3. Define appropriate constraints
    4. Consider edge cases
    5. Maintain professional tone
    
    ## Structure
    1. Role Definition
    2. Key Responsibilities
    3. Process Guidelines
    4. Success Criteria
    5. Limitations
    '''
)

# Generate a specialized prompt
business_case = "Create a prompt for an agent that handles financial reporting"
response = enterprise_agent.run(f"Using this prompt generator guidelines: {prompt_generator.get_prompt()}, create a specialized prompt for: {business_case}")
print(response)"""))

# Memory Management
nb.cells.append(nbf.v4.new_markdown_cell("""## 3. Memory Management Basics

Agents in Swarms have sophisticated memory management capabilities:

1. **Short-term Memory**
   - Handles current conversation context
   - Maintains recent interactions
   - Manages working memory

2. **Long-term Memory**
   - Stores historical knowledge
   - Maintains persistent information
   - Enables learning from past interactions"""))

nb.cells.append(nbf.v4.new_code_cell("""# Memory management example
memory_agent = Agent(
    llm=anthropic_model,
    agent_name="memory-demo-agent",
    system_prompt="You are an assistant with advanced memory capabilities.",
    max_loops=3
)

# Add information to memory
memory_agent.add_message_to_memory("Important client meeting scheduled for tomorrow at 10 AM.")
memory_agent.add_message_to_memory("Client preferences: Prefers detailed technical documentation.")

# Test memory retention
response = memory_agent.run("What do you know about the client and their upcoming meeting?")
print("Agent Response:", response)

# Check memory contents
print("\nCurrent Memory Contents:")
print(memory_agent.short_memory.return_history_as_string())"""))

# Practical Exercise
nb.cells.append(nbf.v4.new_markdown_cell("""## Practical Exercise

Create a specialized enterprise agent that combines all the concepts we've learned:
1. Custom configuration
2. Specialized prompt
3. Memory management

Task: Create an agent that helps with project management tasks."""))

nb.cells.append(nbf.v4.new_code_cell("""# Create a project management prompt
project_mgmt_prompt = Prompt(
    name="project-manager-prompt",
    description="Specialized prompt for project management tasks",
    content='''
    You are a project management specialist who helps with:
    1. Project planning and tracking
    2. Resource allocation
    3. Timeline management
    4. Risk assessment
    
    # Instructions
    - Analyze project requirements
    - Create structured plans
    - Monitor progress
    - Identify and mitigate risks
    
    # Examples
    - When given a project timeline, break it into manageable tasks
    - When asked about resources, provide detailed allocation plans
    
    # Constraints
    - Follow project management best practices
    - Consider budget limitations
    - Maintain realistic timelines
    '''
)

# Create the specialized agent
project_agent = Agent(
    llm=anthropic_model,
    agent_name="project-manager",
    system_prompt=project_mgmt_prompt.get_prompt(),
    max_loops=3,
    temperature=0.7,
    interactive=True
)

# Test the agent with a project scenario
project_scenario = '''
New Website Development Project:
- Timeline: 3 months
- Budget: $50,000
- Team: 2 developers, 1 designer
- Requirements: E-commerce functionality, mobile-friendly design
'''

response = project_agent.run(f"Create a project plan for this scenario: {project_scenario}")
print(response)"""))

# Save the notebook
with open("1.2_Agent_Fundamentals.ipynb", "w") as f:
    nbf.write(nb, f)