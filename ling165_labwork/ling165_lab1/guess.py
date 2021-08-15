# Ling 165 Lab 1 kwiseth Feb-Mar-Apr 2013
# guess.py
# Uses frequency counts from train.py to estimate expected
# bigram frequencies using three different 
# smoothing algorithms. 
# Reports mean frequencies for F_true = 1 through 10.
# 10-Apr, 11-Apr: Created separate module for functions
# 	calculating the expected frequencies, for easier
#   debugging. 

import sys, pickle
import bigram, probs

sys.path.append('/home/students/ling165/lab1/')
import sgt

# Open the test file and process bigrams.

testfile = open('/home/students/ling165/lab1/data/brown.test', 'r') 
#testfile = open('my.test', 'r')
#testfile = open('my.test.SMALL', 'r')
test_data = testfile.readlines()
testfile.close()

# Create a dictionary to count bigrams in our
# test data with counts. These counts are the
# f_true values.

true_bgm_freq = {}
for line in test_data:
	bigram_list = bigram.get_bigrams(line)
	true_bgm_freq = bigram.update_bigram_counts(bigram_list,true_bgm_freq)

# Let's open the training dictionary for use
# in our estimates. We can also make our adjusted_freq_dict
# at this same time (using Hahn's script) since we have the file open.
# bfd is handle for bigram_freq_dict (bigram frequency dictionary)

bfd = open('bigram_freq.save','r')
bfd_train = pickle.load(bfd)
adjusted_freq_dict = sgt.gt_freq(bfd_train)    # Dictionary of adjusted freqs for sgt
bfd.close()


# Need to get our vocabulary count details, so let's open
# the unigram frequency dictionary we saved.
voc = open('vocab.save','r')
voc_train = pickle.load(voc)
voc.close()


# Let's get all the values we'll need for our various formulae, starting with
# values from our training dictionary, vocabulary, and test dictionary.
# Training Dictionary (total bigrams etc)
train_N_types = len(bfd_train) #N_train
train_N_tokens = sum(bfd_train.values()) 
train_N_hapax = sum(bfd_train[word] for word in bfd_train if bfd_train[word] == 1 ) #hapax bigrams 

# Vocabulary (total word types etc)
train_V_types = len(voc_train.items()) # word types
train_V_tokens = sum(voc_train.values()) # total word tokens
train_V_hapax = sum(voc_train[word] for word in voc_train if voc_train[word] == 1 ) #hapax

# Test data (Dictionary of true values)
test_N_tokens = sum(true_bgm_freq.values())     #N_test

print "F_true\t\tF_mle\t\tF_one\t\tF_sgt"

for tru_freq in range(1, 11):
	bucket = [bigram for bigram, count in true_bgm_freq.iteritems() if count == tru_freq]
	#print bucket
	mle_counts = [probs.get_mle(bigram, bfd_train, train_N_tokens, test_N_tokens) for bigram in bucket]
	one_counts = [probs.get_one(bigram, bfd_train, train_V_types, train_N_tokens, test_N_tokens) for bigram in bucket]
	sgt_counts = [probs.get_sgt(bigram, bfd_train, train_N_tokens, train_N_types, train_N_hapax, train_V_types, adjusted_freq_dict, test_N_tokens) for bigram in bucket]
	print str(tru_freq) + '\t\t' + str(round(sum(mle_counts)/len(mle_counts), 4)) + '\t\t' + str(round(sum(one_counts)/len(one_counts), 4)) \
		  + '\t\t' + str(round(sum(sgt_counts)/len(sgt_counts),4))
	

print "Processing complete."



