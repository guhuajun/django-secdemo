FROM python:3.6
ENV PYTHONUNBUFFERED 1

ADD app/ /app/
WORKDIR /app/

RUN pip install -r requirements.prod.txt \
	--index-url http://mirrors.aliyun.com/pypi/simple/ \
	--trusted-host mirrors.aliyun.com

EXPOSE 8000

# CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers=2", "project.wsgi:application"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]