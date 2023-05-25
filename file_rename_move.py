import os
import shutil

for main in os.listdir('Student-engagement-dataset'):
    for sub in os.listdir('Student-engagement-dataset/{}'.format(main)):
        for image in os.listdir('Student-engagement-dataset/{}/{}'.format(main, sub)):
            os.rename('Student-engagement-dataset/{}/{}/{}'.format(main, sub, image), 'dataset/{}/{}_{}'.format(main, sub, image))