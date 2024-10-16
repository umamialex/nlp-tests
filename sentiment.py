from transformers import pipeline

classifier = pipeline("sentiment-analysis")

result = classifier("saying goodbye is death by a thousand cuts")
print(result)
