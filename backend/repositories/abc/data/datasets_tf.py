import tensorflow as tf
import os
import pandas as pd
import cv2
import numpy as np


class TrackNetDataset(tf.keras.utils.Sequence):


    def __init__(self, mode, input_height=360, input_width=640, batch_size=2):
        self.path_dataset = '/workspace/TrackNet_yastr'
        assert mode in ['train', 'val'], 'incorrect mode'
        self.data = pd.read_csv(os.path.join(self.path_dataset, f'labels_{mode}.csv'))
        print(f'mode = {mode}, samples = {self.data.shape[0]}')
        self.height = input_height
        self.width = input_width
        self.batch_size = batch_size
        

    def __len__(self):
        return (self.data.shape[0] + self.batch_size - 1) // self.batch_size  # Number of batches
    

    def __getitem__(self, batch_idx):
        # print("btach no",batch_idx)
        start_idx = batch_idx * self.batch_size
        end_idx = (batch_idx + 1) * self.batch_size
        batch_data = self.data.iloc[start_idx:end_idx]

        inputs_batch = []
        outputs_batch = []

        for idx in range(len(batch_data)):
            path, path_prev, path_preprev, path_gt, x, y, status, vis = batch_data.iloc[idx]

            path = os.path.join(self.path_dataset, path)
            path_prev = os.path.join(self.path_dataset, path_prev)
            path_preprev = os.path.join(self.path_dataset, path_preprev)
            path_gt = os.path.join(self.path_dataset, path_gt)

            inputs = self.get_input(path, path_prev, path_preprev)
            outputs = self.get_output(path_gt)

            inputs_batch.append(inputs)
            outputs_batch.append(outputs)
            # print("x ",x," y ",y," vis ",vis," idx ",idx)
        return np.array(inputs_batch), np.array(outputs_batch)
    

    def get_input(self, path, path_prev, path_preprev):

        img = cv2.imread(path)
        img = cv2.resize(img, (self.width, self.height))

        img_prev = cv2.imread(path_prev)
        img_prev = cv2.resize(img_prev, (self.width, self.height))

        img_preprev = cv2.imread(path_preprev)
        img_preprev = cv2.resize(img_preprev, (self.width, self.height))

        imgs = np.concatenate((img, img_prev, img_preprev), axis=2)
        imgs = imgs.astype(np.float32) / 255.0

        imgs = np.rollaxis(imgs, 2, 0)
        return np.array(imgs)


    def get_output(self,path_gt):
          
          img = cv2.imread(path_gt)
          img = cv2.resize(img, (self.width, self.height))
          img = img[:, :, 0]
          img = np.reshape(img, (self.width * self.height))
          return img
        

    def get_output_one_hot( self, path , nClasses = 256):

        seg_labels = np.zeros((  self.height , self.width  , nClasses ), dtype='uint8')
        # print(seg_labels.shape)
        try:
            img = cv2.imread(path, 1)
            img = cv2.resize(img, ( self.width , self.height))
            img = img[:, : , 0]
            for c in range(nClasses):
                 seg_labels[: , : , c ] = (img == c ).astype(int)

        except Exception as e:
            print(e)
        seg_labels = np.reshape(seg_labels, ( self.width*self.height , nClasses))
        # print(seg_labels.shape)
        return seg_labels




