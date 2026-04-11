---
name: production-ready-check
description: A final checklist to ensure an application is ready for deployment to a production environment. Use before major releases or final delivery.
---

# Production Ready Checklist

## Reliability & Performance
- [ ] **Tests**: Are all unit, integration, and E2E tests passing?
- [ ] **Load Testing**: Can the system handle expected production traffic levels?
- [ ] **Resource Limits**: Are memory and CPU limits configured for the container/environment?
- [ ] **Caching**: Is there a strategy for caching static assets and expensive data?

## Security
- [ ] **Secrets**: Are all passwords, API keys, and certificates stored in a secret manager?
- [ ] **HTTPS**: Is SSL/TLS forced for all connections?
- [ ] **Firewall**: Are only the necessary ports open?

## Observability
- [ ] **Logging**: Is structured logging configured and being sent to a central server?
- [ ] **Monitoring**: Are there alerts for high error rates or system downtime?
- [ ] **Health Checks**: Does the app provide an endpoint (e.g., `/health`) for load balancers?

## Maintenance & DevOps
- [ ] **CI/CD**: Is the deployment process automated and repeatable?
- [ ] **Rollback Plan**: If the deployment fails, is there a clear way to revert to the previous version?
- [ ] **Database Migrations**: are migrations tested and reversible?
- [ ] **Documentation**: Is the `README` clear on how to build, run, and maintain the app?

## User Experience
- [ ] **Error Pages**: Are there custom 404 and 500 pages?
- [ ] **Favicon & Meta Tags**: Basic SEO and branding elements in place.
- [ ] **Analytics**: Is user tracking (if needed) correctly implemented?
