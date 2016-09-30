#a scrabble scorer

#listing scores as tuples of score and string,
#then feeding into dict comprehension for easy changing of scores and/or alphabet
scores =   [(1, 'aeioulnrst'),(2, 'dg'),(3,'bcmp'),
            (4,'fhvwy'),(5,'k'),(8,'jx'),(10,'qz')]
score_map = {letter: score for score, letters in scores for letter in letters}
modifier = {'dletter':2,'tletter':3,'dword':2,'tword':3}

#for giving word/letter bonus, syntax is mod=['modname',pos]
#modnames are: 'dletter', 'tletter', 'dword', 'tword'
#if mod is for letter, pos is index of affected letter, else -1 (for word bonus)
#e.g. double letter score on the third letter would be ['dletter',2]
#triple word score would be ['tword',-1]
def score(word,mod=None):
    pos = None
    if not word.isalpha():
        return 0
    if mod is not None:
        pos = mod[1]
    wordscore = [score_map[letter] for letter in word.lower()]
    if pos > -1:
        wordscore[pos] *= modifier[mod[0]]
        return sum(wordscore)
    elif pos == -1:
        return sum(wordscore)*modifier[mod[0]]
    else:
        return sum(wordscore)
