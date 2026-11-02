"""Verify published transport security and required static resources."""
import socket
import ssl
import urllib.request

BASE = "https://vantmedia.site/"

for hostname in ("vantmedia.site", "www.vantmedia.site"):
    with socket.create_connection((hostname, 443), timeout=15) as connection:
        with ssl.create_default_context().wrap_socket(connection, server_hostname=hostname) as tls:
            names = {value for kind, value in tls.getpeercert()["subjectAltName"] if kind == "DNS"}
            assert hostname in names, (hostname, names)
            print(f"PASS trusted {tls.version()}: {hostname}")
    for scheme in ("http", "https"):
        with urllib.request.urlopen(f"{scheme}://{hostname}/", timeout=20) as response:
            assert response.status == 200
            assert response.url == BASE, response.url
            print(f"PASS {scheme}://{hostname}/ -> {response.url}")

for path in ("", "styles.css", "script.js", "assets/favicon.svg", "assets/port-and-plains.jpg", "assets/southern-ridge.jpg", "assets/flour-and-field.jpg"):
    with urllib.request.urlopen(BASE + path, timeout=20) as response:
        assert response.status == 200
        assert response.url.startswith("https://")
        print(f"PASS published resource: {path or '/'}")
