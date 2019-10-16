from tkinter import Frame, Tk, BOTH, Text, Menu, END, filedialog

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

        fileMenu = Menu(barraMenu)
        fileMenu.add_command(label = 'Abrir', command = self.openFile)
        fileMenu.add_command(label = 'Guardar', command = self.saveAs)
        fileMenu.add_command(label = 'Salir', command = self.parent.destroy)
        barraMenu.add_cascade(label = 'Archivo', menu = fileMenu)

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


def main():
    root = Tk()
    EditorTexto(root)
    root.geometry('800x800')
    root.mainloop()

if __name__ == '__main__':
    main()