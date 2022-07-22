import PyPDF2

with open("D:\\Projects\\Python\\pdf\\speech.pdf", "rb") as file:
    reader = PyPDF2.PdfFileReader(file)
    page = reader.getPage(0)
    page.rotate_clockwise(90)
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    with open("D:\\Projects\\Python\\pdf\\rotated.pdf", "wb") as output:
        writer.write(output)
