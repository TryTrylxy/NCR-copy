#!/bin/bash

# CC152K
python ./NCR/run.py --gpu 0 --workers 2 --warmup_epoch 10 --data_name cc152k_precomp --data_path /home/jncsnlp3/SSD2/th/Noisy_Correspondence/datastet/NCR-data/data/ --vocab_path /home/jncsnlp3/SSD2/th/Noisy_Correspondence/datastet/NCR-data/vocab/

# # MS-COCO: noise_ratio = {0, 0.2, 0.5}
# python ./NCR/run.py --gpu 0 --workers 2 --warmup_epoch 10 --data_name coco_precomp --num_epochs 20 --lr_update 10 --noise_ratio 0.2 --data_path /home/jncsnlp3/SSD2/th/Noisy_Correspondence/datastet/NCR-data/data/ --vocab_path /home/jncsnlp3/SSD2/th/Noisy_Correspondence/datastet/NCR-data/vocab/

# # Flickr30K: noise_ratio = {0, 0.2, 0.5}
# python ./NCR/run.py --gpu 0 --workers 2 --warmup_epoch 5 --data_name f30k_precomp --noise_ratio 0.2 --data_path /home/jncsnlp3/SSD2/th/Noisy_Correspondence/datastet/NCR-data/data/ --vocab_path /home/jncsnlp3/SSD2/th/Noisy_Correspondence/datastet/NCR-data/vocab/
