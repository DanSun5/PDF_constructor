from fpdf import FPDF

pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.set_auto_page_break(auto=False, margin=0)

pdf.add_page()

# header
pdf.set_font(family='Times', style='B', size=20)
pdf.cell(w=0, h=12, txt="Hello World!", align='L', ln=1, border=0)

# line on page
for i in range(20, 235, 10):
    pdf.line(10, i, 200, i)
pdf.line(10, 21, 200, 21)

# text in page
pdf.set_font(family='Times', style='B', size=15)
pdf.cell(w=0, h=12, txt="Hi there!", align='L', ln=1, border=0)

# footer
pdf.ln(245)

pdf.set_font(family='Times', style='I', size=10)
pdf.set_text_color(180, 180, 180)
pdf.cell(w=0, h=12, txt="OwO", align='R', ln=1, border=0)


pdf.output('output.pdf')
