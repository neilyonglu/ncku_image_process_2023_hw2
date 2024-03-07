from PIL import Image
import os

def png_to_jpg_recursive(input_folder, output_folder):
    # 檢查輸出資料夾是否存在，如果不存在則創建
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 取得輸入資料夾中的所有檔案和資料夾
    files_and_folders = os.listdir(input_folder)

    for item in files_and_folders:
        # 構建完整的路徑
        item_path = os.path.join(input_folder, item)
        output_item_path = os.path.join(output_folder, item)

        if os.path.isdir(item_path):
            # 如果是資料夾，遞迴處理
            png_to_jpg_recursive(item_path, output_item_path)
        elif item.endswith('.png'):
            # 如果是PNG檔案，進行轉換並保存到輸出資料夾中
            png_image = Image.open(item_path)

            # 構建輸出檔案的完整路徑，並將檔名的副檔名改為.jpg
            output_file = os.path.splitext(item)[0] + '.jpg'
            output_path = os.path.join(output_folder, output_file)

            # 將PNG圖片轉換為JPG格式並保存
            png_image.convert('RGB').save(output_path)

            print(f"已將 {item} 轉換為 {output_file}")

# 設定輸入和輸出資料夾的路徑
input_folder_path = '../demo_test9'
output_folder_path = 'testing_jpg'

# 呼叫函數執行轉換
png_to_jpg_recursive(input_folder_path, output_folder_path)