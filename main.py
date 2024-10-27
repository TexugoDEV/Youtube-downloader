import PySimpleGUI as sg
from pytubefix import YouTube

sg.theme("Dark Blue 16")

# Layout da interface gráfica
interface = [
    [sg.Text("URL")],
    [sg.Input(size=(50, 1), key="url")],
    [sg.Button("Download")]
]

# Janela com o título no Titlebar
janela = sg.Window("YouTube Downloader", interface)

while True:
    evento, valor = janela.read()

    if evento == sg.WIN_CLOSED:
        break

    if evento == "Download":
        link = valor["url"]
        try:
            video = YouTube(link)
            stream = video.streams.get_highest_resolution()
            stream.download()
            print("Download concluído")
        except Exception as e:
            print(f"Erro: {e}")

janela.close()