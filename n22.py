import plotly.graph_objects as go
import p3_for_9_loop as np

# Create figure
fig = go.Figure()

# Elephant parameters
u = np.linspace(0, 2 * np.pi, 50)
v = np.linspace(0, np.pi, 50)

# Body (ellipsoid)
x_body = 0.6 * np.outer(np.cos(u), np.sin(v))
y_body = 0.8 * np.outer(np.sin(u), np.sin(v))
z_body = 0.5 * np.outer(np.ones(np.size(u)), np.cos(v)) - 0.2

# Add body surface
fig.add_trace(go.Surface(
    x=x_body, y=y_body, z=z_body,
    colorscale=[[0, 'gray'], [1, 'gray']],
    showscale=False,
    opacity=0.8
))

# Add other elephant parts similarly...

# Customize layout
fig.update_layout(
    title='Interactive 3D Elephant',
    scene=dict(
        xaxis=dict(visible=False),
        yaxis=dict(visible=False),
        zaxis=dict(visible=False),
        aspectmode='manual',
        aspectratio=dict(x=1, y=1, z=0.7)
    ),
    width=800,
    height=600
)

fig.show()