from magic_utils import *
from video_player import video_player
from hc_stochastic import hc_stochastic
from hc_random_restart import hc_random_restart
from hc_sideways_move import hc_sideways_move
from hc_steepest_ascent import hc_steepest_ascent

########## EXAMPLE OF USE ##########

n = 5
cube = make_cube(n)
mc = magic_number(n)

best_cube, best_state_value, states = hc_stochastic(cube, mc, 1000) ## Change the local search algorithm and its parameter here
print("Running local search algorithm...")
print("DONE! Best state value:" + str(best_state_value))

## Write the states to a file
filename = input("Enter file name to save states: ")
write_states_to_file(states, filename + ".npz")

show_video = input("Show video? (y/n): ")

if show_video == "y":
    ## Read the states from a file
    read_states = read_states_from_file(filename + ".npz")

    ## Show Video
    fig = video_player(read_states, n)
    fig.show()
else:
    print("Bye, bye!")
