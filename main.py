def main():
  book_path = "books/frankenstein.txt"
  text = get_book_text(book_path)
  word_count = get_word_count(text)
  letter_count = get_letter_count(text)
  book_report(word_count, letter_count)

def get_book_text(path):
  with open(path) as f:
    return f.read()

def get_word_count(text):
  words = text.split()
  return len(words)

def get_letter_count(text):
  letter_dictionary = {}
  lower_text = text.lower()
  for letter in lower_text:
    if letter in letter_dictionary:
      letter_dictionary[letter] += 1
    else:
      letter_dictionary.update({letter: 1})
  return letter_dictionary

def book_report(word_count, letter_count):
  print("--- Begin report of books/frankenstein.txt ---")
  print(f"{word_count} words found in the document")
  print("")
  letter_list = list(letter_count.items())
  letter_list.sort(reverse=True, key=lambda letter: letter[1])
  for i in range(0, len(letter_list)):
    letter = letter_list[i]
    if letter[0].isalpha():
      print(f"The {letter[0]} character was found {letter[1]} times")
  print("--- End Report ---")

main()