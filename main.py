import os
import pyttsx3
import pdfplumber


class PDFReader:
    """
    You just need to pass the book name
    PLEASE MAKE SURE THE PDF IS IN THE SAME PAGE
    """
    path = os.getcwd()
    maria_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_PT-BR_MARIA_11.0"
    speak = pyttsx3.init()
    speak.setProperty('voice', maria_voice_id)
    speak.setProperty("rate", 190)

    def __init__(self, file_name):
        self.file_name = file_name

    def read_page(self, page_number=0):
        """
        :param page_number: Read and specific page of any given PDF,
        default is the page 0 (book cover)
        :return: audio version of the page
        """

        with pdfplumber.open(os.path.join(self.path, f'{self.file_name}.pdf')) as pdf:
            text = pdf.pages[page_number].extract_text()
            self.speak.say(text)
            self.speak.runAndWait()
            self.speak.stop()
            pdf.close()

    def n_of_pages(self):
        with pdfplumber.open(os.path.join(self.path, f'{self.file_name}.pdf')) as pdf:
            text = len(pdf.pages)+1
            pdf.close()
            info = f'The PDF \'{self.file_name}\' has {text} pages'
            return info

    def read_the_whole_book(self):
        """
        Reads the whole book
        :return: audio version of the whole PDF
        """
        with pdfplumber.open(os.path.join(self.path, f'{self.file_name}.pdf')) as pdf:
            for page in range(len(pdf.pages)):
                text = pdf.pages[page].extract_text()
                self.speak.say(text)
                self.speak.runAndWait()
        self.speak.stop()
        pdf.close()

    def extract_data_of_page(self, page_number=0):
        """
        Extract the text data of the pdf of a given page
        :param page_number: default is the page 0 (book cover)
        :return:
        """
        print(f'\n\nLendo: \'{self.file_name.upper()}\'')
        with pdfplumber.open(os.path.join(self.path, f'{self.file_name}.pdf')) as pdf:
            text = pdf.pages[page_number].extract_text()
            return text


if __name__ == '__main__':
    book = PDFReader('Os Homens Que Nao Amavam as Mulheres - Stieg Larsson')
    print(book.extract_data_of_page(5))
    book.read_page(5)
