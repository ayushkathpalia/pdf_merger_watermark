import PyPDF2


def apply_watermark():
    template = PyPDF2.PdfFileReader(open('merged_pdf.pdf', 'rb'))
    watermark = PyPDF2.PdfFileReader(open('wtr.pdf', 'rb'))
    output = PyPDF2.PdfFileWriter()

    for i in range(template.getNumPages()):
        page = template.getPage(i)
        page.mergePage(watermark.getPage(0))
        output.addPage(page)

        with open('watermarked_output.pdf', 'wb') as file:
            output.write(file)


apply_watermark()
