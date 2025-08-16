import fitz  # PyMuPDF
 
import os
def render_pdf_pages_to_png(pdf_path, output_folder, dpi=300):
 
    """
 
    PDFの各ページをレンダリングし、PNG形式で保存する関数。
    Args:
 
        pdf_path (str): 入力PDFファイルのパス。
 
        output_folder (str): 抽出した画像を保存するフォルダのパス。
 
        dpi (int): レンダリングする画像の解像度 (dots per inch)。
 
                   解像度が高いほど画質が良くなるが、ファイルサイズも大きくなります。
 
                   デフォルトは300。
 
    """
 
    if not os.path.exists(output_folder):
 
        os.makedirs(output_folder)
 
        print(f"フォルダ '{output_folder}' を作成しました。")
 
    try:
 
        doc = fitz.open(pdf_path)
 
        print(f"PDFファイル '{pdf_path}' を開きました。ページ数: {doc.page_count}")
 
        for page_num in range(doc.page_count) :
 
            page = doc.load_page(page_num)  # ページを読み込む
 
            # ページをPixmap（画像）としてレンダリング
 
            pix = page.get_pixmap(dpi=dpi)
 
            # 出力ファイル名を生成
 
            output_filename = f"page_{page_num + 1}.png"
 
            output_path = os.path.join(output_folder, output_filename)
 
            # 画像をPNG形式で保存
 
            pix.save(output_path)
 
            print(f"ページ {page_num + 1} を画像として保存しました: {output_path}")
 
        print(f"完了: 合計 {doc.page_count} ページを画像に変換しました。")
        doc.close()
 
    except fitz.FileNotFoundError:
 
        print(f"エラー: 指定されたPDFファイル '{pdf_path}' が見つかりません。")
 
    except Exception as e:
 
        print(f"予期せぬエラーが発生しました: {e}")
 
# --- スクリプトの使用例 ---
 
if __name__ == "__main__":
 
    input_pdf = "input.pdf"  # 実際のファイル名に変更してください
 
    output_directory = "./"
 
    # 300dpiでレンダリング
 
    render_pdf_pages_to_png(input_pdf, output_directory, dpi=300)