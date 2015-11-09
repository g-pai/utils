#!/usr/bin/python

import os, sys

def anagram(s1, s2):
	if len(s1) != len(s2):
		print "No anagram: s1=%s s2=%2", s1, s2
		answer = False
		return answer
	answer = True
	l_s = len(s1)
	i = 0
	hash_bucket = {}
	while ( i < l_s):
		if s1[i] in hash_bucket:
			hash_bucket[s1[i]] = hash_bucket[s1[i]] + 1
		else:
			hash_bucket[s1[i]] = 1
		i = i + 1
	i = 0
	while ( i < l_s ):
		if s2[i] in hash_bucket:
			hash_bucket[s2[i]] = hash_bucket[s2[i]] - 1
		else:
			answer = False
			break
		i = i + 1
	i = 0
	while ( i < l_s ):
		if (hash_bucket[s2[i]] != 0):
			answer = False
			break
		i = i + 1
	return answer
		

if len(sys.argv) >= 2:
	if anagram(sys.argv[1], sys.argv[2]):
		print "Found anagrams"
	else:
		print "No anagrams"
sys.exit()

