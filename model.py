from transformers import pipeline
classifier = pipeline("zero-shot-classification",model="facebook/bart-large-mnli")


# Read website content
with open("markdown4.txt", "r", encoding="utf-8") as f:
    website_content = f.read()

sequence_to_classify = website_content
candidate_labels = ['Digital Marketing Agency','Not a Digital Marketing Agency']
output = classifier(sequence_to_classify, candidate_labels)

print(output)
