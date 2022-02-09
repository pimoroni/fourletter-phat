import sys
import subprocess
import pickle
import os


class SMBus:
    def __init__(self, dummy):
        self._start_simulator()

    def _start_simulator(self):
        self.sdl_phat_process = subprocess.Popen(
            [sys.executable, os.path.dirname(os.path.abspath(
                __file__)) + '/fourletter_phat_simulator.py'],
            stdin=subprocess.PIPE)

    def write_byte_data(self, addr, reg, data):
        pass

    def write_i2c_block_data(self, addr, cmd, vals):
        I2C_ADDR = 0x70

        assert addr == I2C_ADDR

        if cmd & 0xE0:  # Brightness
            vals = [cmd & ~0xE0]
        
        if cmd & 0xE0 or cmd == 0:  # Display data
            try:
                pickle.dump(vals, self.sdl_phat_process.stdin)
                self.sdl_phat_process.stdin.flush()
            except OSError:
                sys.stderr.write('Lost connection to Four Letter pHAT simulator\n')
                sys.stderr.flush()
                sys.exit(-1)
