from langchain_community.tools import DuckDuckGoSearchRun
from langchain.tools import Tool
from datetime import datetime
import wikipediaapi  

# ---------- Save Function ----------
def save_to_txt(data: str, filename: str = "research_output.txt"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_text = f"--- Research Output ---\nTimestamp: {timestamp}\n\n{data}\n\n --- End of Output ---\n\n"

    with open(filename, "a", encoding="utf-8") as f:
        f.write(formatted_text)
    
    return f"Data successfully saved to {filename}"

# ---------- Tool: Save ----------
save_tool = Tool(
    name="save_text_to_file",
    func=save_to_txt,
    description="Saves structured research data to a text file.",
)

# ---------- Tool: DuckDuckGo ----------
search = DuckDuckGoSearchRun()
search_tool = Tool(
    name="search",
    func=search.run,
    description="Search the web for information",
)

# ---------- Tool: Wikipedia (Custom using wikipediaapi) ----------
wiki_api = wikipediaapi.Wikipedia(
    language="en",
    user_agent="MyResearchAgent/1.0 (tpraneelkeshav@gmail.com)"
)

def fetch_wikipedia_summary(query: str) -> str:
    page = wiki_api.page(query)
    if not page.exists():
        return f"No Wikipedia page found for '{query}'."
    return page.summary[:100]  

wiki_tool = Tool(
    name="wikipedia_search",
    func=fetch_wikipedia_summary,
    description="Fetch a summary of a topic from Wikipedia using wikipediaapi. Input should be a topic name.",
)
