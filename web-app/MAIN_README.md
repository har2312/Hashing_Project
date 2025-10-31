# 🔐 Hash Table Simulator - Web Application

![Hash Table Simulator](https://img.shields.io/badge/Status-Ready%20to%20Deploy-success)
![Python](https://img.shields.io/badge/Python-3.7%2B-blue)
![React](https://img.shields.io/badge/React-18-blue)
![Vercel](https://img.shields.io/badge/Vercel-Ready-black)

## 🎯 Overview

**Web version** of the Hash Table Simulator - converted from a Python tkinter desktop application to a modern, responsive web application that runs in your browser!

### ✨ What's This?

This is the complete web conversion of your Hash Table Simulator project. It maintains **all the features** of the desktop version while adding the power of web accessibility:

- 🌐 **Access from anywhere** - no installation needed
- 📱 **Mobile friendly** - works on phones and tablets  
- 🔗 **Shareable** - send a link to students/colleagues
- ☁️ **Cloud hosted** - deploy to Vercel for free
- 🎨 **Modern UI** - beautiful React + Tailwind CSS interface

## 🚀 Quick Deploy

### Option 1: One-Command Deploy (Fastest)

```bash
cd web-app
npx vercel
```

That's it! Follow the prompts and your app will be live in minutes.

### Option 2: Manual Deploy

See [QUICKSTART.md](./QUICKSTART.md) for detailed step-by-step instructions.

## 📸 Features

All your original features, now on the web:

### ✅ Core Features
- **4 Collision Modes**: Chaining, Linear Probing, Quadratic Probing, Double Hashing
- **Full Operations**: Insert, Search, Delete, Resize, Clear
- **Real-time Visualization**: Color-coded buckets, animated operations
- **Pseudocode Panel**: Live code execution with line highlighting
- **Execution Steps**: Detailed step-by-step breakdown
- **Variable Tracking**: Watch variables change in real-time

### 🆕 Web Enhancements
- **Responsive Design**: Works on all screen sizes
- **Modern UI**: Clean, professional interface
- **Fast Performance**: Optimized React components
- **API Architecture**: RESTful backend for extensibility
- **Global CDN**: Fast loading worldwide via Vercel

## 📁 Project Structure

```
web-app/
├── api/                    # Flask Backend (Python)
│   ├── index.py           # API endpoints
│   └── requirements.txt   # Python dependencies
│
├── frontend/              # React Frontend
│   ├── src/
│   │   ├── components/   # React components
│   │   ├── App.js        # Main app
│   │   └── index.css     # Styles
│   └── package.json      # Node dependencies
│
├── vercel.json           # Deployment config
├── README.md             # Full documentation
└── QUICKSTART.md         # Quick start guide
```

## 🛠️ Local Development

### Backend (Flask API)
```bash
cd api
pip install -r requirements.txt
python index.py
# Runs at http://localhost:5000
```

### Frontend (React)
```bash
cd frontend
npm install
npm start
# Runs at http://localhost:3000
```

## 📚 Documentation

- **[README.md](./README.md)** - Complete documentation
- **[QUICKSTART.md](./QUICKSTART.md)** - 5-minute deployment guide
- **[Original README](../README.md)** - Desktop version docs

## 🎓 Educational Use

Perfect for:
- Computer Science courses
- Data structures teaching
- Online learning platforms
- Coding bootcamps
- Self-study and practice

## 🔧 Technology Stack

**Backend:**
- Flask (Python web framework)
- Original hash_table.py (reused!)
- Flask-CORS (for frontend communication)

**Frontend:**
- React 18 (UI framework)
- Tailwind CSS (styling)
- Axios (API calls)

**Deployment:**
- Vercel (serverless hosting)
- Automatic builds
- Global CDN

## 🌟 Highlights

### What Makes This Special?

1. **Zero Installation**: No Python, no dependencies - just open the URL
2. **Always Updated**: Deploy once, update anywhere
3. **Collaborative**: Share with unlimited users
4. **Professional**: Portfolio-ready project
5. **Free Hosting**: Vercel's generous free tier

### Maintained Features from Desktop Version

✅ All collision handling algorithms
✅ Pseudocode visualization  
✅ Step-by-step execution
✅ Color-coded buckets
✅ Load factor monitoring
✅ Educational tooltips and guides

## 🚀 Deploy to Vercel

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone)

Click the button above to deploy your own instance!

Or use CLI:
```bash
npm install -g vercel
cd web-app
vercel
```

## 📊 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/create` | POST | Create new hash table |
| `/api/<id>/insert` | POST | Insert key |
| `/api/<id>/search` | POST | Search key |
| `/api/<id>/delete` | POST | Delete key |
| `/api/<id>/resize` | POST | Resize table |
| `/api/<id>/clear` | POST | Clear table |

## 🎨 Screenshots Preview

**Desktop View:**
- Full visualization with all panels
- Pseudocode on the right
- Control panel on top
- Real-time execution steps

**Mobile View:**
- Responsive stacked layout
- Touch-friendly controls
- Optimized for small screens

## 💡 Usage Example

1. **Create a table**: Choose size and collision mode
2. **Insert keys**: Enter comma-separated values
3. **Watch it work**: See real-time visualization
4. **Learn the algorithm**: Follow pseudocode execution
5. **Understand collisions**: View step-by-step resolution

## 🤝 Contributing

Improvements welcome! The codebase is clean and well-documented.

## 📝 License

MIT License - Same as original project

## 🎉 Success Metrics

After deployment, you can:
- ✅ Access from any device
- ✅ Share via simple URL
- ✅ No installation required
- ✅ Always up-to-date
- ✅ Free forever (Vercel free tier)

## 🔗 Links

- **Original Desktop App**: [../README.md](../README.md)
- **Deployment Guide**: [README.md](./README.md)
- **Quick Start**: [QUICKSTART.md](./QUICKSTART.md)

---

## 🎓 Perfect For Learning

This web app makes hash tables accessible to everyone:

- 👨‍🎓 **Students**: Learn interactively from anywhere
- 👨‍🏫 **Teachers**: Share one link with entire class
- 👨‍💻 **Developers**: Portfolio-ready project
- 🎯 **Interviewers**: Demonstrate understanding visually

---

**Ready to deploy? Run this:**

```bash
cd web-app
npx vercel
```

**That's all it takes to go from desktop to web! 🚀**

---

Made with ❤️ for Data Structures enthusiasts

🔐 **Happy Hashing on the Web!**
