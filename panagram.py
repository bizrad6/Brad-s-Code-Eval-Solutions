import string

def panagram(sentence):
    chars_seen = set()
    for c in sentence:
        if c.isalpha():
            chars_seen.add(c.lower())

    if len(chars_seen) < len(string.ascii_lowercase):
        response = ''
        for c in string.ascii_lowercase:
            if not c in chars_seen:
                response = response + c
        print response
    else:
        print 'NULL'

if __name__ == '__main__':
    test_cases = [
        'A slow yellow fox crawls under the proactive dog',
        'A quick brown fox jumps over the lazy dog',
    ]
    for test in test_cases:
        chars_seen = set()
        if test:
            chars_seen.clear()
            for c in test:
                if c.isalpha():
                    chars_seen.add(c.lower())
        
            if len(chars_seen) < len(string.ascii_lowercase):
                response = ''
                for c in string.ascii_lowercase:
                    if not c in chars_seen:
                        response = response + c
                print response
            else:
                print 'NULL'
    
    
