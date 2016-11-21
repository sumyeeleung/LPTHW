def __init__(self):
    self.mapping = {
          'direction':  ['north', 'south', 'east', 'west'],
          'verb':       ['go', 'kill', 'eat'],
          'stop':       ['the', 'in', 'of'],
          'noun':       ['door', 'bear', 'princess', 'cabinet']              }
    self.mapping_categories = self.mapping.keys()

def scan(self, input):
    self.result = []
    for word in input.split():
        try:
            self.result.append(('number', int(word)))
            except ValueError:
            for category, item in self.mapping.items():
                if word.lower() in item:
                    found_category = category
                    break
                else:
                    found_category = 'error'
            self.result.append((found_category, word))

        return self.result
