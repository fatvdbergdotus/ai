import ollama
output = ollama.generate(model="llama3", prompt="Write me a story on once upon a time there was a boy")
print(output["response"])
