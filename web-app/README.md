# Hash Table Simulator - Web Application Deployment Guide

## 🚀 Quick Overview

This is the **web version** of the Hash Table Simulator, converted from a Python tkinter desktop application to a modern web application that can be deployed on Vercel.

## 📁 Project Structure

```
web-app/
├── api/                          # Flask Backend API
│   ├── index.py                  # Main API file (serverless function)
│   └── requirements.txt          # Python dependencies
│
├── frontend/                     # React Frontend
│   ├── public/
│   │   └── index.html
│   ├── src/
│   │   ├── components/
│   │   │   ├── ControlPanel.js
│   │   │   ├── HashTableVisualization.js
│   │   │   ├── PseudocodePanel.js
│   │   │   └── CollisionStepsPanel.js
│   │   ├── App.js
│   │   ├── App.css
│   │   ├── index.js
│   │   └── index.css
│   ├── package.json
│   ├── tailwind.config.js
│   └── postcss.config.js
│
├── vercel.json                   # Vercel deployment configuration
└── README.md                     # This file
```

## 🛠️ Technology Stack

### Backend
- **Flask** - Python web framework
- **Flask-CORS** - Cross-Origin Resource Sharing support
- **Original hash_table.py** - Core logic (reused from desktop app)

### Frontend
- **React 18** - UI framework
- **Axios** - HTTP client
- **Tailwind CSS** - Styling
- **Modern ES6+** - JavaScript features

### Deployment
- **Vercel** - Serverless deployment platform
- Supports both Python serverless functions and static React builds

## 🔧 Prerequisites

Before deploying, ensure you have:

1. **Node.js** (v14 or higher) - [Download](https://nodejs.org/)
2. **Python** (v3.7 or higher) - Already installed for original project
3. **Vercel Account** - [Sign up free](https://vercel.com/)
4. **Vercel CLI** (optional but recommended)

```bash
npm install -g vercel
```

## 📦 Local Development Setup

### 1. Backend Setup (Flask API)

```bash
# Navigate to API directory
cd web-app/api

# Install Python dependencies
pip install -r requirements.txt

# Run Flask development server
python index.py
```

The API will run at `http://localhost:5000`

### 2. Frontend Setup (React)

```bash
# Navigate to frontend directory
cd web-app/frontend

# Install Node.js dependencies
npm install

# Start React development server
npm start
```

The React app will run at `http://localhost:3000`

### 3. Test Locally

1. Ensure both servers are running
2. Open `http://localhost:3000` in your browser
3. Try creating a hash table and performing operations

## 🚀 Deployment to Vercel

### Method 1: Deploy via Vercel CLI (Recommended)

1. **Install Vercel CLI** (if not already installed):
```bash
npm install -g vercel
```

2. **Navigate to web-app directory**:
```bash
cd web-app
```

3. **Login to Vercel**:
```bash
vercel login
```

4. **Deploy**:
```bash
vercel
```

5. **Follow the prompts**:
   - Set up and deploy? **Y**
   - Which scope? Select your account
   - Link to existing project? **N** (first time)
   - Project name? `hash-table-simulator-web`
   - In which directory is your code located? `./`

6. **Production Deployment**:
```bash
vercel --prod
```

### Method 2: Deploy via Vercel Dashboard

1. **Push your code to GitHub**:
```bash
# From the project root
git init
git add .
git commit -m "Web app conversion complete"
git remote add origin YOUR_GITHUB_REPO_URL
git push -u origin master
```

2. **Import to Vercel**:
   - Go to [vercel.com/dashboard](https://vercel.com/dashboard)
   - Click "Add New Project"
   - Import your GitHub repository
   - Vercel will auto-detect the configuration from `vercel.json`

3. **Configure Environment Variables** (if needed):
   - In Vercel dashboard, go to Project Settings → Environment Variables
   - Add any needed variables (none required for basic setup)

4. **Deploy**:
   - Click "Deploy"
   - Wait for build to complete
   - Your app will be live at `https://your-project-name.vercel.app`

## 🔗 API Endpoints

The Flask backend provides these endpoints:

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/create` | POST | Create new hash table |
| `/api/<table_id>/insert` | POST | Insert key into table |
| `/api/<table_id>/search` | POST | Search for key |
| `/api/<table_id>/delete` | POST | Delete key |
| `/api/<table_id>/resize` | POST | Resize table |
| `/api/<table_id>/clear` | POST | Clear all keys |
| `/api/<table_id>/state` | GET | Get current state |
| `/api/health` | GET | Health check |

## 🎨 Features

All features from the original desktop application:

✅ **Four Collision Handling Modes**
- 🔗 Chaining
- ➡️ Linear Probing
- 📐 Quadratic Probing  
- 🔁 Double Hashing

✅ **Complete Operations**
- Insert (single or multiple keys)
- Search
- Delete
- Resize & Rehash
- Clear table

✅ **Visual Features**
- Real-time hash table visualization
- Color-coded bucket states
- Animated operations
- Load factor monitoring

✅ **Educational Features**
- Real-time pseudocode display
- Step-by-step execution
- Variable tracking
- Collision steps logging

## 🔍 Configuration

### Frontend Configuration

Edit `frontend/src/App.js` to change API URL:

```javascript
const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:5000/api';
```

For production, add environment variable in Vercel:
```
REACT_APP_API_URL=/api
```

### Backend Configuration

The Flask app automatically:
- Imports hash_table.py from parent directory
- Configures CORS for frontend requests
- Handles serverless function execution

## 📊 Performance & Limits

### Vercel Free Tier Limits:
- **Serverless Function Execution**: 10 seconds max
- **Bandwidth**: 100GB/month
- **Deployments**: Unlimited

### Application Limits:
- **Max table size**: 100 buckets (configurable in code)
- **Session storage**: In-memory (resets on new deployment)
- **For production**: Consider adding Redis for persistent storage

## 🐛 Troubleshooting

### Problem: API not responding
**Solution**: Check that `hash_table.py` and `utils.py` are accessible from `api/index.py`

### Problem: CORS errors
**Solution**: Ensure Flask-CORS is installed and configured:
```python
from flask_cors import CORS
CORS(app)
```

### Problem: Build fails on Vercel
**Solution**: 
1. Check `vercel.json` configuration
2. Ensure all dependencies are in requirements.txt and package.json
3. Check build logs in Vercel dashboard

### Problem: Tailwind styles not working
**Solution**: Ensure these files exist:
- `tailwind.config.js`
- `postcss.config.js`
- Correct imports in `index.css`

## 🔐 Security Considerations

For production use:

1. **Add session management**:
   - Use Redis or database for multi-user support
   - Implement user authentication if needed

2. **Rate limiting**:
   - Add rate limiting to API endpoints
   - Use Vercel Edge Config or middleware

3. **Input validation**:
   - Already basic validation exists
   - Add more robust validation for production

4. **Error handling**:
   - Implement comprehensive error logging
   - Use Vercel's built-in monitoring

## 📈 Scaling

To handle more users:

1. **Add database**: Replace in-memory storage with PostgreSQL/MongoDB
2. **Add caching**: Use Redis for frequently accessed tables
3. **Upgrade plan**: Move to Vercel Pro for better limits
4. **Add CDN**: Serve static assets via CDN

## 🎓 Educational Use

Perfect for:
- 📚 Computer Science courses
- 👨‍🏫 Teaching data structures
- 👨‍💻 Self-learning hash tables
- 🎯 Interview preparation

## 📝 Differences from Desktop Version

### What's the Same:
✅ All hash table logic and algorithms
✅ Four collision handling modes
✅ Pseudocode visualization
✅ Step-by-step execution
✅ Color-coded visualization

### What's New:
🆕 Web-based (accessible anywhere)
🆕 Modern React UI
🆕 RESTful API architecture
🆕 Responsive design
🆕 Cloud deployment ready

### What's Different:
- No Windows .exe file
- Runs in browser instead of tkinter
- API-based instead of direct function calls
- Modern web styling (Tailwind CSS)

## 🤝 Contributing

To contribute improvements:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test locally
5. Deploy to Vercel for testing
6. Submit a pull request

## 📞 Support

For issues or questions:
- Check the [original README](../../README.md) for hash table concepts
- Review API documentation above
- Check Vercel deployment logs
- Open an issue on GitHub

## 📜 License

Same as original project: MIT License

## 🎉 Success!

Once deployed, your Hash Table Simulator will be accessible at:
```
https://your-project-name.vercel.app
```

Share this URL with students, teachers, or anyone learning about hash tables!

---

**Made with ❤️ for Data Structures enthusiasts**

*Converted from desktop app to web app - Now accessible anywhere, anytime!*

🔐 **Happy Hashing!**
