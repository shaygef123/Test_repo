FROM python
ENV KEY_FOR_PY="work", VALUE_FOR_PY="just"
ENV ACCESS_KEY="key", SECRET_ACCESS_KEY="s_key"
WORKDIR /app
COPY . .
RUN pip3 install -r requirements.txt
CMD mkdir ~/.aws && mv .aws/* ~/.aws
CMD ["python3","test_env.py"]