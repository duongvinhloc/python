# -*- coding: utf-8 -*-
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.lib.pagesizes import A4, portrait
from reportlab.platypus import Table, TableStyle
from reportlab.lib.units import mm
from reportlab.lib import colors

# 初期設定
def make(filename="給与賞与明細書"): # ファイル名
    pdf_canvas = set_info(filename) # キャンバス名
    print_string(pdf_canvas)
    pdf_canvas.save() # 保存

def set_info(filename):
    pdf_canvas = canvas.Canvas("./{0}.pdf".format(filename)) # 保存先
    pdf_canvas.setAuthor("") # 作者
    pdf_canvas.setTitle("") # 表題
    pdf_canvas.setSubject("") # 件名
    return pdf_canvas

#履歴書フォーマット作成
def print_string(pdf_canvas):
    pdfmetrics.registerFont(UnicodeCIDFont('HeiseiKakuGo-W5')) # フォント
    width, height = A4 # 用紙サイズ

    # タイトル
    font_size = 24  # フォントサイズ
    pdf_canvas.setFont('HeiseiKakuGo-W5', font_size)
    pdf_canvas.drawString(60, 770, '給与賞与証明書')  # 書き出し(横位置, 縦位置, 文字)
    # 日付
    font_size = 10
    pdf_canvas.setFont('HeiseiKakuGo-W5', font_size)
    pdf_canvas.drawString(60, 755, '    年         月分')
    pdf_canvas.drawString(60, 745, '    年         月        　日　　　　 支給')

    # 所属
    data = [
        ['所属', ''],
        ['氏名', ''],
    ]
    table = Table(data, colWidths=(10 * mm, 40 * mm), rowHeights=(7 * mm, 7 * mm))
    table.setStyle(TableStyle([
        ('FONT', (0, 0), (1, 3), 'HeiseiKakuGo-W5', 9),
        ('BOX', (0, 0), (1, 3), 1, colors.black),
        ('INNERGRID', (0, 0), (1, 3), 1, colors.black),
        ('VALIGN', (0, 0), (1, 2), 'MIDDLE'),
        ('VALIGN', (0, 1), (1, 1), 'TOP'),
        ('VALIGN', (0, 3), (1, 3), 'TOP'),
    ]))
    table.wrapOn(pdf_canvas, 20 * mm, 242 * mm)
    table.drawOn(pdf_canvas, 20 * mm, 242 * mm)
    # 承認
    data = [
        ['承認者', '承認者', '承認者'],
        ['㊞', '㊞', '㊞'],
    ]
    table = Table(data, colWidths=(30 * mm, 30 * mm, 30 * mm), rowHeights=(7 * mm, 20 * mm))
    table.setStyle(TableStyle([
        ('FONT', (0, 0), (-1, -1), 'HeiseiKakuGo-W5', 9),
        ('BOX', (0, 0), (-1, -1), 1, colors.black),
        ('INNERGRID', (0, 0), (-1, -1), 1, colors.black),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    table.wrapOn(pdf_canvas, 110 * mm, 242 * mm)
    table.drawOn(pdf_canvas, 110 * mm, 242 * mm)

    data = [
        ['振込合計', ' ', '振込先', '　　　　　銀行', '　　　　支店', '口座番号'],

    ]
    table = Table(data,
                  colWidths=(20 * mm, 30 * mm, 15 * mm, 30 * mm, 30 * mm, 55 * mm),
                  rowHeights=7.5 * mm)
    table.setStyle(TableStyle([
        ('FONT', (0, 0), (-1, -1), 'HeiseiKakuGo-W5', 11),
        ('BOX', (0, 0), (-1, -1), 1, colors.black),
        ('INNERGRID', (0, 0), (-1, -1), 1, colors.black),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    table.wrapOn(pdf_canvas, 20 * mm, 232 * mm)
    table.drawOn(pdf_canvas, 20 * mm, 232 * mm)
    pdf_canvas.drawString(60, 645, '合計欄')
    data = [
        ['支給合計', ' ', '控除合計', '', '差引支給額', ''],

    ]
    table = Table(data,
                  colWidths=(20 * mm, 45 * mm, 18 * mm, 28 * mm, 22 * mm, 48 * mm),
                  rowHeights=7.5 * mm)
    table.setStyle(TableStyle([
        ('FONT', (0, 0), (-1, -1), 'HeiseiKakuGo-W5', 11),
        ('BOX', (0, 0), (-1, -1), 1, colors.black),
        ('INNERGRID', (0, 0), (-1, -1), 1, colors.black),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    table.wrapOn(pdf_canvas, 20 * mm, 218 * mm)
    table.drawOn(pdf_canvas, 20 * mm, 218 * mm)
    pdf_canvas.drawString(60, 585, '支給欄内訳')

    data = [
        ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
        ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
        ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
        ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
        ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
        ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
    ]
    table = Table(data,
                  colWidths=(18 * mm, 18 * mm, 18 * mm, 18 * mm, 18 * mm, 18 * mm, 18 * mm, 18 * mm, 18 * mm, 18 * mm,),
                  rowHeights=7.5 * mm)
    table.setStyle(TableStyle([
        ('FONT', (0, 0), (-1, -1), 'HeiseiKakuGo-W5', 11),
        ('BOX', (0, 0), (-1, -1), 1, colors.black),
        ('INNERGRID', (0, 0), (-1, -1), 1, colors.black),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    table.wrapOn(pdf_canvas, 20 * mm, 158 * mm)
    table.drawOn(pdf_canvas, 20 * mm, 158 * mm)


    pdf_canvas.drawString(60, 425, '控除欄内訳')

    data = [
        ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
        ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
        ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
        ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
        ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
        ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
        ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
        ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
    ]
    table = Table(data,
                  colWidths=(18 * mm, 18 * mm, 18 * mm, 18 * mm, 18 * mm, 18 * mm, 18 * mm, 18 * mm, 18 * mm, 18 * mm,),
                  rowHeights=7.5 * mm)
    table.setStyle(TableStyle([
        ('FONT', (0, 0), (-1, -1), 'HeiseiKakuGo-W5', 11),
        ('BOX', (0, 0), (-1, -1), 1, colors.black),
        ('INNERGRID', (0, 0), (-1, -1), 1, colors.black),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    table.wrapOn(pdf_canvas, 20 * mm, 88 * mm)
    table.drawOn(pdf_canvas, 20 * mm, 88 * mm)


    pdf_canvas.drawString(60, 235, '勤務状況')

    data = [
        ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
        ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
    ]
    table = Table(data,
                  colWidths=(18 * mm, 18 * mm, 18 * mm, 18 * mm, 18 * mm, 18 * mm, 18 * mm, 18 * mm, 18 * mm, 18 * mm,),
                  rowHeights=7.5 * mm)
    table.setStyle(TableStyle([
        ('FONT', (0, 0), (-1, -1), 'HeiseiKakuGo-W5', 11),
        ('BOX', (0, 0), (-1, -1), 1, colors.black),
        ('INNERGRID', (0, 0), (-1, -1), 1, colors.black),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    table.wrapOn(pdf_canvas, 20 * mm, 63 * mm)
    table.drawOn(pdf_canvas, 20 * mm, 63 * mm)

    pdf_canvas.drawString(60, 165, '有給振休')

    data = [
        ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],

    ]
    table = Table(data,
                  colWidths=(18 * mm, 18 * mm, 18 * mm, 18 * mm, 18 * mm, 18 * mm, 18 * mm, 18 * mm, 18 * mm, 18 * mm,),
                  rowHeights=7.5 * mm)
    table.setStyle(TableStyle([
        ('FONT', (0, 0), (-1, -1), 'HeiseiKakuGo-W5', 11),
        ('BOX', (0, 0), (-1, -1), 1, colors.black),
        ('INNERGRID', (0, 0), (-1, -1), 1, colors.black),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    table.wrapOn(pdf_canvas, 20 * mm, 43 * mm)
    table.drawOn(pdf_canvas, 20 * mm, 43 * mm)

    pdf_canvas.drawString(60, 99, '備考')

    data = [
        [''],

    ]
    table = Table(data,
                  colWidths=(180 * mm),
                  rowHeights=30 * mm)
    table.setStyle(TableStyle([
        ('FONT', (0, 0), (-1, -1), 'HeiseiKakuGo-W5', 11),
        ('BOX', (0, 0), (-1, -1), 1, colors.black),
        ('INNERGRID', (0, 0), (-1, -1), 1, colors.black),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    table.wrapOn(pdf_canvas, 20 * mm, 3 * mm)
    table.drawOn(pdf_canvas, 20 * mm, 3 * mm)





    # 1枚目終了
    pdf_canvas.showPage()





# 作成
if __name__ == '__main__':
    make()