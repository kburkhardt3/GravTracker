import matplotlib.pyplot as plt
import numpy as np

m_co2 = 50 # g
runs = m_co2*1000 # step size of 1 mg

v_headspace = 5 # L
d_air = 1.225 # g/L
d_co2 = 1.977 # g/L
v_co2 = m_co2/runs*1/d_co2
den = d_air
log = []

for i in range(runs):
    den = (v_headspace*den + v_co2*d_co2)/(v_headspace + v_co2)
    log.append(den)

x = np.linspace(0, m_co2, runs)

plt.plot(x, log) # should plot vs mass, currently plotted vs mg
plt.xlabel(r'CO$_2$ Production (g)')
plt.ylabel('Headspace Density (g/L)')
plt.title('Headspace Density During Fermentation')
plt.show()


print('Headspace density after ' + str(m_co2) + 'g CO₂ production: ' \
      + str(np.round(den, 2)) + ' g/L')