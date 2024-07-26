server {
    listen 80;

    server_name ax-pro-callback.rydikov.com;
    proxy_buffering off;
    client_max_body_size 1m;

    proxy_set_header Host $http_host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-Proto $scheme;

    location / {
        proxy_pass http://127.0.0.1:8808/;
    }

}