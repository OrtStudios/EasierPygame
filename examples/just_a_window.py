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

    # your code here

    app.UpdateScreen()