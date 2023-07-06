# words = open('words.txt', mode='w')

# LINES=['cat','dog','bird','moose','camel','donkey','elephant','frog','fox','hourse','lion']

# words.writelines(LINES)
# words.close()

import json
def word_creator(LINES):
    objects = []
    for line in LINES:
      obj = {'word': line}
      objects.append(obj)

    with open('words.json', 'w') as file:
      json.dump(objects, file, indent=4)
