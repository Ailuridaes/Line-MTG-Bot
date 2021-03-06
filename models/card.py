class Card(object):
    def __init__(self, response_dict={}):
        self.id = response_dict.get('id')
        self.name = response_dict.get('name')
        self.mana_cost = response_dict.get('mana_cost')
        self.cmc = response_dict.get('cmc')
        self.colors = response_dict.get('colors')
        self.color_identity = response_dict.get('color_identity')
        self.names = response_dict.get('names')
        self.type = response_dict.get('type_line')
        self.power = response_dict.get('power')
        self.toughness = response_dict.get('toughness')
        self.loyalty = response_dict.get('loyalty')
        self.rarity = response_dict.get('rarity')
        self.text = response_dict.get('oracle_text')
        self.flavor = response_dict.get('flavor_text')
        self.layout = response_dict.get('layout')
        self.number = response_dict.get('collector_number')
        self.legalities = response_dict.get('legalities')
        self.is_reprint = response_dict.get('reprint')
        self.artist = response_dict.get('artist')
        self.watermark = response_dict.get('watermark')
        self.border_color = response_dict.get('border_color')
        self.release_date = response_dict.get('released_at')
        self.set = response_dict.get('set')
        self.set_name = response_dict.get('setName')
        self.image_uri = response_dict.get('image_uris').get('normal')
        self.rulings_uri = response_dict.get('rulings_uri')
        self.printings_uri = response_dict.get('prints_search_uri')
