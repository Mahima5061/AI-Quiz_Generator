import nltk
import random
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.tag import pos_tag

nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)
nltk.download('averaged_perceptron_tagger', quiet=True)
nltk.download('punkt_tab', quiet=True)

def get_difficulty(question_number):
    if question_number <= 3:
        return "🟢 Easy"
    elif question_number <= 7:
        return "🟡 Medium"
    else:
        return "🔴 Hard"

def get_sentence_complexity(sentence):
    return len(word_tokenize(sentence))

def extract_keywords(text):
    words = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    tagged = pos_tag(words)
    keywords = []
    for word, tag in tagged:
        if tag in ['NN', 'NNS', 'NNP', 'NNPS']:
            if word.lower() not in stop_words and len(word) > 3:
                keywords.append(word)
    return list(set(keywords))

def generate_wrong_options(correct_answer, all_keywords):
    wrong = [k for k in all_keywords if k.lower() != correct_answer.lower()]
    random.shuffle(wrong)
    return wrong[:3]

def generate_mcqs(text, num_questions=10):
    sentences = sent_tokenize(text)
    keywords = extract_keywords(text)

    if len(keywords) < 4:
        print("❌ Text is too short. Please provide more detailed text.")
        return []

    sorted_sentences = sorted(sentences, key=lambda s: get_sentence_complexity(s))
    n = len(sorted_sentences)
    easy_sentences   = sorted_sentences[:n//3] or sorted_sentences
    medium_sentences = sorted_sentences[n//3: 2*n//3] or sorted_sentences
    hard_sentences   = sorted_sentences[2*n//3:] or sorted_sentences

    def make_questions_from(sentence_list, count):
        questions = []
        for sentence in sentence_list:
            if len(questions) >= count:
                break
            tagged = pos_tag(word_tokenize(sentence))
            for word, tag in tagged:
                if tag in ['NN', 'NNS', 'NNP', 'NNPS'] and word in keywords:
                    blank_sentence = sentence.replace(word, "______", 1)
                    wrong_options = generate_wrong_options(word, keywords)
                    if len(wrong_options) < 3:
                        continue
                    options = wrong_options[:3] + [word]
                    random.shuffle(options)
                    correct_letter = ['A', 'B', 'C', 'D'][options.index(word)]
                    questions.append({
                        'question': blank_sentence,
                        'options': options,
                        'answer': word,
                        'answer_letter': correct_letter
                    })
                    break
        return questions

    all_questions = make_questions_from(easy_sentences, 3) + \
                    make_questions_from(medium_sentences, 4) + \
                    make_questions_from(hard_sentences, 3)
    return all_questions[:num_questions]

def display_quiz(questions):
    print("\n" + "="*60)
    print("         AI GENERATED QUIZ")
    print("  Difficulty increases question by question")
    print("="*60)
    score = 0
    for i, q in enumerate(questions, 1):
        print(f"\nQ{i} [{get_difficulty(i)}]: {q['question']}")
        for j, option in enumerate(q['options']):
            print(f"   {['A','B','C','D'][j]}) {option}")
        answer = input("\nYour answer (A/B/C/D): ").strip().upper()
        if answer == q['answer_letter']:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! Correct answer: {q['answer_letter']}) {q['answer']}")
    print("\n" + "="*60)
    print(f"  YOUR SCORE: {score}/{len(questions)}")
    if score == len(questions):   print("  🏆 Perfect Score!")
    elif score >= len(questions)//2: print("  👍 Good Job!")
    else:                          print("  📚 Keep Practicing!")
    print("="*60)

def show_questions_only(questions):
    print("\n" + "="*60)
    print("         AI GENERATED QUIZ")
    print("  Difficulty increases question by question")
    print("="*60)
    for i, q in enumerate(questions, 1):
        print(f"\nQ{i} [{get_difficulty(i)}]: {q['question']}")
        for j, option in enumerate(q['options']):
            print(f"   {['A','B','C','D'][j]}) {option}")
        print(f"   ✅ Answer: {q['answer_letter']}) {q['answer']}")

def main():
    print("="*60)
    print("       AI-BASED QUIZ GENERATOR")
    print("    Powered by NLP (NLTK)")
    print("    Difficulty: Easy → Medium → Hard")
    print("="*60)
    print("\nPaste your text below. Press ENTER twice when done.\n")

    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)

    text = " ".join(lines)
    if not text.strip():
        print("❌ No text provided.")
        return

    print("\n⏳ Generating questions...")
    questions = generate_mcqs(text, num_questions=10)

    if not questions:
        print("❌ Could not generate questions. Please provide more detailed text.")
        return

    print(f"✅ {len(questions)} questions generated!")
    print("   🟢 Q1–Q3  : Easy")
    print("   🟡 Q4–Q7  : Medium")
    print("   🔴 Q8–Q10 : Hard")
    print("\nChoose mode:")
    print("1. Quiz mode (answer and get score)")
    print("2. View questions with answers")
    mode = input("\nEnter 1 or 2: ").strip()

    if mode == "1":
        display_quiz(questions)
    else:
        show_questions_only(questions)

if __name__ == "__main__":
    main()
