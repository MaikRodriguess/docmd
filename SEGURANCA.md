# ⚠️ ALERTA DE SEGURANÇA: Chave de API Exposta

## 🚨 O Que Aconteceu

Seu arquivo `.env` contendo a chave da API **OCR.space** (`K83237750588957`) foi enviado para o GitHub e ficou público no histórico do repositório.

Mesmo que o arquivo tenha sido removido agora, ele **ainda existe no histórico** do Git e pode ser acessado por qualquer pessoa.

---

## ✅ O Que Já Foi Feito

- [x] Removido `.env` dos commits futuros
- [x] Atualizado `.gitignore` para bloquear `.env`
- [x] Push da correção para o GitHub

---

## 🔒 O Que Você PRECISA Fazer AGORA

### 1. **Trocar sua chave de API do OCR.space** (URGENTE!)

A chave `K83237750588957` foi exposta publicamente. **Alguém pode estar usando ela agora mesmo**.

#### Como trocar:

1. Acesse: https://ocr.space/ocrapi
2. Faça login ou crie uma nova conta
3. Gere uma **nova chave de API**
4. **Revogue/delete a chave antiga** (se possível)

---

### 2. **Atualizar o arquivo .env local**

Depois de gerar a nova chave:

```bash
# Edite o arquivo .env
OCR_SPACE_API_KEY=SUA_NOVA_CHAVE_AQUI
```

⚠️ **NUNCA faça commit do .env novamente!**

---

### 3. **Limpar Completamente o Histórico** (Opcional mas RECOMENDADO)

O `.env` ainda está no histórico antigo. Para remover completamente:

#### **Opção A: Deletar e Recriar Repositório** (Mais Simples)

1. No GitHub, vá em **Settings** do repositório
2. Role até o final → **Delete this repository**
3. Confirme a exclusão
4. Crie um **novo repositório** com o mesmo nome
5. Faça push novamente (agora sem o `.env`)

#### **Opção B: Limpar Histórico (Avançado)**

```powershell
# Instale git-filter-repo (se não tiver)
pip install git-filter-repo

# Remova .env do histórico
git filter-repo --path .env --invert-paths

# Force push (reescreve histórico)
git push origin main --force
```

⚠️ **Atenção:** Isso reescreve TODO o histórico do Git!

---

## 📋 Checklist de Segurança

- [ ] Nova chave de API gerada no OCR.space
- [ ] Chave antiga revogada
- [ ] Arquivo `.env` local atualizado com nova chave
- [ ] `.env` NÃO está no `git status`
- [ ] Histórico do Git limpo (opcional)
- [ ] Deploy no Easypanel com a NOVA chave

---

## 🛡️ Boas Práticas para o Futuro

### **Sempre antes de commitar:**

```powershell
# Verifique o que vai ser enviado
git status

# Se .env aparecer, PARE e adicione ao .gitignore
```

### **Use .env.example para documentação:**

Crie um arquivo `.env.example` (SEM valores reais):

```
# .env.example
OCR_SPACE_API_KEY=sua_chave_aqui
```

Este arquivo PODE ir para o GitHub porque é apenas um template.

---

## 📝 Para Deploy no Easypanel

Quando for fazer deploy:

1. **NÃO** use a chave antiga
2. Use a **nova chave** nas variáveis de ambiente do Easypanel:
   - Key: `OCR_SPACE_API_KEY`
   - Value: `[SUA_NOVA_CHAVE]`

---

## ❓ FAQ

### "Minha chave já foi roubada?"

Possivelmente não (o repo foi criado há poucas horas), mas é melhor trocar preventivamente.

### "Preciso realmente trocar a chave?"

**SIM**. Chaves de API não devem NUNCA ser expostas publicamente. Alguém pode:
- Usar sua cota gratuitamente
- Fazer requisições maliciosas em seu nome
- Te deixar sem créditos

### "Como evito isso no futuro?"

1. **Sempre** adicione `.gitignore` ANTES do primeiro commit
2. Verifique `git status` antes de commitar
3. Use `git-secrets` ou pre-commit hooks para bloquear senhas

---

## 🎯 Próximos Passos

1. **AGORA:** Troque a chave da API
2. **Depois:** Escolha limpar o histórico do Git (recomendado)
3. **Então:** Continue o deploy no Easypanel com a nova chave

---

> [!CAUTION]
> **Não ignore este alerta!** Chaves de API expostas são um risco de segurança real.

---

Qualquer dúvida, me pergunte! 🔒
