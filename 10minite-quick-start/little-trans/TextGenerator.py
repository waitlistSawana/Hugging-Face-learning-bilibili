from transformers import pipeline

module_id = "distilgpt2"
generator = pipeline("text-generation", model=module_id)
res = generator(
    "I love this course, we will knowlege about HuggingFace.",
    max_length = 30,
    num_return_sequences=2
)

print(res)

'''
文本生成器
'''