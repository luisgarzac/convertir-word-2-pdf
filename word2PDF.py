# De la librería docx2pdf importamos convert
from docx2pdf import convert

# la función convert tiene el siguiente formato --> convert(docx,pdf)
convert("archivo1.docx", "archivo1_word2pdf.pdf")