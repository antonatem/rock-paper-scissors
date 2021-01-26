play_order = {}
def player(prev_play, opponent_history=[]):
    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
    guess = 'S'

    if not prev_play:
        prev_play = 'R'
    opponent_history.append(prev_play)

    last_three = ''.join(opponent_history[-3:])
    last_four = ''.join(opponent_history[-4:])
    if len(last_four) == 4:
      if play_order.get(last_four) is not None:
        play_order[last_four] += 1
      else:
        play_order[last_four] = 1

    potential_plays = [
        last_three + "R",
        last_three + "P",
        last_three + "S"
    ]

    sub_order = {
        k: play_order.get(k)
        for k in potential_plays if k in play_order
    }

    if len(sub_order) > 0:
      prediction = max(sub_order, key=sub_order.get)[-1:]
      guess = ideal_response[prediction]

    return guess
