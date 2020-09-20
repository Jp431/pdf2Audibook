# pdf2Audibook

## ENG-US:
  Extract data from a PDF file and read it outlound, basically creating a audiobook of any given pdf.
  I will commit latter changes to this project, such as the ability to export a .mp3 file and a possible machine learning approach to ignore specific data such as page number, header and footer.
  
  ### Current version functions:
  - **read_page** = Reads the specified page outloud, if no page is given it will read the cover page.
  - **n_of_pages** = returns the amount of pages on the specified PDF file. 
  - **read_the_whole_book** = Reads the whole PDF file beginning to end.
  - **extract_data_of_page** = Extract the text information of any given page, can be used with *print()* to display text data in the terminal.
  
  
## PT-BR:
  Extrai dados (text) de um arquivo PDF e lê em voz alta, basicamente criando um áudiolivro.
  Eu ainda irei incrementar, em versões futuras, a habilidade de exportar uma versão .mp3 do arquivo e possivelmente um modelo de ML para ignorar partes espeficias como número de página, cabeçalhos e rodapé.
    
  ### Funções da versão atual:
  - **read_page** = Lê uma página especifica em voz alta, se nenhum parametro for dado, o programa irá ler a capa
  - **n_of_pages** = Retorna o número de páginas do PDF.
  - **read_the_whole_book** = Lê o livro todo, do começo ao fim.
  - **extract_data_of_page** = Extrai o texto de uma página, pode ser usado com *print()* para mostrar as informações no terminal de comando.
  
