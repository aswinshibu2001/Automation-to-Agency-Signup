from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# # Load GPT-2 model and tokenizer
# model_name = "gpt2"
# model = AutoModelForCausalLM.from_pretrained(model_name)
# tokenizer = AutoTokenizer.from_pretrained(model_name)

# Load model directly
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B")
model = AutoModelForCausalLM.from_pretrained("deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B")


# Read website content
with open("markdown1.txt", "r", encoding="utf-8") as f:
    website_content = f.read()

prompt = f"""
Analyze the following website content and determine if it belongs to a Digital Marketing Agency.

Look for these keywords: Services, Web Design, Web Development, SEO Agency, Ads Agency, Digital Marketing Agency, Agency, Website Creation.

If ALL keywords appear multiple times then classify it as **"Digital Marketing Agency"**.
Otherwise classify it as **"Not a Digital Marketing Agency"**
No explanations.



Website Content:
{website_content[:1000]}  # Limit text length to fit token limit

Final Answer:

"""
#Final Answer (ONLY output "Digital Marketing Agency" or "Not a Digital Marketing Agency")
# **🔹 Tokenize input**
inputs = tokenizer(prompt, return_tensors="pt")

# **🔹 Generate response from the model**
output = model.generate(**inputs)

# **🔹 Decode generated text**
response = tokenizer.decode(output[0], skip_special_tokens=True)

# Extract only the classification result

# print("Final Classification:", final_output)

lines = [line.strip() for line in response.split("\n") if line.strip()]

# Get the last non-empty line
if lines:
    final_output = lines[-1]  # Last valid sentence
else:
    final_output = "No classification result found."

# print("Final Classification:", final_output)

print(response)

