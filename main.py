import webcolors

import matplotlib.pyplot as plt


def closest_color(rgb):
  differences = {}
  for color_hex, color_name in webcolors.CSS3_HEX_TO_NAMES.items():
    r, g, b = webcolors.hex_to_rgb(color_hex)
    differences[sum([(r - rgb[0])**2, (g - rgb[1])**2,
                     (b - rgb[2])**2])] = color_name

  return differences[min(differences.keys())]


color = (255, 0, 0)

try:
  cname = webcolors.rgb_to_name(color)
  print(f"The color is exactly {cname}")
except ValueError:
  cname = closest_color(color)
  print(f"The color is closest to {cname}")

plt.imshow([[color]])
plt.show()
