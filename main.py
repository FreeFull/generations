import sdl2
import sdl2.ext
import generations

def run():
    automaton = generations.Automaton(x_size = 64, y_size = 64)
    sdl2.ext.init()
    window = sdl2.ext.window.Window("Generations", (256,256))
    window.show()
    running = True
    while running:
        break

if __name__ == "__main__":
    run()
