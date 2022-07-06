string = "this is text, that contain latin letters"
vowels = "AaEeIiOoUuYy"
def fnd(string, vowels):
    final = [each for each in string if each in vowels]
    final.sort()
    print(string)
    print('Знайдено голосних букв:', len(final), final)
    print(*final, sep='\n')
fnd(string, vowels)
