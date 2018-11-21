## To execute
### 1. Сreate a virtual environment
```
python -m venv gm_venv
```
### 2. Install requirements
```
pip install -r requirements.txt
```
### 3. Start the test
```
pytest tests/test_gmail.py --sender_email [MAIL_#1] --sender_password [PASSWORD_#1] --receiver_email [MAIL_#2] --receiver_password [PASSWORD_#2]
