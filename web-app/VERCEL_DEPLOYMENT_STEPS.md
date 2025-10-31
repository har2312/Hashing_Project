# 🚀 Vercel Deployment Guide - Hash Table Simulator

## Prerequisites

Before deploying, ensure you have:
- ✅ A [Vercel account](https://vercel.com/signup) (free tier works great!)
- ✅ [Git](https://git-scm.com/) installed
- ✅ Your code pushed to GitHub/GitLab/Bitbucket (recommended) or use Vercel CLI

---

## 🎯 Method 1: Deploy via Vercel Dashboard (Recommended)

### Step 1: Push to GitHub

```bash
# Navigate to your project
cd "c:\Users\itsha\Hashing_Project - Copy"

# Initialize git if not already done
git init

# Add all files
git add .

# Commit
git commit -m "Ready for Vercel deployment"

# Create a new repository on GitHub, then:
git remote add origin https://github.com/YOUR_USERNAME/hash-table-simulator.git
git branch -M main
git push -u origin main
```

### Step 2: Import to Vercel

1. Go to [vercel.com](https://vercel.com) and log in
2. Click **"Add New..."** → **"Project"**
3. Import your GitHub repository
4. Configure the project:
   - **Framework Preset:** Other
   - **Root Directory:** `web-app`
   - **Build Command:** Leave default
   - **Output Directory:** Leave default
   - **Install Command:** Leave default

5. Click **"Deploy"**

### Step 3: Wait for Deployment

Vercel will:
- ✅ Install dependencies
- ✅ Build the React frontend
- ✅ Deploy the Flask API
- ✅ Assign you a URL like: `https://hash-table-simulator.vercel.app`

### Step 4: Test Your Deployment

Visit your deployment URL and test:
- ✅ Create a hash table
- ✅ Insert keys
- ✅ Search for keys
- ✅ Delete keys
- ✅ Test all 4 collision modes

---

## 🔧 Method 2: Deploy via Vercel CLI

### Step 1: Install Vercel CLI

```bash
npm install -g vercel
```

### Step 2: Login to Vercel

```bash
vercel login
```

This will open your browser to authenticate.

### Step 3: Deploy to Preview

```bash
# Navigate to web-app directory
cd "c:\Users\itsha\Hashing_Project - Copy\web-app"

# Deploy to preview
vercel
```

Follow the prompts:
- ✅ Set up and deploy? **Yes**
- ✅ Which scope? **Select your account**
- ✅ Link to existing project? **No** (first time)
- ✅ Project name? **hash-table-simulator** (or your choice)
- ✅ In which directory is your code? **./** (current directory)

### Step 4: Deploy to Production

Once you're happy with the preview:

```bash
vercel --prod
```

---

## 🔍 Configuration Files (Already Set Up)

### ✅ vercel.json
```json
{
  "version": 2,
  "builds": [
    {
      "src": "api/index.py",
      "use": "@vercel/python"
    },
    {
      "src": "frontend/package.json",
      "use": "@vercel/static-build"
    }
  ],
  "routes": [
    {
      "src": "/api/(.*)",
      "dest": "/api/index.py"
    },
    {
      "src": "/(.*)",
      "dest": "/frontend/index.html"
    }
  ]
}
```

### ✅ Frontend API Configuration
The `App.js` automatically detects production vs development:
- **Development:** Uses `http://localhost:5000/api`
- **Production:** Uses relative path `/api` (handled by Vercel routing)

### ✅ Backend Dependencies
File: `api/requirements.txt`
```txt
flask==3.0.0
flask-cors==4.0.0
```

---

## 🐛 Troubleshooting

### Issue: "Module not found" error in API

**Solution:** Check that `hash_table.py` and `utils.py` are in the parent directory of `web-app/`.

The API's `index.py` adds the parent directory to the Python path:
```python
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))
```

### Issue: API routes return 404

**Solution:** Ensure `vercel.json` routes are correct:
- `/api/*` → points to Python backend
- `/*` → points to React frontend

### Issue: CORS errors in browser console

**Solution:** The Flask API already has CORS enabled:
```python
from flask_cors import CORS
CORS(app)
```

If still having issues, check browser console for specific error messages.

### Issue: Build fails

**Common causes:**
1. **Missing dependencies:** Run `npm install` in `frontend/` directory
2. **Python version:** Vercel uses Python 3.9 by default
3. **Node version:** Vercel uses Node 18.x by default

**Check Vercel build logs:**
```bash
vercel logs [deployment-url]
```

### Issue: App loads but API calls fail

**Debug steps:**
1. Open browser DevTools (F12) → Network tab
2. Try an operation (create table, insert key)
3. Check if API calls are going to `/api/...`
4. Check response status and error messages

**Manual test API:**
Visit: `https://your-app.vercel.app/api/health`

Should return:
```json
{"status": "healthy", "tables": 0}
```

---

## 🎨 Custom Domain (Optional)

### Add Your Own Domain

1. Go to your project in Vercel dashboard
2. Click **"Settings"** → **"Domains"**
3. Add your domain (e.g., `hashtable.yourdomain.com`)
4. Follow DNS configuration instructions

Vercel automatically provides:
- ✅ Free SSL certificate
- ✅ Automatic HTTPS redirect
- ✅ Global CDN

---

## 📊 Monitoring Your Deployment

### View Analytics

1. Go to Vercel dashboard
2. Select your project
3. Click **"Analytics"** tab

See:
- 📈 Page views
- 🌍 Geographic distribution
- ⚡ Performance metrics
- 🐛 Error rates

### View Logs

```bash
# Real-time logs
vercel logs --follow

# Last 100 logs
vercel logs
```

Or view in dashboard: **Project** → **"Deployments"** → Select deployment → **"Logs"**

---

## 🔄 Updating Your Deployment

### Automatic Deployments (GitHub Integration)

Every time you push to your main branch:
1. Vercel automatically detects the push
2. Builds and deploys the new version
3. Sends you a notification

### Manual Deployments (CLI)

```bash
cd "c:\Users\itsha\Hashing_Project - Copy\web-app"

# Deploy preview
vercel

# Deploy to production
vercel --prod
```

---

## ✅ Post-Deployment Checklist

Test all features in production:

- [ ] Homepage loads correctly
- [ ] Can create hash table (all modes)
- [ ] Can insert keys
- [ ] Can search for keys
- [ ] Can delete keys
- [ ] Can resize table
- [ ] Can clear table
- [ ] Pseudocode displays correctly
- [ ] Execution steps animate properly
- [ ] Toast messages show
- [ ] Responsive on mobile devices
- [ ] All collision modes work:
  - [ ] Chaining
  - [ ] Linear probing
  - [ ] Quadratic probing
  - [ ] Double hashing

---

## 🎓 Example Production URLs

After deployment, you'll get URLs like:

```
Preview:    https://hash-table-simulator-abc123.vercel.app
Production: https://hash-table-simulator.vercel.app
```

**API Endpoints:**
```
Health:  https://hash-table-simulator.vercel.app/api/health
Create:  https://hash-table-simulator.vercel.app/api/create
Insert:  https://hash-table-simulator.vercel.app/api/{id}/insert
Search:  https://hash-table-simulator.vercel.app/api/{id}/search
Delete:  https://hash-table-simulator.vercel.app/api/{id}/delete
```

---

## 🌟 Sharing Your App

Once deployed, share it:

**For Students:**
> 🔐 Check out this interactive Hash Table Simulator I built!
> 
> 🔗 https://hash-table-simulator.vercel.app
> 
> Features:
> - 4 collision resolution strategies
> - Step-by-step algorithm visualization
> - Real-time pseudocode highlighting
> - Fully responsive design

**For Portfolio:**
> Interactive Hash Table Simulator
> - React + Flask full-stack application
> - Deployed on Vercel with serverless functions
> - Visualizes data structure operations with animations
> - Educational tool for learning collision resolution

---

## 💡 Pro Tips

1. **Use Environment Variables:** Store sensitive data in Vercel's Environment Variables (Dashboard → Settings → Environment Variables)

2. **Preview Deployments:** Every branch gets its own preview URL - great for testing features!

3. **Rollback:** Made a mistake? Go to Deployments → Find previous working version → Promote to Production

4. **Performance:** Vercel automatically optimizes your app with:
   - Image optimization
   - Static asset caching
   - Global CDN distribution
   - Automatic compression

5. **Free Tier Limits:**
   - 100 GB bandwidth/month
   - 100 hours serverless function execution
   - Unlimited deployments
   - Perfect for personal projects and demos!

---

## 📚 Additional Resources

- [Vercel Documentation](https://vercel.com/docs)
- [Vercel CLI Reference](https://vercel.com/docs/cli)
- [Python on Vercel](https://vercel.com/docs/functions/serverless-functions/runtimes/python)
- [React Deployment](https://vercel.com/docs/frameworks/react)

---

## 🎉 Congratulations!

Your Hash Table Simulator is now live on the internet! 🚀

**Next Steps:**
1. Share the URL with friends, classmates, or on social media
2. Add it to your portfolio or resume
3. Keep improving and redeploying as you add features
4. Monitor analytics to see how people use it

---

**Questions or issues?** Check the troubleshooting section above or open an issue on GitHub.

🔐 **Happy Hashing!**
