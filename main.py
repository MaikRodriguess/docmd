from markitdown import MarkItDown, FileConversionException
from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os
import mimetypes
import uuid
import requests  # Adicionado para chamadas à API OCR.space

# Inicia o aplicativo Flask
app = Flask(__name__)
load_dotenv()

# Chave da API OCR.space (cadastre grátis em https://ocr.space/ocrapi/freekey)
OCR_SPACE_API_KEY = os.getenv("OCR_SPACE_API_KEY")  # Adicione no .env

def ocr_image_with_ocrspace(image_path):
    """
    Extrai texto de imagem usando OCR.space (substitui OpenAI para imagens).
    Suporta handwriting com OCREngine=2 ou 3.
    """
    if not OCR_SPACE_API_KEY:
        return None
    
    try:
        with open(image_path, 'rb') as f:
            files = {'file': f}
            data = {
                'apikey': OCR_SPACE_API_KEY,
                'language': 'por',  # Português para o vídeo
                'OCREngine': 2,     # 2 para balanceado, 3 para neural (melhor handwriting)
                'isOverlayRequired': False
            }
            response = requests.post('https://api.ocr.space/parse/image', files=files, data=data)
            result = response.json()
        
        if result.get('IsErroredOnProcessing'):
            return None
        
        parsed_text = result['ParsedResults'][0]['ParsedText']
        return parsed_text.strip()
    
    except Exception:
        return None

@app.route('/convert', methods=['POST'])
def convert_file():
    try:
        if not request.content_type:
            return jsonify({"error": "Content-Type header is missing"}), 400
        
        file_data = request.get_data()
        content_type = request.content_type

        if not file_data:
            return jsonify({"error": "No file data provided"}), 400

        extension = mimetypes.guess_extension(content_type) or ""
        temp_filename = f"{uuid.uuid4()}{extension}"
        temp_path = os.path.join("uploads", temp_filename)

        os.makedirs("uploads", exist_ok=True)
        with open(temp_path, "wb") as f:
            f.write(file_data)

        try:
            # Detecta se é imagem (para usar OCR.space em vez de OpenAI)
            is_image = extension and extension.lower() in ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff']
            
            if is_image:
                # Usa OCR.space para imagens (gratuito)
                ocr_text = ocr_image_with_ocrspace(temp_path)
                if ocr_text:
                    # Retorna texto puro do OCR como markdown simples
                    return jsonify({"content": f"# Texto Extraído via OCR\n\n{ocr_text}"})
                else:
                    return jsonify({"error": "Falha no OCR. Tente com OpenAI ou verifique imagem."}), 500
            
            # Para não-imagens, usa MarkItDown sem LLM (ou com OpenAI se quiser fallback)
            md = MarkItDown()  # Sem LLM para docs/planilhas; adicione client se necessário
            result = md.convert(temp_path)
            return jsonify({"content": result.text_content})
        
        except (Exception, FileConversionException) as e:
            return jsonify({"error": str(e)}), 500
        
        finally:
            if os.path.exists(temp_path):
                os.remove(temp_path)
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
