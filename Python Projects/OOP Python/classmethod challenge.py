class Letter:
    def __init__(self, pattern=None):
        self.pattern = pattern
      
    def __iter__(self):
        yield from self.pattern
      
    def __str__(self):
        output = []
        for blip in self:
            if blip == '.':
                output.append('dot')
            else:
                output.append('dash')
        return '-'.join(output)
    @classmethod
    def from_string(cls, something):
        cool_string = something.split('-')
        nice_string = []
        for x in cool_string:
            if x == 'dash':
                nice_string.append('_')
            else:
                nice_string.append('.')
        cls.pattern = nice_string
        return cls(pattern = nice_string)
    

class S(Letter):
    def __init__(self):
         pattern = ['.', '.', '.']
         super().__init__(pattern)
         
answer = Letter.from_string('dot-dot-dash-dot-dash')
print(answer.pattern)