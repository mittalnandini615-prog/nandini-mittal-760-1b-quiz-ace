# Count top 3 most frequent words in a paragraph

# Step 1: Take input
text = input("Enter a paragraph: ")

# Step 2: Convert to lowercase and split into words
words = text.lower().split()

# Step 3: Remove punctuation
import string
clean_words = []
for w in words:
    clean_words.append(w.strip(string.punctuation))

# Step 4: Count word frequencies (dictionary)
freq_map = {}
for w in clean_words:
    if w in freq_map:
        freq_map[w] += 1
    else:
        freq_map[w] = 1

# Step 5: Sort words by frequency
def sort_by_frequency(item):
    return item[1]   # use the count for sorting

sorted_words = sorted(freq_map.items(), key=sort_by_frequency, reverse=True)

# Step 6: Print top 3 words
print("\nTop 3 most frequent words:")
for word, freq in sorted_words[:3]:
    print(word, ":", freq)