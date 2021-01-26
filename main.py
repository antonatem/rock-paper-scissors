from RPS_game import play, mrugesh, abbey, quincy, kris, human, random_player
from RPS import player
from unittest import main

play(player, abbey, 1000)
play(player, kris, 1000)
play(player, mrugesh, 1000)
play(player, quincy, 1000)

# Run unit tests
main(module='test_module', exit=False)