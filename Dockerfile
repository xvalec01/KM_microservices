FROM python:3.9

WORKDIR /usr/app

COPY requirements.txt ./

RUN python3 -m pip install -r requirements.txt

COPY . .

RUN python3 setup.py bdist_wheel \
    && python3 -m pip install dist/*.whl \
    && rm -r ./*

ENTRYPOINT ["image-sorter"]