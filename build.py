# Build script for creating Windows executable
# Run: python build.py

import os
import sys
import subprocess
import shutil

print("=" * 60)
print("  Hash Table Simulator - Build Script")
print("=" * 60)

# Check if PyInstaller is installed
try:
    import PyInstaller
    print("✅ PyInstaller found")
except ImportError:
    print("❌ PyInstaller not found. Installing...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
    print("✅ PyInstaller installed")

# Clean previous builds
if os.path.exists("build"):
    shutil.rmtree("build")
    print("✅ Cleaned build directory")
if os.path.exists("dist"):
    shutil.rmtree("dist")
    print("✅ Cleaned dist directory")

# Build GUI version
print("\n📦 Building GUI version...")
gui_cmd = [
    "pyinstaller",
    "--onefile",
    "--windowed",
    "--name", "HashTableSimulator",
    "--add-data", "utils.py;.",
    "--add-data", "hash_table.py;.",
    "gui_simulator.py"
]

try:
    subprocess.check_call(gui_cmd)
    print("✅ GUI executable created: dist/HashTableSimulator.exe")
except Exception as e:
    print(f"❌ Error building GUI: {e}")

# Build Console version
print("\n📦 Building Console version...")
console_cmd = [
    "pyinstaller",
    "--onefile",
    "--name", "HashTableSimulator-Console",
    "--add-data", "utils.py;.",
    "--add-data", "hash_table.py;.",
    "console_simulator.py"
]

try:
    subprocess.check_call(console_cmd)
    print("✅ Console executable created: dist/HashTableSimulator-Console.exe")
except Exception as e:
    print(f"❌ Error building console: {e}")

# Create distribution package
print("\n📦 Creating distribution package...")
dist_folder = "dist/HashTableSimulator-v1.0"
os.makedirs(dist_folder, exist_ok=True)

# Copy files
files_to_copy = [
    "dist/HashTableSimulator.exe",
    "dist/HashTableSimulator-Console.exe",
    "README.md",
    "QUICKSTART.md"
]

for file in files_to_copy:
    if os.path.exists(file):
        shutil.copy(file, dist_folder)
        print(f"✅ Copied {file}")

print("\n" + "=" * 60)
print("✅ Build complete!")
print(f"📁 Distribution files in: {dist_folder}")
print("=" * 60)
print("\nNext steps:")
print("1. Test the executables")
print("2. Create a ZIP of the distribution folder")
print("3. Upload to GitHub Releases")
