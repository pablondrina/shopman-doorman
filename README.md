# shopman-doorman

OTP authentication with device trust and magic links.

Part of the [Django Shopman](https://github.com/pablondrina/django-shopman) commerce framework.

## Overview

**Domain:** Auth
**Namespace:** `shopman.doorman`
**Pip package:** `shopman-doorman`

### Main Models

VerificationCode, TrustedDevice, AccessLink, MagicCode

## Installation

```bash
pip install shopman-doorman
```

## Quick Start

```python
# settings.py
INSTALLED_APPS = [
    "shopman.doorman",
    # ...
]
```

## Architecture

This package is a **Core app** — it provides domain-specific models, services, and protocols with zero dependencies on other Shopman apps (except `shopman-utils`).

Communication with other apps happens via `typing.Protocol` — no direct imports. The framework layer (`django-shopman`) orchestrates integration between core apps.

## Conventions

- **Monetary values:** `int` in centavos with `_q` suffix (e.g., `price_q = 1050` → R$ 10.50)
- **Identifiers:** `ref` (not `code`). Exception: `Product.sku`
- **Inter-app communication:** `typing.Protocol` + adapters, no direct imports

## Development

This package is developed in the [django-shopman](https://github.com/pablondrina/django-shopman) monorepo under `packages/doorman/`.

```bash
# Clone the monorepo
git clone https://github.com/pablondrina/django-shopman.git
cd django-shopman

# Install in editable mode
pip install -e packages/doorman

# Run tests
make test-doorman
```

## Related Packages

| Package | Domain |
|---------|--------|
| [django-shopman](https://github.com/pablondrina/django-shopman) | Framework orchestrator |
| [shopman-utils](https://github.com/pablondrina/shopman-utils) | Shared utilities |
| [shopman-omniman](https://github.com/pablondrina/shopman-omniman) | Orders |
| [shopman-stockman](https://github.com/pablondrina/shopman-stockman) | Inventory |
| [shopman-craftsman](https://github.com/pablondrina/shopman-craftsman) | Production |
| [shopman-offerman](https://github.com/pablondrina/shopman-offerman) | Catalog |
| [shopman-guestman](https://github.com/pablondrina/shopman-guestman) | CRM |
| [shopman-doorman](https://github.com/pablondrina/shopman-doorman) | Auth |
| [shopman-payman](https://github.com/pablondrina/shopman-payman) | Payments |

## License

MIT — Pablo Valentini
