from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(model='gemini-pro')

with open('demo.txt', 'r') as f:
    context = f.read()


result = llm.invoke(f'Based on following context answer this question what metallic and nonmetallic minerals. \n{context}')

print(result.content)