"""Plot a sine wave using matplotlib and save to sine_wave.png."""
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

plt.plot(x, y)
plt.title('Sine Wave')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.grid(True)
plt.tight_layout()
plt.savefig('sine_wave.png')
plt.close()
