# CSV Catalog Generator

A web application built with Flask that allows users to generate customizable CSV files with catalog data. Instead of fixed fields, this app lets you define multiple columns with custom headers and formatting templates.

## 🌟 Features

- **Dynamic Fields**: Create CSV files with any number of columns
- **Custom Formatting**: Use templates like `ITEM-{n:05d}` for numbered sequences
- **Real-time Preview**: See a preview of your CSV before downloading
- **Multiple Columns**: Support for complex catalogs with ID, Name, Description, etc.
- **Clean UI**: Modern Bootstrap interface for easy field management
- **File Management**: Built-in cleanup of generated files

## 🚀 Quick Start

### Local Development

1. **Clone the repository**:
   ```bash
   git clone https://github.com/jhoncarlosam-dev/csv-catalog-generator.git
   cd csv-catalog-generator
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```bash
   python app.py
   ```

4. **Open your browser** and go to `http://127.0.0.1:5000`

### Deployment on Render

The app is configured for easy deployment on Render.com:

1. Connect your GitHub account to Render
2. Create a new Web Service from your repository
3. Render will automatically detect the `render.yaml` configuration
4. Your app will be live at the provided URL

## 📖 Usage

1. **Access the web interface** at the root URL
2. **Set the number of items** you want to generate
3. **Add fields** by clicking "Agregar Campo":
   - **Encabezado**: Column header (e.g., "ID", "Nombre", "Precio")
   - **Formato**: Template using `{n}` for the sequence number
     - `{n}`: Simple number (1, 2, 3...)
     - `{n:05d}`: Zero-padded number (00001, 00002...)
     - `PROD-{n:04d}`: Custom prefix with padding
4. **Click "Generar CSV"** to create your file
5. **Preview** the first 10 rows in the table
6. **Download** your CSV file
7. **Clean up** old files with the "Limpiar Archivos" button

### Example Fields

| Header | Format | Output |
|--------|--------|--------|
| ID | `ITEM-{n:05d}` | ITEM-00001, ITEM-00002... |
| Name | `Product {n}` | Product 1, Product 2... |
| SKU | `SKU-{n:03d}-CAT` | SKU-001-CAT, SKU-002-CAT... |

## 🛠️ Technologies Used

- **Backend**: Python Flask
- **Frontend**: HTML, CSS (Bootstrap), JavaScript
- **Deployment**: Render.com
- **Version Control**: Git

## 📁 Project Structure

```
csv-catalog-generator/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── render.yaml           # Render deployment configuration
├── templates/
│   └── index.html        # Web interface
├── generated/            # Generated CSV files (auto-created)
└── .gitignore           # Git ignore rules
```

## 🔧 Configuration

### Environment Variables

- `PORT`: Server port (defaults to 5000)
- `FLASK_ENV`: Set to `production` for deployment

### File Storage

Generated CSV files are stored in the `generated/` directory. The app includes a cleanup function to remove old files.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 📞 Support

If you find this project helpful, please give it a ⭐ on GitHub!

---

Built with ❤️ using Flask and deployed on Render</content>
<parameter name="filePath">c:\Users\JHON ACEVEDO\OneDrive\Desktop\code\mi-catalogo-app\README.md