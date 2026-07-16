# NetworkTestCli
## Also known as ntcli
# NOTE: THIS IS UNFINISHED

## Installation
```bash
pip install -i https://test.pypi.org/simple/ NetworkTestCli
```
Remember this is unfinished so its on testpypi.

## Usage
```bash
ntcli
```
Or
```bash
ntcli [flags]
```

## Flags
| Flag | Use |
|------|-----|
| -P   | Force ping to be used reguardless of if gping is installed |
| -I   | Allows specifying an ip instead of the default |
| -N   | When using gping this will remove the --clear flag |
| -V   | Show version information and exit |
## Defaults
| Name | Value |
|------|-------|
| Ip   |  1.1.1.1 (Cloudflare) |
| Ping type | gping / ping |
### Ping type is decided by whether gping is avalible, if gping is avalible then it uses it, if not then it uses ping

## Planned features (OPTIONAL)
- Speedtest-cli intergration
- Menu flag utilising fzf_wrapper

# This project is licensed under the MIT license, see [LICENSE](LICENSE).