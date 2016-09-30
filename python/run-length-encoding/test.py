
def rle_decode_split(input_string):
    return filter(None,re.split(ur'(\d+\w|\d+\s)',input_string,flags=re.UNICODE))

def rle_decode_subsplit(input_string):
    return filter(None,re.split(ur'(\d+)(\w)|(\d+)(\s)',input_string,flags=re.UNICODE))

somelist = [rle_decode_subsplit(elem) for elem in rle_decode_split(input_string)]
def decode(input_string):
    output_string = ''
    subs_list = [rle_decode_subsplit(elem) for elem in rle_decode_split(input_string)]
    for sub in subs_list:
        if len(sub) == 1:
            output_string += sub[0]
        else:
            output_string += sub[1]*int(sub[0])
    return output_string


u'\u23f03\u26bd2\u2b50\u23f0'
u'\u23f03\u26bd2\u2b50\u23f0'

def decode(input_string):
    input_string = input_string.encode('utf-8')
    output_string = u''
    subs_list = [rle_decode_subsplit(elem) for elem in rle_decode_split(input_string)]
    for sub in subs_list:
        if len(sub) == 1:
            print sub[0].decode('utf-8')
        else:
            for i in range(int(sub[0])):
                print sub[1].decode('utf-8')
#    return output_string
