FROM bcgovimages/von-image:py36-1.16-1

RUN pip3 install --no-cache-dir poetry

USER root

# Add docker-compose-wait tool
ENV WAIT_VERSION 2.7.2
ADD https://github.com/ufoscout/docker-compose-wait/releases/download/$WAIT_VERSION/wait /wait
RUN chmod +x /wait

RUN mkdir my_plugin; touch my_plugin/__init__.py
COPY ./README.md .
COPY ./setup.py .
COPY ./pyproject.toml .
COPY ./poetry.lock .
COPY ./docker/default.yml .
USER root
RUN chown indy:indy -R .
USER indy

RUN poetry install --no-dev

# Make site packages location more accessible (for use with volumes)
RUN ln -s $(poetry env info -p)/lib/python3.6/site-packages site-packages

COPY ./my_plugin my_plugin

ENTRYPOINT ["/bin/sh", "-c", "/wait && poetry run aca-py \"$@\"", "--"]
CMD ["start",  "--plugin", "my_plugin", "--arg-file", "default.yml"]
