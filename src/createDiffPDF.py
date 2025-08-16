from PIL import Image
 
import fitz  # PyMuPDF
 
import os
def insert_png_create_diffpdf(
 
    png_path,
 
    png_path2,
 
    output_pdf_path,
 
    position,
 
    image_size=(200, 200),
 
    background_color=(255, 255, 255)
 
):
 
    """
 
    PDF比較用に作成した画像２枚を重ねて挿入して比較用PDFを作成する関数。
    Args:
 
        png_path (str): 透過させたPNG画像のパス（２階層目）。

        png_path2 (str): 重ねて比較するPNG画像のパス（１階層目）。
 
        pdf_path (str): 挿入先のPDFファイルのパス。
 
        output_pdf_path (str): 比較用PDFファイルの保存先パス。
 
        position (tuple): 挿入位置 (x, y) を指定するタプル。左上からの座標。
 
        image_size (tuple): PDFに挿入する際の画像のサイズ (幅, 高さ)。
 
        background_color (tuple): 透過させたい背景色 (R, G, B)。デフォルトは白。
 
    """
 
    try:
 
        # --- ステップ1: １階層目PNG画像の背景を透過させる ---
 
        print("PNG画像の背景を透過処理中です...")
 
        img = Image.open(png_path)
 
        img = img.convert("RGBA")  # RGBAモードに変換して透明度チャネルを追加
 
        datas = img.getdata()
 
        newData = []
 
        for item in datas:
 
            # 指定された背景色と一致する場合、透明にする
 
            if item[0] == background_color[0] and item[1] == background_color[1] and item[2] == background_color[2]:
 
                newData.append((255, 255, 255, 0))  # 透明（RGBAのA=0）
 
            else:
 
                newData.append(item)
 
        img.putdata(newData)
 
        # 透過後の画像を一時ファイルとして保存
 
        transparent_png_path = "temp_transparent_image.png"
 
        img.save(transparent_png_path, "PNG")
 
        print(f"透過後の画像を一時ファイル '{transparent_png_path}' として保存しました。")
 
        # --- ステップ2: 透過させた画像をPDFに挿入する ---
 
        print("PDFに画像を挿入中です...")
 
        doc = fitz.open()
        page = doc.new_page(-1, 800,800) # 新しいページを追加（サイズは800x800）
 
        # 挿入する画像の矩形を定義
 
        rect = fitz.Rect(position[0], position[1], position[0] + image_size[0], position[1] + image_size[1])
 
        # 画像をページに挿入
        # １階層目として先ず透過していない画像を挿入、その後に比較用に透過した画像を挿入
 
        page.insert_image(rect, filename=png_path2)
        page.insert_image(rect, filename=transparent_png_path)
 
        # 比較用PDFファイルを保存
 
        doc.save(output_pdf_path)
 
        doc.close()
 
        print(f"画像をPDFに挿入し、'{output_pdf_path}' として保存しました。")
        # 一時ファイルを削除
 
        os.remove(transparent_png_path)
 
        print(f"一時ファイル '{transparent_png_path}' を削除しました。")
    except FileNotFoundError:
 
        print(f"エラー: 指定されたファイルが見つかりません。パスを確認してください。")
 
    except Exception as e:
 
        print(f"予期せぬエラーが発生しました: {e}")

 
if __name__ == "__main__":
 
    # 挿入するPNGファイル名を指定
 
    input_png = "page2_2_blue.png" #比較用に被せる画像（２回層目）
    input_png2 = "page_2_red.png"  #ベースとなる画像（１回層目）
    # 変更後のPDFファイル名
 
    output_pdf = "output.pdf"
    # 画像を挿入するページ番号（例: 最初のページは0）
 
    target_page = 0
    # 挿入位置 (x, y) とサイズ (幅, 高さ) を指定

    # 例: 左上から0ピクセル、上から0ピクセルの位置に幅500, 高さ500で配置

    insert_position = (0, 0)
 
    insert_size = (500, 500)
    # 実行
 
    insert_png_create_diffpdf(
 
        png_path=input_png,
 
        png_path2=input_png2,
 
        output_pdf_path=output_pdf,
 
        position=insert_position,
 
        image_size=insert_size
 
    )