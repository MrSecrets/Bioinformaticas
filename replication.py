def SymbolArray(Genome, symbol):
    array = {}
    n = len(Genome)
    ExtendedGenome = Genome + Genome[0:n//2]
    for i in range(n):
        array[i] = PatternCount(symbol, ExtendedGenome[i:i+(n//2)])
    return array

def FasterSymbolArray(Genome, symbol):
    array = {}
    n = len(Genome)
    ExtendedGenome = Genome + Genome[0:n//2]
    # look at the first half of Genome to compute first array value
    array[0] = PatternCount(symbol, Genome[0:n//2])
    for i in range(1, n):
        # start by setting the current array value equal to the previous array value
        array[i] = array[i-1]
        # the current array value can differ from the previous array value by at most 1
        if ExtendedGenome[i-1] == symbol:
            array[i] = array[i]-1
        if ExtendedGenome[i+(n//2)-1] == symbol:
            array[i] = array[i]+1
    return array

def SkewArray(Genome):
    Skew = [0]
    Value = {'C': -1, 'G': 1, 'A': 0, 'T': 0}
    for i in range(1, len(Genome)+1):
            Skew.append(Value[Genome[i-1]] + Skew[i-1])
    return Skew

def MinimumSkew(Genome):
    skew = SkewArray(Genome)
    return [i for i in range(len(skew)) if skew[i] == min(skew)]
