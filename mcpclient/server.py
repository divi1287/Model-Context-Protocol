from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

app = FastAPI()

# Enable CORS for client
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class Query(BaseModel):
    query: str
    language: str = "python"

# Load a better model
model_id = "Salesforce/codegen-350M-multi"  # small and works well
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id)
generator = pipeline("text-generation", model=model, tokenizer=tokenizer)

@app.post("/query")
async def generate_code(query: Query):
    prompt = f"'''{query.language}\n{query.query}\n'''\n"
    result = generator(prompt, max_new_tokens=128, do_sample=False)
    return {"code": result[0]["generated_text"].replace(prompt, "").strip()}
