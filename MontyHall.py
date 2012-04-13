import random
"""
===============================================================================
Monty Hall simulation
Author: Mark Irvine (mark@irvinesonline.org)
Date:   13 April 2012
===============================================================================

License:
===============================================================================
Creative Commons CC BY-NC-SA license 
http://creativecommons.org/licenses/by-sa/3.0/

Description:
===============================================================================
The Monty Hall problem is a probability puzzle described as a television 
gameshow.

See http://en.wikipedia.org/wiki/Monty_Hall_problem for a more detailed 
description of the problem.


    "Suppose you're on a game show, and you're given the choice of three doors: 
     Behind one door is a car; behind the others, goats. You pick a door, say 
     No. 1 [but the door is not opened], and the host, who knows what's behind 
     the doors, opens another door, say No. 3, which has a goat. He then says 
     to you, "Do you want to pick door No. 2?" Is it to your advantage to 
     switch your choice?"
     -- wikipedia
     

This program runs many simulations of the Monty Hall game show, and keeps a
running score of the results for two 'policies' - namely 'stick' or 'switch'.

Although the reasoning of the Monty Hall problem may be counter intuitive, the 
simulation shows a clear advantage of one policy over the other...
"""

class Game:
    """
    >>> player_policy = 'stick'
    >>> player = Player(player_policy)
    >>> host = GameShowHost()
    >>> game = Game(player, host)
    >>> game.run_game()
    >>> game.game_state['result'] in ['win','lose']
    True
    """
    def __init__(self,player, gameshowhost):
        self.game_state = {}
        self.player = player
        self.host   = gameshowhost

    def run_game(self):
        
        winning_door = self.host.decide_winning_door()
        self.update_game_status('winning_door', winning_door)
        
        chosen_door = self.player.choose_door()
        self.update_game_status('chosen_door', chosen_door)
        
        revealed_door = self.host.choose_door_to_reveal(winning_door,chosen_door)
        self.update_game_status('revealed_door', revealed_door)
        
        final_choice = self.player.make_final_choice(chosen_door,revealed_door)
        self.update_game_status('final_choice', final_choice)
        
        self.score_game()
    
    
    def update_game_status(self,item,value):
        self.game_state[item] = value
        
        
    def score_game(self):
        if self.game_state['final_choice'] == self.game_state['winning_door']:
            self.game_state['result'] ='win'
        else:
            self.game_state['result'] = 'lose'
    
class Player:
    def __init__(self,policy):
        self.policy = policy 
       
    
    def choose_door(self):
        """
        >>> policy = 'stick'
        >>> p = Player(policy)
        >>> door = p.choose_door()
        >>> door in ['A','B','C']
        True
        """
        doors = ['A','B','C']
        chosen_door = random.sample(doors,1)[0]
        return chosen_door
    
    
    def make_final_choice(self,chosen_door,revealed_door):
        """
        >>> p = Player('stick')
        >>> chosen_door = 'A'
        >>> revealed_door = 'B'
        >>> p.make_final_choice(chosen_door, revealed_door)
        'A'
        
        >>> p = Player('switch')
        >>> chosen_door = 'A'
        >>> revealed_door = 'B'
        >>> p.make_final_choice(chosen_door, revealed_door)
        'C'
        
        """
        final_choice = ''
        
        policy = self.policy
        assert policy in ['switch','stick']
        if  policy == 'switch':
            final_choice = self.switch(chosen_door,revealed_door)
        elif policy == 'stick':
            final_choice = chosen_door
        return final_choice
            
        
    def switch(self,chosen_door,revealed_door):
        """
        >>> p = Player('switch')
        >>> chosen_door = 'A'
        >>> revealed_door = 'B'
        >>> p.switch(chosen_door,revealed_door)
        'C'
        """
        doors = ['A','B','C']
        doors.remove(revealed_door)
        doors.remove(chosen_door)
        
        new_chosen_door = doors[0]
        return new_chosen_door
    
class GameShowHost:
    def __init__(self,name = 'Monty'):
        self.name = name
        
        
    def decide_winning_door(self):
        """
        >>> host = GameShowHost()
        >>> winning_door = host.decide_winning_door()
        >>> winning_door in ['A','B','C']
        True
        """
        doors = ['A','B','C']
        
        door = random.sample(doors,1)[0]
        return door
    
    
    def choose_door_to_reveal(self,winning_door,chosen_door):
        """
        >>> host = GameShowHost()
        >>> chosen_door = 'A'
        >>> winning_door = 'B'
        >>> host.choose_door_to_reveal(winning_door, chosen_door)
        'C'
        
        >>> chosen_door = 'A'
        >>> winning_door = 'A'
        >>> reveal_door = host.choose_door_to_reveal(winning_door, chosen_door)
        >>> reveal_door in ['B','C']
        True
        """
        door_names = ['A','B','C']     
        
        door_names.remove(chosen_door)
        if winning_door == chosen_door:
            pass
        else:
            door_names.remove(winning_door)
            
        door_to_reveal = random.sample(door_names,1)[0]
        
        return door_to_reveal


if __name__=='__main__':
    import doctest
    doctest.testmod(verbose = True)