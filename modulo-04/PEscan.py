# Importar o modulo de analise de arquivo PE
import pefile

def func5():
    #file = input("Select File: ")
    #pe = pefile.PE(file)
        # Passando o paramento pe.file e definindo o exe que vai ser usado 
        pe = pefile.P("test.exe")
        # printar todos os cabeçalhos do arquivo
        pe.print_info() # Prints all Headers in a human readable format
        # Abaixo ele printa os hexadeciminal do cabeçalho DOS e_magic e lfanew
    #print("e_magic : " + hex(pe.DOS_HEADER.e_magic)) # Prints the e_magic field of the DOS_HEADER
    #print("e_lfnew : " + hex(pe.DOS_HEADER.e_lfanew)) # Prints the E_lfnew field of the DOS_HEADER

    #e_magic -> o número mágico do cabeçalho do DOS é 'mZ' (0x5aa4d) e 'MZ' refere-se a Mark Zbikowski, o criador o formato de arquivo executável do MS-DOS.
#e_lfnew -> um ponteiro para o cabeçalho PE (NT Header).
# Para a maioria dos programas do Windows, o cabeçalho DOS contém um programa DOS que não faz nada além de imprimir "Este programa não pode ser executado no modo DOS".
if __name__ == '__main__':
    func5()
    