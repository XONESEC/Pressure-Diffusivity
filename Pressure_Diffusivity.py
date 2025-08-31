# Input Library
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
#----------------------------------------------------------------------------------------------------------------------

# Pressure Diffusivity
st.header("**Pressure Diffusivity with PDE Method**")
st.subheader("Input Parameter")
input_parameter = '''In this section, the user is asked to input the values of variables that have been determined. The required variables are:

* **Porosity**            = the percentage of the total rock volume consisting of pore space or open space (fraction)

* **Permeability**        = the ability of the rock to allow fluids to flow (mD)

* **Viscosity**           = a measure of the fluids thickness (cP)

* **Compressibility**     = the ability of a material to undergo volume changes when subjected to pressure (1/psi)

* **Length (r)**          = the distance between the injection well and the production well (ft)

* **n (i)**               = the number of sections into which the rock sample is divided

* **dx**                  = distance between each section (ft)

* **dt**                  = time  (hour)

* **nt**                  = interval per time step

* **Injection Pressure**  = the pressure of the injected fluid (psi)

* **Initial Pressure**    = the initial fluid pressure in the reservoir (psi)

* **Production Pressure** = the fluid pressure desired during production (psi)'''

st.markdown(input_parameter)

st.subheader("Output Parameter")
output_parameter = '''In this section, the user will obtain output in the form of graphs and tables containing the values of the predefined variables. The variable that will be displayed is:

* **Pressure** = the fluid pressure in the reservoir (psi), at each section and time step'''

st.markdown(output_parameter)

st.subheader("Model")
st.image("data:image/png;base64,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")

#----------------------------------------------------------------------------------------------------------------------

# Input Parameter
st.sidebar.title("Input")
porosity =st.sidebar.number_input("Porosity (Φ)",min_value=0.0, max_value=1.0, value=0.15, step=0.01)

permeability = st.sidebar.number_input("Permeability (md)",min_value=0.0, value=5.0, step=0.1)

viscosity = st.sidebar.number_input("Viscosity (cP)",min_value=0.0, value=0.6, step=0.1)

compressibility = st.sidebar.number_input("Compressibility (1/psi)",min_value=0.0,max_value=1.0, value=0.000003, step=0.00000001, format="%.8f")

length = st.sidebar.number_input("Length (ft)",min_value=0, value=1000)

n = st.sidebar.number_input("n (section)",min_value=0, value=10)

dx = st.sidebar.number_input ("dx (ft)", min_value = 0, value = 100 )

dt = st.sidebar.number_input("dt (hour)",min_value=0, value=1)

nt =st.sidebar.number_input ("nt (time step)", min_value= 0, value= 10)

initial_pressure = st.sidebar.number_input("Initial Pressure (psi)",min_value=0.0, value=4000.0, step=0.1)

injection_pressure = st.sidebar.number_input("Injection Pressure (psi)",min_value=0.0, value=570.0, step=0.1)

production_pressure = st.sidebar.number_input("Production Pressure (psi)",min_value=0.0, value=3000.0, step=0.1)

dr = int(length/dx)

#----------------------------------------------------------------------------------------------------------------------

#Partial Differential Equation
st.subheader("Partial Differential Equation")
st.latex(r'''\frac{d^2 P}{dx^2}=\frac{\text{Φ}\times\text{μ}\times C_t}{0.000264\times{k}}\frac{dP}{dt}''')

st.latex(r'''\lambda = \frac{\text{Φ}\times\text{μ}\times C_t}{0.000264\times{k}}''')


def calc_lamda(porosity, viscosity, compressibility, permeability):
    return    (porosity * viscosity * compressibility) / (0.000264 * permeability)

lamda_value = calc_lamda(porosity, viscosity, compressibility, permeability)

st.badge(f"**Lambda : {lamda_value:,.10f}**")
#----------------------------------------------------------------------------------------------------------------------

#Pressure Diffusivity Equation

st.subheader("Pressure Diffusivity Equation")
st.latex(r'''P_{i}^{(l+1)} = \frac{\Delta t}{\lambda} \left( \frac{P_{i+1}^{l} - 2P_{i}^{l} + P_{i-1}^{l}}{\Delta x^2} \right) + P_{i}^{l}''')

#----------------------------------------------------------------------------------------------------------------------

# Pressure Distribution using PDE Explicit Method
pressure = np.zeros((nt+1, n+1))

pressure[0] = initial_pressure
pressure[:,0] = injection_pressure
pressure[:,-1] = production_pressure

def PressureDiffusivity(nt, n, dt, dx, lamda_value):
    for i in range (0, nt+1):
        for j in range (1, n):
            if i == 0:
                pressure[i,j] = initial_pressure
            else:
                pressure[i,j] = (
                (dt/lamda_value) * (
                    (pressure[i-1,j+1] - 2*pressure[i-1,j] + pressure[i-1,j-1]) / (dx**2)
                ) + pressure[i-1,j]
            )
    return pressure
Result = PressureDiffusivity(nt, n, dt, dx, lamda_value)
st.dataframe(Result)

# Visualize Pressure Distribution
st.subheader("Visualize Pressure Distribution")
x = np.arange(Result.shape[1])  
y = np.arange(Result.shape[0]) 
x, y = np.meshgrid(x, y)

fig = go.Figure(data=[go.Surface(z=Result, x=x, y=y, colorscale="Magma")])

fig.update_layout(
    scene=dict(
        xaxis_title="Number of Sections",
        yaxis_title="Time Step",
        zaxis_title="Pressure",
    ),
    autosize=True,
    height=700,
)

st.plotly_chart(fig, use_container_width=True)

# 1D Visualization
fig, ax = plt.subplots(figsize=(10, 8))

for i in range(0, nt+1):
    color = plt.cm.magma(i/nt)
    ax.plot(Result[i], color= color)

ax.set_xlabel('Number of Sections')
ax.set_ylabel('Pressure')
ax.set_title('Pressure Distribution in Reservoir Using PDE Method')

st.pyplot(fig)


# 2D Visualization 
import time
# Sidebar kontrol auto play
auto_play = st.checkbox("Auto Play", value=False)
play_speed = st.slider("Play Speed (fps)", 0.1, 2.0, 0.5)

# Tempat kosong untuk plotting
plot_placeholder = st.empty()

# Fungsi untuk gambar timestep tertentu
def plot_timestep(selected_timestep):
    pressure_profile = Result[selected_timestep, :].reshape(1, -1)

    fig, ax = plt.subplots(figsize=(10, 2))
    img = ax.imshow(pressure_profile, cmap='magma', aspect='auto',
                    extent=[0, Result.shape[1], 0, 1])

    cbar = fig.colorbar(img, ax=ax, shrink=1.0, aspect=5)
    cbar.set_label('Pressure (psi)')

    ax.set_xlabel('Number of Sections')
    ax.set_yticks([])  
    ax.set_title(f'Pressure Distribution at Timestep {selected_timestep}')

    plot_placeholder.pyplot(fig)

# Kalau Auto Play dicentang → jalan otomatis
if auto_play:
    for t in range(nt):
        plot_timestep(t)
        time.sleep(play_speed)
else:
    # Kalau tidak, manual pakai slider
    selected_timestep = st.slider("Select Timestep", min_value=0, max_value=nt-1, value=0, step=1)
    plot_timestep(selected_timestep)


