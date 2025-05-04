FROM httpd:latest

# Copia os arquivos HTML/CSS/JS
COPY ./index.html /usr/local/apache2/htdocs/

# Copia a configuração de proxy
COPY ./my-proxy.conf /usr/local/apache2/conf/extra/my-proxy.conf

# Inclui a configuração de proxy no httpd.conf (somente se não estiver já)
RUN grep -q "Include conf/extra/my-proxy.conf" /usr/local/apache2/conf/httpd.conf || \
    echo "Include conf/extra/my-proxy.conf" >> /usr/local/apache2/conf/httpd.conf

EXPOSE 80

CMD ["httpd", "-D", "FOREGROUND"]
