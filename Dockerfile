FROM public.ecr.aws/lambda/python:3.9

RUN pip install -U pip
<<<<<<< HEAD
RUN pip install pipenv 
=======
RUN pip install pipenv
>>>>>>> 8c93d3a (Re-initialize repository without old history.)

COPY [ "Pipfile", "Pipfile.lock", "./" ]

RUN pipenv install --system --deploy

COPY [ "lambda_function.py","model.py", "./" ]

<<<<<<< HEAD
CMD [ "lambda_function.lambda_handler" ]
=======
CMD [ "lambda_function.lambda_handler" ]
>>>>>>> 8c93d3a (Re-initialize repository without old history.)
