import EasierPygame as ep

ep.initPygame()

Window = ep.MainWindow(
    width=800,
    height=600,
    title="EasierPygame",
    resizable=True
)

while True:
    Window.NewFrame()

    # your code here

    Window.UpdateScreen()