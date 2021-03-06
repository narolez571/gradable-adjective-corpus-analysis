import string
import random
import math

'''
used for experiment 2
'''

short_list = True
num_stimuli = 100

folder = '../../data/word_sets/kennedy/'
adj_file = folder + 'adj.txt'
mod_file = folder + 'mod.txt'

adjs = [line.rstrip('\n') for line in open(adj_file, 'r').readlines()]
mods = [line.rstrip('\n') for line in open(mod_file, 'r').readlines()]

indices = []
for i in range(0, len(adjs)):
	for j in range(0, len(mods)):
		indices.append([i, j])
		
fout = open('stimuli.js', 'w')
fout_words = open('stimuli.csv', 'w')
fout_indices = open('stimuli_indices.csv', 'w')

all_stimuli = []

random.shuffle(indices)

my_count = 0
for stimuli in indices:
	adj = stimuli[0]
	mod = stimuli[1]
	
	all_stimuli.append('{{"trial": {0}, "isCatch": 0, "phrase": "{1} {2}"}},\n'.format(my_count, mods[mod], adjs[adj]))
	fout_indices.write('{0}, {1}\n'.format(adj + 1, mod + 1))
	fout_words.write('{0}, {1}\n'.format(adjs[adj], mods[mod]))
	my_count += 1

fout_words.close()
fout_indices.close()

stimuliSetSize = len(all_stimuli) / 7
for i in range(7):
	random.shuffle(all_stimuli)
	for j in range(7):
		fout.write('[ //{0}\n'.format(i* 7 + j))
		for k in range(stimuliSetSize):
			fout.write(all_stimuli[j * stimuliSetSize + k])
		fout.write('], \n')
fout.close()
