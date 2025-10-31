# 🚀 Pre-Deployment Checklist

Use this checklist before deploying to ensure everything is ready!

## ✅ Code Quality Checks

- [ ] All features working locally
  - [ ] Backend runs on http://localhost:5000
  - [ ] Frontend runs on http://localhost:3000
  - [ ] Insert operation works in all modes
  - [ ] Delete operation works in all modes
  - [ ] Search operation works in all modes
  - [ ] Pseudocode displays correctly
  - [ ] Steps animation works smoothly

- [ ] No console errors in browser DevTools
- [ ] No Python errors in backend terminal
- [ ] All tests passing (if you have tests)

## 📁 File Structure Check

- [ ] `web-app/api/index.py` exists and updated
- [ ] `web-app/api/requirements.txt` has correct dependencies:
  ```
  flask==3.0.0
  flask-cors==4.0.0
  ```
- [ ] `web-app/frontend/package.json` has `vercel-build` script
- [ ] `web-app/vercel.json` configured correctly
- [ ] `hash_table.py` and `utils.py` exist in project root

## 🔧 Configuration Checks

- [ ] `App.js` uses dynamic API_URL:
  ```javascript
  const API_URL = process.env.REACT_APP_API_URL || (
    process.env.NODE_ENV === 'production' 
      ? '/api'
      : 'http://localhost:5000/api'
  );
  ```

- [ ] CORS enabled in backend:
  ```python
  from flask_cors import CORS
  CORS(app)
  ```

- [ ] No hardcoded localhost URLs in production code

## 🧪 Testing Checklist

### Backend Tests (Flask API)

```bash
cd "c:\Users\itsha\Hashing_Project - Copy\web-app\api"
python index.py
```

Test endpoints:
- [ ] `http://localhost:5000/` returns API info
- [ ] `http://localhost:5000/api/health` returns `{"status": "healthy"}`
- [ ] Can POST to `/api/create` and get table_id
- [ ] Can POST to `/api/{id}/insert` with key
- [ ] Can POST to `/api/{id}/search` with key
- [ ] Can POST to `/api/{id}/delete` with key

### Frontend Tests (React)

```bash
cd "c:\Users\itsha\Hashing_Project - Copy\web-app\frontend"
npm start
```

Test UI:
- [ ] Homepage loads without errors
- [ ] Can create table (size 5-50, all modes)
- [ ] Insert shows animation and updates table
- [ ] Search highlights correct bucket
- [ ] Delete removes key and shows steps
- [ ] Pseudocode highlights correct lines
- [ ] Toast messages display properly
- [ ] Responsive on different screen sizes

## 📦 Build Test

Try building locally to catch any build errors:

```bash
cd "c:\Users\itsha\Hashing_Project - Copy\web-app\frontend"
npm run build
```

Check:
- [ ] Build completes without errors
- [ ] `build/` folder created
- [ ] No warnings that need fixing
- [ ] Build size is reasonable (<5MB)

## 🔐 Security Checks

- [ ] No sensitive data in code (API keys, passwords, etc.)
- [ ] No console.log() with sensitive information
- [ ] CORS configured properly
- [ ] No commented-out debug code that could leak info

## 📝 Documentation

- [ ] README.md updated with deployment URL (after deploy)
- [ ] Comments in code are clear
- [ ] Any environment variables documented
- [ ] Deployment instructions ready

## 🌐 Vercel Account Setup

- [ ] Vercel account created at https://vercel.com
- [ ] Email verified
- [ ] Vercel CLI installed: `npm install -g vercel`
- [ ] Logged in: `vercel login`

## 🎯 Ready to Deploy!

Once all boxes are checked, you're ready to deploy!

### Deploy to Preview (Testing)
```bash
cd "c:\Users\itsha\Hashing_Project - Copy\web-app"
vercel
```

### Deploy to Production
```bash
cd "c:\Users\itsha\Hashing_Project - Copy\web-app"
vercel --prod
```

Or use the deployment script:
```bash
deploy.bat
```

## 🔍 Post-Deployment Testing

After deployment, test on the live URL:

- [ ] Visit your Vercel URL
- [ ] Test all operations:
  - [ ] Create table
  - [ ] Insert keys (5-10 keys)
  - [ ] Search for existing key
  - [ ] Search for non-existing key
  - [ ] Delete a key
  - [ ] Clear table
  - [ ] Resize table
- [ ] Test all collision modes:
  - [ ] Chaining
  - [ ] Linear probing
  - [ ] Quadratic probing
  - [ ] Double hashing
- [ ] Check on different devices:
  - [ ] Desktop (Chrome, Firefox, Safari)
  - [ ] Mobile phone
  - [ ] Tablet
- [ ] Check browser console - no errors
- [ ] Check Network tab - all API calls succeed

## 📊 Monitor

- [ ] Check Vercel dashboard for deployment status
- [ ] Review build logs if any issues
- [ ] Monitor API function logs
- [ ] Check analytics (after a few visits)

## 🐛 Rollback Plan

If something goes wrong:

1. Go to Vercel dashboard
2. Navigate to Deployments
3. Find the last working deployment
4. Click "Promote to Production"

Or from CLI:
```bash
vercel rollback
```

## ✅ Success Criteria

Your deployment is successful when:

✅ Site loads at your Vercel URL
✅ Can create and manipulate hash tables
✅ All 4 collision modes work correctly
✅ Animations and visualizations display properly
✅ No errors in browser console
✅ API endpoints respond correctly
✅ Responsive on mobile devices

---

## 🎉 Ready to Go Live!

Once everything is checked, run:

```bash
cd "c:\Users\itsha\Hashing_Project - Copy\web-app"
vercel --prod
```

Your Hash Table Simulator will be live at:
`https://hash-table-simulator-[your-username].vercel.app`

Share it with the world! 🌍

---

**Last Updated:** Before each deployment
**Next Check:** After any code changes
