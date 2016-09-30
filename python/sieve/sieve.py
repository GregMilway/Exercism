#create a sieve of Eratosthenes

def sieve(limit):
    #setup variables:
    cands = range(2,limit+1)    #candidates for prime-hood
    cand_len = len(cands)       #number of candidates to check
    comps = [0]*cand_len        #track if candidate is composite (not prime)

    for i in range(cand_len):
        if not comps[i]:        #not already been marked composite (so should be prime)
            step = cands[i]
            for j in range(i+step,cand_len,step):
                comps[j] = 1

    return [cands[idx] for idx, val in enumerate(comps) if not val]
