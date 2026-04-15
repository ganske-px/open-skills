# HTTP Hook

POSTs the hook input JSON to an external URL. Useful for webhooks, external monitoring, and third-party integrations.

## Schema

```json
{
  "type": "http",
  "url": "https://hooks.example.com/claude-code",
  "timeout": 30,
  "headers": {
    "Authorization": "Bearer $MY_TOKEN",
    "Content-Type": "application/json"
  },
  "allowedEnvVars": ["MY_TOKEN"],
  "statusMessage": "Sending to webhook...",
  "once": false
}
```

## Fields

| Field | Required | Default | Description |
|-------|----------|---------|-------------|
| `type` | Yes | — | Must be `"http"` |
| `url` | Yes | — | URL to POST the hook input JSON to |
| `timeout` | No | none | Timeout in seconds |
| `headers` | No | none | Additional HTTP headers. Values can reference env vars with `$VAR` or `${VAR}`. |
| `allowedEnvVars` | No | none | Explicit list of env var names allowed for header interpolation. Required for env var interpolation to work. |
| `statusMessage` | No | none | Custom spinner message |
| `once` | No | `false` | If true, runs once then auto-removes |

## Security

HTTP hooks have additional security restrictions:

- **`allowedHttpHookUrls`** — settings-level allowlist of URL patterns (supports `*` wildcards). If set, hooks with non-matching URLs are blocked.
- **`httpHookAllowedEnvVars`** — settings-level allowlist of env var names. Each hook's effective `allowedEnvVars` is the intersection with this list.
- Only variables listed in both the hook's `allowedEnvVars` AND the global `httpHookAllowedEnvVars` (if set) will be interpolated.

## How It Works

1. Claude Code serializes the hook input as JSON
2. POSTs it to the specified URL with configured headers
3. The response body is parsed as JSON for control output
4. Same output contract as command hooks (continue, stopReason, additionalContext, etc.)

## Use Cases

### External audit log
```json
{
  "type": "http",
  "url": "https://audit.internal.example.com/claude-events",
  "headers": {
    "Authorization": "Bearer $AUDIT_TOKEN"
  },
  "allowedEnvVars": ["AUDIT_TOKEN"]
}
```

### Slack notification on session start
```json
{
  "type": "http",
  "url": "https://hooks.slack.com/services/T.../B.../xxx",
  "statusMessage": "Notifying team..."
}
```

## When to Use HTTP vs Command

| Scenario | Use |
|----------|-----|
| Local file operations | `command` |
| External service integration | `http` |
| Need curl with complex auth | `http` (headers + env vars) |
| Need to process response locally | `command` (with curl inside) |
