from PIL import Image
 
import os
def change_black_to_blue(image_path, output_path):
 
    """
 
    指定された画像の黒いピクセルを青色に変換し、背景を透過させた新しい画像を保存する関数。
    Args:
 
        image_path (str): 変換したいPNG画像のパス。
 
        output_path (str): 変換後の画像を保存するパス。
 
    """
 
    try:
 
        # 画像を開く
 
        img = Image.open(image_path).convert('RGBA')
 
        # 画像のピクセルデータの読み込み
 
        pixels = img.load()
 
        # 画像の幅と高さを取得
 
        width, height = img.size
 
        # 閾値（この値以下のRGB値のピクセルを「黒」と判定する値）
        # 完全に純粋な黒（0,0,0）のみを対象にしたい場合は、threshold = 0 と設定する。
 
        threshold = 200
 
        # すべてのピクセルを走査
 
        for y in range(height):
 
            for x in range(width):
 
                # ピクセルのRGBA値を取得
 
                r, g, b, a = pixels[x, y]
 
                # ピクセルが「黒」と判断された場合、青色に変換する
 
                if r <= threshold and g <= threshold and b <= threshold:
 
                    pixels[x, y] = (0, 0, 255, a) # 青色に設定（元の透明度を保持）
                else :
                    pixels[x, y] = (255, 255, 255, 0) # 背景を透過
        # 変更された画像を保存
 
        img.save(output_path, "PNG")
 
        print(f"画像を変換しました: {output_path}")
    except FileNotFoundError:
 
        print(f"エラー: 指定されたファイル '{image_path}' が見つかりません。")
 
    except Exception as e:
 
        print(f"予期せぬエラーが発生しました: {e}")

 
if __name__ == "__main__":
 
    # 変換したい画像のファイル名
 
    input_filename = "page2_2.png"
 
    # 変換後の画像のファイル名
 
    output_filename = "page2_2_blue.png"
 
    # 関数を実行
 
    change_black_to_blue(input_filename, output_filename)