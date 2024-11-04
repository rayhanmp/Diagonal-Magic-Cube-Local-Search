import plotly.graph_objects as go
import numpy as np

# Implementation of a video player to visualise the magic cube states
# @author: Rayhan Maheswara Pramanda (modified from visualize.py)
# @date: 2024-11-04

def animate_cube_evolution(states, n, title="Magic Cube State Evolution", initial_duration=100):
    # Reshape the states to 3D cube since the states are flattened
    states_reshaped = [np.array(state).reshape(n, n, n) for state in states]

    # Initialise the frame array
    frames = []

    # Enumarate for all state in states
    for state_index, cube in enumerate(states_reshaped):
        x_position, y_position, z_position, text_values = [], [], [], []
        
        # Append the position of each cell to the respective axis
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    x_position.append(i)
                    y_position.append(j)
                    z_position.append(k)
                    text_values.append(str(cube[i, j, k]))
        
        # Create the frame for each state
        frame = go.Frame(
            data=[
                go.Scatter3d( # Create scatter plot as bullet data point
                      x=x_position, 
                      y=y_position, 
                      z=z_position,
                      mode='markers',
                      marker=dict(size=5, color=np.arange(len(text_values)), colorscale='Viridis', opacity=0.3)
                ),
                go.Scatter3d( # Create scatter plot for text data point
                    x=x_position,
                    y=y_position,
                    z=z_position,
                    mode='text',
                    text=text_values,
                    textposition="top center",
                    textfont=dict(size=10, color="black")
                )
            ],
            name=state_index
        )
        frames.append(frame) # Append the frame

    # Create the figure with initial state
    fig = go.Figure(
        data=frames[0].data,
        frames=frames,
        layout=go.Layout(
            scene=dict(
                xaxis=dict(nticks=n, range=[-0.5, n - 0.5], title="X"),
                yaxis=dict(nticks=n, range=[-0.5, n - 0.5], title="Y"),
                zaxis=dict(nticks=n, range=[-0.5, n - 0.5], title="Z"),
                aspectmode="cube" # Set the aspect mode to cube
            ),
            title=dict(
                text=title,
                x=0.5,
                y=0.8
            ),
            # Initialise menu for the buttons
            updatemenus=[ 
                {
                    'type': 'buttons',
                    'showactive': True,
                    # Define the relative position of the buttons
                    'x': 0.05,
                    'y': 0.2,
                    'buttons': [{
                        'label': 'Play',
                        'method': 'animate', # Method for button to enable start/stop, check Plotly documentation for more details
                        'args': [None, {
                            'frame': {'duration': initial_duration, 'redraw': True},
                            'fromcurrent': True,
                        }]
                    }, {
                        'label': 'Pause',
                        'method': 'animate', # Method for button to enable start/stop, check Plotly documentation for more details
                        'args': [[None], {
                            'frame': {'duration': 0, 'redraw': False},
                            'mode': 'immediate',
                        }]
                    }]
                },
            ],
            # Initialise slider
            sliders=[{
                'currentvalue': {
                    'prefix': 'State: ',
                    'visible': True
                },
                # Define the steps for the slider
                'steps': [
                    {
                        'label': f'{i}', # Label for each step (what will be shown on the slider)
                        'method': 'animate',
                        'args': [[i], { # What the step will be based on, in this case it's the state_index (see above)
                            'frame': {'duration': 0, 'redraw': True},
                            'mode': 'immediate',
                        }]
                    }
                    for i in range(len(states)) # Iterate over the number of states
                ]
            }]
        )
    )
    
    return fig