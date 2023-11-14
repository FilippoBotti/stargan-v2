import os
import shutil
import re
# Percorsi delle cartelle
images_dir = "/Users/filippo/Desktop/università/laurea/tesi/datasets/horse2zebra/test/zebra"
mask_dir = "/Users/filippo/Desktop/università/laurea/tesi/datasets/horse2zebra/test_mask/zebra"
destination_dir = "/Users/filippo/Desktop/università/laurea/tesi/datasets/horse2zebra/mask_test/zebra"

# Creare la terza cartella se non esiste già
if not os.path.exists(destination_dir):
    os.makedirs(destination_dir)

# Ottenere elenco di file nella cartella "images"
image_files = set(os.listdir(images_dir))

mask_files = set(os.listdir(mask_dir))
# Copiare i file dalla cartella "mask" alla terza cartella se il nome è presente in "images"
# Utilizzare regex per trovare corrispondenze nei nomi dei file nella cartella "mask"

for image in image_files:
    print(image)
    for mask in mask_files:
        #print(mask)
        if(image == mask[5:]):
            source_path = os.path.join(mask_dir, mask)
            destination_path = os.path.join(destination_dir, mask)
            shutil.copy(source_path, destination_path)
            print(f"Copiato {mask} nella terza cartella.")
# for mask_file in os.listdir(mask_dir):
#     # Costruire un pattern regex
#     print(mask_file[5:])
