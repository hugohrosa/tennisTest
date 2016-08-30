'''
Created on Nov 19, 2014

@author: Hugohrosa
'''
from __future__ import division
import random as r

class tennisCourt(object):
    '''
    320
     
    280  _______________
         |             |   
      225|_____________|   
         |      |      |   
         |      |      |   
    160 -----------------
         |      |      |   
      95 |______|_____ |   
         |     61      |   
         |_____________|    
    40  20           102  122
     
     0
    '''
    
    def __init__(self, p1, p2):
        ''' court size x=122, y=320 '''
        self.singles_court = {'horizontal': {'left_line': 20, 'center_serve_line': 61, 'right_line': 102}, 
                              'vertical': {'bottom_baseline': 40, 'bottom_service_line': 95, 'net': 160, 'top_service_line': 225, 'top_baseline': 280},
                              'x_max': 122,
                              'y_max': 320 }
        self.p1 = p1
        self.p2 = p2
        self.top_server_pos = (55,280)
        self.bottom_serve_receiver_pos = (82,40)
        self.bottom_server_pos = (67,40)
        self.top_serve_receiver_pos = (21,280)
        
    def start_rally(self,p_serve, p_response):
        self.serve(p_serve)
        self.response(p_response)
        
        p_hitting = p_response
        p_response = p_serve
        while self.end_point():
            self.hit()
            self.call()
            self.travelling()
            self.bounce()
            
    def end_point(self):
        return True
    
class match(object):
    '''
    classdocs
    '''

    def __init__(self, p1, p2, sets):
        self.p1 = p1
        self.p2 = p2
        self.sets = sets
        self.score = {0:'0', 1:'15', 2:'30', 3:'40'}
        
    def play_match(self):
        sets_played = 0
        p1_sets = 0
        p2_sets = 0
        while self.end_match(p1_sets, p2_sets, self.sets):
            sets_update = self.play_set()
            p1_sets += sets_update[0]
            p2_sets += sets_update[1]
            sets_played += 1
            print '\nSETS SCORE:'
            print self.p1.name+' '+str(p1_sets)
            print self.p2.name+' '+str(p2_sets)
    
    def play_set(self):
        p1_games = 0
        p2_games = 0
        print '\nStarting new set...'
        while self.end_set(p1_games, p2_games):
            games_update = self.play_game()
            p1_games += games_update[0]
            p2_games += games_update[1]
        if p1_games > p2_games:
            return [1,0]
        elif p1_games < p2_games:
            return [0,1]
        elif p1_games == p2_games:
            update_games=self.play_tiebreak()
            p1_games += update_games[0]
            p2_games += update_games[1]
            if p1_games > p2_games:
                self.print_set_score(p1_games, p2_games)
                print self.p1.name + ' wins the set.'
                return [1,0]
            elif p1_games < p2_games:
                self.print_set_score(p1_games, p2_games)
                print self.p2.name + ' wins the set.'
                return [0,1]

    def play_game(self):
        p1_points = 0
        p2_points = 0
        print 'Starting new game...'
        while self.end_game(p1_points, p2_points):
            points_update = self.play_point()
            p1_points += points_update[0]
            p2_points += points_update[1]
        if p1_points > p2_points:
            return [1,0]
        elif p1_points < p2_points:
            return [0,1]
        
    def play_tiebreak(self):
        p1_tb = 0
        p2_tb = 0
        while self.end_tiebreak(p1_tb,p2_tb):
            tiebreak_update = self.play_point()
            p1_tb += tiebreak_update[0]
            p2_tb += tiebreak_update[1]
        if p1_tb > p2_tb:
            return [1,0]
        elif p1_tb < p2_tb:
            return [0,1]
        
    def play_point(self):
        max_range = self.p1.avg_skill() + self.p2.avg_skill()
        point = r.randint(0,max_range)
        if point < self.p1.avg_skill():
            return[1,0]
        else:
            return [0,1]

    def end_match(self, p1_sets, p2_sets, max_sets):
        if p1_sets > p2_sets and float(p1_sets/max_sets) > 0.5:
            print self.p1.name + ' wins the MATCH'
            return False
        elif p1_sets < p2_sets and float(p2_sets/max_sets) > 0.5:
            print self.p2.name + ' wins the MATCH'
            return False
        return True

    def end_set(self, p1_games, p2_games):
        self.print_set_score(p1_games, p2_games)
        dif = p1_games - p2_games
        if p1_games >= 6 and dif >= 2:
            print self.p1.name + ' wins the set.'
            return False
        elif p2_games >= 6 and dif <=-2:
            print self.p2.name + ' wins the set.'
            return False
        elif p1_games == 6 and p2_games == 6:
            print 'We are going into tie-break...'
            return False
        return True
    
    def end_tiebreak(self,p1_tb,p2_tb):
        dif = p1_tb - p2_tb
        if p1_tb >= 7 and dif >= 2:
            print 'SCORE UPDATE:\t'+self.p1.name+' '+str(p1_tb)+' - '+str(p2_tb)+' '+self.p2.name
            return False
        elif p2_tb >= 7 and dif <= -2:
            print 'SCORE UPDATE:\t'+self.p1.name+' '+str(p1_tb)+' - '+str(p2_tb)+' '+self.p2.name
            return False
        print 'SCORE UPDATE:\t'+self.p1.name+' '+str(p1_tb)+' - '+str(p2_tb)+' '+self.p2.name
        return True
    
    def end_game(self, p1_points, p2_points): 
        if p1_points == 4 and p2_points < 3:
            print 'SCORE UPDATE:\t'+self.p1.name+' wins game.'
            return False
        elif p1_points < 3 and p2_points == 4:
            print 'SCORE UPDATE:\t'+self.p2.name+' wins game.'
            return False
        elif (p1_points >= 3 and p2_points >= 3):
            dif = p1_points - p2_points
            if (p1_points > p2_points):
                if dif == 2:
                    print 'SCORE UPDATE:\t'+self.p1.name+' wins game.'
                    return False
                else:
                    p1_score = 'AD'
                    p2_score = '40'
            elif (p1_points < p2_points):
                if dif == -2:
                    print 'SCORE UPDATE:\t'+self.p2.name+' wins game.'
                    return False
                else:
                    p1_score = '40'
                    p2_score = 'AD'
            elif (p1_points == p2_points):
                p1_score = '40'
                p2_score = '40'
        else:
            p1_score = self.score[p1_points]
            p2_score = self.score[p2_points]
        
        print 'SCORE UPDATE:\t'+self.p1.name+' '+p1_score+' - '+p2_score+' '+self.p2.name
        return True

    def print_set_score(self, p1_games, p2_games):
        print '\n'+self.p1.name+' '+str(p1_games)
        print self.p2.name+' '+str(p2_games)+'\n'
        