from PIL import Image

from PIL import Image
import matplotlib.pyplot as plt

# Abre la imagen
image = Image.open('callejon.jpg')

# Muestra la imagen
plt.imshow(image)
plt.axis('off')  # Opcional, para ocultar los ejes
plt.show()
