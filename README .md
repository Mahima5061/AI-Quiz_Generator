# AI-Based Quiz Generator

An AI-powered Quiz Generator that automatically generates 10 MCQ questions from any given text using Natural Language Processing (NLP), with questions progressively increasing in difficulty.

## About the Project

Creating quiz questions manually takes a lot of time. This project solves that by automatically generating 10 MCQ questions from any text — starting from Easy and gradually increasing to Hard.

## Features

- Accepts any text as input
- Automatically generates 10 MCQ questions
- Each question has 4 options (1 correct + 3 wrong)
- Difficulty increases question by question:
  - 🟢 Q1–Q3 : Easy
  - 🟡 Q4–Q7 : Medium
  - 🔴 Q8–Q10 : Hard
- Two modes — Quiz mode and View answers mode
- Shows final score with performance feedback

## Technologies Used

- Python
- NLTK (Natural Language Toolkit)
- NLP Concepts — Tokenization, POS Tagging, Keyword Extraction, Sentence Complexity Analysis

## How to Run

1. Install required library:
```
pip install nltk
```

2. Run the program:
```
python quiz_generator.py
```

3. Paste your text and press ENTER twice
4. Choose Mode 1 (Quiz) or Mode 2 (View answers)

## Project Type

Solo Academic Project

## Author

Mahima
