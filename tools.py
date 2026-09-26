from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.tools import tool
from datetime import datetime

import wikipedia as _wiki_pkg # Phải thêm dòng này vì bản cũ đã lỗi thời gây lỗi khi gọi
_wiki_pkg.set_user_agent("MyResearchAgent/1.0 (contact: your_email@example.com)")

@tool
def save_text_to_file(data: str, filename: str = "research_output.txt") -> str:
    """Saves structured research data to a text file."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_text = f"--- Research Output ---\nTimestamp: {timestamp}\n\n{data}\n\n"

    with open(filename, "a", encoding="utf-8") as f:
        f.write(formatted_text)
    
    return f"Data successfully saved to {filename}"

save_tool = save_text_to_file  # ✅ Dùng trực tiếp

# Search tool
search = DuckDuckGoSearchRun()
search_tool = search  # ✅ Dùng trực tiếp

# Wiki tool
api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=100)
wiki_tool = WikipediaQueryRun(api_wrapper=api_wrapper)