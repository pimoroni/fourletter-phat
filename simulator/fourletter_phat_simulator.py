import threading
import sys
import pickle
import tkinter as tk
import signal

WINDOW_HEIGHT_PX = 220
WINDOW_WIDTH_PX = 600

DIGIT_WIDTH = WINDOW_WIDTH_PX / 4

DRAW_TIMEOUT_MS = 100

# Exported via inscape as HTML/Canvas and then grabbed and sorted...
SEGMENTS = [
    # Top
    [37.21, 14.96, 31.53, 19.95, 41.16, 30.30, 112.08, 30.30, 123.67, 20.44, 118.03, 14.96],
    # Top Right
    [125.29, 23.51, 114.24, 33.08, 108.09, 90.15, 114.42, 97.25, 123.65, 90.01, 130.76, 27.94],
    # Bottom Right
    [113.31, 103.46, 104.79, 110.36, 97.98, 167.00, 107.56, 178.80, 115.00, 173.53, 121.36, 109.74],
    # Bottom Middle
    [26.63, 171.53, 14.55, 180.65, 20.49, 184.98, 100.34, 184.98, 104.96, 179.66, 96.39, 171.53],
    # Bottom Left
    [22.12, 102.50, 12.93, 109.70, 5.83, 172.66, 11.48, 179.09, 24.46, 168.97, 29.44, 109.76],
    # Top Left
    [29.38, 22.77, 23.44, 30.02, 15.69, 90.16, 22.74, 97.46, 32.91, 89.79, 38.61, 32.90],
    # Middle Left
    [58.04, 91.36, 34.48, 91.94, 25.14, 99.32, 31.98, 107.17, 56.82, 107.41, 66.33, 100.15],
    # Middle Right
    [80.20, 91.60, 71.71, 99.34, 78.99, 107.88, 101.98, 108.35, 111.43, 99.89, 103.89, 91.60],
    # Middle Top Left
    [43.38, 34.51, 41.10, 58.34, 56.94, 90.03, 60.23, 64.49],
    # Middle Top
    [75.20, 35.32, 68.12, 40.76, 62.24, 89.69, 69.10, 96.80, 77.16, 88.85, 82.34, 39.65],
    # Middle Top Right
    [109.20, 33.99, 85.56, 64.17, 82.49, 89.45, 106.04, 57.72],
    # Middle Bottom Left
    [53.95, 110.67, 31.48, 141.28, 29.20, 166.94, 52.68, 135.06],
    # Middle Bottom
    [68.91, 104.16, 59.94, 110.39, 54.96, 160.00, 60.84, 165.37, 69.58, 159.62, 75.04, 109.53],
    # Middle Bottom Right
    [80.36, 111.22, 77.06, 133.79, 93.36, 166.64, 96.90, 141.84],
    # Dot
    [128.00, 166.12, 118.69, 175.43, 128.00, 184.75, 137.32, 175.43]
]


class TkPhatSimulator():
    def __init__(self):
        self.brightness = 70
        self.do_run = True
        self.data = [0 for _ in range(8)]

        self.root = tk.Tk()
        self.root.resizable(False, False)

        self.root.bind('<Control-c>', lambda _: self.destroy())
        self.root.bind("<Unmap>", lambda _: self.destroy())
        self.root.protocol('WM_DELETE_WINDOW', self.destroy)

        self.root.title('Four Letter pHAT HD simulator')
        self.root.geometry('{}x{}'.format(WINDOW_WIDTH_PX, WINDOW_HEIGHT_PX))
        self.canvas = tk.Canvas(
            self.root, width=WINDOW_WIDTH_PX, height=WINDOW_HEIGHT_PX)
        self.canvas.config(highlightthickness=0)

    def run(self):
        try:
            self.draw_pixels()
            self.root.mainloop()
        except Exception as e:
            self.destroy()
            raise e

    def destroy(self):
        self.do_run = False

    def running(self):
        return self.do_run

    def draw_pixels(self):
        if not self.running():
            self.root.destroy()
            return

        self.canvas.delete(tk.ALL)
        self.canvas.create_rectangle(0, 0, WINDOW_WIDTH_PX, WINDOW_HEIGHT_PX, width=0, fill='black')

        lit = '#{:02x}{:02x}{:02x}'.format(32 + int(96 * self.brightness), 32 + int(223 * self.brightness), int(32 * (1.0 - self.brightness)))
        unlit = '#{:02x}{:02x}{:02x}'.format(32, 32, 32)

        for digit in range(4):
            for segment in range(15):
                points = self.translate_points(SEGMENTS[segment], digit * DIGIT_WIDTH + 5, 10)
                bit = self.data[digit] & (1 << segment)
                self.canvas.create_polygon(points, fill=lit if bit else unlit)

        self.canvas.pack()

        self.root.after(DRAW_TIMEOUT_MS, self.draw_pixels)

    def translate_points(self, points, x, y):
        result = []
        for p in range(0, len(points), 2):
            result += [points[p] + x,
                       points[p + 1] + y]
        return result

    def set_data(self, data):
        for x in range(8):
            offset = x * 2
            self.data[x] = (data[offset + 1] << 8) | data[offset]

    def set_brightness(self, data):
        self.brightness = data / 15.0


class ReadThread:
    def __init__(self, simulator):
        self.simulator = simulator
        self.stdin_thread = threading.Thread(
            target=self._read_stdin, daemon=True)

    def start(self):
        self.stdin_thread.start()

    def join(self):
        self.stdin_thread.join()

    def _read_stdin(self):
        while self.simulator.running():
            try:
                self._handle_update(pickle.load(sys.stdin.buffer))
            except EOFError:
                self.simulator.destroy()
            except Exception as err:
                self.simulator.destroy()
                raise err

    def _handle_update(self, buffer):
        if len(buffer) == 16:
            self.simulator.set_data(buffer)
        else:
            self.simulator.set_brightness(buffer[0])


def main():
    print('Starting Four Letter pHAT simulator')

    signal.signal(signal.SIGINT, lambda sig, frame: sys.exit(0))

    phat = TkPhatSimulator()
    thread = ReadThread(phat)
    thread.start()
    phat.run()
    thread.join()


if __name__ == "__main__":
    main()
