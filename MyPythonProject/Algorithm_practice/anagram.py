"""
File: anagram.py
Name: Shane
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm
from campy.gui.events.timer import pause

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop


def main():
    """
    In this program, user gives an input string. The program will find
    all the anagrams for the word.
    """
    print('Welcome to stanCode "Anagram Generator" (or -1 to quit)')

    while True:
        word = input('Find anagram for: ')
        start = time.time()
        if word == EXIT:
            break
        ans_list = list(find_anagrams(word))
        print(f'{len(ans_list)} anagram: {ans_list}')
        end = time.time()
        print('----------------------------------')
        print(f'The speed of your anagram algorithm: {end-start} seconds.')


def read_dictionary():
    """In this program, loop over the FILE, and make all the words in the file into a Python list"""
    w_lst = []
    prefix_set = set()
    with open(FILE, 'r') as f:
        for line in f:
            word = line.strip()
            w_lst.append(word)
            # Create all the possibility starting charactor into a dictionary
            for i in range(len(word)):
                prefix_set.add(word[:i+1])
    return w_lst, prefix_set


def find_anagrams(s):
    """
    :param s: a string, a user input word
    :return: ans_lst, a python list with all the word found in the dictionary
    """
    w_lst, prefix_set = read_dictionary()
    ch_lst = []
    ans_lst = []
    # create a charactor list for the word
    for i in range(len(s)):
        ch_lst.append(s[i])
    ans_lst = find_anagrams_helper(s, [], w_lst, prefix_set, ch_lst, set(), [True])
    return ans_lst


def find_anagrams_helper(s, cur_ch_lst, w_lst, prefix_set, ch_lst, ans_set, switch):
    """
    :param s: a string, a user input word
    :param cur_ch_lst: a python list, one of combination of charactor from s
    :param w_lst: a python list, all the words in the dictionary
    :param prefix_set: a python dictionary, store all the starting charactor combinations
    :param ch_lst: a python list, all the charactor from s
    :param ans_set: a python dictionary, all the possibility from combinations of charactor of s
    :param switch: a bool
    :return: ans_lst
    """
    if len(ch_lst) == 0:

        # for ch in cur_ch_lst:
        #     ans += ch
        ans = ''.join(cur_ch_lst)
        # Check if ans in lst
        if ans in w_lst:
            print(f'Found: {ans}')
            ans_set.add(ans)
            switch[0] = True
    else:
        used = set()
        for i in range(len(ch_lst)):
            if switch[0]:
                print('Searching...')
                switch[0] = False
            if ch_lst[i] in used:       # if repeating charactor shows, jump right into the next charactor(the next i)
                continue                # This is to avoid reputation word
            used.add(ch_lst[i])
            # Choose
            cur_ch_lst.append(ch_lst[i])
            ch_lst.pop(i)
            sub_s = ''.join(cur_ch_lst)
            if has_prefix(sub_s, prefix_set):
                # Explore
                find_anagrams_helper(s, cur_ch_lst, w_lst, prefix_set, ch_lst, ans_set, switch)
            # Un-choose
            popped_ch = cur_ch_lst.pop()
            ch_lst.insert(i, popped_ch)

    return ans_set


def has_prefix(sub_s, prefix_set):
    """
    :param sub_s: a string
    :param prefix_set: a python dictionary
    :return: bool
    """
    return sub_s in prefix_set


if __name__ == '__main__':
    main()
