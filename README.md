# 📄 DocMD - Document to Markdown Converter

API REST para conversão de documentos e imagens para Markdown usando OCR e processamento inteligente.

## 🚀 Features

- 📝 Conversão de documentos (PDF, DOCX, XLSX, PPTX) para Markdown
- 🖼️ OCR de imagens (JPG, PNG, GIF, BMP, TIFF) com suporte a texto manuscrito
- 🌐 API REST simples e intuitiva
- 🐳 Deploy com Docker (Docker Compose e Swarm)
- ☁️ Pronto para deploy em Easypanel/CapRover

## 🛠️ Tecnologias

- **Python 3.11** - Backend
- **Flask** - Framework web
- **MarkItDown** - Conversão de documentos
- **OCR.space API** - Reconhecimento óptico de caracteres
- **Docker** - Containerização

## 📦 Instalação

### Requisitos

- Docker e Docker Compose
- Chave de API do [OCR.space](https://ocr.space/ocrapi) (gratuita)

### Deploy Local

```bash
# Clone o repositório
git clone https://github.com/MaikRodriguess/docmd.git
cd docmd

# Configure as variáveis de ambiente
cp .env.example .env
# Edite o .env e adicione sua chave de API

# Suba o container
docker-compose up -d
```

A API estará disponível em `http://localhost`.

## 🔧 Uso

### Endpoint: `POST /convert`

Envie um arquivo via requisição POST:

```bash
curl -X POST http://localhost/convert \
  -H "Content-Type: image/png" \
  --data-binary @imagem.png
```

**Resposta:**
```json
{
  "content": "# Texto Extraído via OCR\n\nConteúdo do documento..."
}
```

## 🌍 Deploy em Produção

### Easypanel / CapRover

1. Conecte com seu repositório GitHub
2. Configure a variável de ambiente: `OCR_SPACE_API_KEY`
3. Build automático via Dockerfile
4. Porta do container: `5000`

### Docker Swarm

```bash
docker swarm init
docker build -t docmd:latest .
docker stack deploy -c stack.yml docmd
```

## ⚙️ Variáveis de Ambiente

| Variável | Descrição | Obrigatória |
|----------|-----------|-------------|
| `OCR_SPACE_API_KEY` | Chave de API do OCR.space | Sim |

## 📄 Licença

MIT License - veja [LICENSE](LICENSE) para mais detalhes.

---

**Desenvolvido por [Maik Rodrigues](https://github.com/MaikRodriguess)**
