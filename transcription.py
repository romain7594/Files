#!/usr/bin/env python
#-*- coding: utf-8 -*-

##### Fonction de transcription d'une sequence ADN

def transcription(sequence):
	D = {'A':'T', 'T':'U', 'C':'G', 'G':'C'}
	seq = ""
	
	for i in sequence :
		seq += D[i]
	
	return seq
