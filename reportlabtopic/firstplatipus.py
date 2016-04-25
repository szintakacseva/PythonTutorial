import os
import reportlab
from _tracemalloc import start

from reportlab.lib import styles
from reportlab.lib.colors import black, green, Color, yellow
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Frame
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.rl_config import defaultPageSize
from reportlab.lib.units import inch

PAGE_HEIGHT=defaultPageSize[1];
PAGE_WIDTH=defaultPageSize[0]
folder = os.path.dirname(reportlab.__file__) + os.sep + 'fonts'

class MyPlatipus:
  def  __init__(self, *args, **kwargs):
    self.styles = getSampleStyleSheet()
    self.Title = "Hello world"
    self.pageinfo = "platypus example"

  def myFirstPage(self, canvas, doc):
    canvas.saveState()
    canvas.setFont('Times-Bold',16)
    canvas.drawCentredString(PAGE_WIDTH/2.0, PAGE_HEIGHT-108, self.Title)
    canvas.setFont('Times-Roman',9)
    canvas.drawString(inch, 0.75 * inch, "First Page / %s" % self.pageinfo)
    canvas.restoreState()

  def myLaterPages(self,canvas, doc):
    canvas.saveState()
    canvas.setFont('Times-Roman',9)
    canvas.drawString(inch, 0.75 * inch, "Page %d %s" % (doc.page, self.pageinfo))
    canvas.restoreState()

  def go(self):
    doc = SimpleDocTemplate("phello.pdf")
    Story = [Spacer(1,2*inch)]
    style = self.styles["Normal"]
    for i in range(100):
        bogustext = ("This is Paragraph number %s.  " % i) *20
        p = Paragraph(bogustext, style)
        Story.append(p)
        Story.append(Spacer(1,0.2*inch))
    doc.build(Story, onFirstPage=self.myFirstPage, onLaterPages=self.myLaterPages)

def myFlowableCanvas():
    pdfmetrics.registerFont(TTFont('tahoma', 'tahoma.ttf'))
    styleSheet = getSampleStyleSheet()
    style = styleSheet['BodyText']
    P = Paragraph('Példa Őöüéáűűűűűű', style)
    canv = Canvas('flowablecanvas.pdf')
    aW = 460  # available width and height
    aH = 800
    w, h = P.wrap(aW, aH)  # find required space
    if w <= aW and h <= aH:
        P.drawOn(canv, 0, aH)
        aH = aH - h  # reduce the available height
        canv.save()
    else:
        raise ValueError("Not enough room")

def myUsingFrames():
    styleSheet = getSampleStyleSheet()
    styleN = styleSheet['Normal']
    styleH = styleSheet['Heading1']
    story = []

    story.append(Paragraph('This is a heading:: ŐŐŐŐŐÚÚÚÜÜÜ', styleH, encoding='utf8'))
    story.append(Paragraph('This is <i>normal</i> paragraph:: ŐŐŐŐŐÚÚÚÜÜÜ', styleN, encoding='utf8'))
    c = Canvas("usingframes.pdf")
    f = Frame(inch, inch, 6*inch, 9*inch, showBoundary=1)
    f.addFromList(story,c)
    c.save()

def mySimpleTemplate():
    styles = getSampleStyleSheet()
    styleN = styles['Normal']
    styleH = styles['Heading1']
    story = []
    # add some flowables
    story.append(Paragraph("This is a Heading", styleH))
    story.append(Paragraph("This is a paragraph in <i>Normal</i> style.",
                           styleN))
    doc = SimpleDocTemplate('mydoc.pdf', pagesize=letter)
    doc.build(story)

def myParagraphStyles():
    szoveg5 = '''<b>You are hereby charged</b>
that on the 28th day of May,
1970, you did willfully,
unlawfully, and <i>with malice
of forethought</i>, publish an
alleged English-Hungarian phrase
book with intent to cause a
breach of the peace. <u>How do
you plead</u>?'''

    szoveg6 = '''This <a href="#MYANCHOR"
color="blue">is a link to</a> an
anchor tag ie <a
name="MYANCHOR"/><font
color="green">here</font>. This
<link href="#MYANCHOR"
color="blue"
fontName="Helvetica">is another
link to</link> the same anchor
tag.'''
    szoveg7 = '''<strong>You are hereby
charged</strong> that on the
28th day of May, 1970, you did
willfully, unlawfully,
<strike>and with malice of
forethought</strike>,
<br/>publish an alleged
English-Hungarian phrase book
with intent to cause a breach of
the peace. How do you plead?'''

    szoveg8 = '''<font face="times"
color="red">You are hereby
charged</font> that on the 28th
day of May, 1970, you did
willfully, unlawfully, and <font
size=14>with malice of
forethought</font>, publish an
alleged English-Hungarian phrase
book with intent to cause a
breach of the peace. How do you
plead?'''

    szoveg9 = '''Equation (&alpha;):
<greek>e</greek>
<super><greek>ip</greek></super>
= -1'''

    szoveg10 = '''<para autoLeading="off"
fontSize=12>This &lt;img/&gt;
<img src="images/testimg.gif"
valign="top"/> is aligned
<b>top</b>.<br/><br/> This
&lt;img/&gt; <img
src="images/testimg.gif"
valign="bottom"/> is aligned
<b>bottom</b>.<br/><br/> This
&lt;img/&gt; <img
src="images/testimg.gif"
valign="middle"/> is aligned
<b>middle</b>.<br/><br/> This
&lt;img/&gt; <img
src="images/testimg.gif"
valign="-4"/> is aligned
<b>-4</b>.<br/><br/> This
&lt;img/&gt; <img
src="images/testimg.gif"
valign="+4"/> is aligned
<b>+4</b>.<br/><br/> This
&lt;img/&gt; <img
src="images/testimg.gif"
width="10"/> has width
<b>10</b>.<br/><br/> </para>'''

    szoveg11 = '''<seq id="spam"/>, <seq
id="spam"/>, <seq id="spam"/>.
Reset<seqreset id="spam"/>. <seq
id="spam"/>, <seq id="spam"/>,
<seq id="spam"/>.'''

    szoveg12 = '''<seqdefault
id="spam"/>Continued... <seq/>,
<seq/>, <seq/>, <seq/>, <seq/>,
<seq/>, <seq/>.'''

    szoveg13 = '''Figure <seq template="%(Chapter)
s-%(FigureNo+)s"/> - Multi-level templates'''

    defaults = {
        'fontName': 'Times-Roman',
        'fontSize': 10,
        'leading': 12,
        'leftIndent': 0,
        'rightIndent': 0,
        'firstLineIndent': 0,
        'alignment': TA_LEFT,
        'spaceBefore': 0,
        'spaceAfter': 0,
        'bulletFontName': 'Times-Roman',
        'bulletFontSize': 10,
        'bulletIndent': 0,
        'textColor': black,
        'backColor': None,
        'wordWrap': None,
        'borderWidth': 0,
        'borderPadding': 0,
        'borderColor': None,
        'borderRadius': None,
        'allowWidows': 1,
        'allowOrphans': 0,
    }
    pdfmetrics.registerFont(TTFont('tahoma', 'tahoma.ttf'))
    pdfmetrics.registerFont(TTFont('DejaVuSans', 'DejaVuSans.ttf'))

    pdfmetrics.registerFont(TTFont('DejaVuSerif', 'DejaVuSerif.ttf'))
    pdfmetrics.registerFont(TTFont('DejaVuSerifB', 'DejaVuSerif-Bold.ttf'))
    pdfmetrics.registerFont(TTFont('DejaVuSerifI', 'DejaVuSerif-Italic.ttf'))
    pdfmetrics.registerFont(TTFont('DejaVuSerifBI', 'DejaVuSerif-BoldItalic.ttf'))
    pdfmetrics.registerFontFamily('DejaVuSerif', normal='DejaVuSerif', bold='DejaVuSerifB', italic='DejaVuSerifI', boldItalic='DejaVuSerifBI')

    BdFile = os.path.join(folder, 'VeraBd.ttf')
    ItFile = os.path.join(folder, 'VeraIt.ttf')
    BIFile = os.path.join(folder, 'VeraBI.ttf')


    pdfmetrics.registerFont(TTFont('Vera', 'Vera.ttf'))
    pdfmetrics.registerFont(TTFont('VeraBd', 'VeraBd.ttf'))
    pdfmetrics.registerFont(TTFont('VeraIt', 'VeraIt.ttf'))
    pdfmetrics.registerFont(TTFont('VeraBI', 'VeraBI.ttf'))
    pdfmetrics.registerFontFamily('Vera', normal='Vera', bold='VeraBd', italic='VeraIt', boldItalic='VeraBI')


    paragraphstyles = getSampleStyleSheet()
    paragraphstyles.add(ParagraphStyle(name='myPStyle1', fontName='tahoma'))
    paragraphstyles.add(ParagraphStyle(name='myPStyle2', fontName='tahoma', fontSize = 18, textcolor=Color(1,0,0,0),
                                       backcolor =Color(0,8,9,1), borderWidth=1))
    paragraphstyles.add(ParagraphStyle(name='myPStyle3', spaceBefore = 16, fontName = 'tahoma', bulletFontName = 'tahoma',
                                       borderRadius = None, firstLineIndent = 0, leftIndent = 0, underlineProportion = 0.0,
                                       rightIndent = 0, wordWrap = None, allowWidows = 1, backColor = None, textTransform = None,
                                       alignment = 0, borderColor = None, splitLongWords = 1, leading = 16, bulletIndent = 0,
                                       allowOrphans = 0, bulletFontSize = 10, fontSize = 10,borderWidth = 0,bulletAnchor = start,
                                       borderPadding = 0, endDots = None, textColor = green, spaceAfter = 16))
    paragraphstyles.add(ParagraphStyle(name='myPStyle4', spaceBefore=22, fontName='DejaVuSerif', bulletFontName='DejaVuSerif',
                                       borderRadius=None, firstLineIndent=0, leftIndent=0, underlineProportion=0.0,
                                       rightIndent=0, wordWrap=None, allowWidows=1, backColor=yellow, textTransform=None,
                                       alignment=0, borderColor=green, splitLongWords=1, leading=16, bulletIndent=0,
                                       allowOrphans=0, bulletFontSize=10, fontSize=10, borderWidth=1,
                                       bulletAnchor=start,
                                       borderPadding=0, endDots=None, textColor=green, spaceAfter=16))

    parastyle1 = paragraphstyles['myPStyle1']
    parastyle2 = paragraphstyles['myPStyle2']
    parastyle3 = paragraphstyles['myPStyle3']
    parastyle4 = paragraphstyles['myPStyle4']
    parastyle6 = paragraphstyles['Normal']

    story = []
    # add some flowables
    story.append(Paragraph("Első paragrafus:::ŐŐŐŐÖÖÜÜűŰŰŰŰŰÚÚÚÚ", parastyle1))
    story.append(Paragraph("Második paragrafus:::ŐŐŐŐÖÖÜÜűŰŰŰŰŰÚÚÚÚ", parastyle2))
    story.append(Paragraph("Harmadik paragrafus:::ŐŐŐŐÖÖÜÜűŰŰŰŰŰÚÚÚÚ", parastyle3))
    story.append(Paragraph("Negyedik paragrafus:::ŐŐŐŐÖÖÜÜűŰŰŰŰŰÚÚÚÚ", parastyle4))
    story.append(Paragraph("Ötödik paragrafus "+szoveg5+":::ŐŐŐŐÖÖÜÜűŰŰŰŰŰÚÚÚÚ", parastyle4))
    story.append(Paragraph("Hatodik paragrafus "+szoveg6 + ":::ŐŐŐŐÖÖÜÜűŰŰŰŰŰÚÚÚÚ", parastyle6))
    story.append(Paragraph("Hetedik paragrafus " + szoveg7 + ":::ŐŐŐŐÖÖÜÜűŰŰŰŰŰÚÚÚÚ", parastyle6))
    story.append(Paragraph("Nyolcadik paragrafus " + szoveg8 + ":::ŐŐŐŐÖÖÜÜűŰŰŰŰŰÚÚÚÚ", parastyle4))
    story.append(Paragraph("Kilencedik paragrafus " + szoveg9 + ":::ŐŐŐŐÖÖÜÜűŰŰŰŰŰÚÚÚÚ", parastyle4))
    story.append(Paragraph(szoveg10, parastyle4))
    story.append(Paragraph(szoveg11, parastyle4))
    story.append(Paragraph(szoveg12, parastyle4))
    story.append(Paragraph(szoveg13, parastyle4))

    doc = SimpleDocTemplate('mypara.pdf', pagesize=letter)
    doc.build(story)

#report = MyPlatipus()
#report.go()
#myFlowableCanvas()
#myUsingFrames()
#mySimpleTemplate()
myParagraphStyles()