'''
Created on Nov 20, 2014

@author: Hugohrosa
'''

class player(object):
    '''
    classdocs
    '''

    def __init__(self, p):
        self.name = p['name']
        self.age = p['age']
        self.hand = p['hand'] # True is right False is left
        ''' Skills range from 0-200 '''
        ''' technical '''
        self.forehand = p['forehand']
        self.backhand = p['backhand']
        self.serve = p['serve']
        self.volley = p['volley']
        self.smash = p['smash']
        self.drop_shot = p['drop_shot']
        self.passing_shot = p['passing_shot']
        ''' tactical '''
        self.cleverness = p['cleverness']
        self.anticipation = p['anticipation']
        self.creativity = p['creativity']
        ''' physical '''
        self.speed = p['speed']
        self.strength = p['strength']
        self.stamina = p['stamina']
        self.injury = p['injury']
        
    def avg_skill(self):
        sum = self.forehand + self.backhand + self.volley + self.serve + self.smash + self.passing_shot + self.drop_shot + self.cleverness + self.anticipation + self.creativity + self.speed + self.strength + self.stamina + self.injury
        return sum / (self.__sizeof__()-3)
         
        