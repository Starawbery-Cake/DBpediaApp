import PySimpleGUI as sg

def main():
  ImgKey = "img"
  InduceSearchTextKey = "induce"
  DoSearchKey = "do_search"
  AbstTextKey = "abst"
  ErrorTextKey = "error"
  ListBoxKey = "listBox"

  layout = [
    [
      sg.Frame("graph", [[sg.Image("white.png", key=ImgKey)]]),
      sg.Frame("operate", [
        [sg.Text("キーワードを入力してください：", key=InduceSearchTextKey), sg.InputText(size=(20,1)), sg.Button("検索", key=DoSearchKey)],
        [sg.Text("概要：")],
        [sg.Text("", key=AbstTextKey)],
        [sg.Text("", key=ErrorTextKey)],
        [sg.Text("検索結果"), sg.Button("決定")],
        [sg.Listbox([], size=(30, 30), key=ListBoxKey)]
      ])
    ],
  ]

  window = sg.Window("深化型学習支援システム", layout, resizable=True)

  # event loop
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