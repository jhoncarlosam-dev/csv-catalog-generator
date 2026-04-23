from flask import Flask, render_template, request, send_file, jsonify
import csv
import os
import json
from datetime import datetime

app = Flask(__name__)
os.makedirs('generated', exist_ok=True)

def generar_catalogo_csv(nombre_archivo, num_items, campos,
                         prefijo="ITEM-", texto_base="Valor de catalogo",
                         inicio_numero=1, ancho_codigo=5, encabezado="valor"):
    """
    Genera CSV con campos dinámicos.
    campos: lista de dicts [{'header': 'ID', 'format': 'ITEM-{n:05d}'}]
    Si campos está vacío, usa el modo clásico con un solo campo.
    """
    ruta = os.path.join('generated', nombre_archivo)
    with open(ruta, 'w', newline='', encoding='utf-8') as archivo:
        writer = csv.writer(archivo)
        
        if campos:
            # Múltiples campos
            headers = [campo['header'] for campo in campos]
            writer.writerow(headers)
            
            for i in range(inicio_numero, inicio_numero + num_items):
                row = []
                for campo in campos:
                    formato = campo['format']
                    try:
                        valor = formato.format(n=i)
                    except Exception:
                        valor = formato.replace('{n}', str(i))
                    row.append(valor)
                writer.writerow(row)
        else:
            # Modo clásico (un solo campo)
            writer.writerow([encabezado])
            for i in range(inicio_numero, inicio_numero + num_items):
                num_formateado = str(i).zfill(ancho_codigo)
                valor = f"{prefijo}{num_formateado} {texto_base} {i}"
                writer.writerow([valor])
    return ruta

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generar', methods=['POST'])
def generar():
    try:
        import json
        num_items = int(request.form.get('num_items', 100))
        campos_json = request.form.get('campos', '[]')
        campos = json.loads(campos_json) if campos_json else []
        
        # Si no hay campos, usar modo clásico
        if not campos:
            prefijo = request.form.get('prefijo', 'ITEM-')
            texto_base = request.form.get('texto_base', 'Valor de catalogo')
            inicio_numero = int(request.form.get('inicio_numero', 1))
            ancho_codigo = int(request.form.get('ancho_codigo', 5))
            encabezado = request.form.get('encabezado', 'valor')
        else:
            # Valores dummy para compatibilidad
            prefijo = ""
            texto_base = ""
            inicio_numero = 1
            ancho_codigo = 5
            encabezado = ""
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        nombre_archivo = f"catalogo_{timestamp}.csv"
        
        ruta_archivo = generar_catalogo_csv(
            nombre_archivo=nombre_archivo,
            num_items=num_items,
            campos=campos,
            prefijo=prefijo,
            texto_base=texto_base,
            inicio_numero=inicio_numero,
            ancho_codigo=ancho_codigo,
            encabezado=encabezado
        )
        
        # Vista previa
        preview = []
        with open(ruta_archivo, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            for i, row in enumerate(reader):
                if i < 10:
                    preview.append(row)
        return jsonify({
            'success': True,
            'filename': nombre_archivo,
            'num_items': num_items,
            'preview': preview,
            'download_url': f'/descargar/{nombre_archivo}'
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 400

@app.route('/descargar/<filename>')
def descargar(filename):
    ruta = os.path.join('generated', filename)
    if os.path.exists(ruta):
        return send_file(ruta, as_attachment=True, download_name=filename, mimetype='text/csv')
    return jsonify({'error': 'Archivo no encontrado'}), 404

@app.route('/limpiar', methods=['POST'])
def limpiar():
    try:
        eliminados = 0
        for f in os.listdir('generated'):
            if f.endswith('.csv'):
                os.remove(os.path.join('generated', f))
                eliminados += 1
        return jsonify({'success': True, 'message': f'Se eliminaron {eliminados} archivos'})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 400

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)