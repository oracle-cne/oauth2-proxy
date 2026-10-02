FROM container-registry.oracle.com/os/oraclelinux:9-slim

COPY rpms /tmp/

RUN microdnf update -y && \
    microdnf clean all && \
    rpm -i /tmp/*.rpm && \
    rm -rf /var/cache/yum/* /var/lib/rpm/* /tmp/*.rpm && \
    mkdir -p /etc/ssl/private && \
    touch /etc/ssl/private/jwt_signing_key.pem

ENTRYPOINT ["/bin/oauth2-proxy"] 

