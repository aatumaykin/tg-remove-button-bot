FROM python:3.9

RUN python -m venv /venv
ENV PATH "/venv/bin:$PATH"

RUN pip install aiogram~=2.18 environs~=9.4.0

COPY . .

CMD python3 -m app