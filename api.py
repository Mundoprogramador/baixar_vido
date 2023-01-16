#importando_as bliblioteca
from tkinter import *
from pytube import YouTube
from tkinter import filedialog
from pytube.exceptions import RegexMatchError
def api_tub():
		
	#criando um variavel para receber a janela e criando um titulo 
	janela = Tk()
	janela.title('Baixando videos do youtube')
	
	#criando uma funçao da biblioteca pytube
	def dowload(link_):
	    if link_:
	        try:
	            pasta = filedialog.askdirectory()
	            YouTube(link_).streams.get_highest_resolution().download(pasta)
	            aviso()
	        except RegexMatchError:
	            aviso_erro()
	    else:
	        aviso_erro()
	
	#criando una funçao de aviso 
	def aviso():
	    janela_msg = Toplevel()
	    janela_msg.title('Aviso')
	    janela_msg.geometry()
	
	    Label(janela_msg, text='Dowload concluido', font='arial 12 bold', pady=30).pack()
	#crianro um button 
	    Button(janela_msg, text='OK', command=janela_msg.destroy).pack()
	
	#funçao de erro 
	def aviso_erro():
	    janela_msg = Toplevel()
	    janela_msg.title('Aviso')
	    janela_msg.geometry()
	
	    Label(janela_msg, text='Insira um link válido', font='arial 12 bold', pady=30).pack()
	
	    Button(janela_msg, text='OK', command=janela_msg.destroy).pack()
	
	
	quadro = Frame(janela)
	quadro.pack()
	
	Label(quadro, text='Inserir link: ', font='arial 12 bold').pack(side='left')
	link = Entry(quadro, font='arial 20', width=10)
	link.pack(side='left')
	
	Button(quadro, bg='green', text='>>>', bd=1, fg='white', width=4, height=2, command=lambda: dowload(link.get())).pack()
	janela.mainloop()
api_tub()
