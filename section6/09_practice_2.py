def animal_crackers(palabra):
  wordlist = palabra.split()
  print(wordlist)

  first = wordlist[0]
  second = wordlist[1]

  return first[0] == second[0]

print(animal_crackers("Spider Llama"))