from pypdf import PdfMerger
import os

merger = PdfMerger()
pdfs = []

iterator = [1,2,3,4,5,6,7,8,9,10]
finishedAt = 0
for i in iterator:
    try:
        merger.append(str(i) + ".pdf")
        finishedAt = i
    except:
        break

if finishedAt > 0:
    folderName = os.path.basename(os.path.dirname(os.path.realpath(str(finishedAt) + ".pdf")))
    merger.write(folderName + "_Responses.pdf")
merger.close()

