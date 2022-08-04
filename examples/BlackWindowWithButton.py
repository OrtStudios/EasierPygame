import EasierPygame as ep

ep.initPygame()

app = ep.Application(
    width=800,
    height=600,
    title="EasierPygame",
    resizable=True
)

while True:
    app.NewFrame()

    button = ep.Entity.Button(
        app.GetScreen(),
        100,
        100,
        app.GetStartingScreenWidth(),
        50,
        app.GetStartingScreenHeight(),
        50,
        "assets/icon.png",
        "assets/iconHover.png",
    )

    button.update()

    if button.click():
        print("Clicked")

    app.UpdateScreen()