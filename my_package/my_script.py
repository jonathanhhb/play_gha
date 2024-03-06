import ctypes
import os

package_dir = os.path.dirname(__file__)

# Construct the path to the shared library file
# Determine the shared library file extension based on the platform
if platform.system() == 'Windows':
    library_ext = '.dll'
elif platform.system() == 'Linux':
    library_ext = '.so'
elif platform.system() == 'Darwin':  # macOS
    library_ext = '.dylib'
else:
    raise RuntimeError("Unsupported platform")

# Construct the path to the shared library file
library_path = os.path.join(script_dir, f'my_extension{library_ext}')

#library_path = os.path.join(package_dir,'my_extension.cpython-310-x86_64-linux-gnu.so')

my_lib = ctypes.CDLL(library_path)
my_lib.call_me.argtypes = []

def my_function():
    print("Hello from my script!")
    my_lib.call_me()

if __name__ == "__main__":
    my_function()
