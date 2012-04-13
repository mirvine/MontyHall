from MontyHall import Game, Player, GameShowHost

scorecard = {'wins':0,'losses':0}
num_of_games = 1000

policies = ['stick','switch']
host = GameShowHost()
 
for each_policy in policies:
    player  = Player(each_policy)
    for each_game in range(1,num_of_games):
        game = Game(player, host)
        game.run_game()
        
        if game.game_state['result'] =='win':
            scorecard['wins'] = scorecard['wins']+1      
        else:
            scorecard['losses'] = scorecard['losses']+1
            
    print "Player Policy: '"+each_policy+"'   Results: ",scorecard
    scorecard = {'wins':0,'losses':0}