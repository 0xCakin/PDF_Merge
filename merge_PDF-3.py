##################################################################################################################################
# Author = Caner Akin                                                                                                            #
# Date = October 01, 2021                                                                                                        #
# Purpose = Merge PDFs from the given folder path                                                                                #
# REF = Found in geektechstuff.com                                                                                               #
# Requirements = 
#       - Python3
#       - PyPDF2 library:                                                                                                        #
#           PIP - pip install PyPDF2                                                                                             #
#           ANACONDA/CONDA - conda install -c conda-forge pypdf2                                                                 #
# Direction = The code will ask for the related folder and export name. Make sure that the folder link doesn't have space.       #
#       Example:                                                                                                                 #
#           Folder path to PDFs that need merging: C:\example\Caner                                                              #
#           What should I call the file? test_caner                                                                              # 
##################################################################################################################################


#Requires the “PyPDF2” and “OS” modules to be imported
import os, PyPDF2
def main():
    #Ask user where the PDFs are
    userpdflocation=input("Folder path to PDFs that need merging:")

    #Sets the scripts working directory to the location of the PDFs
    os.chdir(userpdflocation)

    #Ask user for the name to save the file as
    userfilename=input("What should I call the file?")
    
    # if the user types .pdf at the end of the file, will not keep adding
    #   prevents output.pdf.pdf
    if not userfilename.endswith('.pdf'):
        userfilename += '.pdf'
        
    #Get all the PDF filenames
    pdf2merge = []
    for filename in os.listdir("."):
        if filename.endswith(".pdf"):
            pdf2merge.append(filename)

    pdfWriter = PyPDF2.PdfFileWriter()

    #loop through all PDFs
    for filename in pdf2merge:

    #rb for read binary
        pdfFileObj = open(filename,"rb")
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    #Opening each page of the PDF
        for pageNum in range(pdfReader.numPages):
            pageObj = pdfReader.getPage(pageNum)
            pdfWriter.addPage(pageObj)

    #save PDF to file, wb for write binary
    pdfOutput = open(userfilename, "wb")

    #Outputting the PDF
    pdfWriter.write(pdfOutput)

    #Closing the PDF writer
    pdfOutput.close()

if __name__ == "__main__":
    main()