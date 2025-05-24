from transformers import pipeline
import os

# Read input text
with open("data/text.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Split text into manageable chunks
def chunk_text(text, max_tokens=1000):
    sentences = text.split('. ')
    chunks, chunk = [], ""
    for sentence in sentences:
        if len(chunk + sentence) < max_tokens:
            chunk += sentence + '. '
        else:
            chunks.append(chunk.strip())
            chunk = sentence + '. '
    chunks.append(chunk.strip())
    return chunks

chunks = chunk_text(text)

# Initialize summarizer
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Generate summaries
summaries = [summarizer(chunk, max_length=120, min_length=30, do_sample=False)[0]['summary_text'] for chunk in chunks]
final_summary = ' '.join(summaries)

# Save to file
os.makedirs("outputs", exist_ok=True)
with open("outputs/summary_output.txt", "w", encoding="utf-8") as f:
    f.write(final_summary)