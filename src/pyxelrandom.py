import pyxel


class App:
    def __init__(self):
        pyxel.init(160, 120, title="Yogg vs C'Thun")
        pyxel.image(0).load(0, 0, "assets/yogg cthun.png")
        pyxel.image(0).load(35, 35, "assets/small cube.png")
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_SPACE):
            pyxel.quit()

    def draw(self):
        pyxel.cls(0)
        pyxel.text(40, 20, "PRESS SPACE TO PLAY!", pyxel.frame_count % 10)
        pyxel.text(40, 58, "YOGG          C'THUN", pyxel.frame_count % 16)
        pyxel.blt(33, 66, 0, 0, 0, 128, 128)


App()
