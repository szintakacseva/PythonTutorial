from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import Table, TableStyle, SimpleDocTemplate, Image
from reportlab.platypus.para import Paragraph

'''Table(data, colWidths=None, rowHeights=None, style=None, splitByRow=1,
repeatRows=0, repeatCols=0)'''

'''
TableStyle
FONT - takes fontname, optional fontsize and optional leading.
FONTNAME (or FACE) - takes fontname.
FONTSIZE (or SIZE) - takes fontsize in points; leading may get out of sync.
LEADING - takes leading in points.
TEXTCOLOR - takes a color name or (R,G,B) tuple.
ALIGNMENT (or ALIGN) - takes one of LEFT, RIGHT and CENTRE (or CENTER) or DECIMAL.
LEFTPADDING - takes an integer, defaults to 6.
RIGHTPADDING - takes an integer, defaults to 6.
BOTTOMPADDING - takes an integer, defaults to 3.
TOPPADDING - takes an integer, defaults to 3.
BACKGROUND - takes a color.
ROWBACKGROUNDS - takes a list of colors to be used cyclically.
COLBACKGROUNDS - takes a list of colors to be used cyclically.
VALIGN - takes one of TOP, MIDDLE or the default BOTTOM
'''

def mydrawtable1():
    story = []
    data = [['00', '01', '02', '03', '04'],
            ['10', '11', '12', '13', '14'],
            ['20', '21', '22', '23', '24'],
            ['30', '31', '32', '33', '34']]
    t = Table(data)
    t.setStyle(TableStyle([('BACKGROUND', (1, 1), (-2, -2), colors.green),
                           ('TEXTCOLOR', (0, 0), (1, -1), colors.red)]))
    story.append(t)
    doc = SimpleDocTemplate('mytables.pdf', pagesize=letter)
    doc.build(story)

def mydrawtable2():
    story = []
    data = [['00', '01', '02', '03', '04'],
            ['10', '11', '12', '13', '14'],
            ['20', '21', '22', '23', '24'],
            ['30', '31', '32', '33', '34']]
    t = Table(data, 5 * [0.4 * inch], 4 * [0.4 * inch])
    t.setStyle(TableStyle([('ALIGN', (1, 1), (-2, -2), 'RIGHT'),
                           ('TEXTCOLOR', (1, 1), (-2, -2), colors.red),
                           ('VALIGN', (0, 0), (0, -1), 'TOP'),
                           ('TEXTCOLOR', (0, 0), (0, -1), colors.blue),
                           ('ALIGN', (0, -1), (-1, -1), 'CENTER'),
                           ('VALIGN', (0, -1), (-1, -1), 'MIDDLE'),
                           ('TEXTCOLOR', (0, -1), (-1, -1), colors.green),
                           ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
                           ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
                           ]))
    story.append(t)
    doc = SimpleDocTemplate('mytables.pdf', pagesize=letter)
    doc.build(story)

def mydrawtable3():
    story = []

    data = [['00', '01', '02', '03', '04'],
            ['10', '11', '12', '13', '14'],
            ['20', '21', '22', '23', '24'],
            ['30', '31', '32', '33', '34']]
    t = Table(data, style=[('GRID', (1, 1), (-2, -2), 1, colors.green),
                           ('BOX', (0, 0), (1, -1), 2, colors.red),
                           ('LINEABOVE', (1, 2), (-2, 2), 1, colors.blue),
                           ('LINEBEFORE', (2, 1), (2, -2), 1, colors.pink),
                           ])
    story.append(t)
    doc = SimpleDocTemplate('mytables.pdf', pagesize=letter)
    doc.build(story)

def mydrawtable4():
    szoveg0 = '''1'''

    styleSheet = getSampleStyleSheet()
    style1 = styleSheet['Normal']
    story = []
    P0 = Paragraph(szoveg0, style1)
    P = Paragraph('''
    <para align=center spaceb=3>The <b>ReportLab Left
    <font color=red>Logo</font></b>
    Image</para>''',
                  styleSheet['BodyText'])
    data = [['A', 'B', 'C', P0, 'D'],
            ['00', '01', '02', P, '04'],
            ['10', '11', '12', P, '14'],
            ['20', '21', '22', '23', '24'],
            ['30', '31', '32', '33', '34']]
    t = Table(data, style=[('GRID', (1, 1), (-2, -2), 1, colors.green),
                           ('BOX', (0, 0), (1, -1), 2, colors.red),
                           ('LINEABOVE', (1, 2), (-2, 2), 1, colors.blue),
                           ('LINEBEFORE', (2, 1), (2, -2), 1, colors.pink),
                           ('BACKGROUND', (0, 0), (0, 1), colors.pink),
                           ('BACKGROUND', (1, 1), (1, 2), colors.lavender),
                           ('BACKGROUND', (2, 2), (2, 3), colors.orange),
                           ('BOX', (0, 0), (-1, -1), 2, colors.black),
                           ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
                           ('VALIGN', (3, 0), (3, 0), 'BOTTOM'),
                           ('BACKGROUND', (3, 0), (3, 0), colors.limegreen),
                           ('BACKGROUND', (3, 1), (3, 1), colors.khaki),
                           ('ALIGN', (3, 1), (3, 1), 'CENTER'),
                           ('BACKGROUND', (3, 2), (3, 2), colors.beige),
                           ('ALIGN', (3, 2), (3, 2), 'LEFT'),
                           ])
    t._argW[3] = 1.5 * inch
    story.append(t)
    doc = SimpleDocTemplate('mytables.pdf', pagesize=letter)
    doc.build(story)

def mydrawimage():
    story = []
    #im = Image(20,10, width=2 * inch, height=2 * inch, path="images/replogo.gif")

    #I = Image(0, 0, 110, 44, 'images/replogo.gif')
    #story.append(im)
    story.append(Image('images/replogo.gif'))
    doc = SimpleDocTemplate('mytables.pdf', pagesize=letter)
    doc.build(story)

def concattables():
    ceg = [["Szolgáltató"],
           ['selectedCeg.nev'],
           ['cegcim1'],
           ['cegadoszam'],
           ['cegbankszamlaszam'],
           ['cegemail'],
           ['cegweblap1'],
           ['']]


    megrendelo = [["Megrendelő:"],
              ['selectedVevo.nev'],
              ['vevocim'],
              ['vevorendszam'],
              ['vevogyartmany'],
              ['vevogepjarmutipus'],
              ['vevogepjarmufajta'],
              ['vevogepjarmukmh']]

    cegadatoklist = [[ceg, megrendelo]]


    cegtable1 = Table(ceg, colWidths=[2*inch])
    cegtable2 = Table(megrendelo, colWidths=[2*inch])
    cegadatoktable = [[cegtable1, cegtable2]]
    '''
    cegadatoktable.setStyle(TableStyle([('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
                              ('FONT', (0, 0), (-1, -1), 'DejaVuSerif'),
                              ('BOX', (0, 0), (-1, -1), 0.5, colors.black)]))

    '''
    shell_table = Table(cegadatoktable, colWidths=[2*inch, 2*inch])
    shell_table.setStyle(TableStyle([('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
                              ('BOX', (0, 0), (-1, -1), 0.5, colors.black)]))
    story= []
    story.append(shell_table)
    doc = SimpleDocTemplate('mytables.pdf', pagesize=letter)
    doc.build(story)

#mydrawtable1()
#mydrawtable2()
#mydrawtable3()
#mydrawtable4()
#mydrawimage()
concattables()