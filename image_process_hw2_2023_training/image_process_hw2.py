import cv2
import numpy as np
from sklearn.model_selection import StratifiedKFold
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import sys, hw2_ui
import os
import glob

class MainWindow(QMainWindow, hw2_ui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('image_process_hw2')
        self.setupUi(self)     
        
        self.image_paths = []
        self.current_index = 0
        self.gt_ids = None
        self.image_ids = None
        
        self.pushButton.clicked.connect(self.load_folder)
        self.pushButton_2.clicked.connect(self.pre)
        self.pushButton_3.clicked.connect(self.next)
        self.pushButton_4.clicked.connect(self.load_folder)#detection
        self.pushButton_5.clicked.connect(self.segmentation)
        
    def load_folder(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        self.folder_path = QFileDialog.getExistingDirectory(self, "Select folder: ", options=options)

        if self.folder_path:
            print("Folder path: ", self.folder_path)
        
            self.image_ids = glob.glob(self.folder_path + '/*.png')
            self.gt_ids = glob.glob(self.folder_path + '/*.json')
        
            self.image_paths = self.find_image_files(self.folder_path)

            if self.image_paths:
                # 顯示第一張圖片
                self.show_image(self.image_paths[self.current_index])
            else:
                print("No jpg or png image found in the selected folder.")

    def find_image_files(self, folder_path):
        # 找到資料夾中的所有 jpg 或 png 圖片檔案
        image_paths = [os.path.join(folder_path, file_name) for file_name in os.listdir(folder_path)
                       if file_name.lower().endswith(('.jpg', '.png'))]
        return image_paths

    def pre(self):
        # 顯示前一張圖片
        if self.image_paths:
            self.current_index = (self.current_index - 1) % len(self.image_paths)
            self.show_image(self.image_paths[self.current_index])

    def next(self):
        # 顯示下一張圖片
        if self.image_paths:
            self.current_index = (self.current_index + 1) % len(self.image_paths)
            self.show_image(self.image_paths[self.current_index])

    def show_image(self, image_path):
        # 使用 OpenCV 顯示圖片
        img = cv2.imread(image_path)
        
        # 設定標籤文字為當前圖片的名稱
        current_image_name = os.path.basename(image_path)
        self.label_2.setText("Current Image: " + current_image_name)
        
        cv2.imshow('Original', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
    def segmentation(self):
        print(1)
         
               
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())