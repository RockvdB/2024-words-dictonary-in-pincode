################################################################################
# Description: open een gewone tekst file cryptiony.txt. vertalen naar:
#                     ########################################
#                     ###           24 random woorden      ###
#                     ########################################
# Purpose:     Print een type:dict op het scherm van source seed phrase words.txt
# Author:      Rick van den Berg
# Version:     0.01
################################################################################
################################################################################
# Parameters:
# none
# input:
#       source seed phrase words.txt
# Versie 0.1
#
################################################################################

#fo = open("foo.txt", "r+")
#str = fo.read(10)
#print "Read String is : ", str
#
## Check current position
#position = fo.tell()
#print "Current file position : ", position
#
## Reposition pointer at the beginning once again
#position = fo.seek(0, 0);
#str = fo.read(10)
#print "Again read String is : ", str
## Close opend file
#fo.close()

import random
import string

f = open('source seed phrase words.txt', 'r', encoding="Latin-1")

read_data = f.read()
position = f.seek(0, 0);
oneword = ''
cartel = 0
c = 0

for line in f:
    per_word = read_data.split()

    # met rjust () < br /> # voorloopnul toevoegen
    nummer = str(c+1)
    if len(nummer) == 3:
        res = nummer.rjust (1 + len(nummer), '0' ) 
        nummer = res
    elif len(nummer) == 2:
        res = nummer.rjust (2 + len(nummer), '0' ) 
        nummer = res
    elif len(nummer) == 1:
        res = nummer.rjust (3 + len(nummer), '0' ) 
        nummer = res
    #else:
        #print('niets')

    # format van 1 oneword:  (c+1 , ": '" , per_word[c] , "', ")
    oneword =  ( nummer + ": '" + per_word[c] + "', ")
    cartel += len(oneword)
    if cartel < 80:
        print(oneword,end='')        
        #print(type(oneword), oneword) 
    else:
        # add end-of-line.
        print(oneword)
        cartel = 0
    c += 1
f.close()

#print('1e woord ', per_word[0])
#print('laatste woord ', per_word[2047])

##position = f.seek(0, 0);
##d = 1
##for line0 in f:
##    print('nr0:', d, line0, end ='')
##    d += 1


###lines = f.readlines()
###position = f.seek(0, 0);
###e = 1
###for line1 in lines:
###    print('nr1:', e, line1, end ="")
###    e += 1


####position = f.seek(0, 0);
####x = 0
####for x in per_word:
####    print(x, " is ", per_word[x])
####    x += 1