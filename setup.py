import cx_Freeze
import os
import codecs
import sys

os.environ['TCL_LIBRARY'] = r"C:\Python\Python36\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Python\Python36\tcl\tcl8.6"

exes = [cx_Freeze.Executable("main.py")]

cx_Freeze.setup(name="knapsack_exe",
                options={"build_exe": {"packages": ["pygame"],
                                       "include_files": [r"asserts\dollar.png",
                                                         r"asserts\MoedaSeparada.png",
                                                         r"assets\balance_left_heavy.png",
														 r"assets\balance_left_heavy_pile_coins.png",
														 r"assets\balance_left_heavy_single coin.png",
														 r"assets\balance_right_heavy.png",
														 r"assets\balance_right_heavy_pile_coins.png",
														 r"assets\balance_right_heavy_singlecoin.png",
														 r"assets\balance_equal.png",
														 r"assets\balance_equal_pile_coins.png",
                                                         r"assets\balance_equal_single_coin.png"]
                                       }},
                description="algumas descrição",
                executables=exes
                )

			