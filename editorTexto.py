from tkinter import Frame, Tk, BOTH, Text, Menu, END, filedialog
from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo

class EditorTexto(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.iniGui()
    def iniGui(self):
        """rows = 0
        while rows < 50:
            self.parent.rowconfigure(rows, weight =1)
            self.parent.columnconfigure(rows, weight = 1)
            rows += 1"""
        
        self.parent.title('Busqueda')
        self.pack(fill = BOTH, expand =1)
        barraMenu = Menu(self.parent)
        self.parent.config(menu = barraMenu)

        fileBuscar = Menu(barraMenu)
        fileBuscar.add_command(label = 'Busqueda en el texto', command = self.algoritmoBoyer)

        fileMenu = Menu(barraMenu)
        fileMenu.add_command(label = 'Abrir', command = self.openFile)
        fileMenu.add_command(label = 'Guardar', command = self.saveAs)
        fileMenu.add_command(label = 'Salir', command = self.parent.destroy)
        barraMenu.add_cascade(label = 'Archivo', menu = fileMenu)
        barraMenu.add_cascade(label = 'Buscar', menu = fileBuscar)

        self.txt= Text(self)
        self.txt.pack(fill = BOTH, expand = 1)
    
    def openFile(self):
        ftypes = [('Text files', '*.txt'), ('All files', '*')]
        dialog = filedialog.Open(self, filetypes = ftypes)
        archivo = dialog.show()

        if archivo != '':
            text = self.readFile(archivo)
            self.txt.insert(END, text)
    
    def readFile(self, nombreArchivo):
        f = open(nombreArchivo, 'r')
        text = f.read()
        return text
    
    def saveAs(self):
        toSave = self.txt.get("1.0", "end-1c")
        saveLocation = filedialog.asksaveasfilename()
        fileToSave = open(saveLocation, "w+")
        fileToSave.write(toSave)
        fileToSave.close()

    def malCaracter(self, patron, tamano):
        malCaracter = [-1]*256
        
        for i in range(tamano):
            malCaracter[ord(patron[i])] = i
        
        return malCaracter
    
    def buscarEnCadena(self, cadenaTexto, patronComparar):
        tamanoPatron = len(patronComparar)
        tamanoCadena = len(cadenaTexto)

        caracterIncorrecto = self.malCaracter(patronComparar, tamanoPatron)

        s = 0
        while s < tamanoCadena - tamanoPatron:
            j = tamanoPatron - 1

            while j>= 0 and patronComparar[j] == cadenaTexto[s+j]:
                j-=1
            
            if j<0:
                print("Patron ocurre en la posicion= {}".format(s))
                print(cadenaTexto[(s-3):(s+tamanoPatron+5)])

                
                s+= (tamanoPatron - caracterIncorrecto[ord(cadenaTexto[s+tamanoPatron])] if s+tamanoPatron<tamanoCadena else 1)
            else:
                s+= max(1, j-caracterIncorrecto[ord(cadenaTexto[s+j])])
        
    def algoritmoBoyer(self):
        toSearch = self.txt.get('1.0', 'end-1c')
        textToSearch = askstring('Buscar','Ingrese texto a buscar:')
        self.buscarEnCadena(toSearch, textToSearch)
        

def main():
    root = Tk()
    EditorTexto(root)
    root.geometry('800x800')
    root.mainloop()

if __name__ == '__main__':
    main()