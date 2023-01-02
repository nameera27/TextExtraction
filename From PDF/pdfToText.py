import PyPDF2
a = PyPDF2.PdfReader('cs.pdf')
print(a.documentInfo)
print(a.getNumPages())
str = ' '
for i in range(1,11):
    str += a.getPage(i).extract_text()

with open('text.txt','w',encoding='utf-8') as f:
    f.write(str)