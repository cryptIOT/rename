# batch_rename.py
import os

def batch_rename(prefix, directory="."):
    for filename in os.listdir(directory):
        if filename.startswith(prefix):
            new_name = "new_" + filename
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_name))
            print(f"Renamed {filename} to {new_name}")

if __name__ == "__main__":
    import sys
    prefix_arg = sys.argv[1] if len(sys.argv) > 1 else ""
    batch_rename(prefix=prefix_arg)
