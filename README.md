# 📝 Text Summarization Script

This repository provides a simple yet effective Python script to perform automatic text summarization using state-of-the-art transformer models from HuggingFace 🤗. It is designed for developers and researchers who want a quick way to generate concise summaries of large text files without needing to work inside a Jupyter Notebook environment.

---

## 🚀 Features

- 🔍 Supports long input text with automatic chunking
- 🧠 Uses `facebook/bart-large-cnn` transformer model for summarization
- 🗃️ Saves output summaries to a separate file for review
- 🧪 Minimal setup, ready-to-run with only a few dependencies



## 🗂️ Project Structure

---

.
├── src/
│   └── summarize.py           # Metin özetleme işlemini yapan Python betiği
├── data/
│   └── text.txt               # Özetlenecek giriş metni
├── outputs/
│   └── summary_output.txt     # Oluşturulan özet bu dosyaya yazılır
├── requirements.txt           # Bağımlılıkları tanımlayan dosya
└── README.md                  # Proje açıklaması (bu dosya)


---

## ⚙️ Installation

1. Clone the repository:
git clone https://github.com/your-username/text-summarization-script-only.git
cd text-summarization-script-only

2. Install dependencies:
pip install -r requirements.txt

---

## 📌 Usage

Run the summarization script:

python src/summarize.py

The summarized output will be saved to:
outputs/summary_output.txt

---

## 🤖 Model Information

By default, this script uses the `facebook/bart-large-cnn` model, which is highly effective for general-purpose summarization tasks. You can replace this model with any compatible summarization model from HuggingFace by changing the `pipeline` instantiation in `summarize.py`.

---

## 📎 Example

Input (data/text.txt):
Machine learning is a field of computer science that gives computers the ability to learn without being explicitly programmed...

Output (outputs/summary_output.txt):
Machine learning allows computers to learn automatically without being explicitly programmed.


## 🙌 Acknowledgements

- HuggingFace Transformers: https://huggingface.co/transformers/
- PyTorch: https://pytorch.org/
