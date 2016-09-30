
def verse(n):
    """Returns nth verse of the nursery rhyme
    The house that Jack Built
    """
    verse_string = ['This is ' + verse_line[n][1]]
    for i in range(n-1,-1,-1):
        verse_string.append(''.join(verse_line[i]))
    return '\n'.join(verse_string)
def rhyme():
    """Returns the full nursery rhyme"""
    rhyme_string = [verse(n) for n in range(12)]
    return '\n\n'.join(rhyme_string)

verse_line = {0: ['that lay in ','the house that Jack built.'],
              1: ['that ate ', 'the malt'],
              2: ['that killed ','the rat'],
              3: ['that worried ','the cat'],
              4: ['that tossed ','the dog'],
              5: ['that milked ','the cow with the crumpled horn'],
              6: ['that kissed ','the maiden all forlorn'],
              7: ['that married ','the man all tattered and torn'],
              8: ['that woke ','the priest all shaven and shorn'],
              9: ['that kept ','the rooster that crowed in the morn'],
              10: ['that belonged to ','the farmer sowing his corn'],
              11: ['','the horse and the hound and the horn']}
