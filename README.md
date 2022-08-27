
# LOA.runs

LOA.runs is a website to track the best abyss/legion raids times. People can submit their run for approval.

### Structure
Front-End:
- Vue.Js, Bulma, and Axios

Back-End:
- Django REST, Pillow, and Djoser


### Contribute
If you think you can contribute with anything, follow these steps:

**Back-end:**

Clone the repo:
```bash
git clone https://github.com/matheusclmb/loa-runs.git
cd loa-runs/backend
```

Create a virtual env:
```bash
python -m venv env
```

Activate the env:
```bash
macOS: source env/bin/Activate
winOS: env\scripts\activate
```

Install the requirements:
```bash
pip install -r requirements.txt
```

Make migrations:
```bash
python manage.py migrate
python manage.py makemigrations
```

Run:
```bash
python manage.py runserver
```

**Front-end:**

Clone the repo:
```bash
git clone https://github.com/matheusclmb/loa-runs.git
cd loa-runs/frontend
```

Install packages
```bash
npm i
```

Run:
```bash
npm run serve
```
