import plotly.graph_objects as go
import numpy as np

# Fungsi untuk visualisasi state kubus
def visualize_magic_cube(cube, title="Magic Cube Visualization"):
    n = cube.shape[0]
    x_position, y_position, z_position, text_values = [], [], [], []
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                x_position.append(i)
                y_position.append(j)
                z_position.append(k)
                text_values.append(str(cube[i, j, k]))

    fig = go.Figure(data=[
        go.Scatter3d(
            x=x_position, 
            y=y_position, 
            z=z_position,
            mode='markers',
            marker=dict(size=5, color=np.arange(len(text_values)), colorscale='Viridis', opacity=0.6)
    ),
        go.Scatter3d(
            x=x_position, 
            y=y_position, 
            z=z_position,
            mode='text',
            text=text_values,
            textposition="top center",
            textfont=dict(size=10, color="black"),
        )
    ])

    fig.update_layout(scene=dict(
        xaxis=dict(nticks=n, range=[-0.5, n - 0.5]),
        yaxis=dict(nticks=n, range=[-0.5, n - 0.5]),
        zaxis=dict(nticks=n, range=[-0.5, n - 0.5]),
        aspectmode="cube"
    ), title=title)

    fig.show()