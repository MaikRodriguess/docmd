# 🚀 Como Usar o Docker - Guia para Iniciantes

Este guia mostra como testar sua aplicação localmente antes de subir para o servidor.

---

## 📋 Pré-requisitos

- Docker Desktop instalado no Windows
- Terminal (PowerShell ou CMD)

---

## 🏃 Rodando Localmente (Teste)

### 1. Abra o terminal na pasta do projeto

```powershell
cd c:\Users\maikr\Documents\GitHub\docmd
```

### 2. Suba o Docker

```powershell
docker-compose up -d
```

**O que esse comando faz:**
- `-d` = roda em segundo plano (detached)
- Constrói a imagem do Docker
- Inicia o serviço na porta 80

### 3. Verifique se está rodando

```powershell
docker-compose ps
```

Você deve ver algo como:
```
NAME       IMAGE          STATUS         PORTS
docmd-web  docmd:latest   Up 10 seconds  0.0.0.0:80->5000/tcp
```

### 4. Teste a aplicação

Abra o navegador e acesse: **http://localhost**

Ou teste com curl:
```powershell
curl http://localhost/convert
```

---

## 📊 Comandos Úteis

### Ver logs em tempo real
```powershell
docker-compose logs -f web
```

### Parar o serviço
```powershell
docker-compose stop
```

### Parar e remover tudo
```powershell
docker-compose down
```

### Reconstruir após mudanças no código
```powershell
docker-compose up -d --build
```

---

## 🚢 Subindo para o Servidor (Produção)

Quando você estiver pronto para colocar no servidor:

### Opção 1: Docker Compose (Recomendado para iniciantes)

No servidor, rode:
```bash
docker-compose up -d
```

### Opção 2: Docker Swarm (Para produção com alta disponibilidade)

No servidor, inicialize o Swarm:
```bash
docker swarm init
docker stack deploy -c stack.yml docmd
```

**Importante:** Para usar Swarm, você precisa primeiro construir a imagem:
```bash
docker build -t docmd:latest .
```

---

## ❓ Troubleshooting

### Porta 80 já está em uso?

Edite `docker-compose.yml` e troque a porta:
```yaml
ports:
  - "8080:5000"  # Agora acesse em http://localhost:8080
```

### Preciso ver os logs de erro?

```powershell
docker-compose logs web
```

### Como entrar dentro do container?

```powershell
docker-compose exec web bash
```

---

## 📝 Notas

- **Testes locais:** Use `docker-compose.yml`
- **Produção:** Use `stack.yml` com Docker Swarm
- O arquivo `.env` contém sua chave de API do OCR.space
- Os uploads ficam salvos no volume `uploads`

---

## 🎯 Resumo Rápido

```powershell
# Iniciar
docker-compose up -d

# Ver logs
docker-compose logs -f

# Parar
docker-compose down
```

Pronto! 🎉
