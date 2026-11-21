# AGENTS.md

## Project Overview
Home-automation middleware for a Raspberry Pi: a Flask REST API and Telegram bot control an alarm/gate via `gpiozero` and TP-Link Tapo cameras, while MQTT carries status updates and ESP32 sensor data. The root Compose stack runs Mosquitto plus backend/Alexa/webapp images; `client/` is a small TypeScript MQTT test client. README owns setup and run instructions.

## Technology Stack
- Backend: Python 3.11.14 (`.python-version`), Flask/flask-restful/flask-cors, paho-mqtt 1.6, python-telegram-bot 13.x, pytapo 3.3.56, gpiozero/pigpio, `raspi_home_texx` 0.7.3 (TestPyPI extra index in `requirements.txt`), gunicorn.
- Client: TypeScript 4.5 / commonjs / es6, `mqtt` 4.x, dotenv, ESLint airbnb-base + @typescript-eslint; 4-space indent, 120-char lines, `noImplicitAny`.
- Tooling: Docker Compose v3.8, stdlib `unittest`, npm scripts. `.pylintrc` sets 120-char lines (pylint is not a declared dependency). No CI workflow exists in the repo.

## Architecture
- `backend/main.py` is the composition root: selects `TapoManagementImpl/Mock` from `TAPO_MANAGEMENT=mock` and `AutomationImpl/Mock` from `GPIOZERO_PIN_FACTORY=mock`, builds the Telegram bot via `BotTelegramBuilder`, starts `StatusPublisher` and `Esp32Subscriber` threads, and registers Flask-RESTful resources with `resource_class_kwargs={'automation': automation}`.
- `src/base_automation.py` holds shared automation logic and delegates camera actions to `TapoManagement`. `AutomationImpl` drives GPIO pins defined in `pinout.py`; `AutomationMock` simulates the same states. Both extend the external `raspi_home_texx.automation.Automation` (implementing `temperature()` / `system_info()`) and use its `serialize()` output contract.
- `src/environment.py` is the sole config entry point: `dotenv_values('.env')` merged with `.env.local` (local overrides). Values are module-level constants; missing keys or invalid integers fail at import.
- MQTT: `StatusPublisher` publishes `automation.serialize()` to `STATUS_TOPIC` over websockets every `PUBLISH_TIMEOUT`; `Esp32Subscriber` reads `SENSORS_TOPIC` over TCP, unmarshals with `EnvironmentInfoUnmarshaller`, updates automation under a `Lock`, and marks sensors offline after repeated timeouts. Commands are handled over REST; there is no MQTT command consumer.
- REST: `PUT /api/command` checks `command` against `CommandController.commands`, accepts optional `state`, returns booleans as `{"s": 0|1}`, and aborts with 400 for unknown commands. Wake endpoints build Jenkins trigger URLs in `BaseAutomation`.
- Telegram: `src/bot_telegram/` subclasses the library builder/handler/filter/commands; callbacks are wired in `bot_telegram_builder.py`, command names/descriptions in `commands_extended.py`, emoji labels in `messages.py`. `update-bot-commands.py` pushes descriptions to Telegram.
- The backend image copies only `requirements.txt`, `.env`, `main.py`, `wsgi.py`, and `src/`, then serves `wsgi:app` with gunicorn. Compose files set mock flags and mount `.env.local`.

## Development Guidelines
- Keep changes inside existing modules. Hardware/camera work follows the current interface pattern: shared behavior in `BaseAutomation`, hardware in `AutomationImpl`, simulation in `AutomationMock`; new camera actions require methods on `TapoManagement`, `TapoManagementImpl`, and `TapoManagementMock`.
- Pass collaborators explicitly (constructor arguments / `resource_class_kwargs`). Only `wsgi.py` intentionally imports `main.py`.
- Read settings from `src.environment`. When adding a key, add it to both tracked backend env files (`backend/.env`, `docker/backend/.env`) and to local `.env.local` as needed.
- Match existing logging: `get_console_logger(__name__, env.LOGGING_LEVEL)` or `file_logger.write(...)`. Bot/user-facing strings are Italian and use `emoji.emojize(..., use_aliases=True)`.
- Respect formatting already configured: 120-char lines for Python, 4-space indent / 120-char max for TypeScript, `src/*` path alias, `noImplicitAny`.
- Use the mock modes for hardware-free work. `Pinout` values are Broadcom pin numbers.

## Testing and Verification
- Backend: from `backend/`, run `python -m unittest discover -s tests -v` (or `venv/bin/python` when the venv exists). Tests target `AutomationMock`; there is no pytest config or dependency.
- Known baseline: all 6 tests currently error in `setUp` because `AutomationMock()` requires a `tapo_management` argument. Treat this as pre-existing until fixed.
- Client: `npm run lint` applies ESLint fixes; `npm run build` runs lint then `tsc --build` into `dist/`; `npm run clean` removes build output. `npm test` is a placeholder that exits 1; there are no client tests.
- No CI workflow exists; verify locally. README covers setup/run commands.

## Security Considerations
- `.env.local` files are gitignored; tracked `.env` files hold defaults/placeholders. Never commit real bot tokens, chat IDs, Jenkins/Tapo credentials, MAC addresses, or registry passwords. `build-push.sh` sources `.env`/`.env.local` and expects a `.docker_pass` file for registry login.
- Mosquitto config uses `allow_anonymous true` and exposes MQTT/WS ports with no TLS; treat the broker as LAN-only.
- Flask enables CORS globally and REST endpoints have no authentication; preserve the command whitelist rather than adding arbitrary dispatch.
- Jenkins credentials are embedded in the wake URL and Tapo credentials come from env; avoid logging full URLs or secret values.

## Restrictions
- Do not edit generated/ignored artifacts: `backend/venv/`, `__pycache__/`, `backend/raspi_home.log`, `client/node_modules/`, `client/dist/`, Mosquitto `data/`/`log/`, `.idea/workspace.xml`, or any `.env.local`.
- Do not change IDE configuration (`.idea/`, `.vscode/`) unless explicitly asked.
- Treat external contracts as stable unless requested: REST paths/command names, MQTT topics, Telegram command strings and emoji labels, `Pinout` numbers, and registry/image tags in Compose.
- Adding dependencies requires updating the relevant manifest/lockfile and Docker build inputs; `requirements.txt` depends on the TestPyPI extra index for `raspi_home_texx`.
