FROM centos
RUN yum update -y &\
	yum install -y python3
RUN pip3 install dill &\
	pip3 install sklearn
COPY CUI.py /
COPY rfModel_v1.pk /
CMD python3 /CUI.py
