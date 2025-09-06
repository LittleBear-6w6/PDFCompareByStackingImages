import sys
import os
import tempfile
import shutil
from getPDFImage import render_pdf_pages_to_png
from ChangeImageColor import change_black_to_red
from changeImageColorForStacking import change_black_to_blue
from createDiffPDF import insert_png_create_diffpdf

def main():
    """
    Main console application to compare PDF files by stacking images.
    Usage: python main.py <pdf1_path> <pdf2_path> [output_path]
    """
    if len(sys.argv) < 3:
        print("使用方法: python main.py <PDF1のパス> <PDF2のパス> [出力PDFパス] [ページ番号]")
        print("例: python main.py document1.pdf document2.pdf comparison_result.pdf 1")
        print("")
        print("Usage: python main.py <pdf1_path> <pdf2_path> [output_path] [page_number]")
        print("Example: python main.py document1.pdf document2.pdf comparison_result.pdf 1")
        print("")
        print("ページ番号を指定しない場合、1ページ目が比較されます。")
        print("If page number is not specified, page 1 will be compared.")
        return

    pdf1_path = sys.argv[1]
    pdf2_path = sys.argv[2]
    output_path = sys.argv[3] if len(sys.argv) > 3 else "comparison_result.pdf"
    page_number = int(sys.argv[4]) if len(sys.argv) > 4 else 1

    # Validate input files exist
    if not os.path.exists(pdf1_path):
        print(f"エラー: ファイルが見つかりません - {pdf1_path}")
        print(f"Error: File not found - {pdf1_path}")
        return

    if not os.path.exists(pdf2_path):
        print(f"エラー: ファイルが見つかりません - {pdf2_path}")
        print(f"Error: File not found - {pdf2_path}")
        return

    print(f"PDFファイルを比較しています:")
    print(f"ファイル1: {pdf1_path}")
    print(f"ファイル2: {pdf2_path}")
    print(f"比較ページ: {page_number}")
    print(f"出力先: {output_path}")
    print()
    print(f"Comparing PDF files:")
    print(f"File 1: {pdf1_path}")
    print(f"File 2: {pdf2_path}")
    print(f"Page to compare: {page_number}")
    print(f"Output: {output_path}")

    # Create temporary directories for processing
    temp_dir1 = tempfile.mkdtemp(prefix="pdf1_")
    temp_dir2 = tempfile.mkdtemp(prefix="pdf2_")
    
    try:
        # Step 1: Extract pages from PDFs as images
        print("\nステップ1: PDFからページを画像として抽出中...")
        print("Step 1: Extracting pages from PDFs as images...")
        
        # Extract pages from first PDF
        render_pdf_pages_to_png(pdf1_path, temp_dir1, dpi=300)
        page1_image = os.path.join(temp_dir1, f"page_{page_number}.png")
        
        # Extract pages from second PDF
        render_pdf_pages_to_png(pdf2_path, temp_dir2, dpi=300)
        page2_image = os.path.join(temp_dir2, f"page_{page_number}.png")
        
        # Check if the specified page exists in both PDFs
        if not os.path.exists(page1_image):
            print(f"エラー: PDF1のページ{page_number}が見つかりません")
            print(f"Error: Page {page_number} not found in PDF1")
            return
            
        if not os.path.exists(page2_image):
            print(f"エラー: PDF2のページ{page_number}が見つかりません")
            print(f"Error: Page {page_number} not found in PDF2")
            return
        
        # Step 2: Change colors for comparison
        print("\nステップ2: 比較用に画像の色を変更中...")
        print("Step 2: Changing image colors for comparison...")
        
        # Convert first PDF page to red
        page1_red = f"page_{page_number}_red.png"
        change_black_to_red(page1_image, page1_red)
        
        # Convert second PDF page to blue with transparency
        page2_blue = f"page_{page_number}_blue.png"
        change_black_to_blue(page2_image, page2_blue)
        
        # Step 3: Create comparison PDF
        print("\nステップ3: 比較用PDFを作成中...")
        print("Step 3: Creating comparison PDF...")
        
        insert_position = (0, 0)
        insert_size = (500, 500)
        
        insert_png_create_diffpdf(
            png_path=page2_blue,      # 2階層目（青色、透過）
            png_path2=page1_red,      # 1階層目（赤色、ベース）
            output_pdf_path=output_path,
            position=insert_position,
            image_size=insert_size
        )
        
        print(f"\n比較完了! 結果は '{output_path}' に保存されました。")
        print(f"Comparison completed! Result saved to '{output_path}'.")
        
        # Clean up temporary color-changed images
        if os.path.exists(page1_red):
            os.remove(page1_red)
        if os.path.exists(page2_blue):
            os.remove(page2_blue)
            
    except Exception as e:
        print(f"\nエラーが発生しました: {e}")
        print(f"An error occurred: {e}")
        
    finally:
        # Clean up temporary directories
        try:
            shutil.rmtree(temp_dir1)
            shutil.rmtree(temp_dir2)
            print("\n一時ファイルを削除しました。")
            print("Temporary files cleaned up.")
        except Exception as e:
            print(f"一時ファイルの削除中にエラーが発生しました: {e}")
            print(f"Error while cleaning up temporary files: {e}")

def show_help():
    """Display help information"""
    print("PDFCompareByStackingImages - Console Interface")
    print("=" * 50)
    print("このツールは2つのPDFファイルを画像として重ね合わせて比較します。")
    print("This tool compares two PDF files by stacking them as images.")
    print()
    print("使用方法 / Usage:")
    print("  python main.py <PDF1> <PDF2> [出力PDF] [ページ番号]")
    print("  python main.py <PDF1> <PDF2> [output_PDF] [page_number]")
    print()
    print("例 / Examples:")
    print("  python main.py doc1.pdf doc2.pdf")
    print("  python main.py doc1.pdf doc2.pdf result.pdf")
    print("  python main.py doc1.pdf doc2.pdf result.pdf 2")
    print()
    print("パラメータ / Parameters:")
    print("  PDF1        - 比較する最初のPDFファイル / First PDF file to compare")
    print("  PDF2        - 比較する2番目のPDFファイル / Second PDF file to compare")
    print("  出力PDF     - 結果のPDFファイル名 (省略可) / Output PDF filename (optional)")
    print("  ページ番号  - 比較するページ番号 (省略可、デフォルト: 1) / Page number to compare (optional, default: 1)")
    print()
    print("出力について / About Output:")
    print("  - 1つ目のPDFは赤色で表示されます / First PDF appears in red")
    print("  - 2つ目のPDFは青色で表示されます / Second PDF appears in blue")
    print("  - 違いがある部分は紫色になります / Differences appear in purple")

if __name__ == "__main__":
    if len(sys.argv) == 1 or (len(sys.argv) == 2 and sys.argv[1] in ['-h', '--help', 'help']):
        show_help()
    else:
        main()
