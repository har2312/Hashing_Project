# Deployment Guide

## Option 1: Run from Source (Recommended for Developers)

Users can clone and run directly:
```bash
git clone https://github.com/har2312/Hashing_Project.git
cd Hashing_Project
python gui_simulator.py
```

**Requirements:**
- Python 3.7+
- tkinter (included with Python)

## Option 2: Create Standalone Executable (Windows)

### Using PyInstaller

1. **Install PyInstaller:**
```bash
pip install pyinstaller
```

2. **Create executable:**
```bash
# GUI version
pyinstaller --onefile --windowed --name "HashTableSimulator" --icon=icon.ico gui_simulator.py

# Console version
pyinstaller --onefile --name "HashTableSimulator-Console" console_simulator.py
```

3. **Find executable:**
- Executable will be in `dist/` folder
- Distribute `dist/HashTableSimulator.exe` to users

### Distribution Package
Create a ZIP file with:
```
HashTableSimulator/
├── HashTableSimulator.exe
├── README.md
└── QUICKSTART.md
```

## Option 3: GitHub Releases

1. Go to: https://github.com/har2312/Hashing_Project/releases
2. Click "Create a new release"
3. Tag version: v1.0.0
4. Upload built executables
5. Add release notes

## Option 4: Python Package (PyPI)

For pip installation:
```bash
pip install hash-table-simulator
```

### Setup Steps:
1. Create `setup.py`
2. Register on PyPI
3. Build and upload:
```bash
python setup.py sdist bdist_wheel
twine upload dist/*
```

## Option 5: Web Version (Future)

Convert to web app using:
- Flask/Django backend
- React/Vue frontend
- Deploy to Heroku/Vercel/Netlify

## Platform-Specific Instructions

### Windows
- Run `.exe` directly (no Python needed)
- Or use `run.bat` if Python installed

### macOS
```bash
# Using PyInstaller
pyinstaller --onefile --windowed gui_simulator.py
# Creates .app bundle in dist/
```

### Linux
```bash
# Make executable
chmod +x gui_simulator.py
# Run
./gui_simulator.py
```

## Docker Deployment (Optional)

```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY . .
CMD ["python", "gui_simulator.py"]
```

## Continuous Deployment

### GitHub Actions (CI/CD)
Create `.github/workflows/release.yml` to auto-build executables on tag push.

## Distribution Checklist

- [ ] Test on clean Windows machine
- [ ] Test on macOS
- [ ] Test on Linux
- [ ] Create user manual
- [ ] Record demo video
- [ ] Submit to educational repositories
- [ ] Share on Reddit/forums

## Support

For deployment issues, open an issue at:
https://github.com/har2312/Hashing_Project/issues
