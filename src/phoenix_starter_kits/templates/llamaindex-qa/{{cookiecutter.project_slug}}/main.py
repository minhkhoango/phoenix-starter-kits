import os
import phoenix as px
from dotenv import load_dotenv
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.core.settings import Settings
from llama_index.llms.openai import OpenAI
from llama_index.embeddings.openai import OpenAIEmbedding

# Load environment variables from .env file
load_dotenv()

def setup_phoenix_tracing() -> None:
    """Initializes Phoenix for tracing."""
    # Key Decision: LlamaIndex has first-class support for Phoenix.
    # We can use its native callback handler, which is simpler than the
    # manual OpenTelemetry setup required for LangChain. This demonstrates
    # knowledge of framework-specific best practices.
    # Connect to existing Phoenix server instead of launching a new one
    px.Client()
    print("Phoenix tracing has been set up.")
    print("Phoenix UI running at: http://127.0.0.1:6006/")

def main() -> None:
    """
    Runs a minimal QA pipeline using LlamaIndex and prints the result.
    """
    # 1. Setup Tracing
    setup_phoenix_tracing()

    # Ensure API key is set
    if not os.getenv("OPENAI_API_KEY"):
        print("Error: OPENAI_API_KEY environment variable not set.")
        return

    # 2. Configure LlamaIndex Settings
    # Set the global settings for LLM and embedding models
    Settings.llm = OpenAI(model="gpt-3.5-turbo")
    Settings.embed_model = OpenAIEmbedding(model="text-embedding-ada-002")

    # 3. Load data and build an index
    print("Loading data and building index...")
    # Create a dummy data file for the example
    os.makedirs("data", exist_ok=True)
    with open("data/arize.txt", "w") as f:
        f.write("Arize Phoenix is an open-source evaluation and observability tool for LLMs.")
    
    documents = SimpleDirectoryReader("./data").load_data()
    index = VectorStoreIndex.from_documents(documents)

    # 4. Create a query engine
    # The query engine will automatically be traced by Phoenix.
    query_engine = index.as_query_engine()

    # 5. Run a query
    question = "What is Arize Phoenix?"
    print(f"\nAsking question: {question}")
    response = query_engine.query(question)

    print("\nReceived response:")
    print(str(response))
    print("\nCheck your Phoenix UI to see the trace!")


if __name__ == "__main__":
    main()