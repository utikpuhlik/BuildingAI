import math
from collections import defaultdict

text = '''Humpty Dumpty sat on a wall
Humpty Dumpty had a great fall
all the king's horses and all the king's men
couldn't put Humpty together again'''


def main(text):
    import math
    from collections import defaultdict

    # 1. split the text into words, and get a list of unique words that appear in it
    docs = [line.lower().split() for line in text.split('\n')]
    unique_words = set(word for line in docs for word in line)

    # 2. go over each unique word and calculate its term frequency, and its document frequency
    term_frequencies = [defaultdict(int) for _ in docs]
    document_frequencies = defaultdict(int)

    for i, line in enumerate(docs):
        for word in line:
            term_frequencies[i][word] += 1
            document_frequencies[word] += 1

    # 3. calculate the TF-IDF representations for each line in the text
    tf_idf = []
    for i, line in enumerate(docs):
        line_tf_idf = []
        for word in unique_words:
            tf = term_frequencies[i][word]
            idf = math.log(len(docs) / document_frequencies[word])
            line_tf_idf.append(tf * idf)
        tf_idf.append(line_tf_idf)

    # 4. calculate the distances between each line to find which are the closest
    def cosine_similarity(a, b):
        dot_product = sum(x * y for x, y in zip(a, b))
        norm_a = math.sqrt(sum(x * x for x in a))
        norm_b = math.sqrt(sum(y * y for y in b))
        return dot_product / (norm_a * norm_b)

    similarities = []
    for i in range(len(tf_idf)):
        for j in range(i + 1, len(tf_idf)):
            similarities.append((i, j, cosine_similarity(tf_idf[i], tf_idf[j])))

    closest_lines = sorted(similarities, key=lambda x: x[2], reverse=True)[:1]
    a = [tuple(sorted((line[0], line[1]))) for line in closest_lines]
    print(a[0])

main(text)