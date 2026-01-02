from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever
import sys

# Initialize the LLM model
try:
    model = OllamaLLM(model="llama3.2", temperature=0.7)
except Exception as e:
    print(f"Error initializing model: {e}")
    print("Please make sure Ollama is running and llama3.2 model is installed.")
    sys.exit(1)

# Enhanced prompt template
template = """You are an expert assistant for a pizza restaurant. Your role is to help customers by answering their questions based on real customer reviews.

Here are some relevant customer reviews from the restaurant:
{reviews}

Based on these reviews, please answer the following question in a helpful and informative way. If the reviews don't contain enough information to fully answer the question, say so honestly.

Question: {question}

Answer:"""

prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

def format_reviews(reviews):
    """Format retrieved reviews for better readability"""
    formatted = []
    for i, review in enumerate(reviews, 1):
        rating = review.metadata.get('rating', 'N/A')
        date = review.metadata.get('date', 'N/A')
        content = review.page_content[:200] + "..." if len(review.page_content) > 200 else review.page_content
        formatted.append(f"Review {i} (Rating: {rating}/5, Date: {date}):\n{content}")
    return "\n\n".join(formatted)

def main():
    print("=" * 60)
    print("🍕 Pizza Restaurant Q&A Assistant")
    print("=" * 60)
    print("Ask me anything about the restaurant based on customer reviews!")
    print("Type 'q' or 'quit' to exit.\n")
    
    while True:
        try:
            print("-" * 60)
            question = input("❓ Your question: ").strip()
            
            if question.lower() in ['q', 'quit', 'exit']:
                print("\n👋 Thank you for using the Pizza Restaurant Assistant!")
                break
            
            if not question:
                print("⚠️  Please enter a valid question.\n")
                continue
            
            print("\n🔍 Searching through reviews...")
            
            # Retrieve relevant reviews
            reviews = retriever.invoke(question)
            
            if not reviews:
                print("❌ No relevant reviews found for your question.")
                continue
            
            print(f"📚 Found {len(reviews)} relevant review(s)\n")
            print("🤖 Generating answer...\n")
            print("-" * 60)
            
            # Format reviews for the prompt
            formatted_reviews = format_reviews(reviews)
            
            # Generate answer
            result = chain.invoke({
                "reviews": formatted_reviews,
                "question": question
            })
            
            print("💬 Answer:")
            print(result)
            print()
            
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"\n❌ An error occurred: {e}")
            print("Please try again or type 'q' to quit.\n")

if __name__ == "__main__":
    main()