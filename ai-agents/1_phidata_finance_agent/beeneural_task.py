# from phi.agent import Agent
# from phi.model.groq import Groq
# from phi.tools.duckduckgo import DuckDuckGo
# from dotenv import load_dotenv

# # Load environment variables (if any API keys are required)
# load_dotenv()

# # Content Generator Agent
# content_generator = Agent(
#     name="Content Generator",
#     role="Generate SEO-optimized articles",
#     model=Groq(id="llama-3.3-70b-versatile"),
#     tools=[],  # No tools; purely article generation based on inputs
#     instructions=[
#         "Write SEO-optimized articles based on the given keyword, difficulty, and search volume.",
#         "Ensure the content follows SEO best practices and includes relevant headings and subheadings."
#     ],
#     show_tool_calls=True,
#     markdown=True
# )

# # SEO Policy Agent
# seo_policy_agent = Agent(
#     name="SEO Policy Agent",
#     role="Fetch and summarize SEO policies",
#     model=Groq(id="llama-3.3-70b-versatile"),
#     tools=[DuckDuckGo()],
#     instructions=[
#         "Search for the latest SEO policies and summarize them.",
#         "Always include the sources for any SEO policy findings."
#     ],
#     show_tool_calls=True,
#     markdown=True
# )

# # Analytics Agent
# analytics_agent = Agent(
#     name="Analytics Agent",
#     role="Analyze Google Analytics trends",
#     model=Groq(id="llama-3.3-70b-versatile"),
#     tools=[DuckDuckGo()],  # Use DuckDuckGo for trends, or integrate Google Analytics API
#     instructions=[
#         "Fetch trends for given keywords using Google Analytics or DuckDuckGo.",
#         "Provide a summary of top-performing topics and relevant trends."
#     ],
#     show_tool_calls=True,
#     markdown=True
# )

# # Combined Agent Team
# seo_agent_team = Agent(
#     name="SEO Agent Team",
#     model=Groq(id="llama-3.3-70b-versatile"),
#     team=[content_generator, seo_policy_agent, analytics_agent],
#     instructions=[
#         "Combine the results of all agents to produce SEO-optimized articles.",
#         "Ensure compliance with SEO policies and include trend analysis in the content.",
#         "Use tables or structured formats where appropriate."
#     ],
#     show_tool_calls=True,
#     markdown=True
# )

# # Example Usage
# seo_agent_team.print_response(
#     "Generate an SEO-optimized article for the keyword 'AI Tools for Marketing' with a difficulty of 45 and search volume of 10,000. Also summarize the latest SEO policies and trends for this topic.",
#     stream=True
# )



    # .....................................................2nd try.................................................................

# from phi.agent import Agent
# from phi.model.groq import Groq
# from phi.tools.duckduckgo import DuckDuckGo
# from dotenv import load_dotenv

# load_dotenv()

# # Define the agents
# content_generator = Agent(
#     name="Content Generator",
#     role="Write SEO-optimized articles",
#     model=Groq(id="llama-3.3-70b-versatile"),
#     instructions=[
#         "Write a detailed, SEO-optimized article based on the given keyword, search volume, and difficulty.",
#         "Include headings, subheadings, and bullet points for readability.",
#         "Incorporate the latest SEO trends into the article, such as ideal keyword density, meta tag suggestions, and content length.",
#         "Use Markdown for formatting the article.",
#     ],
#     show_tool_calls=True,
#     markdown=True,
# )

# seo_policy_agent = Agent(
#     name="SEO Policy Agent",
#     role="Analyze SEO policies and trends",
#     model=Groq(id="llama-3.3-70b-versatile"),
#     tools=[DuckDuckGo()],
#     instructions=["Always include sources", "Summarize SEO trends concisely."],
#     show_tool_calls=True,
#     markdown=True,
# )

# agent_team = Agent(
#     model=Groq(id="llama-3.3-70b-versatile"),
#     team=[content_generator, seo_policy_agent],
#     instructions=["Always include sources", "Use Markdown for output."],
#     show_tool_calls=True,
#     markdown=True,
# )

# # Execute the task
# parameters = {
#     "keyword": "AI Tools for Marketing",
#     "difficulty": 45,
#     "search_volume": 10000
# }

# task_description = f"""
# Generate an SEO-optimized article for the keyword '{parameters['keyword']}'.
# Search volume: {parameters['search_volume']}, Difficulty: {parameters['difficulty']}.
# Include insights from SEO trends and a clear structure with headings.
# """

# response = agent_team.print_response(
#     task_description, stream=True
# )

from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv

load_dotenv()

# Function to display search results before proceeding
def display_results(query, results):
    print(f"\n[INFO] Search query: {query}\n")
    if not results:
        print("[ERROR] No search results found.")
        return False
    
    for idx, result in enumerate(results, 1):
        # Check if result is a dictionary
        if isinstance(result, dict):
            title = result.get('title', 'No title available')
            url = result.get('href', 'No URL available')  # Updated 'url' to 'href'
            snippet = result.get('body', 'No snippet available')  # Updated 'snippet' to 'body'
        else:
            # Handle result as string
            title = result
            url = "No URL available"
            snippet = "No snippet available"

        # Print the result
        print(f"[{idx}] {title} - {url}")
        print(f"Snippet: {snippet}\n")
    
    # Prompt user for input
    user_input = input("\nAre these results relevant? (yes/no): ")
    return user_input.strip().lower() == "yes"


# Define the agents
content_generator = Agent(
    name="Content Generator",
    role="Write SEO-optimized articles",
    model=Groq(id="llama-3.3-70b-versatile"),
    instructions=[
        "Write a detailed, SEO-optimized article based on the given keyword, search volume, and difficulty.",
        "Include headings, subheadings, and bullet points for readability.",
        "Incorporate the latest SEO trends into the article, such as ideal keyword density, meta tag suggestions, and content length.",
        "Use Markdown for formatting the article.",
    ],
    show_tool_calls=True,
    markdown=True,
)

seo_policy_agent = Agent(
    name="SEO Policy Agent",
    role="Analyze SEO policies and trends",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources", "Summarize SEO trends concisely."],
    show_tool_calls=True,
    markdown=True,
)

# Execute the task
parameters = {
    "keyword": "AI Tools for Marketing",
    "difficulty": 45,
    "search_volume": 10000
}

query = f"latest SEO trends for {parameters['keyword']}"

# Use DuckDuckGo to search
duckduckgo_tool = DuckDuckGo()
results = duckduckgo_tool.duckduckgo_news(query)

# Display results to the user
if not display_results(query, results):
    print("\n[INFO] Stopping execution. Please refine your query and try again.")
    exit()

# If results are valid, proceed
seo_policy_agent.transfer_task(
    task_description=f"Analyze SEO policies and trends for {parameters['keyword']}.",
    additional_information="Use the provided search results to summarize key trends.",
    context=results
)

# Wait for the SEO policy agent to complete before proceeding
seo_policy_agent_response = seo_policy_agent.wait_for_response()

# Proceed with content generation only if SEO analysis is complete
if seo_policy_agent_response:
    content_generator.transfer_task(
        task_description=f"Write an SEO-optimized article for the keyword '{parameters['keyword']}' with a difficulty of {parameters['difficulty']} and search volume of {parameters['search_volume']}.",
        expected_output="A complete SEO-optimized article with structured formatting.",
        additional_information="Incorporate insights from SEO trends analyzed earlier."
    )

    # Final execution
    response = content_generator.print_response(
        task_description=f"Generate an SEO-optimized article for {parameters['keyword']}.",
        stream=True
    )
else:
    print("[ERROR] SEO policy analysis failed. Task cannot proceed.")
