import cv2 as cv
import numpy as np
import os

for dir in ['Data/Hemorragico', 'Data/Isquemico', 'Data/Normal']:
  k = 0
  tag_list = os.listdir(dir)
  n_tag_list = len(tag_list)

  for tag in tag_list:
    image = cv.imread(f'{dir}/{tag}', cv.IMREAD_GRAYSCALE)

    try:
      image = cv.resize(image, (256, 256))  # resize image
    except:
      print(f'{dir}/{tag}: erro ao redefinir tamanho da imagem...')
      continue

    hight = image.shape[0]
    width = image.shape[1]

    betas = [-50, 50]

    for beta in betas:
      for i in range(hight):
        for j in range(width//16):
          image[i][j] = np.clip(image[i][j] + beta, 0, 255)
          image[i][j+1] = np.clip(image[i][j+1] + beta, 0, 255)
          image[i][j+2] = np.clip(image[i][j+2] + beta, 0, 255)
          image[i][j+3] = np.clip(image[i][j+3] + beta, 0, 255)
          image[i][j+4] = np.clip(image[i][j+4] + beta, 0, 255)
          image[i][j+5] = np.clip(image[i][j+5] + beta, 0, 255)
          image[i][j+6] = np.clip(image[i][j+6] + beta, 0, 255)
          image[i][j+7] = np.clip(image[i][j+7] + beta, 0, 255)
          image[i][j+8] = np.clip(image[i][j+8] + beta, 0, 255)
          image[i][j+9] = np.clip(image[i][j+9] + beta, 0, 255)
          image[i][j+10] = np.clip(image[i][j+10] + beta, 0, 255)
          image[i][j+11] = np.clip(image[i][j+11] + beta, 0, 255)
          image[i][j+12] = np.clip(image[i][j+12] + beta, 0, 255)
          image[i][j+13] = np.clip(image[i][j+13] + beta, 0, 255)
          image[i][j+14] = np.clip(image[i][j+14] + beta, 0, 255)
          image[i][j+15] = np.clip(image[i][j+15] + beta, 0, 255)

      if beta == -30:
        term = 'dark'

      else:
        term = 'light'

      fmt = tag[-3:]
      name = tag[:-4]

      try:
        cv.imwrite(f'{dir}/{name}_{term}.{fmt}', image)
      except:
        print(f'{dir}/{tag}')

      k += 1
      os.system('cls')
      print('%s: %.2f%%' % (dir, 100.*k / (2*n_tag_list)))