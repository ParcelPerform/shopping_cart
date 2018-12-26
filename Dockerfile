FROM python:3.6-alpine3.6

WORKDIR /src/shopping_cart

RUN apk --update add postgresql-client postgresql-dev
RUN apk --update add musl-dev   # for psycopg2-binary
RUN apk --update add gcc    # for psycopg2-binary

RUN pip install --upgrade pip

ADD requirements.txt ./
RUN pip install -r requirements.txt

ADD . ./
RUN chmod 775 start.sh
ENTRYPOINT ["sh", "/src/shopping_cart/start.sh"]
CMD []
