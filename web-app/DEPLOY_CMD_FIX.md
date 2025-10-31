# 🚀 Quick Deploy Commands for CMD

## If you're using CMD (Command Prompt)

Use `npx vercel` instead of just `vercel`:

```cmd
cd "c:\Users\itsha\Hashing_Project - Copy\web-app"

REM Login (first time only)
npx vercel login

REM Deploy to production
npx vercel --prod
```

## If you're using PowerShell

Use `vercel` directly:

```powershell
cd "c:\Users\itsha\Hashing_Project - Copy\web-app"

# Login (first time only)
vercel login

# Deploy to production
vercel --prod
```

## Or Use the Deployment Script (Works in CMD!)

Just double-click `deploy.bat` or run:

```cmd
cd "c:\Users\itsha\Hashing_Project - Copy\web-app"
deploy.bat
```

---

## Why the difference?

- **CMD** needs `npx` because npm's global bin folder isn't in CMD's PATH
- **PowerShell** has the PATH configured correctly during npm installation
- **npx** works everywhere because it finds packages without needing PATH

---

## Recommended: Deploy NOW

**In CMD:**
```cmd
cd "c:\Users\itsha\Hashing_Project - Copy\web-app"
npx vercel login
npx vercel --prod
```

**OR switch to PowerShell:**
```powershell
cd "c:\Users\itsha\Hashing_Project - Copy\web-app"
vercel login
vercel --prod
```

**OR use the script:**
```cmd
deploy.bat
```

Choose option 2 for production!

---

🔐 **You're ready to deploy!**
