# shopman-doorman

Autenticação passwordless para Django. OTP via WhatsApp/SMS com fallback chain, magic links, device trust, e bridge tokens para integração com sistemas externos.

Part of the [Django Shopman](https://github.com/pablondrina/django-shopman) commerce framework.

## Domínio

- **VerificationCode** — código OTP com TTL, rate limiting, e max tentativas. Entrega via WhatsApp (primário) → SMS (fallback).
- **TrustedDevice** — dispositivo confiável do cliente. Fingerprint + user agent + geolocalização. Gerenciável pelo cliente.
- **AccessLink** — magic link para acesso direto (ex: link no WhatsApp abre a conta sem OTP).
- **CustomerUser** — bridge entre Customer (guestman) e User (Django auth). Criado automaticamente no primeiro login.

## Services

| Service | O que faz |
|---------|-----------|
| `VerificationService` | Gera e valida OTP. Fallback chain WhatsApp → SMS → Email. Rate limiting por phone. |
| `DeviceTrustService` | Registra, valida e revoga dispositivos confiáveis. |
| `AccessLinkService` | Gera e valida magic links com TTL. |

## Fluxo de Login

1. Cliente informa telefone
2. Sistema envia OTP via WhatsApp (fallback SMS)
3. Cliente digita código
4. Sistema valida → cria/recupera CustomerUser → login Django
5. Dispositivo é registrado como confiável (opcional)

## Configuração

```python
DOORMAN = {
    "OTP_LENGTH": 6,
    "OTP_TTL_SECONDS": 300,
    "OTP_MAX_ATTEMPTS": 5,
    "DELIVERY_CHAIN": ["whatsapp", "sms"],
    "TRUSTED_DEVICE_TTL_DAYS": 90,
    "ACCESS_LINK_TTL_HOURS": 24,
}
```

## Instalação

```bash
pip install shopman-doorman
```

```python
INSTALLED_APPS = [
    "shopman.doorman",
    "shopman.doorman.contrib.admin_unfold",  # opcional
]

AUTHENTICATION_BACKENDS = [
    "shopman.doorman.backends.PhoneOTPBackend",
    "django.contrib.auth.backends.ModelBackend",
]
```

## Development

```bash
git clone https://github.com/pablondrina/django-shopman.git
cd django-shopman && pip install -e packages/doorman
make test-doorman  # ~80 testes
```

## License

MIT — Pablo Valentini
