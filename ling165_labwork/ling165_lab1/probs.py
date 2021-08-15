# Ling 165 Lab 1 kwiseth Feb and Mar... and April 2013
# probs.py
# Methods to calculate expected frequency
# based on probabilities using three different
# smoothing algorithms.
# Was considering using default values (for dictionaries)
# in method signatures, but perhaps that would be
# overkill, since we only need 10 sets of numbers?

def get_mle (bigram, train_dict, train_n_tokens, test_n_tokens):
    
    if bigram in train_dict:
        train_ct = train_dict[bigram]
        mle_prob = float(train_ct)/float(train_n_tokens)
        exp_f_mle = float(mle_prob) * float(test_n_tokens)
    else:
        exp_f_mle = 0
    return exp_f_mle


def get_one (bigram, train_dict, vocab_types, train_n_tokens, test_n_tokens):
    if bigram in train_dict:
        train_ct = train_dict[bigram]
    else:
        train_ct = 0
    one_prob = float(train_ct + 1)/(float(train_n_tokens) + (vocab_types**2))
    exp_f_one = float(one_prob) * float(test_n_tokens)
    return exp_f_one


def get_sgt (bigram, train_dict, train_n_tokens, train_n_types, train_hapax, vocab_types, adj_freq_dict, test_n_tokens):
    if bigram in train_dict:
        sgt_prob = adj_freq_dict[bigram]/train_n_tokens
    else:
        sgt_prob = train_hapax/((vocab_types**2)-train_n_types)*train_n_tokens

    exp_f_sgt = sgt_prob * test_n_tokens
    return exp_f_sgt
