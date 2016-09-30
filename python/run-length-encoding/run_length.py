#perform run-length encoding:

#```
#"WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB"  ->  "12WB12W3B24WB"
#```
#
#RLE allows the original data to be perfectly reconstructed from
#the compressed data, which makes it a lossless data compression.
#
#```
#"AABCCCDEEEE"  ->  "2AB3CD4E"  ->  "AABCCCDEEEE"
from __future__ import unicode_literals
import re


def rle_decode_split(input_string):
    return filter(None,re.split(u'(\d+\D)',input_string,flags=re.UNICODE))

def rle_decode_subsplit(input_string):
    return filter(None,re.split(u'(\d+)(\D)',input_string,flags=re.UNICODE))

def encode(input_string):
    output_string = ''
    current_char = input_string[0]
    current_count = 0
    for char in input_string:
        if char == current_char:
            current_count += 1
        else: #we found a new character
            #join the count and char
            if current_count > 1:
                output_string += str(current_count)
            output_string += current_char
            #change the current_char and current_count:
            current_char = char
            current_count = 1
    if current_count > 1:
        output_string += str(current_count)
    output_string += current_char
    return output_string

def decode(input_string):
    output_string = ''
    subs_list = [rle_decode_subsplit(elem) for elem in rle_decode_split(input_string)]
    for sub in subs_list:
        if len(sub) == 1:
            output_string += sub[0]
        else:
            for i in range(int(sub[0])):
                output_string += sub[1]
    return output_string
