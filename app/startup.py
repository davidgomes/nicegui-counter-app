from nicegui import Client, ui
import app.counter

def startup() -> None:
    app.counter.create()