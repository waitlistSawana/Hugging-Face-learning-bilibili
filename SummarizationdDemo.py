
model_id = "facebook/bart-large-cnn"

content = """
The explosion of consumer-facing tools that offer generative AI has created plenty of debate: These tools promise to transform the ways in which we live and work while also raising fundamental questions about how we can adapt to a world in which they're extensively used for just about anything.
As with any new technology riding a wave of initial popularity and interest, it pays to be careful in the way you use these AI generators and bots—in particular, in how much privacy and security you're giving up in return for being able to use them.
It's worth putting some guardrails in place right at the start of your journey with these tools, or indeed deciding not to deal with them at all, based on how your data is collected and processed. Here's what you need to look out for and the ways in which you can get some control back.
"""

from transformers import pipeline
pipeline = pipeline("summarization", model=model_id)

output = pipeline(content)

print(output)

'''
link to 'hg_01_get_started.ipynb'
- 用于总结文字的内容
- 可以用于：
    - 总结B站的字幕文件
'''