def analyse(text: str)-> str:
  report = ""
  count_words = len(text.split(" "))
  report += f"O texto tem {count_words} palavras"
  char_counter = dict()
  for char in text:
    if char in char_counter:
      char_counter[char] += 1
    else:
      char_counter[char] = 1
    report += f"\nO caractere '{char}' aparece {char_counter[char]} vezes"  

  return report 
text_to_analyze = "The quick brown fox jumps over the lazy dog"
print(analyse(text_to_analyze))