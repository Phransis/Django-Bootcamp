Supabase connection

1) Connection string (copy into your `.env` replacing YOUR_PASSWORD):

postgresql://postgres:YOUR_PASSWORD@db.mvioxjrqtsanuzebpnrj.supabase.co:5432/postgres

2) Optional: install Agent Skills for Supabase (run locally):

npx skills add supabase/agent-skills

Notes:
- Add `DATABASE_URL` to your Vercel environment variables for production.
- Keep `SUPABASE_KEY` and `DJANGO_SECRET_KEY` secret (do not commit).
