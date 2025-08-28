# ==============================================================================
# Purpose: The main application logic for the generated RAG project.
# This file is a fully functional, minimal example that a user can run
# immediately after generation.
# ------------------------------------------------------------------------------
import os
from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

# --- Phoenix Tracing Setup ---
# Key Decision: Placing the observability setup at the very top ensures that
# all subsequent instrumented libraries are correctly traced.
from openinference.instrumentation.langchain import LangChainInstrumentor
from opentelemetry import trace as trace_api
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk import trace as trace_sdk
from opentelemetry.sdk.trace.export import SimpleSpanProcessor

# Load environment variables from .env file
load_dotenv()

def setup_phoenix_tracing() -> None:
    """Initializes OpenTelemetry and Phoenix for tracing."""
    # Arize Phoenix requires an OTLP endpoint for trace ingestion.
    # The default endpoint for a local Phoenix server is http://127.0.0.1:6006/v1/traces
    endpoint = os.getenv("PHOENIX_TRACE_ENDPOINT", "http://127.0.0.1:6006/v1/traces")

    # Create an OTLP Span Exporter
    tracer_provider = trace_sdk.TracerProvider()
    span_exporter = OTLPSpanExporter(endpoint=endpoint)
    tracer_provider.add_span_processor(SimpleSpanProcessor(span_exporter=span_exporter))
    trace_api.set_tracer_provider(tracer_provider)

    # Instrument LangCHain to automatically capture traces
    LangChainInstrumentor().instrument()
    print("Phoenix tracing has been set up.")

def main() -> None:
    """
    Runs a minimal RAG Pipeline and prints the result.
    """
    # 1. Setup Tracing
    setup_phoenix_tracing()

    # 2. Create a simple in-memory vector store
    print("Creating in-memory vector store...")
    template_text = "Arize Phoenix is a tool for ML observability and evaluation. It helps AI engineers debug, monitor, and evaluate their LLM systems."
    vectorstore = FAISS.from_texts(  # type: ignore
        texts=[template_text], embedding=OpenAIEmbeddings()
    )
    retriever = vectorstore.as_retriever()

    # 3. Define the RAG prompt template
    template = """Answer the question based only on the following context:
    {context}

    Question: {question}
    """
    prompt = ChatPromptTemplate.from_template(template)

    # 4. Initialize the LLM 
    model = ChatOpenAI()
    
    # 5. Build the RAG chain
    # This chain will be automatically traced by Phoenix due to the instrumentation.
    rag_chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | prompt
        | model
        | StrOutputParser()
    )

    # 6. Invoke the chain with a question
    question = "What is Arize Phoenix?"
    print(f"\nAsking question: {question}")
    response = rag_chain.invoke(question)

    print("\nReceived response:")
    print(response)
    print("\nCheck your local Phoenix UI at http://127.0.0.1:6006 to see the trace!")


if __name__ == "__main__":
    main()