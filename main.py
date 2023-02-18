from pypdf import PdfMerger
import os
folderName = os.path.basename(os.path.expanduser('~'))

merger = PdfMerger()
pdfs = []
failed = False

iterator = [1,2,3,4,5,6,7,8,9,10]
for i in iterator:
    try:
        merger.append(str(i) + ".pdf")
    except:
        if i==1:
            failed = True
        break

if failed == False:
    merger.write(folderName + "_Responses.pdf")
merger.close()

