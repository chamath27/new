import math

class NucleotideSequence:
    '''A class which defines and methods base_count,gc_content and reverse complement which are inhrited by DNAsequence and RNA sequence'''
    complements = {'G': 'C',
                   'C': 'G',
                   'A': 'T',
                   'T': 'A'}
    valid=set(complements)
    diff=set()
    
    def __init__(self, sequence):
        assert isinstance(sequence, str)
        assert len(sequence) > 0
        sequence = sequence.upper()
        #valid=set(complements)
        diff = set(sequence).difference(self.valid)
        if not diff == set():
            raise Exception('Invalid bases '+ ','.join(diff) + '.the bases can only be one of ' + ','.join(self.valid))
        
        print "sfddf"
        #assert sequence
        self.sequence = sequence
        #assert isinstance(sequence, str)
        self.base_counts = {}
    def base_count(self, base):
        '''
        Given a base returns the number of time the base occurs
        '''
        assert isinstance(self.sequence, str)
        if base in self.base_counts:
            return self.base_counts[base]
        else:
            count = self.sequence.count(base)
            self.base_counts[base] = count
            return count
    
    def gc_content(self):
        '''retruns the proption of G and C bases in the sequence'''
        g = self.base_count('G')
        c = self.base_count('C')
        return float(g+c)/len(self.sequence)
        
    def reverse_complement(self):
        rev_c = ""
        for base in self.sequence:
            rev_c = self.complements[base] + rev_c
            
        return rev_c
        
        
class DNASequence(NucleotideSequence):
    '''inherites methods in NucleotideSequence. Uses the bases GATC'''
    complements = {'G': 'C',
                   'C': 'G',
                   'A': 'T',
                   'T': 'A'}
    pass

    
class RNASequence(NucleotideSequence):
    '''inherites methods in NucleotideSequence. Uses the bases GAUC'''
    complements = {'G': 'C',
                   'C': 'G',
                   'A': 'U',
                   'U': 'A'}

