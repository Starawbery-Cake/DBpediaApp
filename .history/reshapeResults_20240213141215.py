import PySimpleGUI as sg

def main():
  layout = [
    [
      sg.Frame("graph", [[sg.Image("white.png")]]),
      sg.Frame("operate", [
        [sg.Text("キーワードを入力してください："), sg.InputText(), sg.Button("検索")],
        [sg.Text("概要：")],
        [sg.Text("abst")],
        [sg.Text("Error message here")],
        [sg.Text("検索結果"), sg.Button("決定")],
        [sg.Listbox(["hoge"], size=())]
      ])
    ],
  ]

  window = sg.Window("InputText Widget Example", layout)

  while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == "Submit":
        name = values[0]
        password = values[1]
        sg.popup(f"Name: {name}\nPassword: {password}")

  window.close()

if __name__ == "__main__":
  main()