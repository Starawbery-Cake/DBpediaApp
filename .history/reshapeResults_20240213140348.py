import PySimpleGUI as sg

def main():
  layout = [
    [sg.Frame("graph", [[sg.Image("white.png")]])],
    [sg.Frame("operate", [
      [sg.Text("キーワードを入力してください："), sg.in]
    ])]
  ]

if __name__ == "__main__":
  main()