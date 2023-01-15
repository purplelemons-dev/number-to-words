
magnitude_translations ={
    100: 'hundred',
    1000: 'thousand',
    1000000: 'million',
    1000000000: 'billion',
    1000000000000: 'trillion',
    1000000000000000: 'quadrillion',
    1000000000000000000: 'quintillion',
    1000000000000000000000: 'sextillion',
    1000000000000000000000000: 'septillion'
    # TODO: turn into a function that dynamically generates the prefix before -illion
}

def numtoword(num):
    """Converts a number to a word representation"""
    if num == 0:
        return 'zero'
    elif num < 0:
        return 'negative ' + numtoword(-num)
    elif num < 20:
        return ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen'][num - 1]
    elif num < 100:
        return ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety'][num // 10 - 2] + ('-' + numtoword(num % 10) if num % 10 else '')
    elif num < 1000:
        return numtoword(num // 100) + ' hundred and' + (' ' + numtoword(num % 100) if num % 100 else '')
    else:
        for magnitude in sorted(magnitude_translations.keys(), reverse=True):
            if num >= magnitude:
                return numtoword(num // magnitude) + ' ' + magnitude_translations[magnitude] + (' ' + numtoword(num % magnitude) if num % magnitude else '')
        raise ValueError('Number too large')

if __name__ == '__main__':
    import sys
    if len(sys.argv) == 2:
        print(numtoword(int(sys.argv[1])))
    else:
        print('Usage: %s <number>' % sys.argv[0])
