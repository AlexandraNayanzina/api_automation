FROM python:3.10

WORKDIR /api_automation

COPY tests tests/

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

VOLUME ["/api_automation/allure-results"]

CMD [ "pytest", "-v" , "--alluredir", "allure-results", "tests"]