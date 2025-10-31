# Deployment Commands - Hash Table Simulator Web App

## 🚀 Quick Deploy Commands

### First Time Setup

```bash
# 1. Install Vercel CLI globally
npm install -g vercel

# 2. Navigate to web-app directory
cd "c:\Users\itsha\Hashing_Project - Copy\web-app"

# 3. Login to Vercel (opens browser)
vercel login

# 4. Deploy to preview
vercel

# 5. Deploy to production
vercel --prod
```

### Subsequent Deployments

```bash
cd "c:\Users\itsha\Hashing_Project - Copy\web-app"
vercel --prod
```

---

## 🧪 Local Testing Commands

### Test Backend (Flask API)

```bash
# Terminal 1: Run Flask API
cd "c:\Users\itsha\Hashing_Project - Copy\web-app\api"
pip install -r requirements.txt
python index.py
```

API will run at: http://localhost:5000

### Test Frontend (React)

```bash
# Terminal 2: Run React app
cd "c:\Users\itsha\Hashing_Project - Copy\web-app\frontend"
npm install
npm start
```

Frontend will run at: http://localhost:3000

---

## 📦 Build Commands

### Build Frontend for Production

```bash
cd "c:\Users\itsha\Hashing_Project - Copy\web-app\frontend"
npm run build
```

Creates optimized production build in `frontend/build/`

---

## 🔍 Verification Commands

### Check if everything is ready

```bash
# Check Python version
python --version

# Check Node version  
node --version

# Check npm version
npm --version

# Verify Flask can import hash_table
cd "c:\Users\itsha\Hashing_Project - Copy\web-app\api"
python -c "import sys; sys.path.insert(0, '../..'); from hash_table import HashTable; print('✓ Import successful')"

# Check React dependencies
cd "c:\Users\itsha\Hashing_Project - Copy\web-app\frontend"
npm list react react-dom axios

# Verify Vercel CLI
vercel --version
```

---

## 🎯 Expected Output

### After `vercel` command:
```
Vercel CLI 28.x.x
? Set up and deploy "~\web-app"? [Y/n] y
? Which scope do you want to deploy to? Your Name
? Link to existing project? [y/N] n
? What's your project's name? hash-table-simulator-web
? In which directory is your code located? ./
🔗  Linked to username/hash-table-simulator-web
🔍  Inspect: https://vercel.com/username/hash-table-simulator-web/xxxxx
✅  Preview: https://hash-table-simulator-web-xxxxx.vercel.app
```

### After `vercel --prod` command:
```
🔍  Inspect: https://vercel.com/username/hash-table-simulator-web/xxxxx
✅  Production: https://hash-table-simulator-web.vercel.app
```

---

## 🐛 Troubleshooting Commands

### If deployment fails

```bash
# Clear Vercel cache
vercel --force

# Check logs
vercel logs

# Redeploy from scratch
rm -rf .vercel
vercel
```

### If Flask import fails

```bash
# Make sure you're in the right directory
cd "c:\Users\itsha\Hashing_Project - Copy\web-app\api"

# Test Python path
python -c "import sys; print('\n'.join(sys.path))"

# Verify files exist
dir ..\..\hash_table.py
dir ..\..\utils.py
```

### If React build fails

```bash
cd "c:\Users\itsha\Hashing_Project - Copy\web-app\frontend"

# Clear cache and reinstall
rmdir /s /q node_modules
del package-lock.json
npm install

# Try build again
npm run build
```

---

## 🔗 Useful Vercel Commands

```bash
# View all deployments
vercel list

# View deployment logs
vercel logs [deployment-url]

# Remove a deployment
vercel remove [deployment-name]

# View project info
vercel inspect

# Open project in browser
vercel open

# View environment variables
vercel env ls

# Link to existing project
vercel link
```

---

## 📊 Post-Deployment Checklist

After deploying, test these:

✅ Homepage loads
✅ Can create a hash table
✅ Can insert keys
✅ Can search for keys
✅ Can delete keys
✅ Pseudocode displays correctly
✅ Execution steps show properly
✅ All 4 collision modes work
✅ Resize functionality works
✅ Responsive on mobile

---

## 💡 Pro Tips

1. **Always test locally first**: Run both backend and frontend locally before deploying
2. **Use preview deployments**: `vercel` without `--prod` for testing
3. **Check build logs**: If something breaks, logs are your friend
4. **Environment variables**: Set in Vercel dashboard for sensitive data
5. **Custom domain**: Add your own domain in Vercel dashboard settings

---

## 🎓 Quick Reference

| Command | What it does |
|---------|-------------|
| `vercel` | Deploy to preview URL |
| `vercel --prod` | Deploy to production |
| `vercel logs` | View deployment logs |
| `vercel dev` | Run locally with Vercel environment |
| `vercel list` | List all deployments |
| `vercel --force` | Force new deployment (clear cache) |

---

## 🌐 Sharing Your Deployment

After successful deployment, share:

```
🔗 Your Hash Table Simulator is live at:
   https://hash-table-simulator-web.vercel.app

📱 Works on:
   - Desktop browsers
   - Mobile phones  
   - Tablets

🎓 Perfect for:
   - Teaching hash tables
   - Learning data structures
   - Interview preparation
   - Portfolio showcase
```

---

**Need help? Check:**
- [README.md](./README.md) - Full documentation
- [QUICKSTART.md](./QUICKSTART.md) - Quick start guide
- [Vercel Docs](https://vercel.com/docs) - Official Vercel documentation

🔐 **Happy Deploying!**
