#!/usr/bin/env python
# coding: utf-8

# Name:
# Email:
# 
# ## Write the Comprehensions that answer the following questions
# 
# - Test your comprehensions thoroughly! We want to see your tests and results.

# ### 1.
# 
# Use a comprehension to filter invalid bases (not ATGC) from a sequence

# In[15]:


seq = "ATGNAZCGA"
# results should be ATGACGA
valid_seq = [base for base in seq if base in "ATCG"]
result = ''.join(valid_seq)
print(result)


# ## 2.
# 
# Given a dictionary of headers and sequences, for example
# `d1 = {'seq1':"ATCGA", 'seq2':"GCAGTA", 'seq3':"GCGCGCCGCGCTGACATCGA"}`
# Build a generator comprehension that will yield sequences longer than a certain number
# 

# In[14]:


d1 = {'seq1':"ATCGA", 'seq2':"GCAGTA", 'seq3':"GCGCGCCGCGCTGACATCGA"}
min_seq_length=5
filtered_sequences = (sequence for sequence in d1.values() if len(sequence)>min_seq_length)
for sequence in filtered_sequences:
    print(sequence)


# ## 3.
# 
# Given a dictionary of headers and sequences, for example
# `d1 = {'seq1':"ATCGA", 'seq2':"GCAGTA", 'seq3':"GCGCGCCGCGCTGACATCGA"}`
# Build a comprehension that will create a list of sequences with GC Content higher than 45%

# In[18]:


d1 = {'seq1': "ATCGA", 'seq2': "GCAGTA", 'seq3': "GCGCGCCGCGCTGACATCGA"}
maxGC = 0.45

def calculate_gc_content(sequence):
    gc = sequence.count('G') + sequence.count('C')
    return gc / len(sequence)

GC = [sequence for sequence in d1.values() if calculate_gc_content(sequence) > maxGC]

print(GC)


# ## 4.
# Given a passage, first create a function that will return the number of unique vowels in a string. Then, create a comprehension that will build a list of words in the passage that contain at least 3 unique vowels

# In[23]:


passage = """Once upon a midnight dreary, while I pondered, weak and weary,
Over many a quaint and curious volume of forgotten lore—
    While I nodded, nearly napping, suddenly there came a tapping,
As of some one gently rapping, rapping at my chamber door. 
“’Tis some visitor,” I muttered, “tapping at my chamber door—
            Only this and nothing more.”"""
def Vowel_max(passage):
    vowels = set("AEIOUaeiou")
    vowel_count = 0
    for char in passage:
        if char in vowels:
            vowel_count +=1
    return vowel_count
Vowel_message=[word for word in passage.split() if Vowel_max(word)>=3]
print(Vowel_message)


# ## 5
# 
# Write a comprehension that will generate the reverse complement of a sequence.
# 
# "ATCGACGA" would be 'TCGTCGAT'

# In[24]:


def DNACOMP(bases):
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    reverse_complement = [complement[base] for base in reversed(bases)]
    return ''.join(reverse_complement)

sequence = "ATCGACGA"
result = DNACOMP(sequence)
print(result)


# In[ ]:




