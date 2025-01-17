def find_anagram(words, string):
  """
  Finds the word whose anagram is present in the given string.

  Args:
    words: A list of words.
    string: The string to search in.

  Returns:
    The word whose anagram is present in the string, or None if no such word is found.
  """
  def sorted_word(word):
    return ''.join(sorted(word))
    
  print(sorted_word(string))  

  sorted_words={sorted_word(word):word for word in words}

  for word in words:
    word_length= len(word)
    for i in range(len(string)- word_length+1):
      substr=string[i:i+word_length]
      print(substr)
      if sorted_word(substr) in sorted_words:
        return sorted_words[sorted_word(substr)]

  return None  


def find_anagram_no_counter(words, string):
    def is_anagram(word, string):
        char_count = {}
        for char in word:
            char_count[char] = char_count.get(char, 0) + 1

        for char in string:
            if char in char_count:
                char_count[char] -= 1
                if char_count[char] == 0:
                    del char_count[char]

        return len(char_count) == 0

    for word in words:
        if is_anagram(word, string):
            return word

    return None
from collections import Counter

def find_anagram2(words, string):
    string_counter = Counter(string)

    print(string_counter)

    for word in words:
        word_counter = Counter(word)
        if all(string_counter[char] >= word_counter[char] for char in word_counter):
            return word

    return None

# Example usage
words = ["cat", "baby", "bird", "fruit"]
string1 = "tacjbcebef"
string2 = "bacdrigb"

answer1 = find_anagram2(words, string1)
answer2 = find_anagram2(words, string2)

print(f"String1: {string1}, Answer: {answer1}")
print(f"String2: {string2}, Answer: {answer2}")