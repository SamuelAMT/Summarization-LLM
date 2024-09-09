from transformers import pipeline

summarizer = pipeline("summarization")

article = """
The Apollo program, also known as Project Apollo, was the third United States human spaceflight program carried out by
the National Aeronautics and Space Administration (NASA), which succeeded in landing the first humans on the Moon from 1969 to 1972.
It was first conceived during Dwight D. Eisenhower's administration
"""

summary = summarizer(article, max_length=60, min_length=30, do_sample=False)
print(summary[0]['summary_text'])