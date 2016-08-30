'''
Created on Nov 20, 2014

@author: Hugohrosa
'''

import matchEngine as m
import player

if __name__ == '__main__':
    
    data_rf = {'name':'Roger Federer',
          'age':33,
          'hand':True,
          'forehand':190,
          'backhand':175,
          'volley':180,
          'serve':180,
          'smash':180,
          'drop_shot':170,
          'passing_shot':150,
          'cleverness':190,
          'anticipation':160,
          'creativity':180,
          'speed':160,
          'strength':180,
          'stamina':150,
          'injury':160}
    
    data_rn = {'name':'Rafael Nadal',
          'age':28,
          'hand':False,
          'forehand':180,
          'backhand':180,
          'volley':130,
          'serve':150,
          'smash':120,
          'drop_shot':170,
          'passing_shot':190,
          'cleverness':180,
          'anticipation':190,
          'creativity':175,
          'speed':190,
          'strength':170,
          'stamina':190,
          'injury':150}
    
    rafael_nadal = player.player(data_rn)
    roger_federer = player.player(data_rf)
    
    print str(rafael_nadal.avg_skill())
    print str(roger_federer.avg_skill())
    
    mtc = m.match(roger_federer,rafael_nadal,3)
    mtc.play_match()