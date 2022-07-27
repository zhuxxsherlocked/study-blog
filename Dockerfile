FROM nginx
RUN mkdir -p /usr/share/nginx/html/study
COPY ./ /usr/share/nginx/html/study
COPY home/  /usr/share/nginx/html
