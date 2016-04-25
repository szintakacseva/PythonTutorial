import os

import reportlab.rl_config
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

reportlab.rl_config.warnOnMissingFontGlyphs = 0
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

from reportlab.pdfbase.pdfmetrics import registerFontFamily
registerFontFamily('Vera',normal='Vera',bold='VeraBd',italic='VeraIt',boldItalic='VeraBI')

folder = os.path.dirname(reportlab.__file__) + os.sep + 'fonts'
ttffile = os.path.join(folder, 'tahoma.ttf')

pdfmetrics.registerFont(TTFont('Vera', 'Vera.ttf'))
pdfmetrics.registerFont(TTFont('VeraBd', 'VeraBd.ttf'))
pdfmetrics.registerFont(TTFont('VeraIt', 'VeraIt.ttf'))
pdfmetrics.registerFont(TTFont('VeraBI', 'VeraBI.ttf'))
pdfmetrics.registerFont(TTFont('tahoma', 'tahoma.ttf'))
pdfmetrics.registerFont(TTFont('DejaVuSans', 'DejaVuSans.ttf'))
pdfmetrics.registerFont(TTFont('consola', 'consola.ttf'))
pdfmetrics.registerFont(TTFont('seguisym', 'seguisym.ttf'))
pdfmetrics.registerFont(TTFont('kokila', 'kokila.ttf'))
pdfmetrics.registerFont(TTFont('kalinga', 'kalinga.ttf'))

c = canvas.Canvas("FontTutorial.pdf", bottomup = 0, pagesize=A4)
c.setFont('kalinga', 14)
c.drawString(10, 50, "Some text encoded in UTF-8::::ŐŐŐŐŐŰŰŰŰŰ")
c.drawString(10, 70, "In the " +ttffile+" ÉÁőŐóÓ")
c.save()
print(folder)