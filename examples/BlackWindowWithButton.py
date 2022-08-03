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

    button = ep.Button(
        Window.GetScreen(),
        100,
        100,
        Window.GetStartingScreenWidth(),
        50,
        Window.GetStartingScreenHeight(),
        50,
        "assets/icon.png",
        "assets/iconHover.png",
    )

    button.update()

    if button.click():
        print("Clicked")

    Window.UpdateScreen()