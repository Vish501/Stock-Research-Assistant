from src.helper import llm_construct, embeddings_construct, data_loader, retrieval_construct 

print("loading llm...")

llm = llm_construct()

print("loading embeddings...")
embeddings = embeddings_construct()

print("Loading urls...")

urls = [
    "https://www.moneycontrol.com/news/business/markets/wall-street-rises-as-tesla-soars-on-ai-optimism-11351111.html",
    "https://www.moneycontrol.com/news/business/tata-motors-launches-punch-icng-price-starts-at-rs-7-1-lakh-11098751.html"
]

print("Loading index...")
vector_index = data_loader(urls, embeddings)

print("Loading chain...")
chain = retrieval_construct(llm, vector_index)

query = input(f'What is the question? ')

query_result = chain({"question": query})

print(query_result)
