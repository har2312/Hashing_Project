# 🚀 Backend API Deployment Guide

## Ready to Deploy! ✅

The `api` folder is now ready for Vercel deployment with all dependencies included.

### Files in this folder:
- ✅ `index.py` - Main Flask API (updated to import from same directory)
- ✅ `hash_table.py` - Hash table implementation (copied from root)
- ✅ `utils.py` - Utility functions (copied from root)
- ✅ `requirements.txt` - Python dependencies (Flask, flask-cors)
- ✅ `vercel.json` - Vercel configuration

---

## 📋 Deploy to Vercel (Website Method)

### Step 1: Go to Vercel Dashboard
1. Visit https://vercel.com
2. Click "Add New..." → "Project"

### Step 2: Deploy from Local Directory
1. Click "Browse" or drag and drop
2. Select this folder: `c:\Users\itsha\Hashing_Project - Copy\web-app\api`
3. Or upload as ZIP

### Step 3: Configure Project
- **Project Name:** `hash-table-api` (or your choice)
- **Framework Preset:** Other
- **Root Directory:** `.` (current directory)
- **Build Command:** Leave empty
- **Output Directory:** Leave empty
- **Install Command:** `pip install -r requirements.txt`

### Step 4: Deploy!
Click "Deploy" button

### Step 5: Wait for Deployment
- Takes about 1-2 minutes
- You'll get a URL like: `https://hash-table-api.vercel.app`

### Step 6: Test Your API
Visit these endpoints:

```
https://your-api-url.vercel.app/
https://your-api-url.vercel.app/api/health
```

You should see:
```json
{
  "message": "Hash Table Simulator API",
  "version": "1.0.0",
  ...
}
```

And:
```json
{
  "status": "healthy",
  "tables": 0
}
```

---

## 🧪 Test Your Deployed API

### Create a table:
```bash
curl -X POST https://your-api-url.vercel.app/api/create \
  -H "Content-Type: application/json" \
  -d '{"size": 10, "mode": "chaining"}'
```

### Insert a key:
```bash
curl -X POST https://your-api-url.vercel.app/api/table_0/insert \
  -H "Content-Type: application/json" \
  -d '{"key": 42}'
```

### Search for a key:
```bash
curl -X POST https://your-api-url.vercel.app/api/table_0/search \
  -H "Content-Type: application/json" \
  -d '{"key": 42}'
```

---

## 📝 Save Your API URL!

After deployment, copy your API URL. You'll need it for the frontend deployment.

Example: `https://hash-table-api-abc123.vercel.app`

You'll use this URL in the frontend's `.env` file or directly in `App.js`.

---

## ✅ Success Criteria

Your API is deployed successfully when:
- ✅ Root endpoint returns API info
- ✅ `/api/health` returns `{"status": "healthy"}`
- ✅ Can create a table via POST request
- ✅ Can insert, search, delete keys
- ✅ No CORS errors (flask-cors is configured)

---

## 🐛 Troubleshooting

### If deployment fails:

1. **Check build logs** in Vercel dashboard
2. **Verify Python version**: Vercel uses Python 3.9 by default
3. **Check imports**: All files (hash_table.py, utils.py) must be in the same folder

### If you get import errors:

Make sure these files are in the api folder:
- index.py
- hash_table.py
- utils.py
- requirements.txt

### If CORS errors occur:

The API has `CORS(app)` enabled, which allows all origins. This should work fine.

---

## 🎯 Next Steps

After backend is deployed:

1. ✅ Copy your API URL
2. ➡️ Deploy the frontend
3. ➡️ Update frontend to use your API URL instead of localhost
4. ✅ Test the complete app!

---

## 📦 Alternative: ZIP Upload

If you prefer to upload as ZIP:

1. Zip the entire `api` folder
2. Go to Vercel dashboard
3. Upload the ZIP file
4. Configure and deploy

---

## 🎉 Ready to Deploy!

Everything is configured and ready. Just:

1. Go to https://vercel.com
2. Click "Add New..." → "Project"
3. Upload this `api` folder
4. Click Deploy!

Your backend will be live in ~2 minutes! 🚀

---

**After deployment, come back and we'll deploy the frontend with your API URL!**
