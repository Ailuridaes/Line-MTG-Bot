class Ruling(object):
    def __init__(self, cardname, response_dict={}):
        self.cardname = cardname
        self.id = response_dict.get('oracle_id')
        self.source = _get_source_text(response_dict.get('source'))
        self.date = response_dict.get('published_at').replace('-', '/')
        self.text = response_dict.get('comment')

def _get_source_text(str):
    if(str == 'wotc'):
        return 'WotC'
    elif(str == 'scryfall'):
        return 'Scryfall'
    else:
        return str
        