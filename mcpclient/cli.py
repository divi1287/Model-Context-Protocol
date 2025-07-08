import requests

while True:
    prompt = input("Enter your code prompt (or 'exit'): ")
    if prompt.lower() == "exit":
        break
    res = requests.post("http://localhost:8000/query", json={"query": prompt})
    print("Generated Code:\n", res.json()["code"])
